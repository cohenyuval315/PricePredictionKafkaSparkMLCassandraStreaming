package cassandra.foreachSink

import cassandra.CassandraDriver
import log.LazyLogger
import org.apache.spark.sql.ForeachWriter
import models.KlineData

/**
  * Inspired by
  * https://github.com/ansrivas/spark-structured-streaming/
  * https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#using-foreach
  */
class CassandraSinkForeach() extends ForeachWriter[KlineData] with LazyLogger {
  private def cqlRadio(record: KlineData): String = s"""
       insert into ${CassandraDriver.namespace}.${CassandraDriver.foreachTableSink} 
       (eventType,
        eventTime,
        symbol,
        klineStartTime,
        klineCloseTime,
        interval,
        firstTradeID,
        lastTradeID,
        openPrice,
        closePrice,
        highPrice,
        lowPrice,
        baseAssetVolume,
        numOfTrades,
        klineClosed,
        quoteAssetVolume,
        takerBuyBaseAssetVolume,
        takerBuyQuoteAssetVolume,
        ignore)
       values(
        '${record.eventType}',
        ${record.eventTime},
        '${record.symbol}',
        ${record.klineStartTime},
        ${record.klineCloseTime},
        '${record.interval}',
        ${record.firstTradeID},
        ${record.lastTradeID},
        ${record.openPrice},
        ${record.closePrice},
        ${record.highPrice},
        ${record.lowPrice},
        ${record.baseAssetVolume},
        ${record.numOfTrades},
        ${record.klineClosed},
        ${record.quoteAssetVolume},
        ${record.takerBuyBaseAssetVolume},
        ${record.takerBuyQuoteAssetVolume},
        '${record.ignore}',
        )"""

  def open(partitionId: Long, version: Long): Boolean = {
    // open connection
    //@TODO command to check if cassandra cluster is up
    true
  }

  //https://github.com/datastax/spark-cassandra-connector/blob/master/doc/1_connecting.md#connection-pooling
  def process(record: KlineData) = {
    log.warn(s"Saving record: $record")
    CassandraDriver.connector.withSessionDo(session =>
      session.execute(cqlRadio(record))
    )
  }

  //https://github.com/datastax/spark-cassandra-connector/blob/master/doc/reference.md#cassandra-connection-parameters

  def close(errorOrNull: Throwable): Unit = {
    // close the connection
    //connection.keep_alive_ms	--> 5000ms :	Period of time to keep unused connections open
  }
}