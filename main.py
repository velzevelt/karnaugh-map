from manim import *
import numpy as np
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


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


class FunctionNormalForms(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang='en'))

        title_1 = Title('Нормальные формы в логике', tex_template=MY_TEMPLATE)
        
        text_1 = 'Формула в булевой логике может быть записана в <span foreground="yellow">дизъюнктивной</span> и в <span foreground="yellow">конъюнктивной</span> нормальной форме.'
        text_2 = 'Также выделяют совершенную дизъюнктивную и совершенную конъюктивную нормальную форму.'
        text_1 = MarkupText(text_1, width=12, font_size=65)
        text_2 = MarkupText(text_2, width=12, font_size=65)

        text_1.next_to(title_1, DOWN, buff=1.0)
        text_2.next_to(text_1, DOWN)

        # self.add(title_1, text_1, text_2)
        # return

        self.wait()
        
        with self.voiceover(text="TITLE_1") as tracker:
            self.play(FadeIn(title_1))
        
        self.wait()
        
        with self.voiceover(text="TEXT_1") as tracker:
            self.play(AddTextLetterByLetter(text_1, run_time=2))
        
        self.wait()
        
        with self.voiceover(text="TEXT_2") as tracker:
            self.play(AddTextLetterByLetter(text_2, run_time=2))
        
        self.wait()
        self.play(FadeOut(title_1, text_1, text_2))
        self.wait()
        self.wait()


class KarnaughMapM2(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang='en'))

        title_1 = Title('Составление карты Карно. M=2', tex_template=MY_TEMPLATE)
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
            top_left_entry=top_left.copy(),
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
            top_left_entry=top_left.copy(),
            v_buff=0.4,
            h_buff=0.6,
            line_config={'stroke_width': 1},
        )
        
        
        Group(table, karnaugh_map).arrange_in_grid(buff=1)
        
        with self.voiceover(text="KARNO_CONSTRUCT_M=2") as tracker:
            self.play(FadeIn(title_1))
        
        self.wait()
        self.play(table.create())
        self.wait()
        self.play(karnaugh_map.create())
        self.wait()

        # Выделение номера
        box_1 = SurroundingRectangle(table.get_row_labels(), corner_radius=0.2)
        self.play(Create(box_1))
        
        # Выделение координат
        needle = VGroup(karnaugh_map.get_columns()[1][1:], karnaugh_map.get_columns()[2][1:])
        box_2 = SurroundingRectangle(needle, corner_radius=0.2)
        self.play(Create(box_2))
        self.play(Circumscribe(box_2))
        self.wait()
        
        # Стрелка от номера к координатам
        arrow_1 = Arrow(start=table.get_row_labels()[0], end=karnaugh_map.get_columns()[1][1])
        self.play(Create(arrow_1))
        self.wait()
        
        self.play(FadeOut(box_1, arrow_1))
        
        box_1 = SurroundingRectangle(table.get_columns()[-1][1:], corner_radius=0.2, color=GREEN)
        arrow_1 = Arrow(start=table.get_columns()[-1][1], end=karnaugh_map.get_columns()[1][1])
        with self.voiceover(text="ARROW_COORD") as tracker:
            self.play(Create(box_1))
            self.play(Create(arrow_1))
            self.wait()
        karnaugh_map_2.move_to(karnaugh_map.get_center())
        self.play(karnaugh_map.animate.become(karnaugh_map_2))
        self.wait()
        self.wait()
        
        # Завершение сцены
        self.play(FadeOut(box_1, arrow_1, box_2))
        self.wait()
        
        self.play(FadeOut(title_1, karnaugh_map))
        # Новый фрагмент

        with self.voiceover(text="SDNF_M=2_ALGEBRA") as tracker:
            title_1 = Title('Составление СДНФ. Алгебраический метод', tex_template=MY_TEMPLATE)
            self.play(FadeIn(title_1))
        self.wait()

        gr = VGroup(table.get_columns()[1:][0][3:], table.get_columns()[1:][1][3:], table.get_columns()[1:][2][3:])
        box_1 = SurroundingRectangle(gr, corner_radius=0.2)
        text_1 = MathTex(r"F = X_{1} \bar X_{2} \lor X_{1} X_{2}")
        # text_1 = Tex(r"${F = X_{1} \underline{\bar X_{2}} \lor X_{1} \underline{X_{2}}}$ \\ ${F = X_{1}}$", tex_template=MY_TEMPLATE)
        text_1.next_to(box_1.get_corner(UR) - 0.3, RIGHT, buff=1.0)

        self.play(Create(box_1))
        self.wait()
        self.play(Write(text_1))
        self.wait()
        self.play(text_1.animate.become(MathTex(r"F = X_{1} \underline{\bar X_{2}} \lor X_{1} \underline{X_{2}}").next_to(box_1.get_corner(UR) - 0.3, RIGHT, buff=1.0)))
        self.wait()
        self.play(text_1.animate.become(MathTex(r"F = X_{1} \underline{\bar X_{2}} \lor X_{1} \underline{X_{2}}").next_to(box_1.get_corner(UR) - 0.3, RIGHT, buff=1.0)))
        self.wait()
        self.play(text_1.animate.become(MathTex(r"F = X_{1}(\bar X_{2} + X_{2})}").next_to(box_1.get_corner(UR) - 0.3, RIGHT, buff=1.0)))
        self.wait()
        self.play(text_1.animate.become(MathTex(r"F = X_{1}").next_to(box_1.get_corner(UR) - 0.3, RIGHT, buff=1.0)))
        self.wait()
        self.play(FadeOut(title_1, box_1, text_1))


        with self.voiceover(text="SDNF_M=2_KARNO") as tracker:
            title_1 = Title('Составление СДНФ. Карта Карно', tex_template=MY_TEMPLATE)
            self.play(FadeIn(title_1))
        self.wait()

        self.play(table.animate.shift(LEFT))
        self.play(karnaugh_map_2.create())
        self.wait()
        
        gr = VGroup(karnaugh_map_2.get_rows()[-1][1:])
        box_1 = SurroundingRectangle(gr, corner_radius=0.2)

        text_1.next_to(box_1, DOWN, buff=0.5)
        self.play(Create(box_1))
        self.wait()
        self.play(Write(text_1))
        self.wait()
        self.play(FadeOut(text_1, box_1, table, karnaugh_map_2, title_1))
        self.wait()


