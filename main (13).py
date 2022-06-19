import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import numpy as np
from scipy.fftpack import fft
import math
import pandas as pd
import pyqtgraph as pg
matplotlib.use('Qt5Agg')
#from PySide import QtGui
import pyautogui
#app = QtGui.QApplication([])
#screen_resolution = app.desktop().screenGeometry()
#width, height = screen_resolution.width(), screen_resolution.height()



new_sig = []
t = np.arange(0, 1, 0.001)
class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, dpi=120):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)
        fig.tight_layout()


class sinusoidal():
    def __init__(self, name='unknown', amplitude=0, phaseshift=0, frequency=1):
        self.name = name
        self.phaseShift = phaseshift
        self.amplitude = amplitude
        self.frequency = frequency
        self.time = np.arange(0.0, 1, 0.001)
        self.plot = self.amplitude * np.sin((2 * np.pi * self.frequency * self.time) + (self.phaseShift * np.pi / 180))

    def plotting(self, widget):
        widget.plot(self.time, self.plot)

    def addPlots(self, plot2):
        self.plot = self.plot + plot2

    def getPlot(self):
        return self.plot
    def clearPlot(self):
        self.plot=0



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1608, 1133)
        self.Main_centralwidget_for_layout = QtWidgets.QWidget(MainWindow)
        self.Main_centralwidget_for_layout.setObjectName("Main_centralwidget_for_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Main_centralwidget_for_layout)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter_horizontally_From_mid = QtWidgets.QSplitter(self.Main_centralwidget_for_layout)
        self.splitter_horizontally_From_mid.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_horizontally_From_mid.setObjectName("splitter_horizontally_From_mid")
        self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic = QtWidgets.QFrame(self.splitter_horizontally_From_mid)
        self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic.setObjectName("frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_showhide = QtWidgets.QCheckBox(self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic)
        self.checkBox_showhide.setChecked(True)
        self.checkBox_showhide.setTristate(False)
        self.checkBox_showhide.setObjectName("checkBox_showhide")
        self.gridLayout_2.addWidget(self.checkBox_showhide, 2, 0, 1, 2)
        self.verticalLayout_for_mainGraph_and_illustrator_dynamic = QtWidgets.QVBoxLayout()
        self.verticalLayout_for_mainGraph_and_illustrator_dynamic.setObjectName("verticalLayout_for_mainGraph_and_illustrator_dynamic")
        self.frame_mainGraph = QtWidgets.QFrame(self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic)
        self.frame_mainGraph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mainGraph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mainGraph.setObjectName("frame_mainGraph")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_mainGraph)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_For_Main_graph = QtWidgets.QLabel(self.frame_mainGraph)
        self.label_For_Main_graph.setAlignment(QtCore.Qt.AlignCenter)
        self.label_For_Main_graph.setObjectName("label_For_Main_graph")
        self.gridLayout_3.addWidget(self.label_For_Main_graph, 0, 0, 1, 1)
        self.signalWidget_mainGraph = PlotWidget(self.frame_mainGraph)
        self.signalWidget_mainGraph.setStyleSheet("")
        self.signalWidget_mainGraph.setObjectName("signalWidget_mainGraph")
        self.gridLayout_3.addWidget(self.signalWidget_mainGraph, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 313, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(454, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 33, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 0, 1, 1, 1)
        self.verticalLayout_for_mainGraph_and_illustrator_dynamic.addWidget(self.frame_mainGraph)
        self.frame_for_ilustrator = QtWidgets.QFrame(self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic)
        self.frame_for_ilustrator.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_for_ilustrator.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_for_ilustrator.setObjectName("frame_for_ilustrator")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_for_ilustrator)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.label_for_spectroGram = QtWidgets.QLabel(self.frame_for_ilustrator)
        self.label_for_spectroGram.setAlignment(QtCore.Qt.AlignCenter)
        self.label_for_spectroGram.setObjectName("label_for_spectroGram")
        self.gridLayout.addWidget(self.label_for_spectroGram, 0, 0, 1, 1)
        self.signalWidget2_ilustrator = PlotWidget(self.frame_for_ilustrator)
        self.signalWidget2_ilustrator.setEnabled(True)
        self.signalWidget2_ilustrator.setStyleSheet("")
        self.signalWidget2_ilustrator.setObjectName("signalWidget2_ilustrator")
        self.gridLayout.addWidget(self.signalWidget2_ilustrator, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 228, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 1, 1, 1)
        self.verticalLayout_for_mainGraph_and_illustrator_dynamic.addWidget(self.frame_for_ilustrator)
        self.gridLayout_2.addLayout(self.verticalLayout_for_mainGraph_and_illustrator_dynamic, 0, 0, 1, 3)
        self.horizontalSlider_for_ilustrator = QtWidgets.QSlider(self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic)
        self.horizontalSlider_for_ilustrator.setMinimum(1)
        self.horizontalSlider_for_ilustrator.setMaximum(9)
        self.horizontalSlider_for_ilustrator.setPageStep(1)
        self.horizontalSlider_for_ilustrator.setProperty("value", 1)
        self.horizontalSlider_for_ilustrator.setSliderPosition(1)
        self.horizontalSlider_for_ilustrator.setTracking(True)
        self.horizontalSlider_for_ilustrator.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_for_ilustrator.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_for_ilustrator.setTickInterval(1)
        self.horizontalSlider_for_ilustrator.setObjectName("horizontalSlider_for_ilustrator")
        self.gridLayout_2.addWidget(self.horizontalSlider_for_ilustrator, 4, 0, 1, 1)
        self.label_for_show_frequency = QtWidgets.QLabel(self.frame_for_vertical_layout_for_mainGraph_and_illustrator_dynamic)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_for_show_frequency.setFont(font)
        self.label_for_show_frequency.setStyleSheet("\n"
"color: rgb(255, 0, 0);")
        self.label_for_show_frequency.setObjectName("label_for_show_frequency")
        self.gridLayout_2.addWidget(self.label_for_show_frequency, 4, 1, 1, 2)
        self.splitter_for_generated_and_summation = QtWidgets.QSplitter(self.splitter_horizontally_From_mid)
        self.splitter_for_generated_and_summation.setOrientation(QtCore.Qt.Vertical)
        self.splitter_for_generated_and_summation.setObjectName("splitter_for_generated_and_summation")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_for_generated_and_summation)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_GeneratedSinusoidal = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_GeneratedSinusoidal.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_GeneratedSinusoidal.setObjectName("gridLayout_GeneratedSinusoidal")
        self.gridLayout_For_generating_sinusoidal = QtWidgets.QGridLayout()
        self.gridLayout_For_generating_sinusoidal.setObjectName("gridLayout_For_generating_sinusoidal")
        self.label_frequency = QtWidgets.QLabel(self.layoutWidget)
        self.label_frequency.setObjectName("label_frequency")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.label_frequency, 0, 2, 1, 1)
        self.lineEdit_plotName = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_plotName.setClearButtonEnabled(True)
        self.lineEdit_plotName.setObjectName("lineEdit_plotName")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.lineEdit_plotName, 0, 1, 1, 1)
        self.LineEdit_ferquency = QtWidgets.QLineEdit(self.layoutWidget)
        self.LineEdit_ferquency.setClearButtonEnabled(True)
        self.LineEdit_ferquency.setObjectName("LineEdit_ferquency")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.LineEdit_ferquency, 0, 3, 1, 1)
        self.label_plotName = QtWidgets.QLabel(self.layoutWidget)
        self.label_plotName.setObjectName("label_plotName")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.label_plotName, 0, 0, 1, 1)
        self.label_magnitude = QtWidgets.QLabel(self.layoutWidget)
        self.label_magnitude.setObjectName("label_magnitude")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.label_magnitude, 1, 0, 1, 1)
        self.lineEdit_magnitude = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_magnitude.setClearButtonEnabled(True)
        self.lineEdit_magnitude.setObjectName("lineEdit_magnitude")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.lineEdit_magnitude, 1, 1, 1, 1)
        self.add = QtWidgets.QPushButton(self.layoutWidget)
        self.add.setObjectName("add")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.add, 4, 0, 1, 5)
        self.lineEdit_phaseShift = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_phaseShift.setAutoFillBackground(False)
        self.lineEdit_phaseShift.setInputMask("")
        self.lineEdit_phaseShift.setFrame(True)
        self.lineEdit_phaseShift.setDragEnabled(True)
        self.lineEdit_phaseShift.setClearButtonEnabled(True)
        self.lineEdit_phaseShift.setObjectName("lineEdit_phaseShift")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.lineEdit_phaseShift, 1, 3, 1, 1)
        self.label_phaseShift = QtWidgets.QLabel(self.layoutWidget)
        self.label_phaseShift.setObjectName("label_phaseShift")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.label_phaseShift, 1, 2, 1, 1)
        self.Plot_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.Plot_Button.setObjectName("Plot_Button")
        self.gridLayout_For_generating_sinusoidal.addWidget(self.Plot_Button, 3, 0, 1, 5)
        self.gridLayout_GeneratedSinusoidal.addLayout(self.gridLayout_For_generating_sinusoidal, 1, 0, 1, 1)
        self.frame_for_generated_sinusoidal = QtWidgets.QFrame(self.layoutWidget)
        self.frame_for_generated_sinusoidal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_for_generated_sinusoidal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_for_generated_sinusoidal.setObjectName("frame_for_generated_sinusoidal")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_for_generated_sinusoidal)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_For_generatedSinusoidal = QtWidgets.QLabel(self.frame_for_generated_sinusoidal)
        self.label_For_generatedSinusoidal.setAlignment(QtCore.Qt.AlignCenter)
        self.label_For_generatedSinusoidal.setObjectName("label_For_generatedSinusoidal")
        self.gridLayout_4.addWidget(self.label_For_generatedSinusoidal, 0, 0, 1, 1)
        self.Widget_Plotter = PlotWidget(self.frame_for_generated_sinusoidal)
        self.Widget_Plotter.setEnabled(True)
        palette = QtGui.QPalette()
        self.Widget_Plotter.setPalette(palette)
        self.Widget_Plotter.setStyleSheet("")
        self.Widget_Plotter.setObjectName("Widget_Plotter")
        self.gridLayout_4.addWidget(self.Widget_Plotter, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(405, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 2, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(10, 198, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 1, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(10, 42, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem8, 0, 1, 1, 1)
        self.gridLayout_GeneratedSinusoidal.addWidget(self.frame_for_generated_sinusoidal, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_for_generated_and_summation)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_for_sinusoidalSummation = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_for_sinusoidalSummation.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_for_sinusoidalSummation.setObjectName("gridLayout_for_sinusoidalSummation")
        self.verticalLayout_mainGraphButtons = QtWidgets.QVBoxLayout()
        self.verticalLayout_mainGraphButtons.setObjectName("verticalLayout_mainGraphButtons")
        self.gridLayout_for_sinusoidalSummation.addLayout(self.verticalLayout_mainGraphButtons, 0, 0, 1, 1)
        self.widget_singleuse_as_backGround_for_summation = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_singleuse_as_backGround_for_summation.setObjectName("widget_singleuse_as_backGround_for_summation")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_singleuse_as_backGround_for_summation)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_For_summation = QtWidgets.QLabel(self.widget_singleuse_as_backGround_for_summation)
        self.label_For_summation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_For_summation.setObjectName("label_For_summation")
        self.gridLayout_5.addWidget(self.label_For_summation, 0, 0, 1, 1)
        self.Widget_Adder = PlotWidget(self.widget_singleuse_as_backGround_for_summation)
        palette = QtGui.QPalette()
        self.Widget_Adder.setPalette(palette)
        self.Widget_Adder.setStyleSheet("")
        self.Widget_Adder.setObjectName("Widget_Adder")
        self.gridLayout_5.addWidget(self.Widget_Adder, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(10, 233, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem9, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(346, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem10, 2, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(10, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem11, 0, 1, 1, 1)
        self.gridLayout_for_sinusoidalSummation.addWidget(self.widget_singleuse_as_backGround_for_summation, 0, 1, 1, 1)
        self.gridLayout_For_sunusoidalSummation = QtWidgets.QGridLayout()
        self.gridLayout_For_sunusoidalSummation.setObjectName("gridLayout_For_sunusoidalSummation")
        self.Button_confirmation = QtWidgets.QPushButton(self.layoutWidget1)
        self.Button_confirmation.setObjectName("Button_confirmation")
        self.gridLayout_For_sunusoidalSummation.addWidget(self.Button_confirmation, 1, 0, 1, 2)
        self.Combobox_signal = QtWidgets.QComboBox(self.layoutWidget1)
        self.Combobox_signal.setObjectName("Combobox_signal")
        self.gridLayout_For_sunusoidalSummation.addWidget(self.Combobox_signal, 0, 0, 1, 1)
        self.Button_delete = QtWidgets.QPushButton(self.layoutWidget1)
        self.Button_delete.setObjectName("Button_delete")
        self.gridLayout_For_sunusoidalSummation.addWidget(self.Button_delete, 0, 1, 1, 1)
        self.gridLayout_for_sinusoidalSummation.addLayout(self.gridLayout_For_sunusoidalSummation, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.splitter_horizontally_From_mid)
        MainWindow.setCentralWidget(self.Main_centralwidget_for_layout)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1608, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setCheckable(False)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # buttons

        self.checkBox_showhide.stateChanged.connect(lambda: self.IsChecked())

        self.Plot_Button.clicked.connect(self.plotS)
        self.add.clicked.connect(self.adder_to_summation)
        self.Button_delete.clicked.connect(self.deletePlot)
        self.Button_confirmation.clicked.connect(self.toMainGraph)
        self.horizontalSlider_for_ilustrator.valueChanged.connect(self.Sampling_change)

        self.actionSave.triggered.connect(self.saveToCSV)
        self.actionOpen.triggered.connect(self.Open_file)
        self.actionClear.triggered.connect(self.clearAll)

        self.s = 'none'
        self.sinArr = []
        self.Sinu = sinusoidal()

    ###########################################################################################################################################
    def IsChecked(self):
        if self.checkBox_showhide.isChecked() == False:
            # self.Hide_channel(1)
            # self.signalWidget2_ilustrator.hide()
            self.frame_for_ilustrator.hide()

        else:
            # self.signalWidget2_ilustrator.show()
            self.frame_for_ilustrator.show()

    def plotS(self):
        self.Widget_Plotter.clear()
        name = self.lineEdit_plotName.text()
        freq = int(self.LineEdit_ferquency.text())
        mag = int(self.lineEdit_magnitude.text())
        pS = int(self.lineEdit_phaseShift.text())
        Sinu = sinusoidal(name, mag, pS, freq)
        Sinu.plotting(self.Widget_Plotter)

    def adder_to_summation(self):
        name = self.lineEdit_plotName.text()
        freq = int(self.LineEdit_ferquency.text())
        mag = int(self.lineEdit_magnitude.text())
        pS = int(self.lineEdit_phaseShift.text())
        Sinu = sinusoidal(name, mag, pS, freq)
        self.sinArr.append(Sinu)
        self.Combobox_signal.addItem(Sinu.name)
        self.adderPLot()

    def adderPLot(self):
        self.Widget_Adder.clear()
        for i in range(len(self.sinArr)):
            self.Sinu.addPlots(self.sinArr[i].getPlot())

        self.Sinu.plotting(self.Widget_Adder)

    def deletePlot(self):
        index = self.Combobox_signal.currentIndex()
        self.sinArr.remove(self.sinArr[index])
        self.Combobox_signal.removeItem(index)
        self.Sinu.clearPlot()
        self.adderPLot()

    def toMainGraph(self):
        self.signalWidget_mainGraph.clear()
        # self.Sinu.plotting(self.signalWidget_mainGraph)

        self.data_amplitude = self.Sinu.plot
        self.data_time = self.Sinu.time
        self.Get_max_freq(self.data_amplitude, self.data_time)
        self.plot_mainGraph(self.data_amplitude, self.data_time, 0)

    def Get_max_freq(self, Amplitude, time_Points):
        data_amp = []
        for i in Amplitude:
            if len(data_amp) == len(t):
                break
            else:
                data_amp.append(i)

        n = np.size(time_Points)
        frequency_array = np.arange(1, np.floor(n / 2), dtype='int')
        data_freq = fft(data_amp)

        freq_mag = (2 / n) * abs(data_freq[0:np.size(frequency_array)])

        imp_freq = freq_mag > 0.2
        clean_frequency_array = imp_freq * frequency_array
        self.fmax = round(clean_frequency_array.max())
        ##Getting maximum frequency

    def Open_file(self):
        self.signalWidget2_ilustrator.clear()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open csv', QtCore.QDir.rootPath(), 'csv(*.csv)')
        data_set = pd.read_csv(fileName, header=None)
        self.Save_signal(data_set[0], data_set[1])
        ##Opening csv files

    def Save_signal(self, time, Amplitude):
        self.data_amplitude = Amplitude
        self.data_time = time
        self.Get_max_freq(self.data_amplitude, self.data_time)
        self.plot_mainGraph(self.data_amplitude, self.data_time, 0)



    def plot_mainGraph(self, amplitude, time, Fs):
        self.pink_pen = pg.mkPen((255, 0, 255), width=1)
        self.signalWidget_mainGraph.clear()
        self.signalWidget2_ilustrator.clear()

        self.signalWidget_mainGraph.plotItem.vb.setLimits(xMin=min(time) - 0.01, xMax=max(time),
                                                          yMin=min(amplitude) - 0.2,
                                                          yMax=max(amplitude) + 0.2)
        if Fs == 0:
            self.signalWidget_mainGraph.plot(time, amplitude)
        else:
            sample_time = 1 / Fs
            no_of_samples = math.ceil(max(time)) / sample_time  ##Getting number of samples as a float number
            no_of_samples = math.ceil(no_of_samples)  ##Getting number of samples as an int number

            index_append = len(time) / no_of_samples
            index_append = math.floor(index_append)
            self.Sample_amp = []
            self.Sample_time = []
            index = 0
            for i in range(no_of_samples):
                self.Sample_time.append(time[index])  ##adding the index of point time
                self.Sample_amp.append(amplitude[index])  ##adding the index of point amplitude
                index += index_append

            self.recons_amp = self.sinc_interp(self.Sample_amp, self.Sample_time, time)  ##plotting the new points

            self.signalWidget_mainGraph.plot(time, amplitude)
            self.signalWidget_mainGraph.plot(self.Sample_time, self.Sample_amp, symbol='o', pen=None)
            self.signalWidget_mainGraph.plot(time, self.recons_amp, pen=self.pink_pen)
            self.signalWidget2_ilustrator.plot(time, self.recons_amp, pen=self.pink_pen)
            self.signalWidget2_ilustrator.plotItem.vb.setLimits(xMin=min(self.data_time) - 0.01,
                                                                xMax=max(self.data_time),
                                                                yMin=min(self.data_amplitude) - 0.2,
                                                                yMax=max(self.data_amplitude) + 0.2)

            # plottingGraph.plotItem.vb.setLimits(xMin=min(time) - 0.01, xMax=max(time) - 0.2, yMin=min(amplitude) - 0.2,
            #                                     yMax=max(amplitude) + 0.2)
            # plottingGraph.plot(time, amplitude, pen=pg.mkPen(penColor, width=penWidth, style=penStyle), symbol=symbol,
            #                    symbolPen=symbolPen)

    def sinc_interp(self, sample_amplitude, sample_time, time):
        if len(sample_amplitude) != len(sample_time):
            raise ValueError('sample time and sample amplitude must be the same length')

        sample_time = np.array(sample_time)
        time = np.array(time)

        period_time = sample_time[1] - sample_time[0]  ##Getting the period between two points

        sincM = np.tile(time, (len(sample_time), 1)) - np.tile(sample_time[:, np.newaxis], (1, len(time)))
        recovered_sig = np.dot(sample_amplitude, np.sinc(sincM / period_time))
        return recovered_sig

    def Sampling_change(self):
        print('changing')
        print(self.horizontalSlider_for_ilustrator.value())
        Slider_Value = int(self.horizontalSlider_for_ilustrator.value())
        self.label_for_show_frequency.setText(str(Slider_Value))
        #self.label_For_Main_graph.setText(str(self.horizontalSlider_for_ilustrator.value()))
        if (Slider_Value / 3) * self.fmax * max(self.data_time) < 3:  # 5 #3
            self.value = 3 / (max(self.data_time * self.fmax))  # 3

        else:
            self.value = Slider_Value / 2.75  # 6
        self.plot_mainGraph(self.data_amplitude, self.data_time, self.fmax * self.value)
        #self.SignalReconstruction(self.data_amplitude, self.data_time, self.fmax * value)

    ##Using slider to control Sampling Frequency

    # def SignalReconstruction(self, amplitude, time, fs):
    #     sample_time = 1 / fs
    #     no_of_samples = math.ceil(max(time)) / sample_time
    #     no_of_samples = math.ceil(no_of_samples)
    #     index_append = len(time) / no_of_samples
    #     index_append = math.floor(index_append)
    #     self.Sample_amp = []
    #     self.Sample_time = []
    #     index = 0
    #     for i in range(no_of_samples):
    #         self.Sample_time.append(time[index])
    #         self.Sample_amp.append(amplitude[index])
    #         index += index_append
    #     self.recons_amp = self.sinc_interp(self.Sample_amp, self.Sample_time, time)
    #     self.signalWidget_mainGraph.clear()
    #     self.signalWidget2_ilustrator.clear()
    #     self.plot_mainGraph(self.signalWidget_mainGraph, amplitude, time)
    #     self.signalWidget_mainGraph.plot(self.Sample_time, self.Sample_amp, symbol='o', pen=None)
    #     self.signalWidget_mainGraph.plot(time, self.recons_amp, pen=self.pink_pen)
    #     self.plot_mainGraph(self.signalWidget2_ilustrator, self.recons_amp, time, self.pink_pen)



    def clearAll(self):
        self.deletePlot(self)

    def saveToCSV(self):
        list_dict = {'A': self.Sinu.time, 'B': self.Sinu.plot}
        df = pd.DataFrame(list_dict)
        df.to_csv('GeneratedSignal.csv', header=False, index=False)
    ###########################################################################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_showhide.setText(_translate("MainWindow", "Hide Illustrator"))
        self.label_For_Main_graph.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Main Graph</span></p></body></html>"))
        self.label_for_spectroGram.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\"> Illustrator</span></p></body></html>"))
        self.label_for_show_frequency.setText(_translate("MainWindow", "0"))
        self.label_frequency.setText(_translate("MainWindow", "Frequency"))
        self.lineEdit_plotName.setText(_translate("MainWindow", "Name"))
        self.LineEdit_ferquency.setText(_translate("MainWindow", "20"))
        self.label_plotName.setText(_translate("MainWindow", "Plot Name"))
        self.label_magnitude.setText(_translate("MainWindow", "Magnitude"))
        self.lineEdit_magnitude.setText(_translate("MainWindow", "1"))
        self.add.setText(_translate("MainWindow", "Add"))
        self.lineEdit_phaseShift.setText(_translate("MainWindow", "5"))
        self.label_phaseShift.setText(_translate("MainWindow", "Phase shift"))
        self.Plot_Button.setText(_translate("MainWindow", "Plot"))
        self.label_For_generatedSinusoidal.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Generated Sinusoidal</span></p></body></html>"))
        self.label_For_summation.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Sinusoidal Summation </span></p></body></html>"))
        self.Button_confirmation.setText(_translate("MainWindow", "Add signal to Illustrator"))
        self.Button_delete.setText(_translate("MainWindow", "Delete"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
