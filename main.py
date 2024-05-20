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
        self.math_battle = {}
        # player name
        self.math_battle["lineEdit_player_name"] = self.findChild(
            QtWidgets.QLineEdit, "lineEdit_player_name"
        )

        # score
        self.math_battle["label_score"] = self.findChild(
            QtWidgets.QLabel, "label_score"
        )

        # expression
        self.math_battle["label_expression"] = self.findChild(
            QtWidgets.QLabel, "label_expression"
        )

        # answer
        self.math_battle["lineEdit_answer"] = self.findChild(
            QtWidgets.QLineEdit, "lineEdit_answer"
        )

        # check button
        self.math_battle["pushButton_check"] = self.findChild(
            QtWidgets.QPushButton, "pushButton_check"
        )

        # status
        self.math_battle["label_status"] = self.findChild(
            QtWidgets.QLabel, "label_status"
        )

        # start 
        self.math_battle["pushButton_start"] = self.findChild(
            QtWidgets.QPushButton, "pushButton_start"
        )
        # adding start button click action
        self.math_battle["pushButton_start"].clicked.connect(self.startButtonAction)

        # end
        self.math_battle["pushButton_end"] = self.findChild(
            QtWidgets.QPushButton, "pushButton_end"
        )

    def startButtonAction(self):
        """handle starting process
        when the start button clicked this method will be called
        """
        pass
         

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    m = MathBattle()
    sys.exit(app.exec_())