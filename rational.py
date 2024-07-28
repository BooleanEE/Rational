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

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
