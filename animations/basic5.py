from manim import *

W = 10

class AlgoS(Scene):
    def construct(self):
        # Create a rectangle
        rectangle = Rectangle(width=W, height=1, color=WHITE, fill_opacity=0.4)
        rectangle.move_to(ORIGIN + 1*DOWN)

        # Divide the rectangle into three parts
        line1 = Line(rectangle.get_corner([-1,-1,0]) + 0.4*W*RIGHT, rectangle.get_corner([-1,1,0]) + 0.4*W*RIGHT, color=BLUE_D)
        line2 = Line(rectangle.get_corner([-1,-1,0]) + 0.7*W*RIGHT, rectangle.get_corner([-1,1,0]) + 0.7*W*RIGHT, color=BLUE_D)

        # Label the sides
        label_left = Tex("0", color=WHITE).next_to(rectangle, LEFT)
        label_right = Tex("1", color=WHITE).next_to(rectangle, RIGHT)
        label_04 = Tex("$\\alpha$", color=WHITE).next_to(line1, DOWN)
        label_07 = Tex("$\\beta$", color=WHITE).next_to(line2, DOWN)

        # Create labels for regions
        label_X1 = Tex("$X_1$", color=WHITE).next_to(line2, LEFT)


        # Create an arrow and label for V_3
        arrow = Arrow(line1.get_center() + 0.15*W*RIGHT, line1.get_center() + 0.25*W*RIGHT + 2*DOWN, buff=0.2)
        label_V3 = Tex("$V_1([\\alpha,\\beta]) = \\frac{V_1[0,1]}{3}$", color=WHITE).next_to(arrow, DOWN)

        # Show everything
        self.play(Create(rectangle), Write(label_left), Write(label_right))
        self.wait(0.5)
        self.play(Create(line1), Create(line2), Write(label_04),Write(label_07))
        self.wait(0.5)
        self.play(Create(arrow), Write(label_V3), Create(label_X1))
        self.wait(2)

        # Divide the intervals [0, 0.4] and [0.7, 1] into four parts each
        lines_x1 = [Line(rectangle.get_corner([-1,-1,0])+ 0.1 *W * (i + 1)* RIGHT, rectangle.get_corner([-1,1,0])+ 0.1 *W* (i + 1) * RIGHT, color=YELLOW) for i in range(3)]
        lines_x2 = [Line(rectangle.get_corner([-1,-1,0])+ (0.7 + (0.3/4)*(i + 1 ))*W* RIGHT, rectangle.get_corner([-1,1,0])+ (0.7 + (0.3/4)*(i+1))*W* RIGHT, color=ORANGE) for i in range(3)]

        labs = ["$X_3$","$X_2$","$X_2$","$X_3$"]
        labels_x1 = [Tex(t, color=WHITE).next_to(line, LEFT) for (line,t) in zip(lines_x1,labs)]
        labels_x1.append(Tex("$X_3$", color=WHITE).next_to(lines_x1[-1], RIGHT))
        labels_x2 = [Tex(t, color=WHITE).next_to(line, (0.35/4)*LEFT) for (line,t) in zip(lines_x2,labs)]
        labels_x2.append(Tex("$X_3$", color=WHITE).next_to(lines_x2[-1], (0.35/4)*RIGHT))
        

        self.play(*[Create(line) for line in lines_x1], *[Write(label) for label in labels_x1])
        self.wait(1)
        self.play(*[Create(line) for line in lines_x2], *[Write(label) for label in labels_x2])
        self.wait(2)
        
        
        axes = Axes(
            x_range=[0, 1],
            y_range=[0, 0.6],
            axis_config={"color": BLUE,"include_numbers": False},
            x_length = W,
            y_length = 2,
            tips=True,
        ).add_coordinates()
        
        axes.move_to(ORIGIN + 2*UP)
        
        
        def a1util(x):
            if x >= 0.4 and x <= 0.7:
                return 0
            elif x <= 0.4:
                return x + 0.1
            else:
                return -1.3*x + 1.4

        u1 = axes.plot(a1util, color=GREEN_C, discontinuities=[0.4,0.7])
        
        dotted_lines = VGroup()
        for x_value in [0,0.1,0.2,0.3,0.4,0.7,0.7 + (0.3/4),0.7 + 2*(0.3/4),0.7 + 3*(0.3/4),1]:
            if x_value <= 0.4:
                h = x_value + 0.1
            else:
                h = -1.3*x_value + 1.4
            dotted_line = DashedLine(axes.c2p(x_value, 0), axes.c2p(x_value, h), stroke_width=2)
            dotted_lines.add(dotted_line)
            
        
        coords_to_point = [axes.c2p(x, 0) for x in [0,0.1,0.2,0.3]]
        coords_to_point2 = [axes.c2p(x, 0) for x in [0.7,0.7 + (0.3/4),0.7 + 2*(0.3/4),0.7 + 3*(0.3/4)]]
        
        labs = ["$X_3$","$X_2$","$X_2$","$X_3$"]
        labels_x1 = [Tex(t, color=WHITE).next_to(corrd, RIGHT + UP) for (corrd,t) in zip(coords_to_point,labs)]
        # labels_x1.append(Tex("$X_3$", color=WHITE).next_to(coords_to_point[-1], RIGHT))
        
        
        labels_x2 = [Tex(t, color=WHITE).next_to(line, RIGHT*0.3/4 + UP) for (line,t) in zip(coords_to_point2,labs)]
        # labels_x2.append(Tex("$X_3$", color=WHITE).next_to(coords_to_point2[-1], RIGHT))
        
                
        self.play(Create(axes))
        self.play(Create(u1))
        self.play(Create(dotted_lines))
        
        self.wait(1)
        
        self.play(*[Write(label) for label in labels_x1])
        self.play(*[Write(label) for label in labels_x2])
        
        color_to_use = ORANGE  
        area1 = axes.get_area(u1, [0, 0.1], color=color_to_use, opacity=0.5)
        area2 = axes.get_area(u1, [0.3, 0.4], color=color_to_use, opacity=0.5)
        area3 = axes.get_area(u1, [0.7, 0.7 + 0.3/4], color=color_to_use, opacity=0.5)
        area4 = axes.get_area(u1, [ 1 - 0.3/4,1], color=color_to_use, opacity=0.5)
        
        self.play(Create(area1),Create(area2),Create(area3),Create(area4))
        self.play(FadeOut(arrow),FadeOut(label_V3))
        
        label_V32 = Tex("$V_3([X_3]) = V_3([X_2]) \geq V_3([X_1]) $", color=WHITE).next_to(rectangle, 3*DOWN)
        
        self.play(Create(label_V32))
        
        self.wait(1)
        
        
        poly1_points = [[0,0,0],[0.1,0,0],[0.1,0.2,0],[0,0.1,0]]
        poly2_points = [[0.1,0,0],[0.2,0,0],[0.2,0.3,0],[0.1,0.2,0]]
        
        trapezium1 = Polygon(*[axes.c2p(a,b) for (a,b,c) in poly1_points], fill_color=ORANGE, fill_opacity=0.5, color=PURPLE_A)
        trapezium2 = Polygon(*[axes.c2p(a,b) for (a,b,c) in poly2_points], fill_color=PURPLE_C, fill_opacity=0, color=GRAY_B)
        
        self.play(Create(trapezium1),Create(trapezium2))
        
        
        
        # trapezium1.generate_target()
        
        # self.play(TransformMatchingShapes(trapezium1,trapezium3),MoveToTarget(trapezium1))
        
        self.play(Rotate(trapezium1,angle=-PI,about_point=axes.c2p(0.2,0.3)), Rotate(trapezium2,angle=-PI,about_point=axes.c2p(0.2,0.3)))
        
        self.wait(1)
        
        self.play(FadeOut(trapezium1),FadeOut(trapezium2))
        # self.play(Transform(trapezium1,trapezium3),Transform(trapezium2,trapezium4))
        
        # self.play()
        # self.play()
        
        # self.play(MoveToTarget(trapezium1))
        # trapezium1.add_updater(lambda mob, dt: mob.rotate(180*DEGREES))

        # trapezium1.add_updater(lambda mob, dt: mob.shift(axes.c2p(0.2,0.3)))
        
        # trapezium1.clear_updaters()

        
        def a2util(x):
            if x >= 0.4 and x <= 0.7:
                return 0
            elif x <= 0.4:
                return -1*x + 0.45
            else:
                return x - 0.66

        u2 = axes.plot(a2util, color=GREEN_C, discontinuities=[0.4,0.7])
        
        dotted_lines2 = VGroup()
        for x_value in [0,0.1,0.2,0.3,0.4,0.7,0.7 + (0.3/4),0.7 + 2*(0.3/4),0.7 + 3*(0.3/4),1]:
            x = x_value
            if x_value <= 0.4:
                h = -1*x + 0.45
            else:
                h = x - 0.66
            dotted_line = DashedLine(axes.c2p(x_value, 0), axes.c2p(x_value, h), stroke_width=2)
            dotted_lines2.add(dotted_line)
        
        color_to_use = GREEN_C  
        area11 = axes.get_area(u2, [0.1, 0.2], color=color_to_use, opacity=0.5)
        area21 = axes.get_area(u2, [0.2, 0.3], color=color_to_use, opacity=0.5)
        area31 = axes.get_area(u2, [0.7 + 0.3/4, 0.7 + 0.6/4], color=color_to_use, opacity=0.5)
        area41 = axes.get_area(u2, [1 - 0.6/4, 1 - 0.3/4], color=color_to_use, opacity=0.5)
        
        self.play(Transform(u1,u2),Transform(dotted_lines,dotted_lines2),Transform(area1,area11),Transform(area2,area21),Transform(area3,area31),Transform(area4,area41))
        
        label_V33 = Tex("$V_2([X_2]) = V_2([X_3]) \geq V_2([X_1]) $", color=WHITE).next_to(rectangle, 3*DOWN)
        
        self.play(Transform(label_V32,label_V33))
        
        self.wait(1)
        
        def a3util(x):
            if x >= 0.4 and x <= 0.7:
                return 0
            elif x <= 0.4:
                return -0.5*x + 0.3
            else:
                return 0.2*x

        u3 = axes.plot(a3util, color=GREEN_C, discontinuities=[0.4,0.7])
        
        dotted_lines3 = VGroup()
        for x_value in [0,0.1,0.2,0.3,0.4,0.7,0.7 + (0.3/4),0.7 + 2*(0.3/4),0.7 + 3*(0.3/4),1]:
            x = x_value
            if x_value <= 0.4:
                h = -0.5*x + 0.3
            else:
                h = 0.2*x 
            dotted_line = DashedLine(axes.c2p(x_value, 0), axes.c2p(x_value, h), stroke_width=2)
            dotted_lines3.add(dotted_line)
            
        self.play(Transform(u1,u3),Transform(dotted_lines,dotted_lines3),
                 FadeOut(area1),FadeOut(area2),FadeOut(area3),FadeOut(area4))
        
        label_V34 = Tex("$V_1([X_1]) = V_1([X_2]) = V_1([X_3]) = \\frac{V_1[0,1]}{3}$", color=WHITE).next_to(rectangle, 3*DOWN)
        
        self.play(Transform(label_V32,label_V34))
        
        self.wait(2)