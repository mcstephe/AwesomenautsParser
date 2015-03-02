__author__ = 'mcstephe'

class Player:
    'This is a class object that represents each player in the replays list.'

    was_friendly = 0  # Number of occurences this player was on the same team as base player
    was_enemy = 0  # Number of occurences this player played opposite team as base player
    total_played = 0
    wins = 0
    loses = 0
    #winLossRatio = 0.0

    def __init__(self, name):
        self.name = name

    def set_team(self, team):
        if (team == True):  # On same team as base player
            self.was_friendly += 1
        else:
            self.was_enemy += 1

    def get_total(self):
        tot = self.was_friendly + self.was_enemy
        return tot

    def match_outcome(self, team, won):
        self.total_played += 1

        if (team == True):  # On same team as base player
            self.was_friendly += 1
        else:
            self.was_enemy += 1

        if (won == True):  # This player won a game
            self.wins += 1
        else:
            self.loses += 1

    def ratio(self):  # Calculates win lose ratio for this player.
        rat = 0.0
        if (self.loses != 0 ):
            rat = self.wins / self.loses
        else:
            rat = self.wins

        return rat

#p1 = Player("Player1")
#p1.match_outcome(True, True)
#p1.match_outcome(False, False)
#print(p1.was_friendly, p1.ratio())
