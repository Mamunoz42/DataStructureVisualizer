from PyQt5.QtCore import QObject, pyqtSignal

class StartWindow(QObject):

    merge_signal = pyqtSignal()
    selection_signal = pyqtSignal()
    insertion_signal = pyqtSignal()
    quick_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def page_distributior(self, algorithm):
        if algorithm == 'merge':
            self.merge_signal.emit()
        elif algorithm == 'quick':
            self.quick_signal.emit()
        elif algorithm == 'insertion':
            self.insertion_signal.emit()
        elif algorithm == 'selection':
            self.selection_signal.emit()