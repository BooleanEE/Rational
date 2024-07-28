import pytest
import sys

from rational import Rational

def test_rational_instantiation():
    first_rational = Rational(1, 2)
    second_rational = Rational(3, 5)
    expected_rational = Rational(3,10)

    mult_result_rational = first_rational * second_rational

    assert mult_result_rational.num == expected_rational.num
    assert mult_result_rational.den == expected_rational.den
    assert print(mult_result_rational) == print(expected_rational)
    