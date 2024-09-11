from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]
  expected_score = 7
  # Act
  score = blackjack_score(hand)

  # Assert <-- Write assert statement here
  assert score == expected_score

#@pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  hand_1 = ["King", "Queen"]
  hand_2 = ["Jack", 9]
  assert blackjack_score(hand_1) == 20
  assert blackjack_score(hand_2) == 19

#@pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  hand_1 = ["Ace","King"]
  hand_2 = [4,"Ace"]
  hand_3 = [5,4,"Ace"]
  assert blackjack_score(hand_1) == 21
  assert blackjack_score(hand_2) == 15
  assert blackjack_score(hand_3) == 20

# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  hand_1 = ["Queen","King","Ace"]
  hand_2 = ["Ace",10,9]
  
  assert blackjack_score(hand_1) == 21
  assert blackjack_score(hand_2) == 20

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  hand_1 = []
  hand_2 = ["Queen"]
  hand_3 = [1,"Joker"]
  hand_4 = [1,2,3,4,5,6]

  assert blackjack_score(hand_1) == None
  assert blackjack_score(hand_2) == None
  assert blackjack_score(hand_3) == None
  assert blackjack_score(hand_4) == None

@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  pass

@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
  pass

@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
  pass

@pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
    pass