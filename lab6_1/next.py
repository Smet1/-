# -*- coding:utf8 -*-
import MySQLdb


class Connection:
    def __init__(self, user, password, db, host='localhost', charset='utf8'):
        #  параметры соединения
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None
        self.use_unicode = True
        self.charset = charset

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        # открытие соед.
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                charset=self.charset
            )

    def disconnect(self):
        # закрытие соед.
        if self._connection:
            self._connection.close()


class Bank:
    def __init__(self, db_connection, name, address):
        # соед. и данные о банке
        self.db_connection = db_connection.connection
        self.name = name
        self.address = address

    def save(self):
        # запись данных из объекта в БД
        c = self.db_connection.cursor()
        c.execute("INSERT INTO banks (name, address) VALUES (%s, %s);", (self.name,
                                                                         self.address))
        self.db_connection.commit()
        c.close()


if __name__ == '__main__':
    # sfd
    con = Connection("dbuser", "123", "first_db")

    with con:
        bank = Bank(con, "вапв1", "fdg3")
        bank.save()
