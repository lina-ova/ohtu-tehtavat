import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_search_name_in_players(self):
        player=self.statistics.search('Semenko')
        self.assertEqual(str(player), 'Semenko EDM 4 + 12 = 16')
    
    def test_search_name_not_in_players(self):
        player=self.statistics.search('Semenka')
        self.assertEqual(player, None)

    def test_team_players_correct(self):
        players=self.statistics.team('PIT')
        player='Lemieux PIT 45 + 54 = 99'
        self.assertEqual(str(players[0]), player)
    
    def test_top_scorers_correct(self):
        players=self.statistics.top_scorers(1)
        player='Gretzky EDM 35 + 89 = 124'
        self.assertEqual(str(players[0]), player)