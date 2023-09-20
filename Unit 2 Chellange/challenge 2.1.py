#Define the base class player 
class player:
  def player (self):
    print("The player is playing cricket.")
#Define the derived classBatsman
class Batsman(player):
  def play(self):
    print("Thebatsman is batting.")
#Define the derived class Bowler
class Bowler(player):
  def play(self):
   print("The bowleris bowling.")
#create object of Btsman andBowling classes
batsman=Batsman()
bowler=Bowler()
#call the play() method for each object
batsman.play()
bowler.play()
