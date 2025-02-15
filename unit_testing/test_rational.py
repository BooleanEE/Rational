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

def test_if_rational_negative_is_correct():  # pylint: disable=C0116
    test_rational = Rational(7, 7)
    expected_rational = Rational(-7, 7)

    neg_result_rationl = -test_rational

    assert neg_result_rationl.num == expected_rational.num
    assert neg_result_rationl.den == expected_rational.den

def test_if_rational_leftshift_is_correct():  # pylint: disable=C0116
    test_rational = Rational(7, 2)
    left_shift_times = 2
    expected_rational = Rational(28, 2)

    leftshift_result_rationl = test_rational << left_shift_times

    assert leftshift_result_rationl.num == expected_rational.num
    assert leftshift_result_rationl.den == expected_rational.den

def test_if_rational_rightshift_is_correct():  # pylint: disable=C0116
    test_rational = Rational(7, 2)
    right_shift_times = 2
    expected_rational = Rational(7, 8)

    rightshift_result_rationl = test_rational >> right_shift_times

    assert rightshift_result_rationl.num == expected_rational.num
    assert rightshift_result_rationl.den == expected_rational.den

def test_if_rational_reduced_form_is_correct():
    first_rational = Rational(7, 3)
    second_rational = Rational(2, 4)
    expected_rational = Rational(17, 6)

    sum_result_rationl = first_rational + second_rational

    reduced_rational = sum_result_rationl.reduced_form_conversion()

    assert reduced_rational.num == expected_rational.num
    assert reduced_rational.den == expected_rational.den

def test_if_rational_is_less_than_other_rational():
    first_rational = Rational(1, 2)
    second_rational = Rational(2, 3)
    expected_bool = True

    is_first_less_than_second = first_rational < second_rational

    assert is_first_less_than_second == expected_bool

def test_if_rational_is_equal_than_other_rational():
    first_rational = Rational(1, 7)
    second_rational = Rational(2, 14)
    expected_bool = True

    is_first_equal_than_second = first_rational == second_rational

    assert is_first_equal_than_second == expected_bool

def test_if_rational_is_greater_than_other_rational():
    first_rational = Rational(1, 2)
    second_rational = Rational(1, 3)
    expected_bool = True

    is_first_greater_than_second = first_rational > second_rational

    assert is_first_greater_than_second == expected_bool

def test_if_rational_is_less_equal_than_other_rational():
    first_rational = Rational(1, 2)
    second_rational = Rational(2, 3)
    expected_bool = True

    is_first_greater_than_second = first_rational <= second_rational

    assert is_first_greater_than_second == expected_bool

def test_if_rational_is_greater_equal_than_other_rational():
    first_rational = Rational(7, 3)
    second_rational = Rational(7, 7)
    expected_bool = True

    is_first_greater_than_second = first_rational >= second_rational

    assert is_first_greater_than_second == expected_bool

def test_if_rational_is_not_equal_than_other_rational():
    first_rational = Rational(7, 3)
    second_rational = Rational(7, 7)
    expected_bool = True

    is_first_greater_than_second = first_rational != second_rational

    assert is_first_greater_than_second == expected_bool