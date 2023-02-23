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
    return np.random.randint(2, size=2**var_qty)

PRE = r"""
\usepackage[russian, english]{babel}
\usepackage[T2A, T1]{fontenc}
\usepackage[utf8]{inputenc}
"""

MY_TEMPLATE = TexTemplate(documentclass=r'\documentclass{article}', preamble=PRE)





# class IntegerTableExampe(Scene):
#     def construct(self):
#         var_qty = 2
#         column_size = 2 ** var_qty
#         function_result = [0, 0, 1, 1]
#         table_data = make_truth_table(var_qty)
#         table_data = np.c_[table_data, function_result]

#         table = IntegerTable(table_data,
#             include_outer_lines=True,
#             top_left_entry=Text("N"),
#             col_labels=[Text('a'), Text('b'), Text('F')],
#             row_labels=[MathTex(str(i)) for i in range(column_size)]
#             )
#         table.scale(0.4)
#         self.add(table)

class FunctionNormalForms(Scene):
    def construct(self):
        title_1 = Title('Нормальные формы в логике', tex_template=MY_TEMPLATE)
        
        text_1 = 'Формула в булевой логике может быть записана в дизъюнктивной и в конъюнктивной нормальной форме. Также выделяют совершенную дизъюнктивную и совершенную конъюктивную нормальную форму'
        # tex_1 = Tex(text_1)

        self.add(title_1)
        # self.play(FadeIn(title_1))
        # self.play(FadeIn(tex_1))
        # self.wait()
