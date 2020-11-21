import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()

        coffee = self.cur.execute("""SELECT * FROM coffee""").fetchall()

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)

        self.tableWidget.setHorizontalHeaderLabels(("ID", "название сорта",
                                                    "степень обжарки",
                                                    "молотый/в зернах",
                                                    "описание вкуса",
                                                    "цена", "объем упаковки"))

        for i, elem in enumerate(coffee):
            self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)

            for j, item in enumerate(elem):
                if j == 2:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(
                        self.id_item("roast_degrees", "roast_degree", item)))

                elif j == 3:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(
                        self.id_item("ground_or_drilled", "mode", item)))

                else:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))

        self.tableWidget.resizeColumnsToContents()

    def id_item(self, table, item, id):
        q = f"""SELECT {item} FROM {table} WHERE ID={str(id)}"""
        return str(self.cur.execute(q).fetchone())[2:-3]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
