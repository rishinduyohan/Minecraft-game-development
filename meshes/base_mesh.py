import numpy as np

class BaseMesh:
    def __init__(self):
        #OpenGL context
        self.ctx = None
        #Shader program
        self.program = None
        #vertex buffer data type format: "3f 3f"
        self.vbo_format = None
        #attribute names according to the format:("in_position","in_color")
        self.attrs : tuple[str,...] = None
        #vertex array object
        self.vao = None

    def get_vertex_data(self) -> np.array: ...


