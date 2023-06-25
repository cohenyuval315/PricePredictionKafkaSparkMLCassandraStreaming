package models
import org.apache.spark.sql.types._

object Schemas {
    def getKlineSchema () : StructType = {
        val schema = StructType(Seq(
        StructField("t", LongType),
        StructField("T", LongType),
        StructField("s", StringType),
        StructField("i", StringType),
        StructField("f", LongType),
        StructField("L", LongType),
        StructField("o", StringType),
        StructField("c", StringType),
        StructField("h", StringType),
        StructField("l", StringType),
        StructField("v", StringType),
        StructField("n", IntegerType),
        StructField("x", BooleanType),
        StructField("q", StringType),
        StructField("V", StringType),
        StructField("Q", StringType),
        StructField("B", StringType),
        StructField("E", LongType),
        StructField("e", StringType)
        ))
        return schema
    }
}


