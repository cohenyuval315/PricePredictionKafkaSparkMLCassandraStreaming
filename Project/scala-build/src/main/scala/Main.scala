
package main.scala

// import org.apache.spark.sql
import org.apache.spark.sql.SparkSession
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.streaming
import org.apache.spark
import org.apache.spark.sql.types
import org.apache.kafka.server
// import org.apache.kafka.streams
import java.util.Properties
// nc -lk 9999 



object Main extends App {
  val TEST_TOPIC = "my_topic"
  val TEST_KEY = "key"
  val BOOSTRAP_SERVER = "localhost:9092"

  //  def startKafka() = {
  //   server.
  //  }

  //streaming.kafka010.KafkaUtils.createDirectStream()

  // val sparkConf = new SparkConf().setAppName("WindowClickCount").setMaster("local[2]")
  val appName = "sparkByEx"
  val masterTarget = "local[1]"
  val masterTargetT = "spark://10.0.0.14:7077"
  val logLevel = "ERROR"
  // val sparkConf = new SparkConf()
  //   .setAppName(appName)
  //   .setMaster(masterTargetT)
  // val sc = new SparkContext()

  val spark = SparkSession.builder().appName(appName).master(masterTargetT).getOrCreate()
  spark.sparkContext.setLogLevel(logLevel)
  
  
  // val lines = spark.readStream.format("socket").option("host","localhost").option("port",9999).load() 

  val kafkaDF = spark.readStream
  .format("kafka").option("kafka.bootstrap.servers",BOOSTRAP_SERVER)
  .option("subscribe",TEST_TOPIC).load()

  val proccessedDF = kafkaDF.selectExpr("CAST(key AS STRING)","CAST(value AS STRING)")
  
  
  val schema = types.StructType(Seq(
    types.StructField("column1",types.IntegerType),
    types.StructField("column2",types.StringType),
  ))
  val query = proccessedDF.writeStream
    .outputMode("append")
    .format("console")
    .start()

  query.awaitTermination()

  // val words = lines.as[Integer].flatMap(_.split(" "))
  // val wordCounts = words.groupBy("value").count()
  // val query = wordCounts.writeStream
  //   .outputMode("complete")
  //   .format("console")
  //   .start()

  // query.awaitTermination()
  // print("hello\n")

}



// import events.avro.ClickEvent
// import kafka.serializer.DefaultDecoder
// import org.apache.avro.io.DecoderFactory
// import org.apache.avro.specific.SpecificDatumReader
// import org.apache.spark._
// import org.apache.spark.rdd.RDD
// import org.apache.spark.storage.StorageLevel
// import org.apache.spark.streaming.kafka.KafkaUtils
// import org.apache.spark.streaming.{Minutes, Seconds, StreamingContext}

// object Main extends App {
//   /**
//    * Example Arguments: test 2
//    */
//   if (args.length < 2) {
//     System.err.println("Usage: <topic> <numThreads>")
//     System.exit(1)
//   }

//   println("Initializing App")

//   val Array(topics, numThreads) = args

//   val sparkConf = new SparkConf().setAppName("WindowClickCount").setMaster("local[2]")

//   // Slide duration of ReduceWindowedDStream must be multiple of the parent DStream, and we chose 2 seconds for the reduced
//   // window stream
//   val ssc = new StreamingContext(sparkConf, Seconds(2))

//   // Because we're using .reduceByKeyAndWindow, we need to persist it to disk
//   ssc.checkpoint("./checkpointDir")

//   val kafkaConf = Map(
//     "metadata.broker.list" -> "localhost:9092", // Default kafka broker list location
//     "zookeeper.connect" -> "localhost:2190", // Default zookeeper location
//     "group.id" -> "kafka-spark-streaming-example",
//     "zookeeper.connection.timeout.ms" -> "1000")

//   val topicMap = topics.split(",").map((_, numThreads.toInt)).toMap

//   // Create a new stream which can decode byte arrays.  For this exercise, the incoming stream only contain user and product Ids
//   val lines = KafkaUtils.createStream[String, Array[Byte], DefaultDecoder, DefaultDecoder](ssc, kafkaConf, topicMap, StorageLevel.MEMORY_ONLY_SER).map(_._2)

//   // Create a RDD containing the mapping of ids to names.  In practice, these mappings will come from HDFS/S3/(a real data source)
//   val userNameMapRDD = ssc.sparkContext.parallelize(Array((1,"Joe"), (2, "Michelle"), (3, "David"), (4, "Anthony"), (5, "Lisa")))
//   val productNameMapRDD = ssc.sparkContext.parallelize(Array((1,"Legos"), (2, "Books"), (3, "Board Games"), (4, "Food"), (5, "Computers")))

//   // Join the stream with the userNameMapRDD to map the userName to the userId
//   val mappedUserName = lines.transform{rdd =>
//     val clickRDD: RDD[(Int, Int)] = rdd.map { bytes => AvroUtil.clickEventDecode(bytes) }.map { clickEvent =>
//       (clickEvent.getUserId: Int) -> clickEvent.getProductId
//     }

//     clickRDD.join(userNameMapRDD).map { case (userId, (productId, userName)) => (userName, productId)}
//   }

//   // Join the stream with the productNameMapRDD to map the productName to the productId
//   val mappedProductId = mappedUserName.transform{ rdd =>
//     val productRDD = rdd.map { case (userName, productId) => (productId: Int, userName) }

//     productRDD.join(productNameMapRDD).map { case (productId, (productName, userName)) => (userName, productName)}
//   }

//   // Get a count of all the users and the products they visited in the last 10 minutes, refreshing every 2 seconds
//   val clickCounts = mappedProductId.map(x => (x, 1L))
//     .reduceByKeyAndWindow(_ + _, _ - _, Minutes(10), Seconds(2), 2).map { case ((productName, userName), count) =>
//     (userName, productName, count)
//   }

//   clickCounts.print // Print out the results.  Or we can produce new kafka events containing the mapped ids.

//   ssc.start()
//   ssc.awaitTermination()
// }

// object AvroUtil {
//   // Deserialize the byte array into an avro object
//   // https://cwiki.apache.org/confluence/display/AVRO/FAQtil {
//   val reader = new SpecificDatumReader[ClickEvent](ClickEvent.getClassSchema)
//   def clickEventDecode(bytes: Array[Byte]): ClickEvent = {
//     val decoder = DecoderFactory.get.binaryDecoder(bytes, null)
//     reader.read(null, decoder)
//   }
// }