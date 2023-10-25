from manim import *

class quad_to_lin(Scene):
    def construct(self):
        pass
        # box = Rectangle(stroke_color=GREEN_C, stroke_opacity=0.8, fill_color=RED_B, fill_opacity=1, height=1, width=1)
        
        # self.add(box)
        # self.play(box.animate.shift(UP), run_time=2)
        # self.play(box.animate.shift(RIGHT*2), run_time=5 )
        # self.play(box.animate.shift(LEFT), run_time=2)
        # self.play(box.animate.shift(DOWN), run_time=2)
        
class GraphingIntro(Scene):
    def construct(self):

        backg_plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1]).add_coordinates()
        code = Code("Tute2Intro.py", style=Code.styles_list[12], background ="window", language = "python", insert_line_no = True,
        tab_width = 2, line_spacing = 0.3, scale_factor = 0.5, font="Monospace").set_width(7).to_edge(UL, buff=0)

        axes = Axes(x_range = [0,5,1], y_range = [0,3,1], 
        x_length = 5, y_length = 3,
        axis_config = {"include_tip": True, "numbers_to_exclude": [0]}
        ).add_coordinates()

        axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label = "x", y_label = "f(x)")

        graph = axes.get_graph(lambda x : x**0.5, x_range = [0,4], color = YELLOW)

        graphing_stuff = VGroup(axes, graph, axis_labels)

        self.play(FadeIn(backg_plane), Write(code), run_time=6)
        self.play(backg_plane.animate.set_opacity(0.3))
        self.wait()
        self.play(DrawBorderThenFill(axes), Write(axis_labels), run_time = 2)
        self.wait()
        self.play(Create(graph), run_time = 2)
        self.play(graphing_stuff.animate.shift(DOWN*4), run_time = 3)
        self.wait()
        self.play(axes.animate.shift(LEFT*3), run_time = 3)
        self.wait()
    
class Tute3(Scene): #Showing how to call 2 planes, put graphs on each and call elements to each
    def construct(self):

        backg_plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1]).add_coordinates()

        plane = NumberPlane(x_range = [-4,4,1], x_length = 4, 
        y_range= [0, 20, 5], y_length=4).add_coordinates()
        plane.shift(LEFT*3+DOWN*1.5)
        plane_graph = plane.plot(lambda x : x**2,  x_range = [-4,4], color = GREEN)
        area = plane.get_riemann_rectangles(graph = plane_graph, x_range=[-2,2], dx=0.05)

        axes = Axes(x_range = [-4,4,1], x_length = 4, 
        y_range= [-20,20,5], y_length=4).add_coordinates()
        axes.shift(RIGHT*3+DOWN*1.5)
        axes_graph = axes.plot(lambda x : 2*x, 
        x_range=[-4,4], color = YELLOW)
        v_lines = axes.get_vertical_lines_to_graph(
            graph = axes_graph, x_range=[-3,3], num_lines = 12)

        code = Code("Tute2Code1.py", style=Code.styles_list[12], background ="window", language = "python", insert_line_no = True,
        tab_width = 2, line_spacing = 0.3, font="Monospace").set_width(6).to_edge(UL, buff=0)

        self.play(FadeIn(backg_plane), Write(code), run_time=6)
        self.play(backg_plane.animate.set_opacity(0.3))
        self.play(Write(plane), Create(axes))
        self.wait()
        self.play(Create(plane_graph), Create(axes_graph), run_time = 2)
        self.add(area, v_lines)
        self.wait()

# class GraphSceneCustom(GraphScene):
#     CONFIG = {
#         "x_min": 0,
#         "x_max": 1,
#         "x_tick_frequency": 0.2,
#         "x_axis_label": "$x$",
#         "y_min": 0,
#         "y_max": 3,
#         "y_tick_frequency": 0.5,
#         "y_axis_label": "$y$",
#         "graph_origin": LEFT * 4 + DOWN * 2,
#     }

#     def construct(self):
#         self.setup_axes()

#         # Define the original function y = 3x^2
#         def original_function(x):
#             return 3 * x**2

#         # Create the graph of the original function
#         original_graph = self.get_graph(original_function, color=BLUE, x_min=0, x_max=1)

#         # Create the dotted lines on the x-axis
#         dotted_lines = VGroup()
#         for x_value in [0.1, 0.2, 0.4, 0.5]:
#             dotted_line = DashedLine(self.coords_to_point(x_value, 0), self.coords_to_point(x_value, 0), stroke_width=2)
#             dotted_lines.add(dotted_line)

#         # Define the piecewise uniform function
#         def piecewise_uniform(x):
#             if 0.1 <= x <= 0.2 or 0.4 <= x <= 0.5:
#                 return 2.44
#             else:
#                 return 0

