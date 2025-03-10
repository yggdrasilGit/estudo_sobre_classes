class DataTable:
   def __init__(self, name = ""):
      
      self._name = name
      self._columns = []
      self._data = []
   
   def get_data(self):
      return self._data



test = DataTable()
print(test.get_data())