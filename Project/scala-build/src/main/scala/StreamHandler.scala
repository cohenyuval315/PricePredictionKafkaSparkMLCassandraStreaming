
// import org.apache.spark.sql.SparkSession
// import org.apache.spark.streaming.kafka010.{ConsumerStrategies, KafkaUtils, LocationStrategies}
// import org.apache.kafka.common.serialization.StringDeserializer
// import org.apache.spark.streaming.{Seconds, StreamingContext}
// import com.datastax.spark.connector._

// object KafkaSparkCassandraExample {
//   def main(args: Array[String]): Unit = {
//     val spark = SparkSession
//       .builder()
//       .appName("KafkaSparkCassandraExample")
//       .master("local[2]")  // Set the Spark master URL according to your deployment
//       .config("spark.cassandra.connection.host", "localhost")  // Set Cassandra host
//       .getOrCreate()

//     val ssc = new StreamingContext(spark.sparkContext, Seconds(5))

//     val kafkaParams = Map[String, Object](
//       "bootstrap.servers" -> "localhost:9092",  // Set Kafka broker(s)
//       "key.deserializer" -> classOf[StringDeserializer],
//       "value.deserializer" -> classOf[StringDeserializer],
//       "group.id" -> "spark-consumer-group",
//       "auto.offset.reset" -> "latest",
//       "enable.auto.commit" -> (false: java.lang.Boolean)
//     )

//     val topics = Array("my-topic")  // Specify the Kafka topic(s) to consume from

//     val kafkaStream = KafkaUtils.createDirectStream[String, String](
//       ssc,
//       LocationStrategies.PreferConsistent,
//       ConsumerStrategies.Subscribe[String, String](topics, kafkaParams)
//     )

//     val lines = kafkaStream.map(_.value)

//     // Process the received messages from Kafka and save to Cassandra
//     lines.foreachRDD { rdd =>
//       rdd.foreach { message =>
//         // Perform your processing logic here
//         // For example, you can extract data from the message and save it to Cassandra
//         val data = message.split(",")
//         val id = data(0)
//         val value = data(1)

//         spark.sparkContext.parallelize(Seq((id, value))).saveToCassandra("mykeyspace", "mytable", SomeColumns("id", "value"))
//       }
//     }

//     ssc.start()
//     ssc.awaitTermination()
//   }
// }
