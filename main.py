# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
import splitBackend
from PIL import Image, ImageQt
import requests
from io import BytesIO

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

smallPosterUrl = "https://image.tmdb.org/t/p/w95"
bigPosterUrl = "https://image.tmdb.org/t/p/w145"

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Movie Roulette"
        description = "Movie Roulette - Let's pick you out a movie!"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))


        self.LoadingMovie = QMovie(u":/images/images/images/SpinWheel.gif")
        widgets.LoadingLabel.setMovie(self.LoadingMovie)

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        widgets.btn_spin.clicked.connect(self.buttonClick)
        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.btn_SearchMovie.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        #widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            #UIFunctions.resetStyle(self, btnName)
            #btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            #UIFunctions.resetStyle(self, btnName)
            #btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            #UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            #btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            widgets.stackedWidget.setCurrentWidget(widgets.SearchMoviePage)
            #UIFunctions.resetStyle(self, btnName)
            #btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            
        if btnName == "btn_spin":
            widgets.stackedWidget.setCurrentWidget(widgets.LoadingScreen)
            self.LoadingMovie.start()
            #UIFunctions.resetStyle(self, btnName)
            #$btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            print("Spin button clicked")
        
        if btnName == "btn_SearchMovie":
            print("pressed search")
            
            ##hiding the movie widgets at the start, so multiple searches won't keep old search results
            widgets.SearchMovieWidget.setHidden(True)
            widgets.SearchMovieWidget_2.setHidden(True)
            widgets.SearchMovieWidget_3.setHidden(True)
            widgets.SearchMovieWidget_4.setHidden(True)
            widgets.SearchMovieWidget_5.setHidden(True)
            widgets.SearchMovieWidget_6.setHidden(True)
            widgets.SearchMovieWidget_7.setHidden(True)
            widgets.SearchMovieWidget_8.setHidden(True)
            widgets.SearchMovieWidget_9.setHidden(True)
            widgets.SearchMovieWidget_10.setHidden(True)
            widgets.SearchMovieWidget_11.setHidden(True)
            widgets.SearchMovieWidget_12.setHidden(True)
            widgets.SearchMovieWidget_13.setHidden(True)
            widgets.SearchMovieWidget_14.setHidden(True)
            widgets.SearchMovieWidget_15.setHidden(True)
            
            #Makes a list to show results
            search = str(widgets.searchBar.text())
            self.searchList = splitBackend.Backend.searchMovies(search)
            
            
            widgets.scrollArea_2.setVisible(True)
            #For loop to show results based on how many results come through - max is 15
            for i in range(len(self.searchList)):
                if(i == 0):
                    widgets.SearchMovieWidget.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    if(self.searchList[i].getPoster()):
                        response = requests.get(smallPosterUrl + self.searchList[i].getPoster())
                        posterImg = Image.open(BytesIO(response.content))
                        widgets.posterLabel.setPixmap(ImageQt(posterImg))
                    widgets.Details.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))
                if(i == 1):
                    widgets.SearchMovieWidget_2.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title_2.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title_2.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    widgets.Details_2.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))
                if(i == 2):
                    widgets.SearchMovieWidget_3.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title_3.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title_3.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    widgets.Details_3.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))
                if(i == 3):
                    widgets.SearchMovieWidget_4.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title_4.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title_4.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    widgets.Details_4.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))
                if(i == 4):
                    widgets.SearchMovieWidget_5.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title_5.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title_5.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    widgets.Details_5.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))
                if(i == 5):
                    widgets.SearchMovieWidget_6.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title_6.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title_6.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    widgets.Details_6.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))
                if(i == 6):
                    widgets.SearchMovieWidget_7.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title_7.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title_7.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    widgets.Details_7.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))
                if(i == 7):
                    widgets.SearchMovieWidget_8.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title_8.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title_8.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    widgets.Details_8.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))
                if(i == 8):
                    widgets.SearchMovieWidget_9.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title_9.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title_9.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    widgets.Details_9.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))
                if(i == 9):
                    widgets.SearchMovieWidget_10.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title_10.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title_10.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    widgets.Details_10.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))
                if(i == 10):
                    widgets.SearchMovieWidget_11.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title_11.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title_11.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    widgets.Details_11.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))
                if(i == 11):
                    widgets.SearchMovieWidget_12.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title_12.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title_12.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    widgets.Details_12.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))

                if(i == 12):
                    widgets.SearchMovieWidget_13.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title_13.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title_13.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    widgets.Details_13.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))
                if(i == 13):
                    widgets.SearchMovieWidget_14.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title_14.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title_14.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    widgets.Details_14.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))
                if(i == 14):
                    widgets.SearchMovieWidget_15.setHidden(False)
                    if(self.searchList[i].getDate()):
                        widgets.Title_15.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle() + " (" + str(self.searchList[i].getDate()) + ")", None))
                    else:
                        widgets.Title_15.setText(QCoreApplication.translate("MainWindow", "" + self.searchList[i].getTitle(), None))
                    widgets.Details_15.setText(QCoreApplication.translate("MainWindow", self.searchList[i].getDescription(), None))
            

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
