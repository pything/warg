#!/usr/bin/env python3
import sys

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 9/14/19
           """

from _pytest.capture import CaptureFixture


def test_print_info(capsys: CaptureFixture[str]) -> None:
    """Correct my_name argument prints"""
    text = "hello"
    err = "world"
    print(text)
    sys.stderr.write("world")
    captured = capsys.readouterr()
    assert text in captured.out
    assert err in captured.err


if __name__ == "__main__":
    test_print_info()
