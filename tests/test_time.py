from src.OOP_lab_1.time import Time


class TestTime:
    def test_init_from_numbers(self):
        time = Time(10, 30, 45)
        assert time.hours == 10
        assert time.minutes == 30
        assert time.seconds == 45

    def test_init_from_string(self):
        time = Time("10:30:45")
        assert time.hours == 10
        assert time.minutes == 30
        assert time.seconds == 45

    def test_init_from_seconds(self):
        time = Time(3665)  # 1 hour, 1 minute, 5 seconds
        assert time.hours == 1
        assert time.minutes == 1
        assert time.seconds == 5

    def test_to_seconds(self):
        time = Time(1, 1, 5)
        assert time.to_seconds() == 3665

    def test_add_seconds(self):
        time = Time(1, 1, 5)
        new_time = time.add_seconds(60)  # Add 1 minute
        assert new_time.hours == 1
        assert new_time.minutes == 2
        assert new_time.seconds == 5

    def test_comparison(self):
        time1 = Time(1, 0, 0)
        time2 = Time(2, 0, 0)
        assert time1 < time2
        assert time2 > time1
        assert time1 != time2
