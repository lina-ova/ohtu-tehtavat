class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr
    def matches(self, player):
        player_value=getattr(player, self._attr)

        return player_value < self._value

class Not:
    def __init__(self, ehto):
        self._ehto= ehto

    def matches(self, player):
        if not self._ehto.matches(player):
            return player
        

class All:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        return player

class Or: 
    def __init__(self, *matchers):
        self._matchers= matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        
        return False

class QueryBuilder:
    def __init__(self, matchers = All()):
        self._matchers = matchers

    def build(self):
        return self._matchers

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matchers, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matchers, HasFewerThan(value, attr)))
    
    def oneOf(self, *m):
        return QueryBuilder(Or(*m))


    


