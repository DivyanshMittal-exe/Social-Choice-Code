from manim import *

W = 10

class Rectangles(Scene):
    def construct(self):
        # Create a rectangle
        rectangle = Rectangle(width=W, height=2, color=WHITE, fill_opacity=0.4)
        rectangle.move_to(ORIGIN)

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
        arrow = Arrow(line1.get_center() + 0.15*W*RIGHT, line1.get_center() + 0.25*W*RIGHT + 2*UP, buff=0.2)
        label_V3 = Tex("$V_1([\\alpha,\\beta]) = \\frac{V_1[0,1]}{3}$", color=WHITE).next_to(arrow, UP)

        # Show everything
        self.play(Create(rectangle), Write(label_left), Write(label_right))
        self.wait(0.5)
        self.play(Create(line1), Create(line2), Write(label_04),Write(label_07))
        self.wait(0.5)
        self.play(Create(arrow), Write(label_V3))
        self.wait(2)

        # Divide the intervals [0, 0.4] and [0.7, 1] into four parts each
        lines_x1 = [Line(rectangle.get_corner([-1,-1,0])+ 0.1 *W * (i + 1)* RIGHT, rectangle.get_corner([-1,1,0])+ 0.1 *W* (i + 1) * RIGHT, color=YELLOW) for i in range(3)]
        lines_x2 = [Line(rectangle.get_corner([-1,-1,0])+ (0.7 + (0.3/4)*(i + 1 ))*W* RIGHT, rectangle.get_corner([-1,1,0])+ (0.7 + (0.3/4)*(i+1))*W* RIGHT, color=ORANGE) for i in range(3)]

        labs = ["$X_3$","$X_2$","$X_2$","$X_3$"]
        labels_x1 = [Tex(t, color=WHITE).next_to(line, LEFT) for (line,t) in zip(lines_x1,labs)]
        labels_x1.append(Tex("$X_3$", color=WHITE).next_to(lines_x1[-1], RIGHT))
        labels_x2 = [Tex(t, color=WHITE).next_to(line, LEFT) for (line,t) in zip(lines_x2,labs)]
        labels_x2.append(Tex("$X_3$", color=WHITE).next_to(lines_x2[-1], RIGHT))
        

        self.play(*[Create(line) for line in lines_x1], *[Write(label) for label in labels_x1])
        self.wait(1)
        self.play(*[Create(line) for line in lines_x2], *[Write(label) for label in labels_x2])
        self.wait(2)
