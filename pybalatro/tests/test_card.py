import pytest
from ..Card import Card


def test_valid_suit():
    suit = 'Brown'
    face = 'K'

    with pytest.raises(ValueError):
        Card(suit, face)
