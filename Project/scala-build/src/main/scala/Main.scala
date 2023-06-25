
package main.scala

// import org.apache.spark.sql
import org.apache.spark.sql.SparkSession
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.streaming
import org.apache.spark.sql.types
import org.apache.kafka.server
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.ml.regression.LinearRegression
import scala.util.parsing.json._
// import org.apache.kafka.streams
import java.util.Properties
import org.apache.spark.sql.{Dataset,Row,DataFrame}
// nc -lk 9999 
import com.datastax.spark.connector._
import com.datastax.spark.connector.mapper.DataFrameColumnMapper

import com.datastax.spark.connector.cql._
import org.apache.spark._
import org.apache.log4j._
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
import spark.SparkStart
import kafka.{KafkaSink,KafkaSource,KafkaService}
import models.{KlineData}
import org.apache.spark.sql.streaming.StreamingQuery


object Main extends App {
  val TEST_TOPIC = "my_topic"
  val TEST_KEY = "key"
  val BOOSTRAP_SERVER = "localhost:9092"
  val appName = "sparkByEx"
  val masterTarget = "local[2]"
  val masterTargetT = "spark://DESKTOP-1OCIBRO.localdomain:7077"
  val logLevel = "ERROR"
  val output_topic = "output-topic"

  val spark = SparkStart.getAndConfigureSparkSession()
  import spark.implicits._

  def consoleStream(df: DataFrame) : StreamingQuery = {
    df
      .writeStream
      .queryName("df-console")
      .format("console")
      .start()
  }

  

  // read from kafka 
  val kafkaInputDS = KafkaSource.read()
  val df = kafkaInputDS.select($"timestamp",$"klineOutput").w.select(KafkaService.klineOutput + ".")
  .
       .as[KlineData]
  
  val df = kafkaInputDS

  kafkaInputDS.createOrReplaceTempView("klines")
  // val ddf = spark.sql("select klines.openPrice,klines.closePrice,klines.highPrice,klines.lowPrice from klines")
  val ddf = spark.sql("select klines.timestamp, klines.klineOutput from klines")


    // kafkaInputDS
    // .groupBy(
    //   window($"timestamp","2 minutes","3 minutes"),
    //   $"openPrice"
    //   ).count()

  consoleStream(ddf)





    // ElasticSink.writeStream(songEvent)

    //Send it to Kafka for our example
    // KafkaSink.writeStream(streamDS)

    // //Finally read it from kafka, in case checkpointing is not available we read last offsets saved from Cassandra
    // val (startingOption, partitionsAndOffsets) = CassandraDriver.getKafaMetadata()
    // val kafkaInputDS = KafkaSource.read(startingOption, partitionsAndOffsets)

    // //Just debugging Kafka source into our console
    // KafkaSink.debugStream(kafkaInputDS)

    // //Saving using Datastax connector's saveToCassandra method
    // CassandraDriver.saveStreamSinkProvider(kafkaInputDS)

    // //Saving using the foreach method
    // //CassandraDriver.saveForeach(kafkaInputDS) //Untype/unsafe method using CQL  --> just here for example

    // //Another fun example managing an arbitrary state
    // MapGroupsWithState.write(kafkaInputDS)


  spark.streams.awaitAnyTermination()

  // val writeQuery = kafkaDF.writeStream
  //   .format("kafka")
  //   .option("kafka.bootstrap.servers", BOOSTRAP_SERVER)
  //   .option("topic", output_topic)
  //   .option("checkpointLocation", "/tmp/spark_data")
  //   .start()

  // writeQuery.awaitTermination()
}

// val kafkaDF = spark.readStream
  // .format("kafka")
  // .option("kafka.bootstrap.servers",BOOSTRAP_SERVER)
  // .option("subscribe",TEST_TOPIC)
  // .load()
  // kafkaDF.printSchema()

    

  // val parsedDF = kafkaDF.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
  //   .select(from_json($"value", schema).as("data"))
  //   .select("data.*")
  //   .as[KlineData]

  // val keyspace = "keyspace"
  // val table = "kline"
  // val mapper = new DataFrameColumnMapper(schema)
  
  // mapper.newTable(keyspace,table)
  // parsedDF.
  // parsedDF.writeStream.foreachBatch{(batchDF, _) =>
  //     batchDF.write
  //       .format("org.apache.spark.sql.cassandra")
  //       .mode("append")
  //       .option("table", table)
  //       .option("keyspace", keyspace)
  //       .save()
  //   }
  //   .start()
  //   .awaitTermination()


  // val query = parsedDF.writeStream.outputMode("append").format("console").start()


  // case class KlineData(
  //           eventType:String,
  //           eventTime:Long,
  //           symbol:String,
  //           klineStartTime:Long,
  //           klineCloseTime:Long,
  //           interval:String,
  //           firstTradeID:Long,
  //           lastTradeID:Long,
  //           openPrice:Long,
  //           closePrice:Long,
  //           highPrice:Long,
  //           lowPrice:Long,
  //           baseAssetVolume:Long,
  //           numOfTrades:Long,
  //           klineClosed:Boolean,
  //           quoteAssetVolume:Long,
  //           takerBuyBaseAssetVolume:Long,
  //           takerBuyQuoteAssetVolume:Long)
