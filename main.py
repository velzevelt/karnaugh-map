from manim import *
import numpy as np


def make_truth_table(var_qty: int) -> list:
    column_max_size = 2 ** var_qty
    result = np.zeros(shape=(column_max_size, var_qty), dtype=int)
    for i in range(var_qty):
        counter = 0
        temp = 0
        for j in range(column_max_size):
            if counter == i + 1:
                counter = 0
                temp = 1 if temp == 0 else 0
            result[j][i] = temp
            counter += 1
    
    return result


def get_rand_function_result(var_qty: int) -> list:
    return np.random.randint(2, size=var_qty**2)


class IntegerTableExampe(Scene):
    def construct(self):
        var_qty = 2
        column_size = 2 ** var_qty
        function_result = [0, 0, 1, 1]
        table_data = make_truth_table(var_qty)
        table_data = np.c_[table_data, function_result]

        table = IntegerTable(table_data,
            include_outer_lines=True,
            top_left_entry=Text("N"),
            col_labels=[Text('a'), Text('b'), Text('F')],
            row_labels=[MathTex(str(i)) for i in range(column_size)]
            )
        table.scale(0.4)
        self.add(table)
