from msilib.schema import Icon
from PyQt5.QtWidgets import (QApplication, QMainWindow, QHBoxLayout, QTreeView, 
QComboBox, QLabel, QVBoxLayout, QFileSystemModel, QWidget, QAction, QStyle, QMenu, QToolBar, 
QMessageBox, QDialog, QFileDialog, QMenuBar, QCheckBox, QSizePolicy, QStatusBar,
qApp, QFrame, QProgressDialog, QProgressBar, QInputDialog,QLineEdit
)
from PyQt5.QtCore import pyqtSlot, QObject,  QSettings, Qt, QDir, QUrl, QStandardPaths, QFileInfo, QEventLoop, QPointF, QRect , QSize
from PyQt5.QtGui import QIcon, QColor, QPainter, QFont

import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ui = Ui_MainWindow()
        ui.setupUi(self)



class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        self.mesures = ['in', 'cm', 'mm', 'px']
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(335, 334)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(335, 334))
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_width_2 = QLabel(self.centralwidget)
        self.lbl_width_2.setText(u"Anchura:")
        self.lbl_width_2.setObjectName(u"lbl_width_2")
        self.lbl_width_2.setGeometry(QRect(20, 10, 47, 16))
        self.lbl_height_2 = QLabel(self.centralwidget)
        self.lbl_height_2.setText(u"Altura:")
        self.lbl_height_2.setObjectName(u"lbl_height_2")
        self.lbl_height_2.setGeometry(QRect(20, 60, 47, 16))
        self.txtWidth = QLineEdit(self.centralwidget)
        self.txtWidth.setObjectName(u"txtWidth")
        self.txtWidth.setGeometry(QRect(20, 30, 113, 20))
        self.txtHeight = QLineEdit(self.centralwidget)
        self.txtHeight.setObjectName(u"txtHeight")
        self.txtHeight.setGeometry(QRect(20, 80, 113, 20))
        self.cmbMesure01 = QComboBox(self.centralwidget)
        self.cmbMesure01.addItems(self.mesures)
        self.cmbMesure01.setObjectName(u"cmbMesure01")
        self.cmbMesure01.setGeometry(QRect(200, 54, 111, 22))
        self.cmbMesure02 = QComboBox(self.centralwidget)
        self.cmbMesure02.addItems(self.mesures)
        self.cmbMesure02.setObjectName(u"cmbMesure02")
        self.cmbMesure02.setGeometry(QRect(200, 155, 111, 22))
        self.cbxChain01 = QCheckBox(self.centralwidget)
        self.cbxChain01.setObjectName(u"cbxChain01")
        self.cbxChain01.setGeometry(QRect(150, 60, 31, 17))
        icon = QIcon()
        icon.addFile(u"assets/chain-broken.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cbxChain01.setIcon(icon)
        self.cbxChain01.setIconSize(QSize(24, 24))
        self.cbxChain02 = QCheckBox(self.centralwidget)
        self.cbxChain02.setObjectName(u"cbxChain02")
        self.cbxChain02.setGeometry(QRect(150, 160, 41, 17))
        self.cbxChain02.setIcon(icon)
        self.cbxChain02.setIconSize(QSize(24, 24))
        self.txtAspectRateX = QLineEdit(self.centralwidget)
        self.txtAspectRateX.setObjectName(u"txtAspectRateX")
        self.txtAspectRateX.setGeometry(QRect(20, 140, 113, 20))
        self.txtAspectRateY = QLineEdit(self.centralwidget)
        self.txtAspectRateY.setObjectName(u"txtAspectRateY")
        self.txtAspectRateY.setGeometry(QRect(20, 190, 113, 20))
        self.txtWidthResult = QLineEdit(self.centralwidget)
        self.txtWidthResult.setObjectName(u"txtWidthResult")
        self.txtWidthResult.setGeometry(QRect(20, 260, 113, 20))
        self.txtHeightResult = QLineEdit(self.centralwidget)
        self.txtHeightResult.setObjectName(u"txtHeightResult")
        self.txtHeightResult.setGeometry(QRect(200, 260, 113, 20))
        self.lbl_ppp_x = QLabel(self.centralwidget)
        self.lbl_ppp_x.setText(u"Resolucion X:")
        self.lbl_ppp_x.setObjectName(u"lbl_ppp_x")
        self.lbl_ppp_x.setGeometry(QRect(20, 120, 71, 21))
        self.lbl_ppp_y = QLabel(self.centralwidget)
        self.lbl_ppp_y.setObjectName(u"lbl_ppp_y")
        self.lbl_ppp_y.setText(u"Resolucion Y:")
        self.lbl_ppp_y.setGeometry(QRect(20, 170, 71, 16))
        self.lbl_mesure01 = QLabel(self.centralwidget)
        self.lbl_mesure01.setObjectName(u"lbl_mesure01")
        self.lbl_mesure01.setGeometry(QRect(200, 34, 47, 16))
        self.lbl_mesure02 = QLabel(self.centralwidget)
        self.lbl_mesure02.setObjectName(u"lbl_mesure02")
        self.lbl_mesure02.setGeometry(QRect(200, 135, 47, 16))
        self.lbl_width_result = QLabel(self.centralwidget)
        self.lbl_width_result.setObjectName(u"lbl_width_result")
        self.lbl_width_result.setGeometry(QRect(20, 240, 71, 21))
        self.lbl_width_result.setText(u"Resultado Alto:")
        self.lbl_height_result = QLabel(self.centralwidget)
        self.lbl_height_result.setText(u"Ancho:")
        self.lbl_height_result.setObjectName(u"lbl_height_result")
        self.lbl_height_result.setGeometry(QRect(200, 240, 71, 21))
        self.lbl_width = QLabel(self.centralwidget)
        self.lbl_width.setObjectName(u"lbl_width")
        self.lbl_width.setGeometry(QRect(90, 240, 47, 16))
        self.lbl_height = QLabel(self.centralwidget)
        self.lbl_height.setObjectName(u"lbl_height")
        self.lbl_height.setGeometry(QRect(250, 240, 47, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 335, 21))
        self.menu_Archivo = QMenu(self.menubar)
        self.menu_Archivo.setObjectName(u"menu_Archivo")
        self.menu_About = QMenu(self.menubar)
        self.menu_About.setObjectName(u"menu_About")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu_Archivo.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.menu_About.addAction(self.action)
        
        self.cbxChain01.stateChanged.connect(lambda:self.chainIcon())

    def chainIcon(self):
        self.cbxChain01.setIcon(QIcon('./assets/chain-broken.png'))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
 