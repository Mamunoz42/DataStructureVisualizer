import sys
from frontend.start_window import InicialWindow
from frontend.algorithm_class import MergeWindow, QuickWindow, SelectionWindow, InsertionWindow
from backend.page_distributor import StartWindow

from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])
    window = InicialWindow()
    back_window = StartWindow()
    window.signal_open_algorithm.connect(back_window.page_distributior)
    
    # Se definen estas señales para abrir ventana respectiva
    merge_window = MergeWindow()
    quick_window = QuickWindow()
    insertion_window = InsertionWindow()
    selection_window = SelectionWindow()
    back_window.merge_signal.connect(merge_window.show)
    back_window.quick_signal.connect(quick_window.show)
    back_window.selection_signal.connect(selection_window.show)
    back_window.insertion_signal.connect(insertion_window.show)

    merge_window.back_signal.connect(window.show)
    quick_window.back_signal.connect(window.show)
    insertion_window.back_signal.connect(window.show)
    selection_window.back_signal.connect(window.show)

    window.show()
    app.exec()