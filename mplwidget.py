# -*- coding: utf-8 -*-
"""
Created on Tue May 19 22:29:10 2020

@author: Geosains-UI

Modified by: Prime
"""
#%% Library
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
#from matplotlib.backends.backend_qt5agg import 
from matplotlib.figure import Figure
#from matplotlib.pyplot import plt
#%% Create Widget    
class  MplWidget (QWidget):
    def  __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure(tight_layout = True))
        vertical_layout = QVBoxLayout() 
        vertical_layout.addWidget (self.canvas)
        self.canvas.axes = self.canvas.figure.add_subplot(211)
        #self.canvas.axes = self.canvas.plt.gca().invert_yaxis()
        self.canvas.axes2 = self.canvas.figure.add_subplot(212, projection='polar')
        self.setLayout(vertical_layout)
