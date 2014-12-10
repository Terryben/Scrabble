class player():

  def __init__ (self, name):
    self.score = 0
    self.player_hand = []
    self.name = name

  def update_score(self, points_to_add):
    self.score += points_to_add

