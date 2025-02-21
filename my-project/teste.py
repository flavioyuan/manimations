from manim import *

class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        self.add(circle, square, triangle)
        self.wait(1)
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5),
            triangle.animate.set_fill(GREEN, opacity=0.5)
        )
        self.wait(1)
        self.play(Create(square))
        self.play(square.animate.set_fill(BLUE, opacity=0.5))
        self.play(square.animate.rotate(PI/4))
        self.wait(1)

        self.play(square.animate.set_fill(YELLOW, opacity=0.5))
        self.play(square.animate.rotate(-PI/4))
        self.play(triangle.animate.set_fill(GREEN_A, opacity=0.5))