from meshes.base_mesh import BaseMesh
from settings import *


class QuadMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.ctx = app.ctx
        self.program = app.shadder_program.quad
