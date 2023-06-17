ThisBuild / version      := "0.1.0"
ThisBuild / scalaVersion := "2.12.7"
ThisBuild / organization := "com.example"


val test= "test"
val apacheSpark = "org.apache.spark"
val apacheKafka = "org.apache.kafka"
val apacheHadoop = "org.apache.hadoop"
val apacheCassandra = "org.apache.cassandra"


val log4jVersion = "1.2.17"
val cassandraVersion = "3.11.5"
val sparkVersion = "3.4.0"
val kafkaVersion = "3.4.0"

// libraryDependencies += groupID % artifactID % revision
// libraryDependencies += groupID % artifactID % revision % configuration(Test)
val scalaVersionSuffix = "_2.12"
val sparkKubernetis = apacheSpark %  f"spark-kubernetes$scalaVersionSuffix" % sparkVersion
val sparkMesos = apacheSpark %  f"spark-mesos$scalaVersionSuffix" % sparkVersion
val sparkMllibLocal = apacheSpark %  f"spark-mllib-local$scalaVersionSuffix"  % sparkVersion
val sparkSqlKafka = apacheSpark %  f"spark-sql-kafka-0-10$scalaVersionSuffix" % sparkVersion
val sparkSql = apacheSpark %  f"spark-sql$scalaVersionSuffix" % sparkVersion exclude("org.scala-lang.modules", f"scala-parser-combinators$scalaVersionSuffix")
val sparkStreamingKafkaAssembly = apacheSpark %  f"spark-streaming-kafka-0-10-assembly$scalaVersionSuffix" % sparkVersion
val sparkStreamingKafka = apacheSpark %  f"spark-streaming-kafka-0-10$scalaVersionSuffix" % sparkVersion
val sparkStreaming = apacheSpark %  f"spark-streaming$scalaVersionSuffix" % sparkVersion
val sparkProtobuf = apacheSpark %  f"spark-protobuf$scalaVersionSuffix" % sparkVersion
val sparkLanucher = apacheSpark %  f"spark-launcher$scalaVersionSuffix"  % sparkVersion
val sparkHadoop = apacheSpark %  f"spark-hadoop-cloud$scalaVersionSuffix" % sparkVersion
val sparkAvro = apacheSpark %  f"spark-avro$scalaVersionSuffix"  % sparkVersion
val sparkHive = apacheSpark %  f"spark-hive$scalaVersionSuffix"  % sparkVersion
val sparkMllib = apacheSpark %  f"spark-mllib$scalaVersionSuffix" % sparkVersion
val sparkCore = apacheSpark %  f"spark-core$scalaVersionSuffix" % sparkVersion
val sparkCatalyst = apacheSpark %  f"spark-catalyst$scalaVersionSuffix"  % sparkVersion


val kafka =  apacheKafka %  f"kafka$scalaVersionSuffix" % kafkaVersion
val kafkaStreams =  apacheKafka %  f"kafka-streams-scala$scalaVersionSuffix" % kafkaVersion
val kafkaStreamTest = apacheKafka % "kafka-streams" % kafkaVersion % test classifier test
val kafkaStreamsTestUtils = apacheKafka % "kafka-streams-test-utils" % kafkaVersion % test
val kafkaConnectRuntime = apacheKafka % "connect-runtime" % kafkaVersion
val kafkaPerformance = apacheKafka % "kafka-perf_2.10" % "0.8.0"
val kafkaHadoopConsumer = apacheKafka % "kafka-hadoop-consumer" % "0.8.2.2"
val kafkaHadoopProducer = apacheKafka % "kafka-hadoop-producer" % "0.8.2.2"
val kafkaLog4J = apacheKafka % "kafka-log4j-appender" % kafkaVersion
val kafkaMetadata = apacheKafka % "kafka-metadata" % kafkaVersion
val kafkaServer = apacheKafka % "kafka-server-common" % kafkaVersion
val kafkaClients =  apacheKafka %  "kafka-clients" % kafkaVersion
val kafkaStreamsQuickstart =  apacheKafka %  "streams-quickstart" % kafkaVersion
val kafkaGroupCoordinator = apacheKafka % "kafka-group-coordinator" % kafkaVersion
val kafkaStorage = apacheKafka % "kafka-storage" % kafkaVersion
val kafkaStorageApi = apacheKafka % "kafka-storage-api" % kafkaVersion
val kafkaShell = apacheKafka % "kafka-shell" % kafkaVersion


val cassandra = apacheCassandra % "apache-cassandra" % cassandraVersion

val log4j = "log4j" % "log4j" % log4jVersion
val scalaTest = "org.scalatest" %% "scalatest" % "3.2.7"
val gigahorse = "com.eed3si9n" %% "gigahorse-okhttp" % "0.5.0"
val playJson  = "com.typesafe.play" %% "play-json" % "2.9.2"
val jacksonMapperAsl = "org.codehaus.jackson" % "jackson-mapper-asl" % "1.9.13"
val scalaParser = "org.scala-lang.modules" % "scala-parser-combinators_2.13" % "2.3.0"

val dataDependencies = Seq(
  //scalaParser,
  log4j,
  cassandra,
)


val sparkDependencies = Seq(
  
  sparkCore,
  // sparkMllibLocal, 
  sparkStreamingKafka,
  sparkStreaming,
  sparkSqlKafka,
  sparkLanucher,
  sparkHadoop,
  sparkAvro,  
  sparkKubernetis,
  sparkMesos,
  sparkProtobuf,
  //sparkCatalyst,
  sparkSql,
  sparkStreamingKafkaAssembly,
  // sparkHive,
  // sparkMllib,
)


val kafkaDependencies = Seq(
   kafka,
   kafkaMetadata,
   kafkaServer,
   kafkaStreams,
   kafkaStreamTest,
   kafkaStreamsTestUtils,
   kafkaStreamsQuickstart,
   kafkaGroupCoordinator,
   kafkaLog4J,
   kafkaClients,
   kafkaStorage,
   kafkaStorageApi,
  //  kafkaShell,
  


   //kafkaPerformance,
  //  kafkaHadoopConsumer,
  //  kafkaHadoopProducer, 
)


val othersDependencies = Seq(
  jacksonMapperAsl,
  gigahorse,
  playJson,
  scalaTest % Test
)



lazy val root = (project in file(".")).
  settings(
    libraryDependencies ++= dataDependencies,
    libraryDependencies ++= sparkDependencies,
    libraryDependencies ++= kafkaDependencies,
    libraryDependencies ++= othersDependencies,
    libraryDependencies ++= Seq(gigahorse, playJson),
  )

// mainClass in (Compile, run) := Some("main.scala.Main")

// lazy val hello = (project in file("."))
//   .aggregate(helloCore)
//   .dependsOn(helloCore)
//   .enablePlugins(JavaAppPackaging)
//   .settings(
//     name := "Hello",
//     libraryDependencies += gigahorse,
//     libraryDependencies += playJson,
//     libraryDependencies += scalaTest % Test,
//     // libraryDependencies += "org.apache.spark" %% "spark-core" % "2.0.0",
//     libraryDependencies += "org.apache.spark" %% "spark-streaming" % "2.0.0",
//     // libraryDependencies += "org.apache.spark" %% "spark-streaming-kafka-0-8" % "2.0.0",

//   )

// lazy val helloCore = (project in file("core"))
//   .settings(
//     name := "Hello Core",
//     libraryDependencies ++= Seq(gigahorse, playJson),
//     libraryDependencies += scalaTest % Test,
//   )