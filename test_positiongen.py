import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock
from positiongen import generate_positions

class TestGeneratePositions(unittest.TestCase):
    
    def test_generate_positions(self):
        # Test Case 1: Check if function returns tuple with expected data types
        positions = ['P', 'C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF']
        players = ['John', 'Mike', 'David', 'Tom', 'Jerry', 'Alice', 'Bob']
        innings = 2
        norandomize = False
        keeporder = False
        result = generate_positions(positions, players, innings, norandomize, keeporder)
        
        # Check if return value is a tuple
        self.assertIsInstance(result, tuple)
        
        # Check if tuple contains two elements
        self.assertEqual(len(result), 2)
        
        # Check if the first element of the tuple is a list
        self.assertIsInstance(result[0], list)
        
        # Check if the second element of the tuple is a dictionary
        self.assertIsInstance(result[1], dict)
        
        # Test Case 2: Check if positions and players have been deduped and empty elements removed
        positions = ['P', 'C', '1B', '', '3B', 'SS', 'LF', 'CF', 'RF', 'LF', 'RF']
        players = ['John', '', 'David', 'Tom', 'Jerry', 'Alice', 'Bob', '', '', 'John']
        innings = 2
        norandomize = False
        keeporder = False
        result = generate_positions(positions, players, innings, norandomize, keeporder)
        (batting_order, position_map) = result
        
        # Check if empty elements have been removed from positions and players
        self.assertEqual(len(position_map.keys()), 8)
        self.assertEqual(len(batting_order), 6)
        
        # Check if duplicate elements have been removed from positions and players
        self.assertEqual(len(set(position_map.keys())), 8)
        self.assertEqual(len(set(batting_order)), 6)
        
        # Test Case 3: Check if positions are fixed in the first inning when norandomize option is set
        positions = ['P', 'C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF']
        players = ['John', 'Mike', 'David', 'Tom', 'Jerry', 'Alice', 'Bob']
        innings = 2
        norandomize = True
        keeporder = False
        result = generate_positions(positions, players, innings, norandomize, keeporder)
        
        # Check if positions are fixed in the first inning
        self.assertEqual(result[1]['P'][0], 'John')
        self.assertEqual(result[1]['C'][0], 'Mike')
        self.assertEqual(result[1]['1B'][0], 'David')
        self.assertEqual(result[1]['2B'][0], 'Tom')
        self.assertEqual(result[1]['3B'][0], 'Jerry')
        self.assertEqual(result[1]['SS'][0], 'Alice')
        self.assertEqual(result[1]['LF'][0], 'Bob')
