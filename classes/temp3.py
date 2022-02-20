class Pet:
  def __init__(self, _name, _age, _hunger, _playful):
    self.name = _name
    self.age = _age
    self.hunger = _hunger
    self.playful = _playful
    
  # getters
  def getName(self):
    return self.name
  
  def getAge(self):
    return self.age
  
  def getHunger(self):
    return self.hunger
  
  def getPlayful(self):
    return self.playful
  
  # setters
  def setName(self, _name):
    self.name = _name
  
  def setAge(self, _age):
    self.age = _age
    
  def setHunger(self, _hunger):
    self.hunger = _hunger
    
  def setPlayful(self, _playful):
    self.playful = _playful
    
class Dog(Pet):
  def __init__(self, _name, _age, _hunger, _playful, _breed, _favoriteToy):
    Pet.__init__(self, _name, _age, _hunger, _playful)
    self.breed = _breed
    self.favoriteToy = _favoriteToy
  
  def wantsToPlay(self):
    if self.playful == True:
      return ("Dog wants to play with " + self.favoriteToy)
    else
      return ("Dog doesn't want to play")