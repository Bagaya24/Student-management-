################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

## ==> GUI FILE
from main import *
import platform

class UIFunctions(QtWidgets.QMainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.menu_ajouter.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 128:

                widthExtended = maxExtend

            else:

                widthExtended = standard



            # ANIMATION
            self.animation = QPropertyAnimation(self.menu_ajouter, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
