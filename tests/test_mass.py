# -*- coding: utf-8 -*-
from .base import MeasurementTestBase


from measurement.measures import Mass


class MassTest(MeasurementTestBase):
    def test_round_unit(self):
        mass = Mass(g=1.563)
        expected = Mass(g=2)

        round(mass)

        self.assertEqual(
            mass,
            expected
        )

    def test_round_decimal(self):
        mass = Mass(g=1.563)
        expected = Mass(g=1.56)

        round(mass, 2)

        self.assertEqual(
            mass,
            expected
        )

