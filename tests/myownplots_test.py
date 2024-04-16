import pytest

from myownplots.exceptions import WrongArgsError,DifferentLengthArgsError
from myownplots.myownplots import create_plot,create_random_plot

def test_wrong_arg1():
     with pytest.raises(WrongArgsError):
         create_plot("lol")
def test_wrong_arg2():
     with pytest.raises(WrongArgsError):
         create_plot(["lol","kek"])
def test_different_length():
     with pytest.raises(DifferentLengthArgsError):
         create_plot([1,2],[2,3,4])
