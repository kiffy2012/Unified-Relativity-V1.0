import sys
from PyQt5.QtWidgets import QApplication, QOpenGLWidget, QMainWindow
from OpenGL.GL import *

class TestGLWidget(QOpenGLWidget):
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = TestGLWidget()
        self.setCentralWidget(self.widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())