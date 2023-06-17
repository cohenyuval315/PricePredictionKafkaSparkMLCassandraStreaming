class MissingSequenceNumber(Exception):
    pass


class MissingMessage(Exception):
    pass


class UnsupportedSymbol(Exception):
    pass


class UnsupportedDataFeed(Exception):
    pass


class UnsupportedTradingOption(Exception):
    pass


class UnsupportedType(Exception):
    pass


class ExhaustedRetries(Exception):
    pass


class BidAskOverlapping(Exception):
    pass


class BadChecksum(Exception):
    pass


class RestResponseError(Exception):
    pass


class ConnectionClosed(Exception):
    pass


class UnexpectedMessage(Exception):
    pass