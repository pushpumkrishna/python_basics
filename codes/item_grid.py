#!/usr/bin/env python
from typing import Any

row = 4
column = 3
test_string = "| aaa | aaa | aaa |"

print("-" * 20)


def grid_maker(rows: int,
               columns: int,
               string: str) -> Any:
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if i == 0 or j == 5:
                print(" ", end=" ")
            else:
                print("| aaa | aaa | aaa |")
                if i == 3 or i == 6 or i == 10:
                    print("-" * 20)


# uncomment below to run
# grid_maker(row, column, test_string)
