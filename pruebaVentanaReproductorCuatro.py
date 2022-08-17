from functools import partial
from PyQt5.QtCore import QEvent, QUrl, Qt
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QMainWindow,QDialog,
                             QWidget, QPushButton, QSlider,
                             QVBoxLayout)
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

# Ruta del archivo.
VIDEO_PATH = "/home/anka/Documentos/PruebaReproductor/drop.avi"
VIDEO_PATH_2 = "/home/anka/Documentos/PruebaReproductor/bird.avi"
VIDEO_PATH_3 = "/home/anka/Documentos/PruebaReproductor/MVI_0043.AVI"
VIDEO_PATH_4 = "/home/anka/Documentos/PruebaReproductor/vokoscreenNG-2022-08-17_22-34-58.avi"

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Reproductor(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/anka/Documentos/PruebaReproductor/FondoTESALimpio.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 611, 341))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/home/anka/Documentos/PruebaReproductor/../../Imágenes/Televisió.png"))
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 60, 367, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color: rgba(138, 218, 235, 90);")
        self.widget.setObjectName("widget")
        self.label_Salir = QtWidgets.QLabel(self.centralwidget)
        self.label_Salir.setGeometry(QtCore.QRect(690, 20, 71, 61))
        self.label_Salir.setText("")
        self.label_Salir.setPixmap(QtGui.QPixmap("/home/anka/Documentos/PruebaReproductor/Salir.png"))
        self.label_Salir.setObjectName("label_Salir")
        self.pushButtonSalir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSalir.setGeometry(QtCore.QRect(690, 21, 71, 53))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButtonSalir.setFont(font)
        self.pushButtonSalir.setStyleSheet("QPushButton\n"
"{border-radius:1px;background-color: transparent }\n"
"QPushButton:pressed\n"
"{background-color :  red;}")
        self.pushButtonSalir.setText("")
        self.pushButtonSalir.setObjectName("pushButtonSalir")
        self.pushButtonSalir.clicked.connect(self.salida)

        self.pushButton_Video1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Video1.setGeometry(QtCore.QRect(660, 190, 89, 31))
        self.pushButton_Video1.setStyleSheet("QPushButton\n"
"{border-radius:10px;border :3px solid black;background-color: rgb(255, 190, 111);}\n"
"QPushButton:pressed\n"
"{background-color: rgb(198, 70, 0);}\n"
"\n"
"\n"
"")
        self.pushButton_Video1.setObjectName("pushButton_Video1")
        self.pushButton_Video1.clicked.connect(self.video1)

        self.pushButton_Video2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Video2.setGeometry(QtCore.QRect(660, 230, 89, 31))
        self.pushButton_Video2.setStyleSheet("QPushButton\n"
"{border-radius:10px;border :3px solid black;background-color: rgb(255, 190, 111);}\n"
"QPushButton:pressed\n"
"{background-color: rgb(198, 70, 0);}\n"
"\n"
"\n"
"")
        self.pushButton_Video2.setObjectName("pushButton_Video2")
        self.pushButton_Video2.clicked.connect(self.video2)

        self.pushButton_Video3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Video3.setGeometry(QtCore.QRect(660, 270, 89, 31))
        self.pushButton_Video3.setStyleSheet("QPushButton\n"
"{border-radius:10px;border :3px solid black;background-color: rgb(255, 190, 111);}\n"
"QPushButton:pressed\n"
"{background-color: rgb(198, 70, 0);}\n"
"\n"
"\n"
"")
        self.pushButton_Video3.setObjectName("pushButton_Video3")
        self.pushButton_Video3.clicked.connect(self.video3)

        self.pushButton_Video4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Video4.setGeometry(QtCore.QRect(660, 310, 89, 31))
        self.pushButton_Video4.setStyleSheet("QPushButton\n"
"{border-radius:10px;border :3px solid black;background-color: rgb(255, 190, 111);}\n"
"QPushButton:pressed\n"
"{background-color: rgb(198, 70, 0);}\n"
"\n"
"\n"
"")
        self.pushButton_Video4.setObjectName("pushButton_Video4")
        self.pushButton_Video4.clicked.connect(self.video4)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 390, 89, 31))
        self.pushButton_6.setStyleSheet("QPushButton\n"
"{border-radius:10px;border :3px solid black;background-color: rgb(143, 240, 164);}\n"
"QPushButton:pressed\n"
"{background-color :  green;}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.funPlay)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(130, 390, 91, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_7.setStyleSheet("QPushButton\n"
"{border-radius:10px;border :3px solid black;background-color: rgb(245, 128, 128); }\n"
"QPushButton:pressed\n"
"{background-color :  red;}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.parada)


        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(230, 400, 561, 16))
        self.horizontalSlider.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")


        self.labelVolumen = QtWidgets.QLabel(self.centralwidget)
        self.labelVolumen.setGeometry(QtCore.QRect(370, 440, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelVolumen.setFont(font)
        self.labelVolumen.setStyleSheet("background-color: transparent;\n"
"color: rgb(26, 95, 180);")
        self.labelVolumen.setObjectName("labelVolumen")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(500, 440, 291, 16))
        self.horizontalSlider_2.setStyleSheet("background-color: rgb(174, 191, 64);")
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setRange(0, 100)


        MainWindow.setCentralWidget(self.centralwidget)

        #Hacer el reproductor de video
        self.widgetDeVideo = QVideoWidget(self.centralwidget)
        self.widgetDeVideo.setGeometry(QtCore.QRect(90, 60, 367, 271))
        self.widgetDeVideo.setObjectName("widgetDeVideo")
        self.widgetDeVideo.setStyleSheet("background-color: #2e3436;")

        self.reproductor = QMediaPlayer(self.widgetDeVideo)
        self.reproductor.setVideoOutput(self.widgetDeVideo)

        
        #Para darle funcion a los deslizadores
       
        self.horizontalSlider_2.setRange(0, 100)
        self.horizontalSlider_2.setValue(self.reproductor.volume())
        self.horizontalSlider_2.sliderMoved.connect(self.reproductor.setVolume)

        self.reproductor.positionChanged.connect(self.horizontalSlider.setValue)
        self.reproductor.durationChanged.connect(partial(self.horizontalSlider.setRange, 0))

        #Para posicionar el video con horizontalSlider

        self.horizontalSlider.setValue(self.reproductor.position())
        self.horizontalSlider.sliderMoved.connect(self.reproductor.setPosition)
        self.reproductor.positionChanged.connect(self.horizontalSlider.setValue)
        self.reproductor.durationChanged.connect(partial(self.horizontalSlider.setRange, 0))

        # self.reproductor.setMedia(QMediaContent(QUrl.fromLocalFile(VIDEO_PATH)))




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def video1(self):
        self.reproductor.setMedia(QMediaContent(QUrl.fromLocalFile(VIDEO_PATH)))
        self.reproductor.play()
        
    def video2(self):
        self.reproductor.setMedia(QMediaContent(QUrl.fromLocalFile(VIDEO_PATH_2)))
        self.reproductor.play()
        
    def video3(self):
        self.reproductor.setMedia(QMediaContent(QUrl.fromLocalFile(VIDEO_PATH_3)))
        self.reproductor.play()

    def video4(self):
        self.reproductor.setMedia(QMediaContent(QUrl.fromLocalFile(VIDEO_PATH_4)))
        self.reproductor.play()

    def funPlay(self):
        # Reproducción del video y pausa

        if (self.reproductor.state() in
            (QMediaPlayer.PausedState, QMediaPlayer.StoppedState)):
            self.reproductor.play()
        else:
            self.reproductor.pause()

    def parada(self):
        self.reproductor.stop()

    def salida(self):
        self.reproductor.stop()
        MainWindow.close()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Video1.setText(_translate("MainWindow", "Video 1"))
        self.pushButton_Video2.setText(_translate("MainWindow", "Video 2"))
        self.pushButton_Video3.setText(_translate("MainWindow", "Video 3"))
        self.pushButton_Video4.setText(_translate("MainWindow", "Video 4"))
        self.pushButton_6.setText(_translate("MainWindow", "Play - Pause"))
        self.pushButton_7.setText(_translate("MainWindow", "Detener"))
        self.labelVolumen.setText(_translate("MainWindow", "Volumen"))


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow_Reproductor()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())