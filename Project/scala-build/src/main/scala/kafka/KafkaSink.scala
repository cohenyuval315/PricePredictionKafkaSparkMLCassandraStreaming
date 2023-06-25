package kafka

import org.apache.spark.sql.{DataFrame, Dataset}
import org.apache.spark.sql.functions.{struct, to_json, _}
import _root_.log.LazyLogger
import org.apache.spark.sql.streaming.StreamingQuery
import org.apache.spark.sql.types.{StringType, _}
import models.{KlineData,KlineAggregationKafka}
import spark.SparkStart

object KafkaSink extends LazyLogger {
  private val spark = SparkStart.getSparkSession()

  import spark.implicits._

  def writeStream(staticInputDS: Dataset[KlineData]) : StreamingQuery = {
    log.warn("Writing to Kafka")
    staticInputDS
      .select(to_json(struct($"*")).cast(StringType).alias("value"))
      .writeStream
      .outputMode("update")
      .format("kafka")
      .option("kafka.bootstrap.servers", KafkaService.bootstrapServers)
      .queryName("Kafka - query_name ")
      .option("topic", KafkaService.outputTopic)
      .start()
  }


  def debugStream(staticKafkaInputDS: Dataset[KlineAggregationKafka]) = {
    staticKafkaInputDS
      .writeStream
      .queryName("Debug Stream Kafka")
      .format("console")
      .start()
  }
}