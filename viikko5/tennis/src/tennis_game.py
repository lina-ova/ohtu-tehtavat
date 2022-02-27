from distutils.version import LooseVersion


class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self._score1 = 0
        self._score2 = 0
        self._score=''

    def get_score(self):
        self._check_situation()
        return self._score


    def won_point(self, player_name):
        if player_name == self.player1:
            self._score1 += 1
        else:
            self._score2 += 1
        
        

    def _check_situation(self):
        minus=self._score1-self._score2

        if minus==0:
            self._equal()

        elif self._score1 >= 4 or self._score2 >= 4:
            self._more_then_four(minus)
        
        else:
            self._unequal()


    def _equal(self):
        score={
            0:'Love-All',
            1:'Fifteen-All',
            2:"Thirty-All",
            3:"Forty-All",
            4:"Deuce"
        }
        self._score=score[self._score1]

    def _more_then_four(self, minus):
        score={
            1:"Advantage player1",
            -1:"Advantage player2",
            2:"Win for player1",
            -2:"Win for player2"
        }
        if minus>2:
            minus=2
        elif minus<-2:
            minus=-2
        self._score=score[minus]
    
    def _unequal(self):
        score={
                0:'Love',
                1:"Fifteen",
                2:"Thirty",
                3:"Forty"
            }
        self._score=score[self._score1]+'-'+score[self._score2]

