# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from src.examples.hello_world import print_hi
from src.exercises.misc.minimum_by_column import example_column_minimums

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    output = example_column_minimums()
    # formatted_output = list(map(lambda v: list(map(lambda w: list(w), v)), output))
    print(output)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
