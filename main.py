from core import crawling, calc, data
import time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 505)
        MainWindow.setWindowTitle("Engraving Calculator")
        #MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setProperty("15", "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_tab = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_tab.setObjectName("verticalLayout_tab")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        # TAB0
        self.tab_0 = QtWidgets.QWidget()
        self.tab_0.setObjectName("tab_0")
        self.horizontalLayout_0 = QtWidgets.QHBoxLayout(self.tab_0)
        self.horizontalLayout_0.setObjectName("horizontalLayout_0")

        # TAB0-0
        self.verticalLayout_00 = QtWidgets.QVBoxLayout()
        self.verticalLayout_00.setObjectName("verticalLayout_00")

        # TAB0-0 목표 각인
        self.groupBox_000 = QtWidgets.QGroupBox(self.tab_0)
        self.groupBox_000.setObjectName("groupBox_000")
        self.verticalLayout_000 = QtWidgets.QVBoxLayout(self.groupBox_000)
        #self.verticalLayout_000.setSpacing(10)
        self.verticalLayout_000.setObjectName("verticalLayout_000")
        self.gridLayout_000 = QtWidgets.QGridLayout()
        self.gridLayout_000.setObjectName("gridLayout_000")

        self.comboBox_00000 = QtWidgets.QComboBox(self.groupBox_000)
        self.comboBox_00000.setObjectName("comboBox_00000")
        self.comboBox_00000.addItem('각인1')
        self.comboBox_00000.addItems(data.imprint_dict.keys())
        self.gridLayout_000.addWidget(self.comboBox_00000, 0, 0, 1, 1)
        self.comboBox_00001 = QtWidgets.QComboBox(self.groupBox_000)
        self.comboBox_00001.setObjectName("comboBox_00001")
        self.comboBox_00001.addItem('미사용')
        self.comboBox_00001.addItems(['3레벨', '2레벨', '1레벨'])
        self.gridLayout_000.addWidget(self.comboBox_00001, 0, 1, 1, 1)

        self.comboBox_00010 = QtWidgets.QComboBox(self.groupBox_000)
        self.comboBox_00010.setObjectName("comboBox_00010")
        self.comboBox_00010.addItem('각인2')
        self.comboBox_00010.addItems(data.imprint_dict.keys())
        self.gridLayout_000.addWidget(self.comboBox_00010, 1, 0, 1, 1)
        self.comboBox_00011 = QtWidgets.QComboBox(self.groupBox_000)
        self.comboBox_00011.setObjectName("comboBox_00011")
        self.comboBox_00011.addItem('미사용')
        self.comboBox_00011.addItems(['3레벨', '2레벨', '1레벨'])
        self.gridLayout_000.addWidget(self.comboBox_00011, 1, 1, 1, 1)

        self.comboBox_00020 = QtWidgets.QComboBox(self.groupBox_000)
        self.comboBox_00020.setObjectName("comboBox_00020")
        self.comboBox_00020.addItem('각인3')
        self.comboBox_00020.addItems(data.imprint_dict.keys())
        self.gridLayout_000.addWidget(self.comboBox_00020, 2, 0, 1, 1)
        self.comboBox_00021 = QtWidgets.QComboBox(self.groupBox_000)
        self.comboBox_00021.setObjectName("comboBox_00021")
        self.comboBox_00021.addItem('미사용')
        self.comboBox_00021.addItems(['3레벨', '2레벨', '1레벨'])
        self.gridLayout_000.addWidget(self.comboBox_00021, 2, 1, 1, 1)

        self.comboBox_00030 = QtWidgets.QComboBox(self.groupBox_000)
        self.comboBox_00030.setObjectName("comboBox_00030")
        self.comboBox_00030.addItem('각인4')
        self.comboBox_00030.addItems(data.imprint_dict.keys())
        self.gridLayout_000.addWidget(self.comboBox_00030, 3, 0, 1, 1)
        self.comboBox_00031 = QtWidgets.QComboBox(self.groupBox_000)
        self.comboBox_00031.setObjectName("comboBox_00031")
        self.comboBox_00031.addItem('미사용')
        self.comboBox_00031.addItems(['3레벨', '2레벨', '1레벨'])
        self.gridLayout_000.addWidget(self.comboBox_00031, 3, 1, 1, 1)

        self.comboBox_00040 = QtWidgets.QComboBox(self.groupBox_000)
        self.comboBox_00040.setObjectName("comboBox_00040")
        self.comboBox_00040.addItem('각인5')
        self.comboBox_00040.addItems(data.imprint_dict.keys())
        self.gridLayout_000.addWidget(self.comboBox_00040, 4, 0, 1, 1)
        self.comboBox_00041 = QtWidgets.QComboBox(self.groupBox_000)
        self.comboBox_00041.setObjectName("comboBox_00041")
        self.comboBox_00041.addItem('미사용')
        self.comboBox_00041.addItems(['3레벨', '2레벨', '1레벨'])
        self.gridLayout_000.addWidget(self.comboBox_00041, 4, 1, 1, 1)

        self.comboBox_00050 = QtWidgets.QComboBox(self.groupBox_000)
        self.comboBox_00050.setObjectName("comboBox_00050")
        self.comboBox_00050.addItem('각인6')
        self.comboBox_00050.addItems(data.imprint_dict.keys())
        self.gridLayout_000.addWidget(self.comboBox_00050, 5, 0, 1, 1)
        self.comboBox_00051 = QtWidgets.QComboBox(self.groupBox_000)
        self.comboBox_00051.setObjectName("comboBox_00051")
        self.comboBox_00051.addItem('미사용')
        self.comboBox_00051.addItems(['3레벨', '2레벨', '1레벨'])
        self.gridLayout_000.addWidget(self.comboBox_00051, 5, 1, 1, 1)

        self.gridLayout_000.setColumnStretch(0, 2)
        self.gridLayout_000.setColumnStretch(1, 1)

        self.verticalLayout_000.addLayout(self.gridLayout_000)
        self.verticalLayout_00.addWidget(self.groupBox_000)

        # TAB0-0 장착 각인
        self.groupBox_001 = QtWidgets.QGroupBox(self.tab_0)
        self.groupBox_001.setObjectName("groupBox_001")
        self.verticalLayout_001 = QtWidgets.QVBoxLayout(self.groupBox_001)
        #self.verticalLayout_001.setSpacing(10)
        self.verticalLayout_001.setObjectName("verticalLayout_001")
        self.gridLayout_001 = QtWidgets.QGridLayout()
        self.gridLayout_001.setObjectName("gridLayout_001")
        
        self.comboBox_00100 = QtWidgets.QComboBox(self.groupBox_001)
        self.comboBox_00100.setObjectName("comboBox_00100")
        self.comboBox_00100.addItem('각인1')
        self.gridLayout_001.addWidget(self.comboBox_00100, 0, 0, 1, 1)
        self.comboBox_00101 = QtWidgets.QComboBox(self.groupBox_001)
        self.comboBox_00101.setObjectName("comboBox_00101")
        self.comboBox_00101.addItems(['12', '9', '6', '3'])
        self.gridLayout_001.addWidget(self.comboBox_00101, 0, 1, 1, 1)
        
        self.comboBox_00110 = QtWidgets.QComboBox(self.groupBox_001)
        self.comboBox_00110.setObjectName("comboBox_00110")
        self.comboBox_00110.addItem('각인2')
        self.gridLayout_001.addWidget(self.comboBox_00110, 1, 0, 1, 1)
        self.comboBox_00111 = QtWidgets.QComboBox(self.groupBox_001)
        self.comboBox_00111.setObjectName("comboBox_00111")
        self.comboBox_00111.addItems(['12', '9', '6', '3'])
        self.gridLayout_001.addWidget(self.comboBox_00111, 1, 1, 1, 1)

        self.gridLayout_001.setColumnStretch(0, 2)
        self.gridLayout_001.setColumnStretch(1, 1)
        
        self.verticalLayout_001.addLayout(self.gridLayout_001)
        self.verticalLayout_00.addWidget(self.groupBox_001)

        # TAB0-0 어빌리티 스톤
        self.groupBox_002 = QtWidgets.QGroupBox(self.tab_0)
        self.groupBox_002.setObjectName("groupBox_002")
        self.verticalLayout_002 = QtWidgets.QVBoxLayout(self.groupBox_002)
        #self.verticalLayout_002.setSpacing(10)
        self.verticalLayout_002.setObjectName("verticalLayout_002")
        self.gridLayout_002 = QtWidgets.QGridLayout()
        self.gridLayout_002.setObjectName("gridLayout_002")
        
        self.comboBox_00200 = QtWidgets.QComboBox(self.groupBox_002)
        self.comboBox_00200.setObjectName("comboBox_00200")
        self.comboBox_00200.addItem('각인1')
        self.gridLayout_002.addWidget(self.comboBox_00200, 0, 0, 1, 1)
        self.comboBox_00201 = QtWidgets.QComboBox(self.groupBox_002)
        self.comboBox_00201.setObjectName("comboBox_00201")
        self.comboBox_00201.addItems(['10', '9', '8', '7', '6', '5', '4', '3', '2', '1'])
        self.gridLayout_002.addWidget(self.comboBox_00201, 0, 1, 1, 1)
        
        self.comboBox_00210 = QtWidgets.QComboBox(self.groupBox_002)
        self.comboBox_00210.setObjectName("comboBox_00210")
        self.comboBox_00210.addItem('각인2')
        self.gridLayout_002.addWidget(self.comboBox_00210, 1, 0, 1, 1)
        self.comboBox_00211 = QtWidgets.QComboBox(self.groupBox_002)
        self.comboBox_00211.setObjectName("comboBox_00211")
        self.comboBox_00211.addItems(['10', '9', '8', '7', '6', '5', '4', '3', '2', '1'])
        self.gridLayout_002.addWidget(self.comboBox_00211, 1, 1, 1, 1)
        
        self.comboBox_00220 = QtWidgets.QComboBox(self.groupBox_002)
        self.comboBox_00220.setObjectName("comboBox_00220")
        self.comboBox_00220.addItem('디버프')
        self.comboBox_00220.addItems(data.debuff_dict.keys())
        self.gridLayout_002.addWidget(self.comboBox_00220, 2, 0, 1, 1)
        self.comboBox_00221 = QtWidgets.QComboBox(self.groupBox_002)
        self.comboBox_00221.setObjectName("comboBox_00221")
        self.comboBox_00221.addItems(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.gridLayout_002.addWidget(self.comboBox_00221, 2, 1, 1, 1)

        self.gridLayout_002.setColumnStretch(0, 2)
        self.gridLayout_002.setColumnStretch(1, 1)
        
        self.verticalLayout_002.addLayout(self.gridLayout_002)
        self.verticalLayout_00.addWidget(self.groupBox_002)

        # TAB0-0 비율 조정(5:2:3)
        self.verticalLayout_00.setStretch(0, 5)
        self.verticalLayout_00.setStretch(1, 2)
        self.verticalLayout_00.setStretch(2, 3)
        # TAB0-0 end
        self.horizontalLayout_0.addLayout(self.verticalLayout_00)

        # TAB0-1
        self.verticalLayout_01 = QtWidgets.QVBoxLayout()
        self.verticalLayout_01.setObjectName("verticalLayout_01")

        # TAB0-1 특성
        self.groupBox_010 = QtWidgets.QGroupBox(self.tab_0)
        self.groupBox_010.setObjectName("groupBox_010")
        self.verticalLayout_010 = QtWidgets.QVBoxLayout(self.groupBox_010)
        self.verticalLayout_010.setObjectName("verticalLayout_010")
        self.gridLayout_010 = QtWidgets.QGridLayout()
        self.gridLayout_010.setObjectName("gridLayout_010")
        
        self.label_01000 = QtWidgets.QLabel(self.groupBox_010)
        self.label_01000.setObjectName("label_01000")
        self.gridLayout_010.addWidget(self.label_01000, 0, 0, 1, 1)
        self.comboBox_01001 = QtWidgets.QComboBox(self.groupBox_010)
        self.comboBox_01001.setObjectName("comboBox_01001")
        self.comboBox_01001.addItems(data.nature_dict.keys())
        self.gridLayout_010.addWidget(self.comboBox_01001, 0, 1, 1, 1)
        self.comboBox_01002 = QtWidgets.QComboBox(self.groupBox_010)
        self.comboBox_01002.setObjectName("comboBox_01002")
        self.comboBox_01002.addItems(data.nature_dict.keys())
        self.gridLayout_010.addWidget(self.comboBox_01002, 0, 2, 1, 1)
        
        self.label_01010 = QtWidgets.QLabel(self.groupBox_010)
        self.label_01010.setObjectName("label_01010")
        self.gridLayout_010.addWidget(self.label_01010, 1, 0, 1, 1)
        self.comboBox_01011 = QtWidgets.QComboBox(self.groupBox_010)
        self.comboBox_01011.setObjectName("comboBox_01011")
        self.comboBox_01011.addItems(data.nature_dict.keys())
        self.gridLayout_010.addWidget(self.comboBox_01011, 1, 1, 1, 1)
        
        self.label_01020 = QtWidgets.QLabel(self.groupBox_010)
        self.label_01020.setObjectName("label_01020")
        self.gridLayout_010.addWidget(self.label_01020, 2, 0, 1, 1)
        self.comboBox_01021 = QtWidgets.QComboBox(self.groupBox_010)
        self.comboBox_01021.setObjectName("comboBox_01021")
        self.comboBox_01021.addItems(data.nature_dict.keys())
        self.gridLayout_010.addWidget(self.comboBox_01021, 2, 1, 1, 1)
        
        self.label_01030 = QtWidgets.QLabel(self.groupBox_010)
        self.label_01030.setObjectName("label_01030")
        self.gridLayout_010.addWidget(self.label_01030, 3, 0, 1, 1)
        self.comboBox_01031 = QtWidgets.QComboBox(self.groupBox_010)
        self.comboBox_01031.setObjectName("comboBox_01031")
        self.comboBox_01031.addItems(data.nature_dict.keys())
        self.gridLayout_010.addWidget(self.comboBox_01031, 3, 1, 1, 1)
        
        self.label_01040 = QtWidgets.QLabel(self.groupBox_010)
        self.label_01040.setObjectName("label_01040")
        self.gridLayout_010.addWidget(self.label_01040, 4, 0, 1, 1)
        self.comboBox_01041 = QtWidgets.QComboBox(self.groupBox_010)
        self.comboBox_01041.setObjectName("comboBox_01041")
        self.comboBox_01041.addItems(data.nature_dict.keys())
        self.gridLayout_010.addWidget(self.comboBox_01041, 4, 1, 1, 1)

        self.verticalLayout_010.addLayout(self.gridLayout_010)
        self.verticalLayout_01.addWidget(self.groupBox_010)

        # TAB0-1 보유한 악세서리
        self.groupBox_011 = QtWidgets.QGroupBox(self.tab_0)
        #self.groupBox_011.setLayoutDirection(QtCore.Qt.LeftToRight)
        #self.groupBox_011.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_011.setObjectName("groupBox_011")
        self.verticalLayout_011 = QtWidgets.QVBoxLayout(self.groupBox_011)
        self.verticalLayout_011.setObjectName("verticalLayout_011")
        self.gridLayout_011 = QtWidgets.QGridLayout()
        self.gridLayout_011.setObjectName("gridLayout_011")

        self.checkBox_01100 = QtWidgets.QCheckBox(self.groupBox_011)
        self.checkBox_01100.setObjectName("checkBox_01100")
        self.gridLayout_011.addWidget(self.checkBox_01100, 0, 0, 1, 1)
        self.pushButton_01101 = QtWidgets.QPushButton(self.groupBox_011)
        self.pushButton_01101.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_01101.setObjectName("pushButton_01101")
        self.gridLayout_011.addWidget(self.pushButton_01101, 0, 1, 1, 1)
        self.checkBox_01110 = QtWidgets.QCheckBox(self.groupBox_011)
        self.checkBox_01110.setObjectName("checkBox_01110")
        self.gridLayout_011.addWidget(self.checkBox_01110, 1, 0, 1, 1)
        self.pushButton_01111 = QtWidgets.QPushButton(self.groupBox_011)
        self.pushButton_01111.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_01111.setObjectName("pushButton_01111")
        self.gridLayout_011.addWidget(self.pushButton_01111, 1, 1, 1, 1)
        self.verticalLayout_011.addLayout(self.gridLayout_011)
        self.pushButton_011 = QtWidgets.QPushButton(self.groupBox_011)
        self.pushButton_011.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_011.setObjectName("pushButton_011")
        self.verticalLayout_011.addWidget(self.pushButton_011, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_01.addWidget(self.groupBox_011)
        # TAB0-1 end
        self.horizontalLayout_0.addLayout(self.verticalLayout_01)

        # TAB0-2
        self.verticalLayout_02 = QtWidgets.QVBoxLayout()
        self.verticalLayout_02.setObjectName("verticalLayout_02")

        # TAB0-2 세부 설정
        self.groupBox_020 = QtWidgets.QGroupBox(self.tab_0)
        self.groupBox_020.setObjectName("groupBox_020")
        self.verticalLayout_020 = QtWidgets.QVBoxLayout(self.groupBox_020)
        self.verticalLayout_020.setObjectName("verticalLayout_020")
        self.gridLayout_020 = QtWidgets.QGridLayout()
        self.gridLayout_020.setObjectName("gridLayout_020")

        self.label_02000 = QtWidgets.QLabel(self.groupBox_020)
        self.label_02000.setObjectName("label_02000")
        self.gridLayout_020.addWidget(self.label_02000, 0, 0, 1, 1)
        self.comboBox_02001 = QtWidgets.QComboBox(self.groupBox_020)
        self.comboBox_02001.setObjectName("comboBox_02001")
        self.gridLayout_020.addWidget(self.comboBox_02001, 0, 1, 1, 1)
        self.comboBox_02002 = QtWidgets.QComboBox(self.groupBox_020)
        self.comboBox_02002.setObjectName("comboBox_02002")
        self.gridLayout_020.addWidget(self.comboBox_02002, 0, 2, 1, 1)
        
        self.label_02010 = QtWidgets.QLabel(self.groupBox_020)
        self.label_02010.setObjectName("label_02010")
        self.gridLayout_020.addWidget(self.label_02010, 1, 0, 1, 1)
        self.comboBox_02011 = QtWidgets.QComboBox(self.groupBox_020)
        self.comboBox_02011.setObjectName("comboBox_02011")
        self.gridLayout_020.addWidget(self.comboBox_02011, 1, 1, 1, 1)
        
        self.label_02020 = QtWidgets.QLabel(self.groupBox_020)
        self.label_02020.setObjectName("label_02020")
        self.gridLayout_020.addWidget(self.label_02020, 2, 0, 1, 1)
        self.comboBox_02021 = QtWidgets.QComboBox(self.groupBox_020)
        self.comboBox_02021.setObjectName("comboBox_02021")
        self.gridLayout_020.addWidget(self.comboBox_02021, 2, 1, 1, 1)
        
        self.label_02030 = QtWidgets.QLabel(self.groupBox_020)
        self.label_02030.setObjectName("label_02030")
        self.gridLayout_020.addWidget(self.label_02030, 3, 0, 1, 1)
        self.comboBox_02031 = QtWidgets.QComboBox(self.groupBox_020)
        self.comboBox_02031.setObjectName("comboBox_02031")
        self.gridLayout_020.addWidget(self.comboBox_02031, 3, 1, 1, 1)

        self.label_02040 = QtWidgets.QLabel(self.groupBox_020)
        self.label_02040.setObjectName("label_02040")
        self.gridLayout_020.addWidget(self.label_02040, 4, 0, 1, 1)
        self.comboBox_02041 = QtWidgets.QComboBox(self.groupBox_020)
        self.comboBox_02041.setObjectName("comboBox_02041")
        self.gridLayout_020.addWidget(self.comboBox_02041, 4, 1, 1, 1)

        self.verticalLayout_020.addLayout(self.gridLayout_020)
        self.verticalLayout_02.addWidget(self.groupBox_020)

        # TAB0-2 불러오기
        self.groupBox_021 = QtWidgets.QGroupBox(self.tab_0)
        self.groupBox_021.setObjectName("groupBox_021")
        self.verticalLayout_021 = QtWidgets.QVBoxLayout(self.groupBox_021)
        self.verticalLayout_021.setObjectName("verticalLayout_021")
        self.gridLayout_021 = QtWidgets.QGridLayout()
        self.gridLayout_021.setObjectName("gridLayout_021")

        self.label_02100 = QtWidgets.QLabel(self.groupBox_021)
        self.label_02100.setObjectName("label_02100")
        self.gridLayout_021.addWidget(self.label_02100, 0, 0, 1, 1)
        self.pushButton_02101 = QtWidgets.QPushButton(self.groupBox_021)
        self.pushButton_02101.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_02101.setObjectName("pushButton_02101")
        self.gridLayout_021.addWidget(self.pushButton_02101, 0, 1, 1, 1)
        
        self.label_02110 = QtWidgets.QLabel(self.groupBox_021)
        self.label_02110.setObjectName("label_02110")
        self.gridLayout_021.addWidget(self.label_02110, 1, 0, 1, 1)
        self.pushButton_02111 = QtWidgets.QPushButton(self.groupBox_021)
        self.pushButton_02111.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_02111.setObjectName("pushButton_02111")
        self.gridLayout_021.addWidget(self.pushButton_02111, 1, 1, 1, 1)
        
        self.label_02120 = QtWidgets.QLabel(self.groupBox_021)
        self.label_02120.setObjectName("label_02120")
        self.gridLayout_021.addWidget(self.label_02120, 2, 0, 1, 1)
        self.pushButton_02121 = QtWidgets.QPushButton(self.groupBox_021)
        self.pushButton_02121.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_02121.setObjectName("pushButton_02121")
        self.gridLayout_021.addWidget(self.pushButton_02121, 2, 1, 1, 1)
        
        self.verticalLayout_021.addLayout(self.gridLayout_021)
        self.verticalLayout_02.addWidget(self.groupBox_021)

        # progress bar
        self.progressBar1 = QtWidgets.QProgressBar(self.tab_0)
        self.progressBar1.setObjectName("progressBar1")
        self.verticalLayout_02.addWidget(self.progressBar1)
        self.progressBar2 = QtWidgets.QProgressBar(self.tab_0)
        self.progressBar2.setObjectName("progressBar2")
        self.verticalLayout_02.addWidget(self.progressBar2)


        # calc button
        self.pushButton_calc = QtWidgets.QPushButton(self.tab_0)
        self.pushButton_calc.setObjectName("pushButton_calc")
        self.verticalLayout_02.addWidget(self.pushButton_calc)
        # TAB0-2 end
        self.horizontalLayout_0.addLayout(self.verticalLayout_02)
        # TAB0 end
        self.tabWidget.addTab(self.tab_0, "")

        # TAB1
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")

        # TAB1-0
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")

        # TAB1-0 불러오기
        self.groupBox_100 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_100.setObjectName("groupBox_100")
        self.verticalLayout_100 = QtWidgets.QVBoxLayout(self.groupBox_100)
        self.verticalLayout_100.setObjectName("verticalLayout_100")
        self.pushButton_100 = QtWidgets.QPushButton(self.groupBox_100)
        self.pushButton_100.setObjectName("pushButton_100")
        self.verticalLayout_100.addWidget(self.pushButton_100)
        self.verticalLayout_10.addWidget(self.groupBox_100)

        # TAB1-0 필터
        self.groupBox_101 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_101.setObjectName("groupBox_101")
        self.verticalLayout_1001 = QtWidgets.QVBoxLayout(self.groupBox_101)
        self.verticalLayout_1001.setObjectName("verticalLayout_1001")
        self.verticalLayout_10.addWidget(self.groupBox_101)

        # TAB1-0 비율 조정(1:3)
        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 3)
        # TAB1-0 end
        self.horizontalLayout_1.addLayout(self.verticalLayout_10)

        # TAB1-1
        self.tableWidget = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_1.addWidget(self.tableWidget)

        # TAB1 비율 조정(1:3)
        self.horizontalLayout_1.setStretch(0, 1)
        self.horizontalLayout_1.setStretch(1, 3)
        # TAB1 end
        self.verticalLayout_1.addLayout(self.horizontalLayout_1)
        self.tabWidget.addTab(self.tab_1, "")
        # TAB end
        self.verticalLayout_tab.addWidget(self.tabWidget)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox_000.setTitle(_translate("MainWindow", "목표 각인"))
        self.groupBox_001.setTitle(_translate("MainWindow", "장착 각인"))
        self.groupBox_002.setTitle(_translate("MainWindow", "어빌리티 스톤"))
        self.groupBox_010.setTitle(_translate("MainWindow", "특성"))
        self.label_01000.setText(_translate("MainWindow", "목걸이"))
        self.label_01010.setText(_translate("MainWindow", "귀걸이1"))
        self.label_01020.setText(_translate("MainWindow", "귀걸이2"))
        self.label_01030.setText(_translate("MainWindow", "반지1"))
        self.label_01040.setText(_translate("MainWindow", "반지2"))
        self.groupBox_011.setTitle(_translate("MainWindow", "보유한 악세서리"))
        self.checkBox_01100.setText(_translate("MainWindow", "checkBox_01100"))
        self.pushButton_01101.setText(_translate("MainWindow", "Del"))
        self.checkBox_01110.setText(_translate("MainWindow", "checkBox_01100"))
        self.pushButton_01111.setText(_translate("MainWindow", "Del"))
        self.pushButton_011.setText(_translate("MainWindow", "Add"))
        self.groupBox_020.setTitle(_translate("MainWindow", "세부 설정"))
        self.label_02040.setText(_translate("MainWindow", "TextLabel"))
        self.label_02000.setText(_translate("MainWindow", "TextLabel"))
        self.label_02010.setText(_translate("MainWindow", "TextLabel"))
        self.label_02020.setText(_translate("MainWindow", "TextLabel"))
        self.label_02030.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_021.setTitle(_translate("MainWindow", "불러오기"))
        self.label_02100.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_02101.setText(_translate("MainWindow", "Save"))
        self.label_02110.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_02111.setText(_translate("MainWindow", "Save"))
        self.label_02120.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_02121.setText(_translate("MainWindow", "Save"))
        self.pushButton_calc.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_0), _translate("MainWindow", "Tab 1"))
        self.groupBox_100.setTitle(_translate("MainWindow", "불러오기"))
        self.pushButton_100.setText(_translate("MainWindow", "PushButton"))
        self.groupBox_101.setTitle(_translate("MainWindow", "필터"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "특성합"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "가격"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "자세히 보기"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1456"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "20000"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "234234234"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "111"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "2222"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "33333"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Tab 2"))


    def connect_event(self):
        self.comboBox_00000.currentIndexChanged.connect(self.selectionchange)
        self.comboBox_00010.currentIndexChanged.connect(self.selectionchange)
        self.comboBox_00020.currentIndexChanged.connect(self.selectionchange)
        self.comboBox_00030.currentIndexChanged.connect(self.selectionchange)
        self.comboBox_00040.currentIndexChanged.connect(self.selectionchange)
        self.comboBox_00050.currentIndexChanged.connect(self.selectionchange)
        self.pushButton_calc.clicked.connect(self.Calcbutton_click)


    def selectionchange(self):
        self.comboBox_00100.clear()
        self.comboBox_00110.clear()
        self.comboBox_00200.clear()
        self.comboBox_00210.clear()

        imprint_list = []
        imprint_list.append(self.comboBox_00000.currentText())
        imprint_list.append(self.comboBox_00010.currentText())
        imprint_list.append(self.comboBox_00020.currentText())
        imprint_list.append(self.comboBox_00030.currentText())
        imprint_list.append(self.comboBox_00040.currentText())
        imprint_list.append(self.comboBox_00050.currentText())

        for i in imprint_list[:]:
            if i[:2] == '각인': imprint_list.remove(i)

        self.comboBox_00100.addItems(imprint_list)
        self.comboBox_00110.addItems(imprint_list)
        self.comboBox_00200.addItems(imprint_list)
        self.comboBox_00210.addItems(imprint_list)


    def progress_set(self):
        self.progressBar1.setMaximum()




    def imprintsetting(self):
        imprint0_name = self.comboBox_00000.currentText()
        imprint0_value = self.comboBox_00001.currentText()
        imprint1_name = self.comboBox_00010.currentText()
        imprint1_value = self.comboBox_00011.currentText()
        imprint2_name = self.comboBox_00020.currentText()
        imprint2_value = self.comboBox_00021.currentText()
        imprint3_name = self.comboBox_00030.currentText()
        imprint3_value = self.comboBox_00031.currentText()
        imprint4_name = self.comboBox_00040.currentText()
        imprint4_value = self.comboBox_00041.currentText()
        imprint5_name = self.comboBox_00050.currentText()
        imprint5_value = self.comboBox_00051.currentText()

        temp_list = [(imprint0_name, imprint0_value), (imprint1_name, imprint1_value), (imprint2_name, imprint2_value), (imprint3_name, imprint3_value), (imprint4_name, imprint4_value), (imprint5_name, imprint5_value)]
        imprint_list = []
        for name, value in temp_list[:]:
            if name[:2] == '각인' or value == '미사용':
                temp_list.remove((name, value))
                continue
            value = int(value.replace('레벨', ''))
            imprint_list.append((name, value))

        imprint0_name = self.comboBox_00100.currentText()
        imprint0_value = self.comboBox_00101.currentText()
        imprint1_name = self.comboBox_00110.currentText()
        imprint1_value = self.comboBox_00111.currentText()

        imprint_bonus = [(imprint0_name, int(imprint0_value)), (imprint1_name, int(imprint1_value))]

        imprint0_name = self.comboBox_00200.currentText()
        imprint0_value = self.comboBox_00201.currentText()
        imprint1_name = self.comboBox_00210.currentText()
        imprint1_value = self.comboBox_00211.currentText()
        debuff_name = self.comboBox_00220.currentText()
        debuff_value = self.comboBox_00221.currentText()

        imprint_stone = [(imprint0_name, int(imprint0_value)), (imprint1_name, int(imprint1_value)), (debuff_name, int(debuff_value))]

        ac1_nature1 = self.comboBox_01001.currentText()
        ac1_nature2 = self.comboBox_01002.currentText()
        ac2_nature = self.comboBox_01011.currentText()
        ac3_nature = self.comboBox_01021.currentText()
        ac4_nature = self.comboBox_01031.currentText()
        ac5_nature = self.comboBox_01041.currentText()

        nature_list = [('목걸이', (ac1_nature1, ac1_nature2)), ('귀걸이', (ac2_nature, '')), ('귀걸이', (ac3_nature, '')), ('반지', (ac4_nature, '')), ('반지', (ac5_nature, ''))]

        print(imprint_list)
        print(imprint_bonus)
        print(imprint_stone)
        print(nature_list)

        ac_com, ac_kind = calc.calc(imprint_list, imprint_bonus, imprint_stone)
        for i in ac_com:
            print(i)
        for i in ac_kind:
            print(i)

        crawling.access()
        session = crawling.make_session()
        item_list = crawling.crawling(session, ac_kind, nature_list)

        tm1 = time.time()
        cd = calc.calc_ac(ac_com, item_list, nature_list, imprint_stone)
        tm2 = time.time()
        print(tm2 - tm1)


    def Calcbutton_click(self):
        self.imprintsetting()



def main1():
    imprint_value = [('만개', 3), ('중갑 착용', 3), ('전문의', 3), ('각성', 3), ('구슬동자', 3)]
    bonus = (('만개', 12), ('전문의', 12))
    stone = (('각성', 5), ('중갑 착용', 8), ('방어력 감소', 2))
    nature_list = (('목걸이', ('신속', '특화')), ('귀걸이', ('신속', '')), ('귀걸이', ('신속', '')), ('반지', ('신속', '')), ('반지', ('신속', '')))
    quality = [90, 70, 70, 70, 70]

    ac_com, ac_pair, ac_kind = calc.calc(imprint_value, bonus, stone)
    for i in ac_com:
        print(i)
    for i in ac_pair:
        print(i)
    for i in ac_kind:
        print(i)

    #crawling.access()
    session = crawling.make_session()
    crawling.crawling(session, ac_pair, nature_list, quality)

    tm1 = time.time()
    calc.calc_ac1(ac_com, ac_kind, nature_list, stone)
    tm2 = time.time()
    print(tm2 - tm1)

    calc.filtering()


if __name__ == '__main__':
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # ui.connect_event()
    #
    # MainWindow.show()
    # sys.exit(app.exec_())

    main1()
    # calc.minn()



