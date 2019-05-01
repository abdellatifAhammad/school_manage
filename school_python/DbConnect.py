import sqlite3
from sqlite3 import *
import time
from time import gmtime, strftime
strftime("%Y-%m-%d %H:%M:%S", gmtime())


class StudentsData():
    def __init__(self):
        self._db=sqlite3.connect('{}'.format(strftime("%Y-%m-%d ", gmtime())))
        self._db.row_factory=sqlite3.Row
        self._db.execute("CREATE TABLE IF NOT EXISTS `{}` (`Number` INTEGER PRIMARY KEY  AUTOINCREMENT,`firstName`	TEXT,`LastName`	TEXT,`Section`	TEXT,`Class`	TEXT)".format(strftime("%Y-%m-%d H:00", gmtime())))
        self._db.commit()

    def Add(self,firstName,LastName,Section,Class):
        self._db.execute("insert into`{}` (`firstName`,`LastName`	, `Section`,`Class`) values(?,?,?,?)".format(strftime("%Y-%m-%d H:00", gmtime())),(firstName,LastName,Section,Class))
        self._db.commit()
        return 'Data Submitted!'


    def ListInfo(self):
        cursor = self._db.execute("Select * from `{}` ".format((strftime("%Y-%m-%d H:00", gmtime()))))
        return cursor;