#         # Create the graph of the piecewise uniform function
#         uniform_graph = self.get_graph(piecewise_uniform, color=GREEN, x_min=0, x_max=1)

#         # Display the original graph and dotted lines
#         self.play(ShowCreation(original_graph), ShowCreation(dotted_lines))

#         # Transform the original graph into the uniform graph
#         self.play(Transform(original_graph, uniform_graph))

#         self.wait(2)

# class test(Scene):
#     def construct(self):
        
#         plane = NumberPlane(x_range = [-0.2,1.2,0.2], x_length = 7, y_range= [-0.2,1.2,0.2], y_length=7).to_edge(DOWN)
        
#         parab = plane.get_gr

from manim import *

import math

class PlotFunctions(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 1,0.1],
            y_range=[0, 3.5,0.5],
            axis_config={"color": BLUE},
        ).add_coordinates()
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Define the original function y = 3x^2
        def original_function(x):
            return 3 * x**2

        def original_function2(x):
            c = 0.1
            if x<= 0.25:
                to_add = 0
            elif x > 0.5 and x <= 0.75:
                to_add = c*math.sin(8*math.pi*x)
            else:
                to_add = c*math.cos(8*math.pi*x)
            return 3 * x**2 + to_add
        
        # Plot the original function
        original_graph = axes.plot(original_function, color=BLUE)
        original_graph2 = axes.plot(original_function2, color=BLUE, discontinuities=[0,0.25,0.5,0.75])
        # original_graph_copy = axes.plot(original_function, color=BLUE).set_opacity(0.3)
        
        
        area1 = axes.get_area(original_graph, [0, 1], color=GREY, opacity=0.5)

        
        # shaded_area = Polygon(
        #     *[
        #         axes.coords_to_point(x, 0)
        #         for x in np.arange(0, 1.1, 0.01)
        #     ],
        #     stroke_opacity=0,
        #     fill_color=YELLOW,
        #     fill_opacity=0.3,
        # )

        # Define the piecewise uniform function
        def piecewise_uniform(x):
            if x >= 0.75 or x >= 0.75-0.12837837837 or (x <= 0.5 and x >= 0.5 - 0.04729729729) or (x <= 0.25 and x >= 0.25 - 0.01292184075
):
                return 2.3125
            else:
                return 0
                
        def piecewise_uniform2(x):
            if x <= 0.25:
                return 0.0625
            elif x <= 0.5:
                return 0.4375
            elif x <= 0.75:
                return 1.1875
            elif x <= 1:
                return 2.3125
            else:
                return 0

        # Plot the piecewise uniform function
        uniform_graph = axes.plot(piecewise_uniform, color=GREEN, discontinuities=[0,0.25 - 0.01292184075,0.25,0.5 - 0.04729729729,0.5,0.75-0.12837837837,0.75])
        
        
        uniform_graph2 = axes.plot(piecewise_uniform2, color=GREEN_C, discontinuities=[0,0.25,0.5,0.75])
        
        area2 = axes.get_area(uniform_graph2, [0, 1], color=GREY, opacity=0.5)
        area3 = axes.get_area(uniform_graph, [0, 1], color=GREY, opacity=0.5)
        area4 = axes.get_area(original_graph2, [0, 1], color=GREY, opacity=0.5)
        

    

        dotted_lines = VGroup()
        for x_value in [0.25, 0.5, 0.75,1]:
            dotted_line = DashedLine(axes.c2p(x_value, 0), axes.c2p(x_value, 2.3125), stroke_width=2)
            dotted_lines.add(dotted_line)

        # Create the dotted lines on the x-axis
        dotted_lines2 = VGroup()
        for x_value in [0.25 - 0.01292184075, 0.5 - 0.04729729729, 0.75-0.12837837837]:
            dotted_line2 = DashedLine(axes.c2p(x_value, 0), axes.c2p(x_value, 2.3125), stroke_width=2)
            dotted_lines2.add(dotted_line2)

        # Display the axes, original graph, and dotted lines
        self.play(Create(axes), Write(axes_labels), Create(dotted_lines))
        
        self.play(Create(original_graph))
        self.play(FadeIn(area1))    
        
        self.wait(1) 
        
        self.play(Transform(original_graph, original_graph2), Transform(area1,area4))
        
        self.wait(1) 
        
        self.play(Transform(original_graph, uniform_graph2), Transform(area1,area2))
        
        
        self.wait(3) 

        # self.play(Create(shaded_area))
        
        # Transition to the piecewise uniform graph and dotted lines
        self.play(Transform(original_graph, uniform_graph), Create(dotted_lines2), Transform(area1,area3))

        self.wait(3)
        
