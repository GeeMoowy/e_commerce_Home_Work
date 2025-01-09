import os
import unittest
from unittest.mock import patch, mock_open
from src.utils import read_json


class TestReadJson(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    def test_read_json(self, mock_file):
        result = read_json("products.json")
        self.assertEqual(result, {"key": "value"})
        mock_file.assert_called_once_with(os.path.abspath("products.json"), 'r', encoding='UTF-8')
