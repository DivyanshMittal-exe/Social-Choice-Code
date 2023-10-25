from manim import *

W = 10

class Champion(Scene):
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
        label_X1 = Tex("$X_p$", color=WHITE).next_to(line2, LEFT)

        # Create an arrow and label for V_3
        arrow = Arrow(line1.get_center() + 0.15*W*RIGHT, line1.get_center() + 0.25*W*RIGHT + 2*UP, buff=0.2)
        label_V3 = Tex("$V_p([\\alpha,\\beta]) = \\frac{V_p[0,1]}{n}$", color=WHITE).next_to(arrow, UP)

        # Show everything
        self.play(Create(rectangle), Write(label_left), Write(label_right))
        self.wait(0.5)
        self.play(Create(line1), Create(line2), Write(label_04),Write(label_07))
        self.wait(0.5)
        self.play(Create(arrow), Write(label_V3),Write(label_X1))
        self.wait(2)
        
        
        arrow2 = Arrow(line1.get_center() + 0.15*W*RIGHT, line1.get_center() + 0.05*W*RIGHT + 2*DOWN, buff=0.2)
        label_down = Tex("For everyone else $i \\in {[n] \\backslash {p}}$", color=WHITE).next_to(arrow2, DOWN)
        label_down2 = Tex("$V_i([\\alpha,\\beta]) \\leq \\frac{V_i[0,1]}{n}$", color=WHITE).next_to(label_down, DOWN)
        
        self.play(Create(arrow2), Write(label_down), Write(label_down2))
        self.wait(2)
        
