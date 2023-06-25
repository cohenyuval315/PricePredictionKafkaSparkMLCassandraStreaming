package models
import java.sql.Timestamp

// case class KlineData(
//     e: String,     // Event type
//     E: Long,   // Event time
//     s:String,    // Symbol
//     t: Long, // Kline start time
//     T: Long, // Kline close time
//     i: String,      // Interval
//     f: Long,       // First trade ID
//     L: Long,       // Last trade ID
//     o: String,  // Open price
//     c: String,  // Close price
//     h: String,  // High price
//     l: String,  // Low price
//     v: String,    // Base asset volume
//     n: Long,       // Number of trades
//     x: Boolean,     // Is this kline closed?
//     q: String,  // Quote asset volume
//     V: String,     // Taker buy base asset volume
//     Q: String,   // Taker buy quote asset volume
//     B: String// Ignore
// )
  case class KlineData(
            eventType:String,
            eventTime:Long,
            symbol:String,
            klineStartTime:Long,
            klineCloseTime:Long,
            interval:String,
            firstTradeID:Long,
            lastTradeID:Long,
            openPrice:Double,
            closePrice:Double,
            highPrice:Double,
            lowPrice:Double,
            baseAssetVolume:Double,
            numOfTrades:Integer,
            klineClosed:Boolean,
            quoteAssetVolume:Double,
            takerBuyBaseAssetVolume:Double,
            takerBuyQuoteAssetVolume:Double,
            ignore:String)

case class KlineAggregationKafka(topic: String, partition: Int, offset: Long, timestamp: Timestamp, klineOutput: KlineData)