import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Email check")
        self.setGeometry(700, 300, 500, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setColumnWidth(0, 60) 
        self.table_widget.setColumnWidth(1, 400) 
        self.table_widget.setHorizontalHeaderLabels(["arrived", "Email Subject"])
        layout.addWidget(self.table_widget)
        self.add_button = QPushButton("Add New Subject")
        layout.addWidget(self.add_button)

        self.add_button.clicked.connect(self.add_task)
        self.add_default_rows()

    def add_task(self):
        row_count = self.table_widget.rowCount()
        self.table_widget.setRowCount(row_count + 1)

        done_checkbox = QTableWidgetItem()
        done_checkbox.setCheckState(Qt.Unchecked)
        task_name_item = QTableWidgetItem()

        self.table_widget.setItem(row_count, 0, done_checkbox)
        self.table_widget.setItem(row_count, 1, task_name_item)
       
        self.table_widget.setColumnWidth(0, 60) 
        self.table_widget.setColumnWidth(1, 400)   

    def add_default_rows(self):
            tasks = ["NGD_BDS_ITEM_VS_SRC_DBS_ITEM_COUNT", 
                     "NGD_tb_charge TXN COUNT VS RA_tb_charge TXN COUNT",
                        "TOTAL MAP COUNT NGD_SYSTEM VS RA_SOURCEDB",
                        "NGD_PRG TXN COUNT VS RA_RPG TXN COUNT",
                        "IAS TXN COUNT VS DATAMART TXN COUNT ",
                        "RMS TXN COUNT VS DATAMART TXN COUNT"]

            self.table_widget.setRowCount(len(tasks))

            for row_count, task_name in enumerate(tasks):
                task_name_item = QTableWidgetItem(task_name)
                done_checkbox = QTableWidgetItem()
                done_checkbox.setCheckState(Qt.Unchecked)

                self.table_widget.setItem(row_count, 1, task_name_item)
                self.table_widget.setItem(row_count, 0, done_checkbox)
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
