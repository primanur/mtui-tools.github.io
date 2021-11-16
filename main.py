#%% Library
import os
from PyQt5.QtWidgets import * 
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import numpy as np 
import random
import dimensionality as dim
  
class MatplotlibWidget (QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("mtuitools.ui",self)
        self.setWindowTitle("MTUI_Tools: Dimensionality and Strike Analysis")
        self.push_load.clicked.connect(self.Browseclick)
        #self.addToolBar(NavigationToolbar(self.MplWidget.canvas,self))
        self.radio_swift.toggled.connect(self.update_graph)
        self.radio_bahr.toggled.connect(self.update_graph)
        self.radio_ellips.toggled.connect(self.update_graph)
        self.radio_strike.toggled.connect(self.update_graph)
        self.show()
#%% Read Data File
    def isValid(self, fileName):
        try: 
            file = open( fileName, 'r' )
            file.close()
            return True
        except:
            return False
    
    def setFileName(self, fileName):
        if self.isValid( fileName ):
            self.fileName = fileName
            self.fileContents = open( fileName, 'r' ).read()
            self.freq = np.genfromtxt('{}'.format(fileName), delimiter="   ", skip_header=92, skip_footer=418-111)
            self.Zxxr = np.genfromtxt('{}'.format(fileName), delimiter="   ", skip_header=109, skip_footer=418-128)
            self.Zxxi = np.genfromtxt('{}'.format(fileName), delimiter="   ", skip_header=126, skip_footer=418-145)  
            self.Zxyr = np.genfromtxt('{}'.format(fileName), delimiter="   ", skip_header=160, skip_footer=418-179)
            self.Zxyi = np.genfromtxt('{}'.format(fileName), delimiter="   ", skip_header=177, skip_footer=418-196)
            self.Zyxr = np.genfromtxt('{}'.format(fileName), delimiter="   ", skip_header=211, skip_footer=418-230)
            self.Zyxi = np.genfromtxt('{}'.format(fileName), delimiter="   ", skip_header=228, skip_footer=418-247)
            self.Zyyr = np.genfromtxt('{}'.format(fileName), delimiter="   ", skip_header=262, skip_footer=418-281)
            self.Zyyi = np.genfromtxt('{}'.format(fileName), delimiter="   ", skip_header=279, skip_footer=418-298)
        else:
            self.freq = ""
            self.Zxxr = ""
            self.Zxxi = ""
            self.Zxyr = ""
            self.Zxyi = ""
            self.Zyxr = ""
            self.Zyxi = ""
            self.Zyyr = ""
            self.Zyyi = ""
            self.fileName = ""
    
    def getFileName(self):
        return self.fileName
    
    def getFileContents(self):
        return self.fileContents
    
    def getfreq(self):
        return self.freq
        
    def getZxxr(self):
        return self.Zxxr
    
    def getZxxi(self):
        return self.Zxxi
    
    def getZxyr(self):
        return self.Zxyr
    
    def getZxyi(self):
        return self.Zxyi
    
    def getZyxr(self):
        return self.Zyxr
    
    def getZyxi(self):
        return self.Zyxi
    
    def getZyyr(self):
        return self.Zyyr
    
    def getZyyi(self):
        return self.Zyyi
    
    def refreshAll(self):
        self.lineEdit.setText(self.getFileName())
        
    def returnPressedSlot(self):
        fileName =  self.lineEdit.text()
        if self.MainWindow.isValid(fileName):
            self.MainWindow.setFileName(self.lineEdit.text())
            self.refreshAll()
        else:
            m = QMessageBox()
            m.setText("Invalid file name!\n" + fileName )
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QMessageBox.Ok
                                 | QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            '''ret = m.exec_()'''
            self.lineEdit.setText("")
            self.refreshAll()
            self.debugPrint("Invalid file specified: " + fileName)
    
    def Browseclick(self):
        import os
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.centralwidget, 'Choose a File', os.curdir, 'EDI File (*.edi)', options=options)
        if fileName:
            self.setFileName(fileName)
            self.refreshAll()
