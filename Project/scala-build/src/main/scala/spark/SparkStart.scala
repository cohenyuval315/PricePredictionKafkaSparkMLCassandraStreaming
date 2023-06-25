package spark

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.SparkSession

object SparkStart {
  def getAndConfigureSparkSession() = {
    //val logLevel = "ERROR"
    val logLevel = "WARN"
    val conf = new SparkConf()
      .setAppName("TestApp")
      .setMaster("local[2]")
     // .set("spark.cassandra.connection.host", "127.0.0.1")
      .set("spark.sql.streaming.checkpointLocation", "checkpoint")
      .set("spark.sql.caseSensitive","true")
      .set("spark.streaming.stopGracefullyOnShutdown", "true")
    .set("spark.sql.warehouse.dir", "")
    .set("spark.sql.catalog.history", "com.datastax.spark.connector.datasource.CassandraCatalog")
    .set("spark.cassandra.connection.host", "localhost")
    .set("spark.sql.extensions", "com.datastax.spark.connector.CassandraSparkExtensions")
    //   .set("es.nodes", "localhost") // full config : https://www.elastic.co/guide/en/elasticsearch/hadoop/current/configuration.html
    //   .set("es.index.auto.create", "true") //https://www.elastic.co/guide/en/elasticsearch/hadoop/current/spark.html
    //   .set("es.nodes.wan.only", "true")

    val sc = new SparkContext(conf)
    sc.setLogLevel(logLevel)

    SparkSession
      .builder()
      .getOrCreate()
  }

  def getSparkSession() = {
    SparkSession
      .builder()
      .getOrCreate()
  }
}