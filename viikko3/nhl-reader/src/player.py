class Player:
    def __init__(self, name, team, goals, assists, nation):
        self.name = name
        self.team=team
        self.goals=goals
        self.assists=assists
        self.nation=nation
    
    def __str__(self):
        return f'{self.name:25}{self.team:3} {str(self.goals):2} + {str(self.assists):2} = {self.goals+self.assists}'
        
