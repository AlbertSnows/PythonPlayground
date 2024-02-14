from functools import reduce
from src.lib.collections import first, rest
from src.lib.functions import reduce_while

sample_data_1 = [{"a": 1, "b": 0, "c": 0, "d": 0},
                 {"a": 0, "b": 2, "c": 3, "d": 0},
                 {"a": 0, "b": 0, "c": 0, "d": 4}]
sd_2 = [{"a": 1}, {"a": 2}, {"a": 3}]


def minimum_value_for_column(data, column_name):
    return reduce(lambda min_val, row: min(min_val, row.get(column_name, 0)), data, float('inf'))


def rows_with_column_minimum(table, column_name, minimum_for_column):
    return filter(lambda row: row[column_name] == minimum_for_column, table)


def minimum_rows_for_key(table, column_name):
    """
    :param table: [{...}, ...]
    :param column_name: [...]
    :return: filter obj
    """
    filtered_rows = rows_with_column_minimum(table, column_name, minimum_value_for_column(table, column_name))
    return filtered_rows


def random_minimum_row_for_column(table, column_name):
    return first(list(minimum_rows_for_key(table, column_name)))


#
def minimum_row_for_columns(table, columns):
    """
    given a set of rows T and columns [a, b, c, ...]
    takes min_rows(T(a)) and iterates over [b, c, ...] until
    len(T) == 1, or we run out of columns
    """
    return reduce_while(
        lambda remaining_rows, _: len(remaining_rows) > 1,
        lambda remaining_rows, column_name: list(minimum_rows_for_key(remaining_rows, column_name)),
        rest(columns),
        list(minimum_rows_for_key(table, first(columns))))


sd_3 = [{"a": 1, "b": 2},
        {"a": 1, "b": 3},
        {"a": 1, "b": 4}]


def example_column_minimums():
    first_example = map(
        lambda sample_data: random_minimum_row_for_column(sample_data, "a"),
        [sample_data_1, sd_2])
    second_example = map(lambda table: minimum_row_for_columns(table, ["a", "b"]), [sd_3])
    return [first_example, second_example]
