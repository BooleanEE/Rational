""" Module to provide a way to unit test the ADT rational. """

import pytest

from rational import Rational


def test_exception_when_zero_denominator():  # pylint: disable=C0116
    with pytest.raises(ValueError, match="The number 0 can't be a denominator."):
        Rational(1, 0)


def test_if_rational_multiplication_is_correct():  # pylint: disable=C0116
    first_rational = Rational(1, 2)
    second_rational = Rational(3, 5)
    expected_rational = Rational(3, 10)

    mult_result_rational = first_rational * second_rational

    assert mult_result_rational.num == expected_rational.num
    assert mult_result_rational.den == expected_rational.den


def test_if_rational_division_is_correct():  # pylint: disable=C0116
    first_rational = Rational(7, 11)
    second_rational = Rational(7, 22)
    expected_rational = Rational(154, 77)

    div_result_rational = first_rational / second_rational

    assert div_result_rational.num == expected_rational.num
    assert div_result_rational.den == expected_rational.den


def test_if_rational_summation_is_correct():  # pylint: disable=C0116
    first_rational = Rational(3, 7)
    second_rational = Rational(3, 5)
    expected_rational = Rational(36, 35)

    sum_result_rationl = first_rational + second_rational

    assert sum_result_rationl.num == expected_rational.num
    assert sum_result_rationl.den == expected_rational.den


def test_if_rational_subtraction_is_correct():  # pylint: disable=C0116
    first_rational = Rational(3, 7)
    second_rational = Rational(3, 5)
    expected_rational = Rational(-6, 35)

    sub_result_rationl = first_rational - second_rational

    assert sub_result_rationl.num == expected_rational.num
    assert sub_result_rationl.den == expected_rational.den
