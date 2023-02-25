from manim import *
import numpy as np



def make_text(text, font_size, width_from: MarkupText = None) -> MarkupText:
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
            if counter == 2**i:
                counter = 0
                temp = 1 if temp == 0 else 0
            result[j][i] = temp
            counter += 1
    
    result = np.fliplr(result)
    return result



def get_rand_function_result(var_qty: int) -> list:
    return np.random.randint(2, size=2**var_qty)


PRE = r"""
\usepackage[utf8]{inputenc}
\usepackage[english, russian]{babel}
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

MY_TEMPLATE = TexTemplate(preamble=PRE)


class FunctionNormalForms(Scene):
    def construct(self):
        
        title_1 = Title('Нормальные формы в логике', tex_template=MY_TEMPLATE)
        
        text_1 = 'Формула в булевой логике может быть записана в <span foreground="yellow">дизъюнктивной</span> и в <span foreground="yellow">конъюнктивной</span> нормальной форме.'
        text_2 = 'Также выделяют совершенную дизъюнктивную и совершенную конъюктивную нормальную форму.'
        text_1 = make_text(text_1, font_size=24, width_from=None)
        text_2 = make_text(text_2, font_size=24, width_from=text_1)

        text_1.next_to(title_1, DOWN, buff=1.0)
        text_2.next_to(text_1, DOWN)

        self.wait()
        self.play(FadeIn(title_1))
        self.wait()
        self.play(AddTextLetterByLetter(text_1, run_time=2))
        self.wait()
        self.play(AddTextLetterByLetter(text_2, run_time=2))
        self.wait()
        self.play(FadeOut(title_1, text_1, text_2))
        self.wait()


class DisjunctiveNormalForm(Scene):
    def construct(self):
        
        title_1 = Title('Дизъюнктивная нормальная форма', tex_template=MY_TEMPLATE)
        
        text_1 = 'Дизъюнктивная нормальная форма (ДНФ) в булевой логике — нормальная форма, в которой булева формула имеет вид дизъюнкции конъюнкций литералов. Любая булева формула может быть приведена к ДНФ.'
        text_2 = 'Для этого можно использовать <span foreground="yellow">закон двойного отрицания, закон де Моргана, закон дистрибутивности.</span>'
        text_3 = 'Дизъюнктивная нормальная форма удобна для автоматического доказательства теорем.'
        text_1 = make_text(text_1, 24, None)
        text_2 = make_text(text_2, 24, text_1)
        text_3 = make_text(text_3, 24, text_1)

        text_1.next_to(title_1, DOWN, buff=1.0)
        text_2.next_to(text_1, DOWN)
        text_3.next_to(text_2, DOWN)

        example_1 = r'${A\lor B}$ \\ ${\displaystyle (A\land B)\lor {\overline {A}}}$ \\ ${\displaystyle (A\land B\land {\overline {C}})\lor ({\overline {D}}\land E\land F)\lor (C\land D)\lor B}$'
        example_1 = Tex(example_1)

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
        self.play(FadeIn(title_1, example_1))
        self.wait()
        self.play(FadeOut(title_1, example_1))
        
        title_1 = Title('Построение ДНФ', tex_template=MY_TEMPLATE)
        text_1 = make_text('Избавиться от всех логических операций, содержащихся в формуле, заменив их основными: конъюнкцией, дизъюнкцией, отрицанием. Это можно сделать, используя равносильные формулы:', 24)
        text_1.next_to(title_1, DOWN, buff=1.0)
        example_1 = Tex(r'${A\rightarrow B=\neg A\vee B}$ \\ ${A\leftrightarrow B=(A\wedge B)\vee (\neg A\wedge \neg B)}$')
        example_1.next_to(text_1, DOWN, buff=0.8)

        self.play(FadeIn(title_1))
        self.play(AddTextLetterByLetter(text_1, run_time=6.0))
        self.wait()
        self.play(Write(example_1))
        self.wait()
        self.play(FadeOut(text_1))
        example_2 = Tex(r'${\neg (A\vee B)=\neg A\wedge \neg B}$ \\ ${\neg (A\wedge B)=\neg A\vee \neg B}$')
        example_2.next_to(example_1, UP)
        self.play(Write(example_2))
        self.wait()

        self.play(FadeOut(title_1, example_1, example_2))
        
        title_1 = Title('Пример построения ДНФ', tex_template=MY_TEMPLATE)
        text_1 = make_text('Приведем к ДНФ формулу', 24)
        text_1.next_to(title_1, DOWN, buff=1.0)
        
        func_1 = Tex(r'${\displaystyle F=\neg ((X\rightarrow Y)\vee \neg (Y\rightarrow Z))}$')
        func_2 = Tex(r'1) ${\displaystyle F=\neg ((\neg X\vee Y)\vee \neg (\neg Y\vee Z))}$')
        func_3 = Tex(r'2) ${\displaystyle F=(\neg \neg X\wedge \neg Y)\wedge (\neg Y\vee Z)=(X\wedge \neg Y)\wedge (\neg Y\vee Z)}$')
        func_4 = Tex(r'3) ${\displaystyle F=(X\wedge \neg Y\wedge \neg Y)\vee (X\wedge \neg Y\wedge Z)}$')
        
        VGroup(func_1, func_2, func_3, func_4).arrange(DOWN).next_to(text_1, DOWN)

        self.play(FadeIn(title_1))
        self.play(AddTextLetterByLetter(text_1))
        self.play(Write(func_1))
        self.wait()
        self.play(FadeOut(text_1))
        self.wait()
        self.play(Write(func_2))
        self.wait()
        self.play(Write(func_3))
        self.wait()
        self.play(Write(func_4))
        self.wait()
        self.play(FadeOut(title_1, func_1, func_2, func_3, func_4))
        self.wait()
        
        title_1 = Title('Совершенная дизъюнктивная нормальная форма', tex_template=MY_TEMPLATE)
        text_1 = make_text('(СДНФ) — одна из форм представления функции алгебры логики (булевой функции) в виде логического выражения. Представляет собой частный случай ДНФ, удовлетворяющий следующим трём условиям: ', font_size=20)
        text_2 = make_text('1) В ней нет одинаковых слагаемых (элементарных конъюнкций);', font_size=20)
        text_3 = make_text('2) В каждом слагаемом нет повторяющихся переменных;', font_size=20)
        text_4 = make_text('3) Каждое слагаемое содержит все переменные, от которых зависит булева функция (каждая переменная может входить в слагаемое либо в прямой, либо в инверсной форме).', font_size=20)
        VGroup(text_1, text_2, text_3, text_4).arrange(DOWN).next_to(title_1, DOWN, buff=1.0)

        self.play(FadeIn(title_1))
        self.play(AddTextLetterByLetter(text_1, run_time=6.0))
        self.play(Write(text_2, run_time=2.0))
        self.play(Write(text_3, run_time=2.0))
        self.play(Write(text_4, run_time=5.0))
        self.wait()
        self.play(FadeOut(title_1, text_1, text_2, text_3, text_4))

        title_1 = Title('Переход от ДНФ к СДНФ', tex_template=MY_TEMPLATE)
        transition_1 = Tex(r'${X\vee \neg Y\neg Z=X(Y\vee \neg Y)(Z\vee \neg Z)\vee (X\vee \neg X)\neg Y\neg Z=}$ \\ ${XYZ\vee X\neg YZ\vee XY\neg Z\vee X\neg Y\neg Z\vee X\neg Y\neg Z\vee \neg X\neg Y\neg Z=}$ \\ ${=XYZ\vee X\neg YZ\vee XY\neg Z\vee X\neg Y\neg Z\vee \neg X\neg Y\neg Z}$')
        transition_1.next_to(title_1, DOWN, buff=1.0)
        self.play(FadeIn(title_1))
        self.wait()
        self.play(Write(transition_1, run_time=8.0))
        self.wait()


class KarnaughMap(Scene):
    def construct(self):
        title_1 = Title('Составление карты Карно', tex_template=MY_TEMPLATE)
        var_qty = 2
        column_size = 2 ** var_qty
        # function_result = [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1]
        function_result = [0, 0, 1, 1]
        table_data = make_truth_table(var_qty)
        table_data = np.c_[table_data, function_result]

        # Таблица истинности
        table = IntegerTable(table_data,
            include_outer_lines=True,
            top_left_entry=Tex('N'),
            col_labels=[Tex('$X_{1}$'), Tex('$X_{2}$'), Tex('F')],
            # col_labels=[Tex('$X_{1}$'), Tex('$X_{2}$'), Tex('$X_{3}$'), Tex('$X_{4}$'), Tex('F')],
            row_labels=[MathTex(str(i)) for i in range(column_size)],
            v_buff=0.4,
            h_buff=0.6,
            line_config={'stroke_width': 1}
            )
        

        t_1 = Tex('$X_{2}$')
        t_2 = Tex('$X_{1}$')
        t_1.rotate(PI / 4)
        t_2.rotate(PI / 4)

        top_left = MobjectTable([t_1, t_2], line_config={'stroke_width': 1.3},
            v_buff=0.4,
            h_buff=0.6,
        )
        top_left.rotate(-PI / 4)

        # Карта координат
        karnaugh_map = MobjectTable(
            [[Tex(0), Tex(1)], [Tex(2), Tex(3)]], 
            include_outer_lines=True,
            col_labels=[Tex(0), Tex(1)],
            row_labels=[Tex(0), Tex(1)],
            top_left_entry=top_left,
            v_buff=0.4,
            h_buff=0.6,
            line_config={'stroke_width': 1},
        )

        # Настоящая карта
        karnaugh_map_2 = MobjectTable(
            [[Tex(0), Tex(0)], [Tex(1), Tex(1)]], 
            include_outer_lines=True,
            col_labels=[Tex(0), Tex(1)],
            row_labels=[Tex(0), Tex(1)],
            top_left_entry=top_left,
            v_buff=0.4,
            h_buff=0.6,
            line_config={'stroke_width': 1},
        )
        
        
        Group(table, karnaugh_map).arrange_in_grid(buff=1)
        
        

        # Подстановка значений в координаты
        # table.add(SurroundingRectangle(table.get_columns()[-1][1:], corner_radius=0.2, color=GREEN))
        # arrow_2 = Arrow(start=table.get_columns()[-1][1], end=karnaugh_map.get_columns()[1][1])

        # self.add(arrow_1)
        # self.add(title_1)
        # self.add(table)
        # self.add(karnaugh_map)
        
        self.play(FadeIn(title_1))
        self.wait()
        self.play(table.create())
        self.wait()
        self.play(karnaugh_map.create())
        self.wait()

        # Выделение координат
        self.play(table.animate.add(SurroundingRectangle(table.get_row_labels(), corner_radius=0.2)))
        
        # needle = VGroup(karnaugh_map.get_columns()[1][1:], karnaugh_map.get_columns()[2][1:])
        # karnaugh_map.add(SurroundingRectangle(needle, corner_radius=0.2))
        # arrow_1 = Arrow(start=table.get_row_labels()[0], end=karnaugh_map.get_columns()[1][1])