from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

window_name, base_class = uic.loadUiType('frontend/ui_files/mainmenu.ui')

class InicialWindow(window_name, base_class):

    signal_open_algorithm = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.setGeometry(200, 100, 300, 300)
        self.setWindowTitle('Data Structure Visualizer')
        self.init_gui()

    def init_gui(self):
        self.merge_button.clicked.connect(lambda i: self.display_algorithm('merge'))
        self.quick_button.clicked.connect(lambda i: self.display_algorithm('quick'))
        self.insertion_button.clicked.connect(lambda i: self.display_algorithm('insertion'))
        self.selection_button.clicked.connect(lambda i: self.display_algorithm('selection'))
    
    def display_algorithm(self, algorithm):
        self.hide()
        self.signal_open_algorithm.emit(algorithm)
