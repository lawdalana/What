import pymysql

class db:
    
  def __init__(self, hostname, port, username, password, databasename):
    self.Connection = pymysql.connect(host=hostname, port=port, user=username, password=password, 
         db=databasename ,charset='utf8mb4' ,cursorclass=pymysql.cursors.DictCursor )
    self.cursor = self.Connection.cursor()  

  def __del__(self):
    self.cursor.close()
    self.Connection.close()

  def find(self, statement):
    self.cursor.execute(statement)
    buf = list()
    for row in self.cursor.fetchall():
        buf.append(row)
    return buf

  def CURD(self, statement):
    try:
       # Execute the SQL command
      self.cursor.execute(statement)
       # Commit your changes in the database
      self.Connection.commit()
    except:
      print("Error" + statement)
       # Rollback in case there is any error
      self.Connection.rollback() 

  def CURD_SP(self, statement, title):
    try:
       # Execute the SQL command
      self.cursor.execute(statement,(title))
       # Commit your changes in the database
      self.Connection.commit()
    except pymysql.MySQLError as e:
      print("Error: " , e)  
       # Rollback in case there is any error
      self.Connection.rollback() 