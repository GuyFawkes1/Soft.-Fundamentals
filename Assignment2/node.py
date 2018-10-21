class node():
    def __init__(self, team1, team2, next_node=None):
        self.team1 = team1
        self.team2 = team2
        self.next_node = next

    def __return__(self):
        return ('{} {}'.format(self.team1, self.team2))

    def set_next(self, new_next):
        self.next_node = new_next

    def get_data(self):
        return ('{} {} {}'.format(self.team1, self.team2, self.colour))

    def compare(self, key):
        if self.team1 == key.team1 and self.team2 == key.team2:
            return 1
        return 0
