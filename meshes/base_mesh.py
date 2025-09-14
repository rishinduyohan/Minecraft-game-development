import numpy as np

class BaseMesh:
    def __init__(self):
        #OpenGL
        self.ctx = None
        #Shader program
        self.program = None
        #vertex buffer data type format: "3f 3f"
        self.vbo_format = None
        #attribute names ("in_position", "in_color")
        self.attrs: tuple[str,...] = None
        #vertex array object
        self.vbo = None