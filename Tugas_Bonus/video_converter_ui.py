# Form implementation generated from reading ui file 'c:\Users\Asus\Tutorial-Git\Juan\Tugas_Bonus\video_converter.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(459, 206)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_status = QtWidgets.QLabel(parent=Form)
        self.label_status.setObjectName("label_status")
        self.gridLayout.addWidget(self.label_status, 0, 0, 1, 1)
        self.button_select_video = QtWidgets.QPushButton(parent=Form)
        self.button_select_video.setObjectName("button_select_video")
        self.gridLayout.addWidget(self.button_select_video, 1, 0, 1, 1)
        self.button_convert = QtWidgets.QPushButton(parent=Form)
        self.button_convert.setObjectName("button_convert")
        self.gridLayout.addWidget(self.button_convert, 2, 0, 1, 1)
        self.progress_bar = QtWidgets.QProgressBar(parent=Form)
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout.addWidget(self.progress_bar, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_status.setText(_translate("Form", "                                                           Pilih Video Anda"))
        self.button_select_video.setText(_translate("Form", "Pilih Video"))
        self.button_convert.setText(_translate("Form", "Mulai Konversi"))
