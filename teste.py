# from PySide2.QtWidgets import QApplication, QWidget, QStackedWidget, QComboBox, QVBoxLayout
#
# class StackedWidgetDemo(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         # Créer trois widgets à empiler
#         widget1 = QWidget()
#         widget1.setStyleSheet("background-color: red")
#         widget2 = QWidget()
#         widget2.setStyleSheet("background-color: green")
#         widget3 = QWidget()
#         widget3.setStyleSheet("background-color: blue")
#
#         # Créer un QStackedWidget et ajouter les widgets
#         self.stacked_widget = QStackedWidget()
#         self.stacked_widget.addWidget(widget1)
#         self.stacked_widget.addWidget(widget2)
#         self.stacked_widget.addWidget(widget3)
#
#         # Créer un QComboBox et ajouter les titres des widgets
#         self.combo_box = QComboBox()
#         self.combo_box.addItem("Widget 1")
#         self.combo_box.addItem("Widget 2")
#         self.combo_box.addItem("Widget 3")
#
#         # Connecter le signal du QComboBox au slot du QStackedWidget
#         self.combo_box.activated.connect(self.stacked_widget.setCurrentIndex)
#
#         # Créer un layout vertical et ajouter le QComboBox et le QStackedWidget
#         layout = QVBoxLayout()
#         layout.addWidget(self.combo_box)
#         layout.addWidget(self.stacked_widget)
#         self.setLayout(layout)
#
# if __name__ == "__main__":
#     app = QApplication([])
#     demo = StackedWidgetDemo()
#     demo.show()
#     app.exec_()
import sys

from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QTableWidget,
    QTableWidgetItem, QDockWidget, QFormLayout,
    QLineEdit, QWidget, QPushButton, QSpinBox,
    QMessageBox, QToolBar, QMessageBox, QAction
)
# from PySide2.QtCore import Qt, QSize
# from PySide2.QtGui import QIcon
#
#
# class MainWindow(QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.setWindowTitle('Employees')
#
#         self.setGeometry(100, 100, 600, 400)
#
#         employees = [
#             {'First Name': 'John', 'Last Name': 'Doe', 'Age': 25},
#             {'First Name': 'Jane', 'Last Name': 'Doe', 'Age': 22},
#             {'First Name': 'Alice', 'Last Name': 'Doe', 'Age': 22},
#         ]
#
#         self.table = QTableWidget(self)
#         self.setCentralWidget(self.table)
#
#         self.table.setColumnCount(3)
#         self.table.setColumnWidth(0, 150)
#         self.table.setColumnWidth(1, 150)
#         self.table.setColumnWidth(2, 50)
#
#         self.table.setHorizontalHeaderLabels(employees[0].keys())
#         self.table.setRowCount(len(employees))
#
#         row = 0
#         for e in employees:
#             self.table.setItem(row, 0, QTableWidgetItem(e['First Name']))
#             self.table.setItem(row, 1, QTableWidgetItem(e['Last Name']))
#             self.table.setItem(row, 2, QTableWidgetItem(str(e['Age'])))
#             row += 1
#
#         dock = QDockWidget('New Employee')
#         dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
#         self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)
#
#         # create form
#         form = QWidget()
#         layout = QFormLayout(form)
#         form.setLayout(layout)
#
#         self.first_name = QLineEdit(form)
#         self.last_name = QLineEdit(form)
#         self.age = QSpinBox(form, minimum=18, maximum=67)
#         self.age.clear()
#
#         layout.addRow('First Name:', self.first_name)
#         layout.addRow('Last Name:', self.last_name)
#         layout.addRow('Age:', self.age)
#
#         btn_add = QPushButton('Add')
#         btn_add.clicked.connect(self.add_employee)
#         layout.addRow(btn_add)
#
#         # add delete & edit button
#         toolbar = QToolBar('main toolbar')
#         toolbar.setIconSize(QSize(16, 16))
#         self.addToolBar(toolbar)
#
#         delete_action = QAction(QIcon('./assets/remove.png'), '&Delete', self)
#         delete_action.triggered.connect(self.delete)
#         toolbar.addAction(delete_action)
#         dock.setWidget(form)
#
#     def delete(self):
#         current_row = self.table.currentRow()
#         if current_row < 0:
#             return QMessageBox.warning(self, 'Warning', 'Please select a record to delete')
#
#         button = QMessageBox.question(
#             self,
#             'Confirmation',
#             'Are you sure that you want to delete the selected row?',
#             QMessageBox.StandardButton.Yes |
#             QMessageBox.StandardButton.No
#         )
#         if button == QMessageBox.StandardButton.Yes:
#             self.table.removeRow(current_row)
#
#     def valid(self):
#         first_name = self.first_name.text().strip()
#         last_name = self.last_name.text().strip()
#
#         if not first_name:
#             QMessageBox.critical(self, 'Error', 'Please enter the first name')
#             self.first_name.setFocus()
#             return False
#
#         if not last_name:
#             QMessageBox.critical(self, 'Error', 'Please enter the last name')
#             self.last_name.setFocus()
#             return False
#
#         try:
#             age = int(self.age.text().strip())
#         except ValueError:
#             QMessageBox.critical(self, 'Error', 'Please enter a valid age')
#             self.age.setFocus()
#             return False
#
#         if age <= 0 or age >= 67:
#             QMessageBox.critical(
#                 self, 'Error', 'The valid age is between 1 and 67')
#             return False
#
#         return True
#
#     def reset(self):
#         self.first_name.clear()
#         self.last_name.clear()
#         self.age.clear()
#
#     def add_employee(self):
#         if not self.valid():
#             return
#
#         row = self.table.rowCount()
#         self.table.insertRow(row)
#         self.table.setItem(row, 0, QTableWidgetItem(
#             self.first_name.text().strip())
#                            )
#         self.table.setItem(
#             row, 1, QTableWidgetItem(self.last_name.text())
#         )
#         self.table.setItem(
#             row, 2, QTableWidgetItem(self.age.text())
#         )
#
#         self.reset()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QFrame

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Créer un widget central pour la fenêtre
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Créer un layout vertical pour le widget central
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Ajouter l'image en arrière-plan
        background_label = QLabel(self)
        background_pixmap = QPixmap("image/bg.jpeg")
        background_label.setPixmap(background_pixmap)
        layout.addWidget(background_label)

        # Ajouter un frame avec un bouton par-dessus l'image
        frame = QFrame(self)
        layout.addWidget(frame)

        button = QPushButton("Cliquez ici", self)
        frame_layout = QVBoxLayout()
        frame.setLayout(frame_layout)
        frame_layout.addWidget(button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