class KarnaughMapM4(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang='en'))
        title_1 = Title('Составление карты Карно. M=4', tex_template=MY_TEMPLATE)
        var_qty = 4
        column_size = 2 ** var_qty
        function_result = [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1]
        table_data = make_truth_table(var_qty)
        table_data = np.c_[table_data, function_result]

        # Таблица истинности
        table = IntegerTable(table_data,
            include_outer_lines=True,
            top_left_entry=Tex('N'),
            col_labels=[Tex('$X_{1}$'), Tex('$X_{2}$'), Tex('$X_{3}$'), Tex('$X_{4}$'), Tex('F')],
            row_labels=[MathTex(str(i)) for i in range(column_size)],
            v_buff=0.2,
            h_buff=0.3,
            line_config={'stroke_width': 1}
            )
        

        t_1 = Tex('$X_{3}X_{4}$').rotate(PI / 2)
        t_2 = Tex('$X_{1}X_{2}$')
        t_1.rotate(PI / 4)
        t_2.rotate(PI / 4)

        top_left = MobjectTable([t_1, t_2], line_config={'stroke_width': 1.3},
            v_buff=0.4,
            h_buff=0.6,
        )
        top_left.rotate(-PI / 4)

        # Карта координат
        karnaugh_map = MobjectTable(
            [[Tex(0), Tex(1), Tex(3), Tex(2)], 
            [Tex(4), Tex(5), Tex(7), Tex(6)],
            [Tex(12), Tex(13), Tex(15), Tex(14)],
            [Tex(8), Tex(9), Tex(11), Tex(10)]
            ], 
            include_outer_lines=True,
            row_labels=[Tex('00'), Tex('01'), Tex('11'), Tex('10')],
            col_labels=[Tex('00').rotate(PI / 2), Tex('01').rotate(PI / 2), Tex('11').rotate(PI / 2), Tex('10').rotate(PI / 2)],
            top_left_entry=top_left.copy(),
            v_buff=0.4,
            h_buff=0.6,
            line_config={'stroke_width': 1},
        )

        # Настоящая карта
        karnaugh_map_2 = MobjectTable(
            [[Tex(0), Tex(0), Tex(0), Tex(0)], 
            [Tex(1), Tex(1), Tex(1), Tex(1)],
            [Tex(0), Tex(0), Tex(1), Tex(1)],
            [Tex(0), Tex(1), Tex(0), Tex(1)]
            ], 
            include_outer_lines=True,
            row_labels=[Tex('00'), Tex('01'), Tex('11'), Tex('10')],
            col_labels=[Tex('00').rotate(PI / 2), Tex('01').rotate(PI / 2), Tex('11').rotate(PI / 2), Tex('10').rotate(PI / 2)],
            top_left_entry=top_left.copy(),
            v_buff=0.4,
            h_buff=0.6,
            line_config={'stroke_width': 1},
        )
        

        table.scale(0.5)
        Group(table, karnaugh_map).arrange_in_grid(buff=1)
        
        self.wait()
        with self.voiceover(text="KARNO_CONSTRUCT_M=4") as tracker:
            self.play(FadeIn(title_1))
        self.wait()
        self.play(table.create())
        self.wait()
        self.play(karnaugh_map.create())
        self.wait()

        # Выделение номера
        box_1 = SurroundingRectangle(table.get_row_labels(), corner_radius=0.2)
        self.play(Create(box_1))
        
        # Выделение координат
        t = [c[1:] for c in karnaugh_map.get_rows()[1:]]
        needle = VGroup(*t)
        box_2 = SurroundingRectangle(needle, corner_radius=0.2)
        self.play(Create(box_2))
        self.play(Circumscribe(box_2))
        self.wait()
        
        # Стрелка от номера к координатам
        arrow_1 = Arrow(start=table.get_row_labels()[0], end=karnaugh_map.get_columns()[1][1])
        self.play(Create(arrow_1))
        self.wait()
        
        self.play(FadeOut(box_1, arrow_1))
        
        # Подстановка значений в координаты. Объяснение
        with self.voiceover(text="ARROW_COORD") as tracker:
            box_1 = SurroundingRectangle(table.get_columns()[-1][1:], corner_radius=0.2, color=GREEN)
            arrow_1 = Arrow(start=table.get_columns()[-1][1], end=karnaugh_map.get_columns()[1][1])
            self.play(Create(box_1))
            self.play(Create(arrow_1))
        self.wait()

        karnaugh_map_2.move_to(karnaugh_map.get_center())
        self.play(karnaugh_map.animate.become(karnaugh_map_2))
        self.wait()
        
        # Завершение сцены
        self.play(FadeOut(box_1, arrow_1, box_2))
        self.wait()
        
        self.play(FadeOut(title_1, karnaugh_map, table))
        # Новый фрагмент

        title_1 = Title('Составление СДНФ. Карта Карно', tex_template=MY_TEMPLATE)
        with self.voiceover(text="SDNF_M=4_KARNO") as tracker:
            self.play(FadeIn(title_1))
        self.wait()

        karnaugh_map_2.scale(2.0)
        karnaugh_map_2.next_to(title_1, DOWN, buff=0.6)

        self.play(karnaugh_map_2.create())
        self.play(karnaugh_map_2.animate.to_edge(LEFT, buff=1.0))
        self.wait()
        
        gr = [karnaugh_map_2.get_rows()[2][1:], VGroup(karnaugh_map_2.get_columns()[3][2:4], karnaugh_map_2.get_columns()[4][2:4]), karnaugh_map_2.get_columns()[2][-1], VGroup(karnaugh_map_2.get_columns()[-1][-2], karnaugh_map_2.get_columns()[-1][-1]), VGroup(karnaugh_map_2.get_columns()[-1][-3], karnaugh_map_2.get_columns()[-1][-2])]
        box_1 = SurroundingRectangle(gr[0], corner_radius=0.2)
        box_2 = SurroundingRectangle(gr[1], corner_radius=0.2, color=GREEN).scale(1.1)
        box_3 = SurroundingRectangle(gr[2], corner_radius=0.2, color=RED)
        box_4 = SurroundingRectangle(gr[3], corner_radius=0.2, color=BLUE).scale(1.15)
        # box_5 = SurroundingRectangle(gr[4], corner_radius=0.2, color=PURPLE).scale(1.20)
        
        boxes = [box_1, box_2, box_3, box_4]
        boxes = AnimationGroup(*[Create(i) for i in boxes], lag_ratio=2)

        self.play(boxes)
        self.wait()
        
        tex_1 = Tex("$S_{1}$", color=YELLOW)
        tex_2 = Tex("$S_{2}$", color=GREEN)
        tex_3 = Tex("$S_{3}$", color=RED)
        tex_4 = Tex("$S_{4}$", color=BLUE)
        # tex_5 = Tex("$S_{5}$", color=PURPLE)

        VGroup(tex_1, tex_2, tex_3, tex_4).arrange(DOWN).next_to(karnaugh_map_2, buff=1.0)

        arrow_1 = always_redraw(lambda: Arrow(start=box_1, end=tex_1, color=YELLOW))
        arrow_2 = always_redraw(lambda: Arrow(start=box_2.get_corner(RIGHT), end=tex_2, color=GREEN))
        arrow_3 = always_redraw(lambda: Arrow(start=box_3, end=tex_3, color=RED))
        arrow_4 = always_redraw(lambda: Arrow(start=box_4.get_corner(DR), end=tex_4, color=BLUE))
        # arrow_5 = always_redraw(lambda: Arrow(start=box_5.get_corner(DR), end=tex_5, color=PURPLE))

        texes = AnimationGroup(*[Write(i) for i in [tex_1, tex_2, tex_3, tex_4]], lag_ratio=1)
        arrows = [arrow_1, arrow_2, arrow_3, arrow_4]
        arrows = AnimationGroup(*[Create(i) for i in arrows], lag_ratio=1)

        self.play(texes, arrows)
        self.wait()

        func_1 = always_redraw(lambda: MathTex(r'\bar X_{1} X_{2}').next_to(tex_1))
        func_2 = always_redraw(lambda: MathTex(r'X_{2} X_{3}').next_to(tex_2))
        func_3 = always_redraw(lambda: MathTex(r'X_{1} \bar X_{2} \bar X_{3} X_{4}').next_to(tex_3))
        func_4 = always_redraw(lambda: MathTex(r'X_{1} X_{3} \bar X_{4}').next_to(tex_4))
        # func_5 = always_redraw(lambda: MathTex(r'X_{2} X_{3} \bar X_{4}').next_to(tex_5))

        funcs = [func_1, func_2, func_3, func_4]
        funcs = AnimationGroup(*[Write(i) for i in funcs], lag_ratio=1)

        self.play(funcs)
        self.wait()
        
        gr = VGroup(tex_1, tex_2, tex_3, tex_4)
        self.play(gr.animate.shift(UP))
        self.wait()

        total_tex = MathTex(r'F = \bar X_{1} X_{2} \lor X_{2} X_{3} \\ \lor X_{1} \bar X_{2} \bar X_{3} X_{4} \lor X_{1} X_{3} \bar X_{4}').scale(0.8)
        
        total_tex.next_to(func_4, DOWN, buff=0.5)
        total_tex.shift(np.array([0.5, 0., 0.]))
        
        self.play(Write(total_tex))
        self.wait()
        self.play(FadeOut(title_1, total_tex, karnaugh_map_2, *[func_1, func_2, func_3, func_4], *[arrow_1, arrow_2, arrow_3, arrow_4], *[tex_1, tex_2, tex_3, tex_4], *[box_1, box_2, box_3, box_4]))
        self.wait()


