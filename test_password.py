import unittest

import password


class IterationOneTest(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(password.validate_1("VALID password_5"))

        self.assertTrue(password.validate_1("Long_3nough"), "password long enough")
        self.assertFalse(password.validate_1("Short_5"), "password too short")

        self.assertTrue(password.validate_1("has A capital_5"))
        self.assertFalse(password.validate_1("has no capital_5"))

        self.assertTrue(password.validate_1("HAS a LOWERCASE_5"))
        self.assertFalse(password.validate_1("HAS NO LOWERCASE_5"))

        self.assertTrue(password.validate_1("HA5 A_number"))
        self.assertFalse(password.validate_1("HAS NO_number"))

        self.assertTrue(password.validate_1("HAS_an_underscor3"))
        self.assertFalse(password.validate_1("HAS n0 underscore"))

    def test_long_password_valid(self):
        self.assertTrue(password.check_length("long enough"), "password long enough")

    def test_short_password_invalid(self):
        self.assertFalse(password.check_length("short"), "password too short")

    def test_password_with_capital_letter_valid(self):
        self.assertTrue(password.check_uppercase("no Capital"), "password has capital letter")

    def test_password_without_capital_letter_invalid(self):
        self.assertFalse(password.check_uppercase("no capital"), "password has no capital letter")

    def test_password_with_lowercase_valid(self):
        self.assertTrue(password.check_lowercase("password"), "password has a lowercase")

    def test_password_with_no_lowercase_invalid(self):
        self.assertFalse(password.check_lowercase("PASSWORD"), "password has no lowercase")

    def test_password_contains_number_valid(self):
        self.assertTrue(password.check_number("password5"))

    def test_password__without_number_invalid(self):
        self.assertFalse(password.check_number("password"))

    def test_password_with_underscore_valid(self):
        self.assertTrue(password.check_underscore("passw_rd"))

    def test_password_without_underscore_invalid(self):
        self.assertFalse(password.check_underscore("password"))
    

class IterationTwoTest(unittest.TestCase):
    def test_password_valid(self):
        self.assertTrue(password.validate_2("VALID password 6"))

        self.assertTrue(password.validate_2("Enough7"), "password long enough")
        self.assertFalse(password.validate_2("Srt5"), "password too short")

        self.assertFalse(password.validate_2("has no capital 5"))
        self.assertFalse(password.validate_2("HAS NO LOWERCASE 5"))

        self.assertFalse(password.validate_2("HAS NO number"))


class IterationThreeTest(unittest.TestCase):
    def test_password_valid(self):
        self.assertTrue(password.validate_3("This is a VALID password_"))

        self.assertTrue(password.validate_3("Password_is long enough"), "password long enough")
        self.assertFalse(password.validate_3("Too_short"), "password too short")

        self.assertFalse(password.validate_3("has no capital_"))
        self.assertFalse(password.validate_3("HAS NO LOWERCASE_"))

        self.assertFalse(password.validate_3("HAS NO underscore"))
        self.assertTrue(password.validate_3("HAS an _underscore"))


class IterationFourTest(unittest.TestCase):
    def test_password_value(self):
        self.assertTrue(password.validate_4("Valid_Pa22word"))

    def test_one_error(self):
        self.assertEqual(password.validate_4("Sh0r_"), ["Too short"])
        self.assertEqual(password.validate_4("n0_uppercase"), ["No uppercase letter"])
        self.assertEqual(password.validate_4("N0_LOWERCASE"), ["No lowercase letter"])
        self.assertEqual(password.validate_4("No_numBER"), ["No number"])
        self.assertEqual(password.validate_4("N0 underSCORE"), ["No underscore"])

    def test_two_errors(self):
        self.assertEqual(password.validate_4("Shor_"), ["Too short", "No number"])
        self.assertEqual(password.validate_4("2hor_"), ["Too short", "No uppercase letter"])
        self.assertEqual(password.validate_4("2HOR_"), ["Too short", "No lowercase letter"])
        self.assertEqual(password.validate_4("sHOR_"), ["Too short", "No number"])
        self.assertEqual(password.validate_4("sH0R"), ["Too short", "No underscore"])

    def test_three_errors(self):
        self.assertEqual(
            password.validate_4("INCORRECT"), ["No lowercase letter", "No number", "No underscore"]
        )
        self.assertEqual(
            password.validate_4("incorrect"),["No uppercase letter", "No number", "No underscore"]
        )
        self.assertEqual(
            password.validate_4("inc_"), ["Too short", "No uppercase letter", "No number"]
        )

    def test_four_errors(self):
        self.assertEqual(
            password.validate_4("SHORT"),
            ["Too short", "No lowercase letter", "No number", "No underscore"]
        )


class IterationFiveTest(unittest.TestCase):
    def test_all_criteria_valid(self):
        self.assertTrue(password.validate_5("Valid_Passw0rd"))

    def test_password_ignore_uppercase_valid(self):
        self.assertTrue(password.validate_5("n0_uppercase"))

    def test_password_ignore_length_valid(self):
        self.assertTrue(password.validate_5("Sh0R_"))

    def test_two_errors_invalid(self):
        self.assertFalse(password.validate_5("SH0R_"))

    def test_three_errors_invalid(self):
        self.assertFalse(password.validate_5("SHOR_"))

    def test_four_errors_invalid(self):
        self.assertFalse(password.validate_5("SHORT"))


if __name__ == "__main__":
    unittest.main()
