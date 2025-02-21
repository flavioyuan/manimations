from manim import *

class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # place the circle two units left from the origin
        #circle.move_to(RIGHT)
        # place the square to the left of the circle
        #square.next_to(circle, LEFT)
        # align the left border of the triangle to the left border of the circle
        #triangle.align_to(circle, LEFT)
        #square.set_fill(BLUE, opacity=0.5)
        #square.rotate(PI/4)

        self.add(circle, square, triangle)
        self.wait(1)
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5),
            triangle.animate.set_fill(GREEN, opacity=0.5)
        )
        self.wait(1)
        self.play(Create(square))
        square.rotate(PI/4)
        self.wait(1)