class DataTable:
   def __init__(self, name = "test"):
      
      self._name = name
      self._columns = []
      self._data = []
   
   @property
   def data(self):
      return self._data



test = DataTable()
print(test.data)