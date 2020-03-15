import sys
import subprocess
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import abspath, dirname
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from os.path import abspath, dirname
from Close import Accident as init
from Close import split as sp

sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))

class Ui_MainWindow(object):
    def fonction(self):
        self.pushButton1.setEnabled(False)
        init.main()
        self.pushButton2.setEnabled(True)
    def fonction1(self):
        self.pushButton2.setEnabled(False)
        self.items_resultat = QtWidgets.QTextEdit()
        self.items_resultat.setReadOnly(True) 
        self.items_resultat.setText("Items fréquents fermés : \n")
        self.gridLayout_ac.addWidget(self.items_resultat, 2, 5, 4 ,10)

        fHandle = open("Accidents_out", "r")
        nTId = 0
        for i in fHandle.readlines():
            nTId += 1
            lineSplitted = i.split()
            self.items_resultat.append(i)
           

        fHandle.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setStyleSheet("QMainWindow{background-color:\n"
"\n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:0.40 rgba(245, 245, 245, 255), stop:0.80 rgba(250, 250, 250, 255), stop:1 rgba(250, 255, 250, 255))}\n"
"\n"
"\n"
"QLabel#label_Heading{\n"
"font: 55 25pt \"Century Schoolbook L\";\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:rgb(252, 233, 30);\n"
"}\n"
)  
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        

        ###############################################################################################################"ACCUEIL
        self.Accueil = QtWidgets.QWidget()
        self.Accueil.setObjectName("Accueil")
        self.gridLayout_ac = QtWidgets.QGridLayout(self.Accueil)
        self.gridLayout_ac.setObjectName("gridLayout_ac")
        #self.gridLayout_ac.setContentsMargins(20, 0, 20, 0)
        
        self.Accueil.setStyleSheet("QWidget#Accueil{background-color:\n"
        "\n"
        "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(21, 145, 236, 1), stop:0.25 rgba(101,220,241,1), stop:0.80 rgba(203,246,253,1), stop:1 rgba(250, 255, 250, 255))}\n"
        "\n")

        self.icon1 = QIcon("Icones/Accueil.png")

        self.appli = QtWidgets.QVBoxLayout(self.Accueil)
        self.appli.setObjectName("appli")
        #self.appli.setSpacing(30)
        self.appli.setContentsMargins(0, 0, 0, 0)
        #self.fonction1()
        self.image_appli = QImage('Images/overturn.png')
        self.image_appli_affiche = QPixmap.fromImage(self.image_appli.scaled(300,100,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        
        self.label_appli = QLabel(self.Accueil)
        self.label_appli.setObjectName("label_12")
        self.label_appli.setPixmap(self.image_appli_affiche)

        self.pushButton1 = QtWidgets.QPushButton("Rechercher les itemsets fréquents")
        self.pushButton1.setObjectName("pushButton1")
       
        #self.pushButton1.setEnabled(False)
        self.pushButton1.clicked.connect(self.fonction)


        self.items_resultat = QtWidgets.QTextEdit()
        self.items_resultat.setReadOnly(True) 
        self.items_resultat.setText("Items fréquents fermés : ")
        

        self.items_spmin = QtWidgets.QTextEdit()
        self.label_appli.setObjectName("label_13")
        

        
        self.pushButton2 = QtWidgets.QPushButton("itemsets frequents fermés")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.resize(10,10)
        self.pushButton2.clicked.connect(self.fonction1)


        self.gridLayout_ac.addWidget(self.pushButton1, 6, 1, 2, 4)
        self.gridLayout_ac.addWidget(self.pushButton2, 6, 14, 2, 4)

        self.gridLayout_ac.addWidget(self.label_appli, 2, 2, 2 ,8)
        self.gridLayout_ac.addWidget(self.items_resultat, 2, 5, 4 ,10)
        
        self.tabWidget.addTab(self.Accueil,self.icon1, "Test")
        self.verticalLayout_5.addWidget(self.tabWidget)   
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    
    # setup ui
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.setWindowTitle("Extraction d'itemset fréquent fermés")
    window.setWindowIcon(QIcon('Images/overturned-vehicle.png'))
    if "--travis" in sys.argv:
        QtCore.QTimer.singleShot(2000, app.exit)
    # run
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
	
