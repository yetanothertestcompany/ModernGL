import struct

import GLWindow
import ModernGL

wnd = GLWindow.create_window()
ctx = ModernGL.create_context()

prog = ctx.program([
    ctx.vertex_shader('''
        #version 330
        in vec2 vert;
        void main() {
            gl_Position = vec4(vert, 0.0, 1.0);
        }
    '''),
    ctx.fragment_shader('''
        #version 330
        out vec4 color;
        void main() {
            color = vec4(0.3, 0.5, 1.0, 1.0);
        }
    '''),
])

vbo = ctx.buffer(struct.pack('6f', 0.0, 0.8, -0.6, -0.8, 0.6, -0.8))
vao = ctx.simple_vertex_array(prog, vbo, ['vert'])

while wnd.update():
    ctx.viewport = wnd.viewport
    ctx.clear(0.9, 0.9, 0.9)
    vao.render()
