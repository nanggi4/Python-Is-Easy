class Team:
  def __init__(self, Name = "Name", Origin = "Origin"):
    self.TeamName = Name
    self.TeamOrigin = Origin
  
  def DefineTeamName(self, Name):
    self.TeamName = Name
 
  def DefineTeamOrigin(self, Origin):
    self.TeamOrigin = Origin   
    
#class InheritanceClassName(ParentClass):
#  def __init__(self, Input1, Input2):
#    ParentClass.__init__(self)
#    self.Attribite1 = Input1
#    self.Attribite2 = Input2
#    self.Attribite3 = 0
#  
#  def AnotherMethod(self):
#    Action(s)

class Player(Team):
  def __init__(self, PlayerName, PlayerPoints, TeamName, TeamOrigin):
    Team.__init__(self, TeamName, TeamOrigin)
    self.PlayerName = "None"
    self.PlayerPoints = 0
    
  def ScoredPoint(self):
    self.PlayerName += 1
  
  def setName(self, Name):
    self.PlayerName = Name
  
  def __str__(self):
    return "Player has scored: " + str(self.PlayerPoints) + " Player ..." 
    
Player1 = Player("Sid", 0, "Sharks", "Chicago")

print(Player1.PlayerName)
print(Player1.PlayerPoints)
print(Player1.TeamName)
print(Player1.TeamOrigin)