package kafka
import org.apache.spark.sql.types._
import spark.SparkStart

object KafkaService {
  private val spark = SparkStart.getSparkSession()

  val topicName = "my_topic"
  val key = "key"
  val bootstrapServers = "localhost:9092"
  val klineOutput = "klineOutput"
  val groupId = "Structured-Streaming-Examples"
  val outputTopic = "output-topic"

  val klineSchema = StructType(Seq(
    StructField("klineStartTime", LongType),
    StructField("klineCloseTime", LongType),
    StructField("symbol", StringType),
    StructField("interval", StringType),
    StructField("firstTradeID", LongType),
    StructField("lastTradeID", LongType),
    StructField("openPrice", DoubleType),
    StructField("closePrice", DoubleType),
    StructField("highPrice", DoubleType),
    StructField("lowPrice", DoubleType),
    StructField("baseAssetVolume", DoubleType),
    StructField("numOfTrades", IntegerType),
    StructField("klineClosed", BooleanType),
    StructField("quoteAssetVolume", DoubleType),
    StructField("takerBuyBaseAssetVolume", DoubleType),
    StructField("takerBuyQuoteAssetVolume", DoubleType),
    StructField("ignore", StringType),
    StructField("eventTime", LongType),
    StructField("eventType", StringType)
  ))
}