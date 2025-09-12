from settings import *

class ShaderProgram:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        #----------shaders---------------
        self.quad = self.get_program(shader_name = 'quad')
        #--------------------------------

        self.set_uniforms_on_init()

    def set_uniforms_on_init(self):
        # Example: setting a uniform variable
        # self.quad['u_resolution'].value = (800, 600)
        pass  # Replace with actual uniform setup

    def get_program(self,shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader = vertex_shader, fragment_shader = fragment_shader)
        return program

    def update(self):
        # Example: update time uniform
        # self.quad['u_time'].value = time.time()
        pass  # Replace with actual logic
