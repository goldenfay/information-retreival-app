# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("* {\n"
"    background-color:white;\n"
"}\n"
"QPushButton#showIndexesButton:hover,QPushButton#booleanSearchButton:hover,QPushButton#vectorialSearchButton:hover{\n"
"background-color:red;\n"
"}\n"
"QTabBar::tab{\n"
"background-color:white;\n"
"height: 40px;\n"
"min-width: 50px;\n"
"width:150px;\n"
"color: #156abf;\n"
"\n"
"}\n"
"QTabBar::tab:selected {\n"
"background-color:#48a5e8;\n"
"border-top-right-radius: 4px;\n"
"border-top-left-radius: 4px;\n"
"color:white;\n"
"}\n"
"   \n"
"QTabWidget>QWidget>QWidget{\n"
"}\n"
"\n"
"#indexesTab QRadioButton::indicator,#vectorialModelTab QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"\n"
"}\n"
"\n"
"#indexesTab QRadioButton::indicator:checked,#vectorialModelTab QRadioButton::indicator:checked {\n"
"    background-color:   #48a5e8;\n"
"    border:                 2px solid #075891;\n"
"    margin :3px;\n"
"}\n"
"\n"
"#indexesTab QRadioButton::indicator:unchecked,#vectorialModelTab QRadioButton::indicator:unchecked {\n"
" border:  2px solid #dbd5d5;\n"
"}\n"
"#indexesTreeWidget {\n"
"    border:None\n"
"} \n"
"#indexesTreeWidget::Item{\n"
"        border-bottom:2px solid black;\n"
"        color: rgba(255,255,255,255);\n"
"}\n"
"\n"
"\n"
"/******************************************************/\n"
"#rechercheTab QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:          9px;\n"
"\n"
"}\n"
"\n"
"#rechercheTab QRadioButton::indicator:checked {\n"
"    background-color:   #48a5e8;\n"
"    border:2px solid #075891;\n"
"    margin :7px;\n"
"\n"
"}\n"
"#rechercheTab QRadioButton:checked{\n"
"    color:   #48a5e8;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#rechercheTab QRadioButton::indicator:unchecked {\n"
"     border:  2px solid #dbd5d5;\n"
"}\n"
"\n"
"#rechercheTab #searchWordField{\n"
"     background-color: red;\n"
"}\n"
"#rechercheTab #searchWordField:focus{\n"
"    width:200px;\n"
" background-color: green;\n"
"}\n"
"\n"
"*[cssClass=\"large\"] {\n"
"background-color:red;\n"
"color:blue;\n"
"}\n"
"/****************************************************/\n"
"\n"
"#vectorialModelTab #measurementGroupBox,#vectorialModelTab #label_11 {\n"
"    color:#0fb9f2;\n"
"}\n"
"\n"
"#measurementGroupBox QRadioButton{\n"
"color:#f54242;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"\n"
"\n"
"}\n"
"QComboBox::down-arrow {\n"
"    \n"
"}\n"
"QPushButton:hover#vectorielEvalButton{\n"
"background-color:yellow;\n"
"}\n"
"\n"
"\n"
"/*******************************************************************************************/\n"
"\n"
"#evaluationTab #measurementGroupBox_2  {\n"
"    color:#0b4c8c;\n"
"}\n"
"#measurementGroupBox_2 QRadioButton{\n"
"color:#2ba3e3;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 1px solid #1e72c7;\n"
"    background: none;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 2px solid white;\n"
"    background:#1e72c7;\n"
"   padding:2px;\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"")
        MainWindow.setIconSize(QtCore.QSize(33, 33))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(-10, 10, 781, 591))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabs.setFont(font)
        self.tabs.setStyleSheet("border: Opx;")
        self.tabs.setTabsClosable(False)
        self.tabs.setObjectName("tabs")
        self.indexesTab = QtWidgets.QWidget()
        self.indexesTab.setMinimumSize(QtCore.QSize(100, 465))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.indexesTab.setFont(font)
        self.indexesTab.setStyleSheet("height : 50px;\n"
"")
        self.indexesTab.setObjectName("indexesTab")
        self.label = QtWidgets.QLabel(self.indexesTab)
        self.label.setGeometry(QtCore.QRect(240, 20, 241, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#107ac7;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.indexesTab)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.indexesTab)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.indexesTab)
        self.groupBox.setGeometry(QtCore.QRect(250, 130, 361, 41))
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.classicIndexRB = QtWidgets.QRadioButton(self.groupBox)
        self.classicIndexRB.setGeometry(QtCore.QRect(20, 10, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.classicIndexRB.setFont(font)
        self.classicIndexRB.setObjectName("classicIndexRB")
        self.weightedIndexRB = QtWidgets.QRadioButton(self.groupBox)
        self.weightedIndexRB.setGeometry(QtCore.QRect(180, 10, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.weightedIndexRB.setFont(font)
        self.weightedIndexRB.setObjectName("weightedIndexRB")
        self.groupBox_2 = QtWidgets.QGroupBox(self.indexesTab)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 190, 361, 41))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.frequencyIndexRB = QtWidgets.QRadioButton(self.groupBox_2)
        self.frequencyIndexRB.setGeometry(QtCore.QRect(20, 10, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.frequencyIndexRB.setFont(font)
        self.frequencyIndexRB.setObjectName("frequencyIndexRB")
        self.reverseIndexRB = QtWidgets.QRadioButton(self.groupBox_2)
        self.reverseIndexRB.setGeometry(QtCore.QRect(180, 10, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.reverseIndexRB.setFont(font)
        self.reverseIndexRB.setObjectName("reverseIndexRB")
        self.showIndexesButton = QtWidgets.QPushButton(self.indexesTab)
        self.showIndexesButton.setGeometry(QtCore.QRect(670, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.showIndexesButton.setFont(font)
        self.showIndexesButton.setStyleSheet("background-color:#107ac7;\n"
"color: white;\n"
"\n"
"")
        self.showIndexesButton.setObjectName("showIndexesButton")
        self.showIndexesArea = QtWidgets.QScrollArea(self.indexesTab)
        self.showIndexesArea.setGeometry(QtCore.QRect(80, 280, 651, 221))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.showIndexesArea.setFont(font)
        self.showIndexesArea.setStyleSheet("background-color:white;")
        self.showIndexesArea.setWidgetResizable(True)
        self.showIndexesArea.setObjectName("showIndexesArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 651, 221))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.indexesTreeWidget = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        self.indexesTreeWidget.setGeometry(QtCore.QRect(70, 10, 461, 192))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.indexesTreeWidget.setFont(font)
        self.indexesTreeWidget.setStyleSheet("border:0.3px solid #609af7;\n"
"background-color: white;")
        self.indexesTreeWidget.setObjectName("indexesTreeWidget")
        self.indexesTreeWidget.headerItem().setText(0, "1")
        self.showIndexesArea.setWidget(self.scrollAreaWidgetContents)
        self.errorLabel = QtWidgets.QLabel(self.indexesTab)
        self.errorLabel.setGeometry(QtCore.QRect(130, 250, 581, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setItalic(True)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color:#e61c1c;")
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.constructTimeLabel = QtWidgets.QLabel(self.indexesTab)
        self.constructTimeLabel.setGeometry(QtCore.QRect(40, 522, 481, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.constructTimeLabel.setFont(font)
        self.constructTimeLabel.setStyleSheet("color:#107ac7;")
        self.constructTimeLabel.setText("")
        self.constructTimeLabel.setObjectName("constructTimeLabel")
        self.constructTimeLabel_2 = QtWidgets.QLabel(self.indexesTab)
        self.constructTimeLabel_2.setGeometry(QtCore.QRect(530, 520, 261, 21))
        self.constructTimeLabel_2.setText("")
        self.constructTimeLabel_2.setObjectName("constructTimeLabel_2")
        self.tabs.addTab(self.indexesTab, "")
        self.rechercheTab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rechercheTab.setFont(font)
        self.rechercheTab.setStyleSheet("*{\n"
"background-color:white;\n"
"}\n"
"")
        self.rechercheTab.setObjectName("rechercheTab")
        self.label_7 = QtWidgets.QLabel(self.rechercheTab)
        self.label_7.setGeometry(QtCore.QRect(210, 30, 331, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#107ac7;\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.groupBox_5 = QtWidgets.QGroupBox(self.rechercheTab)
        self.groupBox_5.setGeometry(QtCore.QRect(100, 120, 641, 91))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setItalic(True)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.searchWordRB = QtWidgets.QRadioButton(self.groupBox_5)
        self.searchWordRB.setGeometry(QtCore.QRect(20, 30, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.searchWordRB.setFont(font)
        self.searchWordRB.setObjectName("searchWordRB")
        self.fileIndexExpRB = QtWidgets.QRadioButton(self.groupBox_5)
        self.fileIndexExpRB.setGeometry(QtCore.QRect(320, 30, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.fileIndexExpRB.setFont(font)
        self.fileIndexExpRB.setObjectName("fileIndexExpRB")
        self.searchWordField = QtWidgets.QLineEdit(self.rechercheTab)
        self.searchWordField.setGeometry(QtCore.QRect(130, 230, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setItalic(True)
        self.searchWordField.setFont(font)
        self.searchWordField.setStyleSheet("")
        self.searchWordField.setObjectName("searchWordField")
        self.searchSA = QtWidgets.QScrollArea(self.rechercheTab)
        self.searchSA.setGeometry(QtCore.QRect(150, 330, 521, 181))
        self.searchSA.setWidgetResizable(True)
        self.searchSA.setObjectName("searchSA")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 519, 179))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 501, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.indexedSearchVBox = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.indexedSearchVBox.setContentsMargins(0, 0, 0, 0)
        self.indexedSearchVBox.setObjectName("indexedSearchVBox")
        self.searchSA.setWidget(self.scrollAreaWidgetContents_3)
        self.docNumGroupBox = QtWidgets.QGroupBox(self.rechercheTab)
        self.docNumGroupBox.setGeometry(QtCore.QRect(410, 220, 301, 61))
        self.docNumGroupBox.setTitle("")
        self.docNumGroupBox.setObjectName("docNumGroupBox")
        self.numDocSpinBox = QtWidgets.QSpinBox(self.docNumGroupBox)
        self.numDocSpinBox.setGeometry(QtCore.QRect(120, 20, 161, 41))
        self.numDocSpinBox.setMaximum(99999)
        self.numDocSpinBox.setObjectName("numDocSpinBox")
        self.label_4 = QtWidgets.QLabel(self.docNumGroupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.searchDocWordButton = QtWidgets.QPushButton(self.rechercheTab)
        self.searchDocWordButton.setGeometry(QtCore.QRect(560, 290, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.searchDocWordButton.setFont(font)
        self.searchDocWordButton.setStyleSheet("background-color:#34eb5e;\n"
"color:white;")
        self.searchDocWordButton.setObjectName("searchDocWordButton")
        self.errorLabel_2 = QtWidgets.QLabel(self.rechercheTab)
        self.errorLabel_2.setGeometry(QtCore.QRect(80, 290, 451, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setItalic(True)
        self.errorLabel_2.setFont(font)
        self.errorLabel_2.setStyleSheet("color:#e61c1c;")
        self.errorLabel_2.setText("")
        self.errorLabel_2.setObjectName("errorLabel_2")
        self.tabs.addTab(self.rechercheTab, "")
        self.booleanModelTab = QtWidgets.QWidget()
        self.booleanModelTab.setObjectName("booleanModelTab")
        self.label_8 = QtWidgets.QLabel(self.booleanModelTab)
        self.label_8.setGeometry(QtCore.QRect(150, 30, 471, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:#107ac7;\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.booleanModelTab)
        self.label_9.setGeometry(QtCore.QRect(100, 130, 371, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.booleansearchEdit = QtWidgets.QLineEdit(self.booleanModelTab)
        self.booleansearchEdit.setGeometry(QtCore.QRect(110, 190, 401, 31))
        self.booleansearchEdit.setObjectName("booleansearchEdit")
        self.booleanSearchButton = QtWidgets.QPushButton(self.booleanModelTab)
        self.booleanSearchButton.setGeometry(QtCore.QRect(560, 150, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.booleanSearchButton.setFont(font)
        self.booleanSearchButton.setStyleSheet("background-color:#107ac7;\n"
"color: white;\n"
"")
        self.booleanSearchButton.setObjectName("booleanSearchButton")
        self.booleanSA = QtWidgets.QScrollArea(self.booleanModelTab)
        self.booleanSA.setGeometry(QtCore.QRect(140, 280, 521, 231))
        self.booleanSA.setWidgetResizable(True)
        self.booleanSA.setObjectName("booleanSA")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 519, 229))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 501, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.booleanSearchVBox = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.booleanSearchVBox.setContentsMargins(0, 0, 0, 0)
        self.booleanSearchVBox.setObjectName("booleanSearchVBox")
        self.booleanSA.setWidget(self.scrollAreaWidgetContents_4)
        self.errorLabel_3 = QtWidgets.QLabel(self.booleanModelTab)
        self.errorLabel_3.setGeometry(QtCore.QRect(130, 240, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setItalic(True)
        self.errorLabel_3.setFont(font)
        self.errorLabel_3.setStyleSheet("color:#e61c1c;")
        self.errorLabel_3.setText("")
        self.errorLabel_3.setWordWrap(True)
        self.errorLabel_3.setObjectName("errorLabel_3")
        self.tabs.addTab(self.booleanModelTab, "")
        self.vectorialModelTab = QtWidgets.QWidget()
        self.vectorialModelTab.setObjectName("vectorialModelTab")
        self.label_10 = QtWidgets.QLabel(self.vectorialModelTab)
        self.label_10.setGeometry(QtCore.QRect(160, 10, 471, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:#107ac7;\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.vectorialModelTab)
        self.label_11.setGeometry(QtCore.QRect(50, 140, 371, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.vectorialSearchEdit = QtWidgets.QLineEdit(self.vectorialModelTab)
        self.vectorialSearchEdit.setGeometry(QtCore.QRect(60, 170, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setItalic(True)
        self.vectorialSearchEdit.setFont(font)
        self.vectorialSearchEdit.setObjectName("vectorialSearchEdit")
        self.vectorialSA = QtWidgets.QScrollArea(self.vectorialModelTab)
        self.vectorialSA.setGeometry(QtCore.QRect(60, 310, 691, 221))
        self.vectorialSA.setAutoFillBackground(True)
        self.vectorialSA.setWidgetResizable(True)
        self.vectorialSA.setObjectName("vectorialSA")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 689, 219))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 341, 181))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.vectorialResultsVBox = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.vectorialResultsVBox.setContentsMargins(0, 0, 0, 0)
        self.vectorialResultsVBox.setObjectName("vectorialResultsVBox")
        self.vectorial_exectime_label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.vectorial_exectime_label_1.setGeometry(QtCore.QRect(400, 20, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.vectorial_exectime_label_1.setFont(font)
        self.vectorial_exectime_label_1.setStyleSheet("color:#107ac7;")
        self.vectorial_exectime_label_1.setText("")
        self.vectorial_exectime_label_1.setObjectName("vectorial_exectime_label_1")
        self.vectorialSA.setWidget(self.scrollAreaWidgetContents_2)
        self.vectorialSearchButton = QtWidgets.QPushButton(self.vectorialModelTab)
        self.vectorialSearchButton.setGeometry(QtCore.QRect(310, 220, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.vectorialSearchButton.setFont(font)
        self.vectorialSearchButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.vectorialSearchButton.setStyleSheet("background-color:#107ac7;\n"
"color: white;\n"
"")
        self.vectorialSearchButton.setObjectName("vectorialSearchButton")
        self.measurementGroupBox = QtWidgets.QGroupBox(self.vectorialModelTab)
        self.measurementGroupBox.setGeometry(QtCore.QRect(470, 130, 301, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.measurementGroupBox.setFont(font)
        self.measurementGroupBox.setStyleSheet("")
        self.measurementGroupBox.setObjectName("measurementGroupBox")
        self.innerProductRB = QtWidgets.QRadioButton(self.measurementGroupBox)
        self.innerProductRB.setGeometry(QtCore.QRect(20, 30, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.innerProductRB.setFont(font)
        self.innerProductRB.setObjectName("innerProductRB")
        self.diceRB = QtWidgets.QRadioButton(self.measurementGroupBox)
        self.diceRB.setGeometry(QtCore.QRect(20, 80, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.diceRB.setFont(font)
        self.diceRB.setObjectName("diceRB")
        self.cosinusRB = QtWidgets.QRadioButton(self.measurementGroupBox)
        self.cosinusRB.setGeometry(QtCore.QRect(140, 30, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cosinusRB.setFont(font)
        self.cosinusRB.setObjectName("cosinusRB")
        self.jacardRB = QtWidgets.QRadioButton(self.measurementGroupBox)
        self.jacardRB.setGeometry(QtCore.QRect(140, 80, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.jacardRB.setFont(font)
        self.jacardRB.setObjectName("jacardRB")
        self.errorLabel_4 = QtWidgets.QLabel(self.vectorialModelTab)
        self.errorLabel_4.setGeometry(QtCore.QRect(130, 270, 451, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setItalic(True)
        self.errorLabel_4.setFont(font)
        self.errorLabel_4.setStyleSheet("color:#e61c1c;")
        self.errorLabel_4.setText("")
        self.errorLabel_4.setObjectName("errorLabel_4")
        self.tabs.addTab(self.vectorialModelTab, "")
        self.evaluationTab = QtWidgets.QWidget()
        self.evaluationTab.setObjectName("evaluationTab")
        self.vectorielEvalButton = QtWidgets.QPushButton(self.evaluationTab)
        self.vectorielEvalButton.setGeometry(QtCore.QRect(590, 200, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.vectorielEvalButton.setFont(font)
        self.vectorielEvalButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.vectorielEvalButton.setStyleSheet("background-color:#f54242;\n"
"color: white;\n"
"")
        self.vectorielEvalButton.setObjectName("vectorielEvalButton")
        self.label_18 = QtWidgets.QLabel(self.evaluationTab)
        self.label_18.setGeometry(QtCore.QRect(170, 10, 471, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:#107ac7;\n"
"")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.reqComboBox_2 = QtWidgets.QComboBox(self.evaluationTab)
        self.reqComboBox_2.setGeometry(QtCore.QRect(320, 130, 74, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.reqComboBox_2.setFont(font)
        self.reqComboBox_2.setAutoFillBackground(False)
        self.reqComboBox_2.setStyleSheet("\n"
"color:#0b4c8c;\n"
"\n"
"      border:none;\n"
"      border-radius: 3px;\n"
"\n"
"")
        self.reqComboBox_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.reqComboBox_2.setObjectName("reqComboBox_2")
        self.label_14 = QtWidgets.QLabel(self.evaluationTab)
        self.label_14.setGeometry(QtCore.QRect(20, 124, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:#0b4c8c;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.evaluationSA = QtWidgets.QScrollArea(self.evaluationTab)
        self.evaluationSA.setGeometry(QtCore.QRect(70, 310, 711, 211))
        self.evaluationSA.setStyleSheet("")
        self.evaluationSA.setWidgetResizable(True)
        self.evaluationSA.setObjectName("evaluationSA")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 711, 211))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.precisionLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.precisionLabel_2.setGeometry(QtCore.QRect(170, 130, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.precisionLabel_2.setFont(font)
        self.precisionLabel_2.setStyleSheet("color:#0b4c8c;")
        self.precisionLabel_2.setText("")
        self.precisionLabel_2.setObjectName("precisionLabel_2")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_17.setGeometry(QtCore.QRect(50, 130, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:#0b4c8c;")
        self.label_17.setObjectName("label_17")
        self.rappelLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.rappelLabel_2.setGeometry(QtCore.QRect(170, 100, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.rappelLabel_2.setFont(font)
        self.rappelLabel_2.setStyleSheet("color:#0b4c8c;")
        self.rappelLabel_2.setText("")
        self.rappelLabel_2.setObjectName("rappelLabel_2")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_16.setGeometry(QtCore.QRect(50, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:#0b4c8c;")
        self.label_16.setObjectName("label_16")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_15.setGeometry(QtCore.QRect(30, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:#f54242;")
        self.label_15.setObjectName("label_15")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_19.setGeometry(QtCore.QRect(440, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color:#0b4c8c;")
        self.label_19.setObjectName("label_19")
        self.requestContentLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.requestContentLabel.setGeometry(QtCore.QRect(450, 80, 211, 131))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setItalic(True)
        self.requestContentLabel.setFont(font)
        self.requestContentLabel.setStyleSheet("color:#115eab;")
        self.requestContentLabel.setText("")
        self.requestContentLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.requestContentLabel.setWordWrap(True)
        self.requestContentLabel.setObjectName("requestContentLabel")
        self.plotButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_5)
        self.plotButton.setGeometry(QtCore.QRect(580, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.plotButton.setFont(font)
        self.plotButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.plotButton.setStyleSheet("background-color:#1c59ba;\n"
"color: white;\n"
"")
        self.plotButton.setObjectName("plotButton")
        self.vectorial_exectime_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.vectorial_exectime_label.setGeometry(QtCore.QRect(50, 50, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.vectorial_exectime_label.setFont(font)
        self.vectorial_exectime_label.setStyleSheet("color:#0b4c8c;")
        self.vectorial_exectime_label.setText("")
        self.vectorial_exectime_label.setWordWrap(True)
        self.vectorial_exectime_label.setObjectName("vectorial_exectime_label")
        self.evaluationSA.setWidget(self.scrollAreaWidgetContents_5)
        self.measurementGroupBox_2 = QtWidgets.QGroupBox(self.evaluationTab)
        self.measurementGroupBox_2.setGeometry(QtCore.QRect(20, 170, 301, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.measurementGroupBox_2.setFont(font)
        self.measurementGroupBox_2.setStyleSheet("")
        self.measurementGroupBox_2.setObjectName("measurementGroupBox_2")
        self.innerProductRB_2 = QtWidgets.QRadioButton(self.measurementGroupBox_2)
        self.innerProductRB_2.setGeometry(QtCore.QRect(20, 30, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.innerProductRB_2.setFont(font)
        self.innerProductRB_2.setObjectName("innerProductRB_2")
        self.diceRB_2 = QtWidgets.QRadioButton(self.measurementGroupBox_2)
        self.diceRB_2.setGeometry(QtCore.QRect(20, 80, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.diceRB_2.setFont(font)
        self.diceRB_2.setObjectName("diceRB_2")
        self.cosinusRB_2 = QtWidgets.QRadioButton(self.measurementGroupBox_2)
        self.cosinusRB_2.setGeometry(QtCore.QRect(140, 30, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cosinusRB_2.setFont(font)
        self.cosinusRB_2.setObjectName("cosinusRB_2")
        self.jacardRB_2 = QtWidgets.QRadioButton(self.measurementGroupBox_2)
        self.jacardRB_2.setGeometry(QtCore.QRect(140, 80, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.jacardRB_2.setFont(font)
        self.jacardRB_2.setObjectName("jacardRB_2")
        self.errorLabel_5 = QtWidgets.QLabel(self.evaluationTab)
        self.errorLabel_5.setGeometry(QtCore.QRect(200, 290, 521, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setItalic(True)
        self.errorLabel_5.setFont(font)
        self.errorLabel_5.setStyleSheet("color:#e61c1c;")
        self.errorLabel_5.setText("")
        self.errorLabel_5.setObjectName("errorLabel_5")
        self.globalEvalCB = QtWidgets.QCheckBox(self.evaluationTab)
        self.globalEvalCB.setGeometry(QtCore.QRect(510, 130, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.globalEvalCB.setFont(font)
        self.globalEvalCB.setStyleSheet("color:#0b4c8c;")
        self.globalEvalCB.setObjectName("globalEvalCB")
        self.seuil_slider = QtWidgets.QSlider(self.evaluationTab)
        self.seuil_slider.setGeometry(QtCore.QRect(370, 210, 160, 19))
        self.seuil_slider.setStyleSheet("")
        self.seuil_slider.setMinimum(0)
        self.seuil_slider.setMaximum(100)
        self.seuil_slider.setProperty("value", 0)
        self.seuil_slider.setOrientation(QtCore.Qt.Horizontal)
        self.seuil_slider.setObjectName("seuil_slider")
        self.label_5 = QtWidgets.QLabel(self.evaluationTab)
        self.label_5.setGeometry(QtCore.QRect(410, 180, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#0b4c8c;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.seuil_label = QtWidgets.QLabel(self.evaluationTab)
        self.seuil_label.setGeometry(QtCore.QRect(420, 230, 47, 13))
        self.seuil_label.setText("")
        self.seuil_label.setObjectName("seuil_label")
        self.tabs.addTab(self.evaluationTab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Système de recherche d\'information"))
        self.label.setText(_translate("MainWindow", "Indexation"))
        self.label_2.setText(_translate("MainWindow", "Choisissez un index :"))
        self.label_3.setText(_translate("MainWindow", "Choisissez le type d\'index :"))
        self.classicIndexRB.setText(_translate("MainWindow", "Index classique"))
        self.weightedIndexRB.setText(_translate("MainWindow", "Index pondéré"))
        self.frequencyIndexRB.setText(_translate("MainWindow", "Index Par mots"))
        self.reverseIndexRB.setText(_translate("MainWindow", "Index Fichier inversé"))
        self.showIndexesButton.setText(_translate("MainWindow", "Afficher"))
        self.tabs.setTabText(self.tabs.indexOf(self.indexesTab), _translate("MainWindow", "Indexes"))
        self.label_7.setText(_translate("MainWindow", "Rechercher dans les indexes"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Choisissez une option :"))
        self.searchWordRB.setText(_translate("MainWindow", "Rechercher un mot"))
        self.fileIndexExpRB.setText(_translate("MainWindow", "Explorer un index d\'un fichier"))
        self.searchWordField.setPlaceholderText(_translate("MainWindow", "Tapez le mot à rechercher ..."))
        self.label_4.setText(_translate("MainWindow", "N° de document :"))
        self.searchDocWordButton.setText(_translate("MainWindow", "→"))
        self.tabs.setTabText(self.tabs.indexOf(self.rechercheTab), _translate("MainWindow", "Recherche indexée"))
        self.label_8.setText(_translate("MainWindow", "Recherche basée sur le modèle Booléen"))
        self.label_9.setText(_translate("MainWindow", "Introduisez votre requête sous un format booléen :"))
        self.booleansearchEdit.setPlaceholderText(_translate("MainWindow", "Requête au format booléen ..."))
        self.booleanSearchButton.setText(_translate("MainWindow", "Rechercher"))
        self.tabs.setTabText(self.tabs.indexOf(self.booleanModelTab), _translate("MainWindow", "Modèle Booléen"))
        self.label_10.setText(_translate("MainWindow", "Recherche basée sur le modèle Vectoriel"))
        self.label_11.setText(_translate("MainWindow", "Introduisez votre requête (liste de terms):"))
        self.vectorialSearchEdit.setPlaceholderText(_translate("MainWindow", "Votre requête ici ..."))
        self.vectorialSearchButton.setText(_translate("MainWindow", "Rechercher"))
        self.measurementGroupBox.setTitle(_translate("MainWindow", "Choisissez la mesure d\'appariment :"))
        self.innerProductRB.setText(_translate("MainWindow", "Inner Product"))
        self.diceRB.setText(_translate("MainWindow", "Coeif. De Dice"))
        self.cosinusRB.setText(_translate("MainWindow", "Mesure de Cosinus"))
        self.jacardRB.setText(_translate("MainWindow", "Mesure de Jacard"))
        self.tabs.setTabText(self.tabs.indexOf(self.vectorialModelTab), _translate("MainWindow", "Modèle Vectoriel"))
        self.vectorielEvalButton.setText(_translate("MainWindow", "Evaluer le modèle"))
        self.label_18.setText(_translate("MainWindow", "Evaluation du modèle vectoriel"))
        self.label_14.setText(_translate("MainWindow", "Choisissez le numéro de la requête :"))
        self.label_17.setText(_translate("MainWindow", "Précision :"))
        self.label_16.setText(_translate("MainWindow", "Rappel :"))
        self.label_15.setText(_translate("MainWindow", "Résultats :"))
        self.label_19.setText(_translate("MainWindow", "Requête :"))
        self.plotButton.setText(_translate("MainWindow", "Voir le graph"))
        self.measurementGroupBox_2.setTitle(_translate("MainWindow", "Choisissez la mesure d\'appariment :"))
        self.innerProductRB_2.setText(_translate("MainWindow", "Inner Product"))
        self.diceRB_2.setText(_translate("MainWindow", "Coeif. De Dice"))
        self.cosinusRB_2.setText(_translate("MainWindow", "Mesure de Cosinus"))
        self.jacardRB_2.setText(_translate("MainWindow", "Mesure de Jacard"))
        self.globalEvalCB.setToolTip(_translate("MainWindow", "Evaluer toutes les requêtes en graduant pour chacune le nombres de documents pertinants. ( Prend énormement de temps)"))
        self.globalEvalCB.setText(_translate("MainWindow", "Evaluation Globale du système"))
        self.label_5.setText(_translate("MainWindow", "Seuil"))
        self.tabs.setTabText(self.tabs.indexOf(self.evaluationTab), _translate("MainWindow", "Evaluation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
