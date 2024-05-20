from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
import sys
import random
from operations import MathGame
from  data import gamer_names
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

        # operations
        self.op = MathGame()
        # showing the windows
        self.show()
        self.loadElements()

        # setting a gamer name randomly
        self.math_battle["lineEdit_player_name"].setText(random.choice(gamer_names))


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
        # adding check button click action
        self.math_battle["pushButton_check"].clicked.connect(self.checkButtonAction)

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
        # adding end button click action
        self.math_battle["pushButton_end"].clicked.connect(self.endButtonAction)


        # timer
        self.math_battle["timer"] = self.findChild(
            QtWidgets.QLCDNumber, "lcdNumber_time"
        )

    def checkButtonAction(self):
        # stop the timer
        self.timer.stop()
        # enable startButton
        self.math_battle["pushButton_start"].setEnabled(True)
        # disable check button
        self.math_battle["pushButton_check"].setEnabled(False)
        # getting the answer from the line edit
        answer = self.math_battle["lineEdit_answer"].text().strip()

        # checking the answer
        if self.op.solve_expression() == answer:
            # when answer is correct
            # show status CORRECT
            self.math_battle["label_status"].setText('<span style="color: green; font-weight: bold;">CORRECT</span>')
            # update score
            score = self.getScore() + 1
            self.math_battle["label_score"].setText(str(score) + " (+1)")
        else:
            # when answer is wrong
            # show status WRONG
            self.math_battle["label_status"].setText('<span style="color: red; font-weight: bold;">WRONG</span>')
            # update score
            score = self.getScore() - 1
            self.math_battle["label_score"].setText(str(score) + " (-1)")
            

    def startButtonAction(self):
        """handle starting process
        when the start button clicked this method will be called
        """
        # disable startButton
        self.math_battle["pushButton_start"].setEnabled(False)
        # enable check button
        self.math_battle["pushButton_check"].setEnabled(True)
        # showing new expression
        self.showNewExpression(self.op.generate_expression())
        # clearing answer field
        self.math_battle["lineEdit_answer"].clear()
        self.startTimer()
    
    def endButtonAction(self):
        try:
            self.timer.stop()
        except:
            pass
        finally:
            self.showFinalResult()
            self.reset()
            # enable startButton
            self.math_battle["pushButton_start"].setEnabled(True)
            # disable check button
            self.math_battle["pushButton_check"].setEnabled(False)
    
    def reset(self):
        self.math_battle["label_score"].setText('0')
        self.math_battle["label_expression"].setText("XXXX")
        self.math_battle["lineEdit_answer"].clear()
        self.math_battle["timer"].display("5")
        self.math_battle["label_status"].setText("Waiting")
    
    def showNewExpression(self, expression):
        self.math_battle["label_expression"].setText(expression)

    def startTimer(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateLCD)
        self.timer.start(1000)  # Update every second

        # Initialize counter for LCD display (start from 5)
        self.counter = 5
        self.math_battle["timer"].display(self.counter)

    def updateLCD(self):
        if self.counter > 0:
            self.counter -= 1
            self.math_battle["timer"].display(self.counter)
        else:
            # when time over
            # show status WRONG
            self.math_battle["label_status"].setText('<span style="color: red; font-weight: bold;">Time End</span>')
            # update score
            score = self.getScore() - 2
            self.math_battle["label_score"].setText(str(score) + " (-2)")
            self.math_battle["label_expression"].setText("XXXX")
            self.math_battle["lineEdit_answer"].clear()
            self.math_battle["timer"].display("5")
            # enable startButton
            self.math_battle["pushButton_start"].setEnabled(True)
            # disable check button
            self.math_battle["pushButton_check"].setEnabled(False)
            # stoping the timer
            self.timer.stop()

    def getScore(self) -> int:
        score = list(self.math_battle["label_score"].text().strip())
        s = ""
        i = 0
        for i in score:
            if i == '(':
                break
            else:
                s += i
        return int(s)    

        
    def showFinalResult(self):
        msg = MessageBox()
        msg.showMessage(f"total score: {self.getScore()}")
class MessageBox:
    """
    show pop up window with spacific text. Make sure you use setMessage method
    to show spacific text
    """

    def showMessage(self, message: str):
        self.msg_box = QtWidgets.QMessageBox()
        self.msg_box.setText(message)
        x = self.msg_box.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    m = MathBattle()
    sys.exit(app.exec_())