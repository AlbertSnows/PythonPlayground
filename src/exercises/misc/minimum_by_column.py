from functools import reduce
from itertools import takewhile

sample_data_1 = [{"a": 1, "b": 0, "c": 0, "d": 0},
                 {"a": 0, "b": 2, "c": 3, "d": 0},
                 {"a": 0, "b": 0, "c": 0, "d": 4}]
sd_2 = [{"a": 1}, {"a": 2}, {"a": 3}]

min_val_for_key = lambda data, column_name: (reduce(lambda min_val, row: min(min_val, row.get(column_name, 0)),
                                                    data,
                                                    float('inf')))

def minimum_rows_for_key(table, column_name, minimum_for_column):
    return filter(lambda row: row[column_name] == minimum_for_column, table)

def minimum_row_for_column(table, column_name):
    return minimum_rows_for_key(table, column_name, min_val_for_key(table, column_name))

min_by_columns = lambda table, column_priority: (reduce_while(

))

example_column_minimums = lambda: (map(lambda sample_data: min_by_column(sample_data, "a"),
                                       [sample_data_1, sd_2]))
