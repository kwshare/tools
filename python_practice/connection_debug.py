import mysql.connector


# debug for zihao Wang
# issue: no __init__ for class

class conn(object):
    cnx = None
    co = None

    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='test', port=3306)

    def select_user(self):
        self.co = self.cnx.cursor()
        self.co.execute('select * from table1')
        if self.co:
            print True
        else:
            print False

        self.cnx.close()


if __name__ == "__main__":
    test = conn()
    test.select_user()
