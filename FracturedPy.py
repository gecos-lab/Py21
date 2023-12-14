from FracturedPy.windows_factory import ProjectWindow

from sys import argv, exit
from PyQt5.QtWidgets import QApplication

app = QApplication(argv)
project_window = ProjectWindow()
project_window.show()
exit(app.exec_())
