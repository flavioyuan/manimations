0) Instalar manim no environment local - Windows

[text](https://docs.manim.community/en/stable/installation/uv.html)

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv python install

Para adicionar o manim no environment local:
uv add manim

Para verificar se o manim foi corretamente instalado:
uv run manim checkhealth

1) Criar e inicializar um projeto:
1.1 Criar uma nova pasta

    $ uv run manim init project my-project --


1.2 Exemplo de código
    
    from manim import *


    class CreateCircle(Scene):
        def construct(self):
            circle = Circle()  # create a circle
            circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
            self.play(Create(circle))  # show the circle on screen

1.3 Renderizar o objeto:

    $ manim -pql main.py CreateCircle
