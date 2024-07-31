""" Module to provide a way to make operations using rational values. """

from __future__ import annotations


class Rational:
    """ADT class to behaviour as a rational number."""

    def __init__(self, numerator: int, denominator: int):
        self.num = numerator
        if denominator == 0:
            raise ValueError("The number 0 can't be a denominator.")
        self.den = denominator

    def __mul__(self, other_rational: Rational) -> Rational:
        num = self.num * other_rational.num
        den = self.den * other_rational.den
        return Rational(num, den)

    def __truediv__(self, other_rational: Rational) -> Rational:
        num = self.num * other_rational.den
        den = self.den * other_rational.num
        return Rational(num, den)

    def __add__(self, other_rational: Rational) -> Rational:
        if self.den == other_rational.den:
            num = self.num + other_rational.num
            den = self.den
        else:
            num = self.num * other_rational.den + other_rational.num * self.den
            den = self.den * other_rational.den
        return Rational(num, den)

    def __sub__(self, other_rational: Rational) -> Rational:
        if self.den == other_rational.den:
            num = self.num - other_rational.num
            den = self.den
        else:
            num = self.num * other_rational.den - other_rational.num * self.den
            den = self.den * other_rational.den
        return Rational(num, den)

    def __neg__(self) -> Rational:
        return Rational(-self.num, self.den)

    def __lshift__(self, left_shift_operations: int) -> Rational:
        num = self.num << left_shift_operations
        return Rational(num, self.den)

    def __rshift__(self, right_shift_operations: int) -> Rational:
        den = self.den << right_shift_operations
        return Rational(self.num, den)

    def __lt__(self, other_rational: Rational) -> bool:
        result = Rational(self.num, self.den) - other_rational
        if result.num < -0.00000000:
            return True
        return False

    def __eq__(self, other_rational: Rational) -> bool:
        result = Rational(self.num, self.den) - other_rational
        if result.num == 0.00000000:
            return True
        return False

    def __gt__(self, other_rational: Rational) -> bool:
        result = Rational(self.num, self.den) - other_rational
        if result.num > 0.00000000:
            return True
        return False

    def __ne__(self, other_rational: Rational) -> bool:
        if (
            Rational(self.num, self.den) < other_rational
            or Rational(self.num, self.den) > other_rational
        ):
            return True
        return False

    def __le__(self, other_rational: Rational) -> bool:
        if (
            Rational(self.num, self.den) < other_rational
            or Rational(self.num, self.den) == other_rational
        ):
            return True
        return False

    def __ge__(self, other_rational: Rational) -> bool:
        if (
            Rational(self.num, self.den) > other_rational
            or Rational(self.num, self.den) == other_rational
        ):
            return True
        return False

    def great_common_divisor(self) -> int:  # pylint: disable=C0116
        first_number = self.num
        second_number = self.den
        while first_number % second_number > 0:
            remainder = first_number % second_number
            first_number = second_number
            second_number = remainder
        great_common_divisor = second_number

        return great_common_divisor

    def reduced_form_conversion(self) -> Rational:  # pylint: disable=C0116
        gdc = self.great_common_divisor()
        self.num /= gdc
        self.den /= gdc
        return Rational(self.num, self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
