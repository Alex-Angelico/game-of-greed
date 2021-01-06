import pytest
from tests.flo import diff
from game_of_greed.game import Game

#pytestmark = [pytest.mark.version_2, pytest.mark.version_3]

#@pytest.mark.skip("pending")
def test_quitter():
    game = Game()
    errors = diff(game.play, path="tests/assets/quitter.sim.txt")
    assert not errors, errors[0]

#@pytest.mark.skip("pending")
def test_one_and_done():
    game = Game()
    errors = diff(game.play, path="tests/assets/one_and_done.sim.txt")
    assert not errors, errors[0]

@pytest.mark.skip("pending")
def test_single_bank():
    game = Game()
    errors = diff(game.play, path="tests/assets/bank_one_roll_then_quit.sim.txt")
    assert not errors, errors[0]

@pytest.mark.skip("pending")
def test_bank_first_for_two_rounds():
    game = Game()
    errors = diff(game.play, path="tests/assets/bank_first_for_two_rounds.sim.txt")
    assert not errors, errors[0]