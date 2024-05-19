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
        self.loadElements()

    def loadElements(self):
        # deshboard section
        self.dash_board = {}
        element_names = ['label_rank1_name', 'label_rank1_score', 'label_rank2_name', 'label_rank2_score', 'label_rank3_name', 'label_rank3_score']
        for ele in element_names:
            self.dash_board[ele] = self.findChild(
                QtWidgets.QLabel, ele
            )
        self.dash_board["pushButton_reset"] = self.findChild(
            QtWidgets.QPushButton, "pushButton_reset"
        )

        # Math Battle Section
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    m = MathBattle()
    sys.exit(app.exec_())