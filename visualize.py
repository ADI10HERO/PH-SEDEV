import json
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
import os
from PyQt5 import QtWidgets

matplotlib.use('Qt5Agg')
matplotlib.use('TkAgg')


class ScrollableWindow(QtWidgets.QMainWindow):
    def __init__(self, fig):

        self.q_app = QtWidgets.QApplication([])

        QtWidgets.QMainWindow.__init__(self)

        #  To set this size of the Display Window
        self.setFixedSize(1025, 1000)

        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(QtWidgets.QVBoxLayout())
        self.widget.layout().setContentsMargins(0, 0, 0, 0)
        self.widget.layout().setSpacing(10)

        self.fig = fig
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.scroll = QtWidgets.QScrollArea(self.widget)
        self.scroll.setWidget(self.canvas)

        self.nav = NavigationToolbar(self.canvas, self.widget)
        self.widget.layout().addWidget(self.nav)
        self.widget.layout().addWidget(self.scroll)

        self.show()
        exit(self.q_app.exec_())


def visualize(outdir="output_files"):
    """
    Generate PyQt5 plot for visualizing ECG data.
    Inputs:
    ------
    outdir: (str) Path to the directory with all the json files

    Returns:
    --------
    None
    """

    files = os.listdir(outdir)
    files.remove('.gitkeep')

    fig, axes = plt.subplots(ncols=1, nrows=12, figsize=(10, 20))

    for i, filename in enumerate(files):
        if 'json' not in filename.split('.')[-1]:
            continue

        with open(outdir + os.sep + filename, "r") as f:
            ecg_data = json.load(f)

            data = ecg_data.get("data", [])
            x_axis = np.arange(len(data))

            # TODO: Handle sampling...
            axes[i].set_title(ecg_data.get("name", "Untitled"))
            axes[i].plot(x_axis, data)

    fig.tight_layout()
    ScrollableWindow(fig)


if __name__ == "__main__":
    visualize()
