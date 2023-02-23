from manim import *
import numpy as np


def make_truth_table(var_qty: int) -> list:
    column_max_size = 2 ** var_qty
    result = np.zeros(shape=(var_qty, column_max_size), dtype=int)
    for i in range(var_qty):
        counter = 0
        temp = 0
        for j in range(column_max_size):
            if counter == i + 1:
                counter = 0
                temp = 1 if temp == 0 else 0
            result[i][j] = temp
            counter += 1
    
    return result


class MathTableExampe(Scene):
    def construct(self):
        table_data = make_truth_table(var_qty=2)
        table = MathTable(table_data,
            include_outer_lines=True
            )
        self.add(table)
