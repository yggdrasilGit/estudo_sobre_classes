class DataTable:
   """Representa um Tabela de dados

      Essas classes representa uma tabela de dados do portal
      da transparencia. Deve ser capas de validar linhas inserindo
      de acordo com as colunas que possui. As linhas inseridas 
      ficam registradas dentro delas. 

      Atribultes:
         name: Nome da tabela
         columns: Lista de coluna da tabela.
         data: [Lista de dados]
   """
   def __init__(self, name = ""):
      """Construtor

         Args:
            name: Nome da tabela
      """     
      self._name = name
      self._columns = []
      self._data = []
   
   @property
   def data(self):
      return self._data
   
   @property
   def name(self):
      return self._name
   
   @property
   def columns(self):
      return self._columns


class Column:
   """Representa uma coluna em um DataTable

      Essa classe contém as informacoes de uma coluna
      e deve validar um dado de acordo com um tipo de 
      dado configurando o construtor.

      Attribultes:
         name : Nome da Coluna
         kind : Tipos de dados (varchar, bigith, numeric)
         description: Descricao da coluna
   """
   def __init__(self, name, kind, description):
      """Contructor:
         
         Args:
            name = Nome da coluna
            kind: Tipos de dados (varchar, bigint, numeric)
            description: Descricao da coluna 
      """
      self._name = name
      self._kind = kind
      self._description = description

   @property
   def name(self):
      return self._name
   
   @property
   def kind(self):
      return self._kind
   
   @property
   def description(self):
      return self._description
   
test = DataTable()
print(test.data)
