from manim import *

W = 10

class Cover(Scene):
    def construct(self):
        # Create a rectangle
        rectangle = Rectangle(width=W, height=1, color=WHITE, fill_opacity=0.4)
        rectangle.move_to(ORIGIN + 1*UP)

        # Divide the rectangle into three parts
        line1 = Line(rectangle.get_corner([-1,-1,0]) + 0.1*W*RIGHT, rectangle.get_corner([-1,1,0]) + 0.1*W*RIGHT, color=BLUE_D)
        line2 = Line(rectangle.get_corner([-1,-1,0]) + 0.25*W*RIGHT, rectangle.get_corner([-1,1,0]) + 0.25*W*RIGHT, color=BLUE_D)
        line3 = Line(rectangle.get_corner([-1,-1,0]) + 0.85*W*RIGHT, rectangle.get_corner([-1,1,0]) + 0.85*W*RIGHT, color=BLUE_D)

        # Label the sides
        label_left = Tex("0", color=WHITE).next_to(rectangle, LEFT)
        label_right = Tex("1", color=WHITE).next_to(rectangle, RIGHT)
        # label_04 = Tex("$\\alpha$", color=WHITE).next_to(line1, DOWN)
        # label_07 = Tex("$\\beta$", color=WHITE).next_to(line2, DOWN)

        # Create labels for regions
        label_X1 = Tex("$X_p$", color=WHITE).next_to(line1, LEFT)
        label_X2 = Tex("$X_q$", color=WHITE).next_to(line2, LEFT)
        label_dots = Tex("$\ldots$", color=WHITE).next_to(line2, RIGHT)

        # Create an arrow and label for V_3
        # arrow = Arrow(line1.get_center() + 0.15*W*RIGHT, line1.get_center() + 0.25*W*RIGHT + 2*UP, buff=0.2)
        # label_V3 = Tex("$V_p([\\alpha,\\beta]) = \\frac{V_p[0,1]}{n}$", color=WHITE).next_to(arrow, UP)
        
        
        arrow21 = Arrow(label_X1.get_center(), label_X1.get_center() + 0.1*W*RIGHT + 2*UP, buff=0.2)
        label_ownerp = Tex("$V_p(X_p) = \\frac{V_p[0,1]}{n}$", color=WHITE).next_to(arrow21, UP)
        
        arrow22 = Arrow(label_X2.get_center(), label_X2.get_center() + 0.1*W*RIGHT + 2*UP, buff=0.2)
        label_ownerq = Tex("$V_q(X_q) = \\frac{V_q[0,1]}{n}$", color=WHITE).next_to(arrow22, UP)
        

        # Show everything
        self.play(Create(rectangle), Write(label_left), Write(label_right))
        self.wait(0.5)
        self.play(Create(line1), Write(label_X1))
        self.play(Create(arrow21), Write(label_ownerp))
        self.play(Create(line2), Write(label_X2))
        self.play(Transform(arrow21,arrow22), Transform(label_ownerp,label_ownerq))
        self.play(Write(label_dots))
        self.wait(0.5)
        
        self.play(FadeOut(arrow21), FadeOut(label_ownerp))
        
        self.play(Create(line3))
        
        
        
        
        arrow2 = Arrow(line3.get_center() + 0.1*W*RIGHT, line3.get_center() + 0.25*W*RIGHT + 2*UP, buff=0.2)
        label_down2 = Tex("$V_i([\\alpha,\\beta]) < \\frac{V_i[0,1]}{n}$", color=WHITE).next_to(arrow2, UP)
        label_down = Tex("$\\forall i \\in [n],$", color=WHITE).next_to(label_down2, LEFT)
        
        self.play(Create(arrow2), Write(label_down), Write(label_down2))
        self.wait(2)
        
        rec_w = W*0.2
        
        rectangle2 = Rectangle(width=rec_w, height=1, color=WHITE, fill_opacity=0.4)
        rectangle2.move_to(rectangle.get_corner([1,1,0]) + (rec_w/2)*LEFT + 2*DOWN)
        
        self.play(Create(rectangle2))
        
        arrow3 = Arrow(rectangle2.get_center() + 0*W*LEFT, rectangle2.get_center() + 0.3*W*LEFT, buff=0.2)
        label_side = Tex("Smallest region, such that", color=WHITE).next_to(arrow3, LEFT)
        label_side2 = Tex("for some agent p", color=WHITE).next_to(label_side, DOWN)
        label_side3= Tex("$V_p([\\alpha^*,1]) = \\frac{V_p[0,1]}{n}$", color=WHITE).next_to(label_side2, DOWN)
        
        self.play(Create(arrow3), Write(label_side), Write(label_side2), Write(label_side3))
        
    
        self.wait(4)
        
        
