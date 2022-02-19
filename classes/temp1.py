#class ClassName:
#  def __init__(self):
#    self.Attribute = 0
#  
#  def AnotherFunction(self):
#    Action(s)

class Team:
  def __init__(self, Name, Origin):
    self.TeamName = Name
    self.TeamOrigin = Origin
  
  def DefineTeamName(self, Name):
    self.TeamName = Name
 
  def DefineTeamOrigin(self, Origin):
    self.TeamOrigin = Origin    

Team1 = Team()

print(Team1.TeamName)

Team1.DefineTeamName("test")

print(Team1.TeamName)