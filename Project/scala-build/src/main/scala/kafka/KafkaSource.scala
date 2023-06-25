package kafka

import org.apache.spark.sql.{DataFrame, Dataset}
import org.apache.spark.sql.functions.{struct, to_json, _}
import _root_.log.LazyLogger
import org.apache.spark.sql.types.{StringType, _}
import models.{KlineData,KlineAggregationKafka}
import spark.SparkStart

/**
 @see https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html
 */
object KafkaSource extends LazyLogger {
  private val spark = SparkStart.getSparkSession()

  import spark.implicits._

    def read(startingOption: String = "startingOffsets", partitionsAndOffsets: String = "earliest") : Dataset[KlineAggregationKafka] = {
      log.warn("Reading from Kafka")

      spark
      .readStream
      .format("kafka")
      .option("kafka.bootstrap.servers", KafkaService.bootstrapServers)
      .option("subscribe", KafkaService.topicName)
      .option("enable.auto.commit", false) // Cannot be set to true in Spark Strucutured Streaming https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html#kafka-specific-configurations
      .option("group.id", KafkaService.groupId)
      .option("failOnDataLoss", false) // when starting a fresh kafka (default location is temporary (/tmp) and cassandra is not (var/lib)), we have saved different offsets in Cassandra than real offsets in kafka (that contains nothing)
      .option(startingOption, partitionsAndOffsets) //this only applies when a new query is started and that resuming will always pick up from where the query left off
      .load()
      .withColumn(KafkaService.klineOutput, // nested structure with our json
        from_json($"value".cast(StringType), KafkaService.klineSchema) //From binary to JSON object
      ).as[KlineAggregationKafka]
      //.filter(_.radioCount != null) //TODO find a better way to filter bad json
  }
}