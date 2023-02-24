from manim import *
import numpy as np



def make_text(text, font_size, width_from: MarkupText) -> MarkupText:
    if width_from:
        res = MarkupText(text)
        res.font_size = font_size
        res.width = width_from.width
    else:
        res = MarkupText(text)
        res.font_size = font_size
    return res


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
    
    result = np.fliplr(result)
    return result


def get_rand_function_result(var_qty: int) -> list:
    return np.random.randint(2, size=2**var_qty)


PRE = r"""
\usepackage[english, russian]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T2A, T1]{fontenc}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{setspace}
\usepackage{tipa}
\usepackage{relsize}
\usepackage{textcomp}
\usepackage{mathrsfs}
\usepackage{calligra}
\usepackage{wasysym}
\usepackage{ragged2e}
\usepackage{xcolor}
\usepackage{microtype}
\DisableLigatures{encoding = *, family = * }
\linespread{1}
"""

MY_TEMPLATE = TexTemplate(documentclass=r'\documentclass{article}', preamble=PRE, placeholder_text='placeholder')


# class IntegerTableExample(Scene):
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
        
        text_1 = 'Формула в булевой логике может быть записана в <span foreground="yellow">дизъюнктивной</span> и в <span foreground="yellow">конъюнктивной</span> нормальной форме.'
        text_2 = 'Также выделяют совершенную дизъюнктивную и совершенную конъюктивную нормальную форму.'
        text_1 = make_text(text_1, font_size=24, width_from=None)
        text_2 = make_text(text_2, font_size=24, width_from=text_1)

        text_2.next_to(text_1, DOWN)

        # self.add(title_1)
        # self.add(text_1, text_2)

        self.wait()
        self.play(FadeIn(title_1))
        self.wait()
        self.play(AddTextLetterByLetter(text_1, run_time=2))
        self.wait()
        self.play(AddTextLetterByLetter(text_2, run_time=2))
        self.wait()


class DisjunctiveNormalForm(Scene):
    def construct(self):
        
        title_1 = Title('Дизъюнктивная нормальная форма', tex_template=MY_TEMPLATE)
        
        text_1 = 'Дизъюнктивная нормальная форма (ДНФ) в булевой логике — нормальная форма, в которой булева формула имеет вид дизъюнкции конъюнкций литералов. Любая булева формула может быть приведена к ДНФ.'
        text_2 = 'Для этого можно использовать <span foreground="yellow">закон двойного отрицания, закон де Моргана, закон дистрибутивности.</span>'
        text_3 = 'Дизъюнктивная нормальная форма удобна для автоматического доказательства теорем.'
        text_1 = make_text(text_1, 24, None)
        text_2 = make_text(text_2, 24, text_1)
        text_3 = make_text(text_2, 24, text_1)

        text_2.next_to(text_1, DOWN)
        text_3.next_to(text_2, DOWN)

        example = r'${A\lor B}$ \\ ${\displaystyle (A\land B)\lor {\overline {A}}}$ \\ ${\displaystyle (A\land B\land {\overline {C}})\lor ({\overline {D}}\land E\land F)\lor (C\land D)\lor B}$'
        example = Tex(example)

        self.wait()
        self.play(FadeIn(title_1))
        self.wait()
        self.play(AddTextLetterByLetter(text_1, run_time=6))
        self.wait()
        self.play(AddTextLetterByLetter(text_2, run_time=2))
        self.wait()
        self.play(AddTextLetterByLetter(text_3, run_time=2))
        self.wait()
        self.play(FadeOut(text_1, text_2, text_3, title_1))
        
        title_1 = Title('Примеры ДНФ', tex_template=MY_TEMPLATE)
        self.play(FadeIn(title_1, example))
        self.wait()
        self.play(FadeOut(title_1, example))
        
        title_1 = Title('Построение ДНФ', tex_template=MY_TEMPLATE)
        text_1 = make_text('Избавиться от всех логических операций, содержащихся в формуле, заменив их основными: конъюнкцией, дизъюнкцией, отрицанием. Это можно сделать, используя равносильные формулы:', 24)
        example = Tex(r'${A\rightarrow B=\neg A\vee B}$ \\ ${A\leftrightarrow B=(A\wedge B)\vee (\neg A\wedge \neg B)}$')
        example.next_to(text_1, DOWN, buff=0.8)

        self.play(FadeIn(title_1), AddTextLetterByLetter(text_1, run_time=6.0))
        self.wait()
        self.play(Write(example))
        self.wait()
    