from settings import *
import moderngl as mgl
import pygame as pg
import sys

class Minecraft:
    def __init__(self):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION,3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE,24)

    def update(self):
        pass
    def render(self):
        pass
    def handle_events(self):
        pass
    def run(self):
        pass

if __name__ == '__main__':
    app = Minecraft()
    app.run()