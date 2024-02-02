import pytest


def param(*args):
    return pytest.param(*args, marks=pytest.mark.xfail)
