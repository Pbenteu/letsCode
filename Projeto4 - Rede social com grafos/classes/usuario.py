class Usuario(object): 

  def __init__(self, name, userName):
    self.name = name
    self.userName = userName
    
  def __repr__(self) -> str:
      return f'Object: {self.userName}'