from meshes.base_mesh import BaseMesh
from settings import *


class QuadMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.ctx = app.ctx
        self.program = app.shadder_program.quad

    def get_vertex_data(self):
        vertices = [
            (0.5,0.5,0.0),(-0.5,0.5,0.0),(-0.5,-0.5,0.0),
            (0.5, 0.5, 0.0), (-0.5, -0.5, 0.0), (0.5, -0.5, 0.0)
        ]
        colors = [
            (0,1,0),(1,0,0),(1,1,0),
            (0,1,0),(1,1,0),(0,0,1)
        ]
        vertex_data = np.hstack([vertices, colors],dtype = 'float32')
        return vertex_data