#%% Plotting
    def update_graph(self):

        x = dim.frequency(self.getfreq())
        swift = dim.skewswift(self.getfreq(), self.getZxxr(), self.getZxxi(),
                              self.getZxyr(), self.getZxyi(), self.getZyxr(),
                              self.getZyxi(), self.getZyyr(), self.getZyyi())
        bahr = dim.skewbahr(self.getfreq(), self.getZxxr(), self.getZxxi(),
                            self.getZxyr(), self.getZxyi(), self.getZyxr(),
                            self.getZyxi(), self.getZyyr(), self.getZyyi())
        ellips = dim.ellips(self.getfreq(), self.getZxxr(), self.getZxxi(),
                            self.getZxyr(), self.getZxyi(), self.getZyxr(),
                            self.getZyxi(), self.getZyyr(), self.getZyyi())
        strike = dim.strikeanalysis(self.getfreq(), self.getZxxr(), self.getZxxi(),
                            self.getZxyr(), self.getZxyi(), self.getZyxr(),
                            self.getZyxi(), self.getZyyr(), self.getZyyi())


        self.MplWidget.canvas.axes.clear()
        if self.radio_swift.isChecked() == True:
            self.MplWidget.canvas.axes.plot(x, swift, 'o')
            self.MplWidget.canvas.axes.set_xscale('log')
            self.MplWidget.canvas.axes.invert_xaxis()
            self.MplWidget.canvas.axes.set_ylim(0, 2)
            self.MplWidget.canvas.axes.set_title('Swift-Skew Plot')
            self.MplWidget.canvas.axes.set_xlabel('Frequency (Hz)', fontsize=16)
            self.MplWidget.canvas.axes.set_ylabel('Swift-Skew', fontsize=16)
            self.MplWidget.canvas.axes.grid()
            self.MplWidget.canvas.draw()
        
        elif self.radio_bahr.isChecked() == True:
            self.MplWidget.canvas.axes.plot(x, bahr, 'o') 
            self.MplWidget.canvas.axes.set_xscale('log')
            self.MplWidget.canvas.axes.invert_xaxis()
            self.MplWidget.canvas.axes.set_ylim(0, 2)
            self.MplWidget.canvas.axes.set_title('Bahr-Skew Plot')
            self.MplWidget.canvas.axes.set_xlabel('Frequency (Hz)', fontsize=16)
            self.MplWidget.canvas.axes.set_ylabel('Bahr-Skew', fontsize=16)
            self.MplWidget.canvas.axes.grid()
            self.MplWidget.canvas.draw()
        
        elif self.radio_ellips.isChecked() == True:
            self.MplWidget.canvas.axes.plot(x, ellips, 'o') 
            self.MplWidget.canvas.axes.set_xscale('log')
            self.MplWidget.canvas.axes.invert_xaxis()
            self.MplWidget.canvas.axes.set_ylim(0, 2)
            self.MplWidget.canvas.axes.set_title('Ellipticity Plot')
            self.MplWidget.canvas.axes.set_xlabel('Frequency (Hz)', fontsize=16)
            self.MplWidget.canvas.axes.set_ylabel('Ellipticity', fontsize=16)
            self.MplWidget.canvas.axes.grid()
            self.MplWidget.canvas.draw()
        
        elif self.radio_strike.isChecked() == True:
            #strike = TetaGB1
            bin_edges = np.arange(-5, 366, 10)
            number_of_strikes, bin_edges = np.histogram(strike, bin_edges)

            # Sum the last value with the first value.

            number_of_strikes[0] += number_of_strikes[-1]

            # Sum the first half 0-180° with the second half 180-360° to achieve the "mirrored behavior" of Rose Diagrams.

            half = np.sum(np.split(number_of_strikes[:-1], 2), 0)
            two_halves = np.concatenate([half, half])
            
            self.MplWidget.canvas.axes2.bar(np.deg2rad(np.arange(0, 360, 10)), two_halves, 
                                           width=np.deg2rad(10), bottom=0.0, color='b', edgecolor='m')
            self.MplWidget.canvas.axes2.set_theta_zero_location('N')
            self.MplWidget.canvas.axes2.set_theta_direction(-1)
            self.MplWidget.canvas.axes2.set_thetagrids(np.arange(0, 360, 10), labels=np.arange(0, 360, 10))
            #self.MplWidget.canvas.axes2.set_rgrids(np.arange(1, two_halves.max() + 1, 2), angle=0, weight= 'black')
            self.MplWidget.canvas.axes2.set_title('Swift-Strike Analysis Diagram', y=1.10, fontsize=15)
            self.MplWidget.canvas.draw()
#%% Execute GUI
app = QApplication([]) 
window = MatplotlibWidget() 
window.show() 
app.exec_()
