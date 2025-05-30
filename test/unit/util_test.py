import unittest
import pytest

from app import util


@pytest.mark.unit
class TestUtil(unittest.TestCase):
    def test_convert_to_number_correct_param(self):
        self.assertEqual(4, util.convert_to_number("4"))
        self.assertEqual(0, util.convert_to_number("0"))
        self.assertEqual(0, util.convert_to_number("-0"))
        self.assertEqual(-1, util.convert_to_number("-1"))
        self.assertAlmostEqual(4.0, util.convert_to_number("4.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("0.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("-0.0"), delta=0.0000001)
        self.assertAlmostEqual(-1.0, util.convert_to_number("-1.0"), delta=0.0000001)

    def test_InvalidConvertToNumber_with_integer(self):
        # Reconocer enteros sin punto
        self.assertEqual(util.InvalidConvertToNumber("7"), 7)

    def test_InvalidConvertToNumber_with_float(self):
        # Reconocer números con punto
        self.assertEqual(util.InvalidConvertToNumber("3.14"), 3.14)

    def test_InvalidConvertToNumber_raises_on_invalid(self):
        # Causa un ValueError interno y luego TypeError con mensaje exacto
        with self.assertRaises(TypeError) as cm:
            util.InvalidConvertToNumber("not_a_number")
        self.assertEqual(str(cm.exception), "Operator cannot be converted to number")

    def test_convert_to_number_invalid_type(self):
        self.assertRaises(TypeError, util.convert_to_number, "")
        self.assertRaises(TypeError, util.convert_to_number, "3.h")
        self.assertRaises(TypeError, util.convert_to_number, "s")
        self.assertRaises(TypeError, util.convert_to_number, None)
        self.assertRaises(TypeError, util.convert_to_number, object())

    def test_convert_to_number_value_error_message(self):
        with self.assertRaises(TypeError) as cm:
            util.convert_to_number("abc")
        self.assertEqual(str(cm.exception), "Operator cannot be converted to number")

    def test_validate_permissions(self):
        # Solo 'user1' debe recibir True
        self.assertTrue(util.validate_permissions("any op", "user1"))
        # Cualquier otro usuario → False
        self.assertFalse(util.validate_permissions("any op", "other_user"))