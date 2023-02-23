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

t = make_truth_table(2)
t = np.append(t, 0, axis=1)
print(t)


class IntegerTableExampe(Scene):
    def construct(self):
        var_qty = 2
        column_size = 2 ** var_qty

        table_data = make_truth_table(var_qty)
        table = IntegerTable(table_data,
            include_outer_lines=True,
            top_left_entry=Text("N"),
            col_labels=[Text('a'), Text('b'), Text('F')],
            row_labels=[MathTex(str(i)) for i in range(column_size)]
            )
        table.scale(0.4)
        self.add(table)
