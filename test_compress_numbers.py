import pytest

from compress_numbers import compress_numbers


class TestBasicCases:
    def test_example_1(self):
        assert compress_numbers([1, 1, 2, 2, 3]) == [1, 2, 3]

    def test_example_2(self):
        assert compress_numbers([0, 0, 1, 1, 0]) == [0, 1, 0]

    def test_all_same(self):
        assert compress_numbers([5, 5, 5, 5, 5]) == [5]

    def test_no_duplicates(self):
        assert compress_numbers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_alternating(self):
        assert compress_numbers([1, 2, 1, 2, 1]) == [1, 2, 1, 2, 1]


class TestEdgeCases:
    def test_empty_list(self):
        assert compress_numbers([]) == []

    def test_single_element(self):
        assert compress_numbers([42]) == [42]

    def test_two_equal(self):
        assert compress_numbers([7, 7]) == [7]

    def test_two_different(self):
        assert compress_numbers([7, 8]) == [7, 8]

    def test_duplicates_at_start(self):
        assert compress_numbers([1, 1, 1, 2, 3]) == [1, 2, 3]

    def test_duplicates_at_end(self):
        assert compress_numbers([1, 2, 3, 3, 3]) == [1, 2, 3]


class TestNumberTypes:
    def test_negative_numbers(self):
        assert compress_numbers([-1, -1, -2, -2, -1]) == [-1, -2, -1]

    def test_floats(self):
        assert compress_numbers([1.0, 1.0, 2.5, 2.5]) == [1.0, 2.5]

    def test_mixed_int_and_float(self):
        # 1 и 1.0 считаются равными
        assert compress_numbers([1, 1.0, 2, 2.0]) == [1, 2]

    def test_zero_and_negative_zero(self):
        assert compress_numbers([0, -0, 1]) == [0, 1]


class TestReturnBehavior:
    def test_returns_new_list(self):
        source = [1, 1, 2, 2, 3]
        result = compress_numbers(source)
        assert result is not source

    def test_source_not_modified(self):
        source = [1, 1, 2, 2, 3]
        compress_numbers(source)
        assert source == [1, 1, 2, 2, 3]

    def test_returns_list_type(self):
        assert isinstance(compress_numbers((1, 1, 2)), list)

    def test_accepts_tuple(self):
        assert compress_numbers((1, 1, 2, 2, 3)) == [1, 2, 3]

    def test_accepts_generator(self):
        assert compress_numbers(x for x in [1, 1, 2, 2, 3]) == [1, 2, 3]

    def test_accepts_range(self):
        assert compress_numbers(range(3)) == [0, 1, 2]


class TestLongerSequences:
    def test_long_run(self):
        assert compress_numbers([1] * 1000 + [2] * 1000) == [1, 2]

    def test_many_alternations(self):
        data = [i % 2 for i in range(1000)]
        assert compress_numbers(data) == data

    @pytest.mark.parametrize(
        "source, expected",
        [
            ([1, 1, 2, 2, 3], [1, 2, 3]),
            ([0, 0, 1, 1, 0], [0, 1, 0]),
            ([], []),
            ([9], [9]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1, 1, 2, 3, 3], [3, 2, 1, 2, 3]),
        ],
    )
    def test_parametrized(self, source, expected):
        assert compress_numbers(source) == expected