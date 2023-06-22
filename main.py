import sys

from PyQt5.QtWidgets import QApplication

from view import View



app = QApplication(sys.argv)

view = View()
view.show()

sys.exit(app.exec_())





