import unittest

from translator import english_to_french, english_to_german


class EnglishFrenchUnittest(unittest.TestCase):
    """This is the unit test for validating the enlish to french module"""
    def test1(self):
        """test2 function will do the unit testing of enlish to french module"""
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Thank you"), "Je vous remercie")
        self.assertEqual(english_to_french("Welcome"), "Bienvenue")
                      

class EnglishGermanUnittest(unittest.TestCase):
    """This is the unit test for validating the enlish to german module"""
    def test2(self):
        """test2 function will do the unit testing of enlish to german module"""
        self.assertEqual(english_to_german("Hello"), "Hallo")
        self.assertEqual(english_to_german("Thank you"), "Danke.")
        self.assertEqual(english_to_german("Welcome"), "Begrüßung")


unittest.main()
