from render import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 
if (__name__ == '__main__') :
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0) 
    window = glutCreateWindow("Tubes Algeo 2")
    glutKeyboardFunc(on_keyPressed)
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()