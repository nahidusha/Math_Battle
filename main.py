from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys

class MathBattle(QtWidgets.QMainWindow):
    """this class is responsible for load the main
        window of Math Battle
        NOTE: here self instance will be operate all over the elements
        which means, self = app window
    """
    def __init__(self):
        super(MathBattle, self).__init__()
        # loading the .ui file
        loadUi('gui/mainpage.ui', self)
        # showing the windows
        self.show()
    
    def loadElements(self):
        pass
        # deshboard section
        # Math Battle section

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    m = MathBattle()
    sys.exit(app.exec_())