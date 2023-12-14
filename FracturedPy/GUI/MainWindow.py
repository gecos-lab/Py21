# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(909, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.VtkLayout = QtWidgets.QVBoxLayout()
        self.VtkLayout.setObjectName("VtkLayout")
        self.verticalLayout_3.addLayout(self.VtkLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 909, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPlot = QtWidgets.QMenu(self.menubar)
        self.menuPlot.setObjectName("menuPlot")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.OptionsDockWidget = QtWidgets.QDockWidget(MainWindow)
        self.OptionsDockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.OptionsDockWidget.setObjectName("OptionsDockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OptionTabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OptionTabWidget.sizePolicy().hasHeightForWidth())
        self.OptionTabWidget.setSizePolicy(sizePolicy)
        self.OptionTabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.OptionTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.OptionTabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.OptionTabWidget.setDocumentMode(False)
        self.OptionTabWidget.setTabsClosable(False)
        self.OptionTabWidget.setMovable(True)
        self.OptionTabWidget.setTabBarAutoHide(False)
        self.OptionTabWidget.setObjectName("OptionTabWidget")
        self.BoundTab = QtWidgets.QWidget()
        self.BoundTab.setObjectName("BoundTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.BoundTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AddBoundaryButton = QtWidgets.QPushButton(self.BoundTab)
        self.AddBoundaryButton.setObjectName("AddBoundaryButton")
        self.verticalLayout.addWidget(self.AddBoundaryButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.OptionTabWidget.addTab(self.BoundTab, "")
        self.FracTab = QtWidgets.QWidget()
        self.FracTab.setObjectName("FracTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.FracTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.AddFractureButton = QtWidgets.QPushButton(self.FracTab)
        self.AddFractureButton.setObjectName("AddFractureButton")
        self.verticalLayout_2.addWidget(self.AddFractureButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.OptionTabWidget.addTab(self.FracTab, "")
        self.OtherTab = QtWidgets.QWidget()
        self.OtherTab.setObjectName("OtherTab")
        self.OptionTabWidget.addTab(self.OtherTab, "")
        self.horizontalLayout.addWidget(self.OptionTabWidget)
        self.OptionsDockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.OptionsDockWidget)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPlot.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.OptionTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPlot.setTitle(_translate("MainWindow", "Plotter"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.AddBoundaryButton.setText(_translate("MainWindow", "+ Add boundary"))
        self.OptionTabWidget.setTabText(self.OptionTabWidget.indexOf(self.BoundTab), _translate("MainWindow", "Domain Options"))
        self.AddFractureButton.setText(_translate("MainWindow", "+ Add fractures"))
        self.OptionTabWidget.setTabText(self.OptionTabWidget.indexOf(self.FracTab), _translate("MainWindow", "Fracture Options"))
        self.OptionTabWidget.setTabText(self.OptionTabWidget.indexOf(self.OtherTab), _translate("MainWindow", "Other Options"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
