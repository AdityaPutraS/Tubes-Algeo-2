from render import draw2d,on_keyPressed
from OpenGL.GLUT import glutInit,glutInitDisplayMode,glutInitWindowSize,glutCreateWindow
from OpenGL.GLUT import glutInitWindowPosition,glutKeyboardFunc,glutDisplayFunc,glutIdleFunc,glutMainLoop
from OpenGL.GLUT import GLUT_RGBA, GLUT_DOUBLE, GLUT_ALPHA,GLUT_DEPTH
from config import *

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutInitWindowPosition(0, 0) 
window = glutCreateWindow("Tubes Algeo 2")
glutKeyboardFunc(on_keyPressed)
glutDisplayFunc(draw2d)
glutIdleFunc(draw2d)
glutMainLoop()