import time
from collections import defaultdict
from typing import List


def in_x_smaller_lists(large_list: list, number_of_lists: int) -> List[list]:
    """
    Split one large list into smaller ones.

    See https://stackoverflow.com/q/752308#11574640
    """
    if not large_list:
        return []
    return [large_list[i::number_of_lists] for i in range(number_of_lists)]


def list_by_max_items(large_list: list, max_items: int) -> List[list]:
    """
    Optimize splitting to get minimal number of smaller lists.

    Each returned smaller list has about the same number of items that is less than or equal to max_items.
    """
    number_of_lists = max(1, len(large_list) // max_items)
    return in_x_smaller_lists(large_list, number_of_lists)

_perf_data = defaultdict(lambda: defaultdict(dict))
_perf_stats = defaultdict(list)


def perf_start(exchange: str, key: str):
    _perf_data[exchange][key]['start'] = time.time()


def perf_end(exchange: str, key: str):
    _perf_data[exchange][key]['end'] = time.time()
    _perf_stats[f"{exchange}-{key}"].append(_perf_data[exchange][key]['end'] - _perf_data[exchange][key]['start'])


def perf_log(exchange: str, key: str, stats=1000, stats_only=True):
    if not stats_only:
        print("{}: {} - {:.2f} ms".format(exchange, key, 1000 * (_perf_data[exchange][key]['end'] - _perf_data[exchange][key]['start'])))
    if stats and len(_perf_stats[f"{exchange}-{key}"]) > stats:
        stats_key = f"{exchange}-{key}"
        print(f"For last {stats} executions:")
        _min = min(_perf_stats[stats_key]) * 1000
        _max = max(_perf_stats[stats_key]) * 1000
        _avg = sum(_perf_stats[stats_key]) / len(_perf_stats[stats_key]) * 1000
        print(f"   Min: {_min} ms")
        print(f"   Max: {_max} ms")
        print(f"   Average: {_avg} ms")
        _perf_stats[stats_key] = []





def book_delta(former: dict, latter: dict, book_type=L2_BOOK) -> list:
    ret = {BID: [], ASK: []}
    if book_type == L2_BOOK:
        for side in (BID, ASK):
            fkeys = set(list(former[side].keys()))
            lkeys = set(list(latter[side].keys()))
            for price in fkeys - lkeys:
                ret[side].append((price, 0))

            for price in lkeys - fkeys:
                ret[side].append((price, latter[side][price]))

            for price in lkeys.intersection(fkeys):
                if former[side][price] != latter[side][price]:
                    ret[side].append((price, latter[side][price]))
    else:
        raise ValueError("Not supported for L3 Books")

    return ret



def timedelta_str_to_sec(td: str):
    if td == '1m':
        return 60
    if td == '3m':
        return 180
    if td == '5m':
        return 300
    if td == '10m':
        return 600
    if td == '15m':
        return 900
    if td == '30m':
        return 1800
    if td == '1h':
        return 3600
    if td == '2h':
        return 7200
    if td == '4h':
        return 14400
    if td == '6h':
        return 21600
    if td == '8h':
        return 28800
    if td == '12h':
        return 43200
    if td == '1d':
        return 86400
    if td == '3d':
        return 259200
    if td == '1w':
        return 604800
    if td == '2w':
        return 1209600
    if td == '1M':
        return 2592000
    if td == '1Y':
        return 31536000