import unittest
import sys
import os
import json

from checker import find_matches
from database_loader import load_database

class TestChecker(unittest.TestCase):

    def setUp(self):
        test_db_path = os.path.join(os.path.dirname(__file__),  'data', 'test_database.json')
        self.db = load_database(test_db_path)

    def test_multiple_matches_same_id(self):
        result = find_matches(self.db, "commonID")
        expected = [
            ("TournamentAlpha", "Round1", "SlotC"),
            ("TournamentBeta", "Round1", "SlotY"),
            ("TournamentGamma", "QuarterFinals", "Slot2"),
        ]
        self.assertEqual(sorted(result), sorted(expected))

    def test_single_match(self):
        result = find_matches(self.db, "gamma002")
        expected = [("TournamentGamma", "SemiFinals", "Slot1")]
        self.assertEqual(result, expected)

    def test_multiple_matches_across_rounds(self):
        result = find_matches(self.db, "alpha001")
        expected = [
            ("TournamentAlpha", "Round1", "SlotA"),
            ("TournamentAlpha", "Round2", "SlotB"),
        ]
        self.assertEqual(sorted(result), sorted(expected))

    def test_multiple_matches_across_tournaments(self):
        result = find_matches(self.db, "alpha002")
        expected = [
            ("TournamentAlpha", "Round1", "SlotB"),
            ("TournamentBeta", "Round2", "SlotY"),
        ]
        self.assertEqual(sorted(result), sorted(expected))

    def test_no_matches(self):
        result = find_matches(self.db, "nonexistentID")
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
