import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.db")
        self.pushButton.clicked.connect(self.pain)
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pedit.clicked.connect(self.edit)
        self.padd.clicked.connect(self.add)

    def pain(self):
        title1 = self.connection.cursor().execute(f"""SELECT id FROM Shows
                WHERE title = '{self.sender().text()}'""").fetchall()
        title2 = self.connection.cursor().execute(f"""SELECT title FROM Shows
                        WHERE title = '{self.sender().text()}'""").fetchall()
        state = self.connection.cursor().execute(f"""SELECT [степень обжарки] FROM Shows
                        WHERE title = '{self.sender().text()}'""").fetchall()
        seria = self.connection.cursor().execute(f"""SELECT [молотый/в зернах] FROM Shows
                        WHERE title = '{self.sender().text()}'""").fetchall()
        nomer = self.connection.cursor().execute(f"""SELECT [описание вкуса] FROM Shows
                        WHERE title = '{self.sender().text()}'""").fetchall()
        massa = self.connection.cursor().execute(f"""SELECT цена FROM Shows
                        WHERE title = '{self.sender().text()}'""").fetchall()
        level = self.connection.cursor().execute(f"""SELECT [объем упаковки] FROM Shows
                        WHERE title = '{self.sender().text()}'""").fetchall()
        self.label_8.setText(*title1[0])
        self.label_9.setText(*title2[0])
        self.label_10.setText(*state[0])
        self.label_11.setText(*seria[0])
        self.label_12.setText(str(*nomer[0]))
        self.label_13.setText(str(*massa[0]))
        self.label_14.setText(*level[0])

    def edit(self):
        id = self.lineEdit.text()
        tit = self.lineEdit_2.text()
        obz = self.lineEdit_3.text()
        zer = self.lineEdit_4.text()
        des = self.lineEdit_5.text()
        pr = self.lineEdit_6.text()
        vol = self.lineEdit_7.text()
        if obz:
            self.connection.cursor().execute(f"""UPDATE Shows
                    SET [степень обжарки] = '{obz}'
                WHERE id = '{id}'""")
            self.connection.commit()
        if zer:
            self.connection.cursor().execute(f"""UPDATE Shows
                                SET [молотый/в зернах] = '{zer}'
                            WHERE id = '{id}'""")
            self.connection.commit()
        if des:
            self.connection.cursor().execute(f"""UPDATE Shows
                                            SET [описание вкуса] = '{des}'
                                        WHERE id = '{id}'""")
            self.connection.commit()
        if pr:
            self.connection.cursor().execute(f"""UPDATE Shows
                                                        SET цена = '{pr}'
                                                    WHERE id = '{id}'""")
            self.connection.commit()
        if vol:
            self.connection.cursor().execute(f"""UPDATE Shows
                                                                    SET [объем упаковки] = '{vol}'
                                                                WHERE id = '{id}'""")
            self.connection.commit()

    def add(self):
        id = self.lineEdit.text()
        tit = self.lineEdit_2.text()
        obz = self.lineEdit_3.text()
        zer = self.lineEdit_4.text()
        des = self.lineEdit_5.text()
        pr = self.lineEdit_6.text()
        vol = self.lineEdit_7.text()
        par = (id, tit, obz, zer, des, pr, vol)
        self.connection.cursor().executemany(f"INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?)", par)
        self.connection.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
