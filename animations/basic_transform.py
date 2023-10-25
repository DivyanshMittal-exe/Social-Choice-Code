from manim import *

class GraphSceneCustom(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 1,
        "x_tick_frequency": 0.2,
        "x_axis_label": "$x$",
        "y_min": 0,
        "y_max": 3,
        "y_tick_frequency": 0.5,
        "y_axis_label": "$y$",
        "graph_origin": LEFT * 4 + DOWN * 2,
    }

    def construct(self):
        self.setup_axes()

        # Define the original function y = 3x^2
        def original_function(x):
            return 3 * x**2

        # Create the graph of the original function
        original_graph = self.get_graph(original_function, color=BLUE, x_min=0, x_max=1)

        # Create the dotted lines on the x-axis
        dotted_lines = VGroup()
        for x_value in [0.1, 0.2, 0.4, 0.5]:
            dotted_line = DashedLine(self.coords_to_point(x_value, 0), self.coords_to_point(x_value, 0), stroke_width=2)
            dotted_lines.add(dotted_line)

        # Define the piecewise uniform function
        def piecewise_uniform(x):
            if 0.1 <= x <= 0.2 or 0.4 <= x <= 0.5:
                return 2.44
            else:
                return 0

        # Create the graph of the piecewise uniform function
        uniform_graph = self.get_graph(piecewise_uniform, color=GREEN, x_min=0, x_max=1)

        # Display the original graph and dotted lines
        self.play(ShowCreation(original_graph), ShowCreation(dotted_lines))

        # Transform the original graph into the uniform graph
        self.play(Transform(original_graph, uniform_graph))

        self.wait(2)
