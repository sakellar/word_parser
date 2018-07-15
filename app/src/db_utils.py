import mysql.connector

class DB:
    def connect(self):
        raise NotImplementedError
    def update(self, dictionary):
        raise NotImplementedError
    def close(self):
        raise NotImplementedError

class WordDB(DB):
  def __init__(self):
      self.table_exists = False
  def connect(self):
      pass
  def update(self, dictionary):
      pass
  def close(self):
      pass
