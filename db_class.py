
# coding: utf-8

# In[1]:


import pymysql


# In[2]:


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
    
    def Operation(self, statement):
        try:
           # Execute the SQL command
           self.cursor.execute(sql)
           # Commit your changes in the database
           self.Connection.commit()
        except:
           # Rollback in case there is any error
           self.Connection.rollback()

