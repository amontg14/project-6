"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
from acp_times import open_time, close_time
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_brevet1():
    start_time = arrow.get("2023-02-19T00:00", "YYYY-MM-DDTHH:mm")
    dist = 200
    checkpoint = {
    0: (start_time, start_time.shift(hours=1)),
    50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3, minutes=30)),
    150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10)),
    200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=30)),
    }

    for km, times_t in checkpoint.items():
        assert open_time(km, dist, start_time) == times_t[0]
        assert close_time(km, dist, start_time) == times_t[1]

def test_brevet2():
    start_time = arrow.get("2023-02-19T00:00", "YYYY-MM-DDTHH:mm")
    dist = 300
    checkpoint = {
    0: (start_time, start_time.shift(hours=1)),
    100: (start_time.shift(hours=2, minutes=56), start_time.shift(hours=6, minutes=40)),
    200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=20)),
    300: (start_time.shift(hours=9), start_time.shift(hours=20)),
    }

    for km, times_t in checkpoint.items():
        assert open_time(km, dist, start_time) == times_t[0]
        assert close_time(km, dist, start_time) == times_t[1]

def test_brevet3():
    start_time = arrow.get("2023-02-19T00:00", "YYYY-MM-DDTHH:mm")
    dist = 400
    checkpoint = {
    0: (start_time, start_time.shift(hours=1)),
    100: (start_time.shift(hours=2, minutes=56), start_time.shift(hours=6, minutes=40)),
    300: (start_time.shift(hours=9), start_time.shift(hours=20)),
    400: (start_time.shift(hours=12, minutes=8), start_time.shift(hours=27)),
    }

    for km, times_t in checkpoint.items():
        assert open_time(km, dist, start_time) == times_t[0]
        assert close_time(km, dist, start_time) == times_t[1]

def test_brevet4():
    start_time = arrow.get("2023-02-19T00:00", "YYYY-MM-DDTHH:mm")
    dist = 600
    checkpoint = {
    0: (start_time, start_time.shift(hours=1)),
    300: (start_time.shift(hours=9), start_time.shift(hours=20)),
    500: (start_time.shift(hours=15, minutes=28), start_time.shift(hours=33, minutes=20)),
    600: (start_time.shift(hours=18, minutes=48), start_time.shift(hours=40)),
    }

    for km, times_t in checkpoint.items():
        assert open_time(km, dist, start_time) == times_t[0]
        assert close_time(km, dist, start_time) == times_t[1]

def test_brevet5():
    start_time = arrow.get("2023-02-19T00:00", "YYYY-MM-DDTHH:mm")
    dist = 1000
    checkpoint = {
    0: (start_time, start_time.shift(hours=1)),
    250: (start_time.shift(hours=7, minutes=27), start_time.shift(hours=16, minutes=40)),
    500: (start_time.shift(hours=15, minutes=28), start_time.shift(hours=33, minutes=20)),
    750: (start_time.shift(hours=24, minutes=9), start_time.shift(hours=53, minutes=8)),
    1000: (start_time.shift(hours=33, minutes=5), start_time.shift(hours=75)),
    }

    for km, times_t in checkpoint.items():
        assert open_time(km, dist, start_time) == times_t[0]
        assert close_time(km, dist, start_time) == times_t[1]