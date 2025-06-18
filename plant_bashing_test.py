import pytest
from unittest.mock import patch
import plant_bashing

@patch('builtins.input', return_value='Alice')
@patch('builtins.print')
def test_greet_player(mock_print, mock_input):
    plant_bashing.greet_player()
    mock_print.assert_any_call("Welcome to the game!")
    mock_print.assert_any_call("Hello Alice!")

def test_if_answer_valid():
    assert plant_bashing.if_answer_valid("yes") == True
    assert plant_bashing.if_answer_valid("No") == True
    assert plant_bashing.if_answer_valid("Y") == True
    assert plant_bashing.if_answer_valid("n") == True
    assert plant_bashing.if_answer_valid("maybe") == False
    assert plant_bashing.if_answer_valid("") == False

@patch('builtins.input', side_effect=['maybe', 'yes'])
def test_is_yes_or_no_yes(mock_input):
    # This simulates user first typing 'maybe' (invalid),
    # then 'yes' (valid), so the function should eventually return True.
    result = plant_bashing.is_yes_or_no("Please confirm")
    assert result is True

@patch('builtins.input', side_effect=['nope', 'no'])
def test_is_yes_or_no_no(mock_input):
    # Simulates invalid 'nope' then valid 'no', should return False.
    result = plant_bashing.is_yes_or_no("Please confirm")
    assert result is False

@patch('builtins.print')
def test_farewell_player(mock_print):
    plant_bashing.farewell_player()
    mock_print.assert_any_call("Thank you for playing!")
    mock_print.assert_any_call("See you Alice!")
