from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

window_name, base_class = uic.loadUiType('frontend/ui_files/algorithm.ui')

class AlgorithmWindow(window_name, base_class):

    back_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.back_button.clicked.connect(self.back_to_menu)

    def back_to_menu(self):
        self.hide()
        self.back_signal.emit()


class MergeWindow(AlgorithmWindow):

    def __init__(self):
        super().__init__()
        self.title_label.setText("Merge Sort Algorithm")


class QuickWindow(AlgorithmWindow):

    def __init__(self):
        super().__init__()
        self.title_label.setText("Quick Sort Algorithm")


class InsertionWindow(AlgorithmWindow):

    def __init__(self):
        super().__init__()
        self.title_label.setText("Insertion Sort Algorithm")


class SelectionWindow(AlgorithmWindow):

    def __init__(self):
        super().__init__()
        self.title_label.setText("Selection Sort Algorithm")