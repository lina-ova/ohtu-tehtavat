
class PlayerStats:
    def __init__(self, reader):
        self.players=reader.players

    def top_scorers_by_nationality(self, nationality):
        players=[]

        for p in self.players:
            if p.nation==nationality:
                players.append(p)
        
        players.sort(key=lambda player:(player.assists+player.goals), reverse=True)

        return players