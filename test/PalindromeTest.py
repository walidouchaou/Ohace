import unittest
import parameterized.parameterized
from utilities.LangueSpy import LangueSpy

from src.Ohce import Ohce

class PalindromeTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        chaine = "toto"

        # QUAND on saisit une chaîne
        ohce = Ohce()
        resultat = ohce.palindrome(chaine)

        # ALORS celle-ci est renvoyée en miroir
        self.assertIn(chaine[::-1], resultat)


        "test ETANT DONNE un utilisateur parlant la langue %s \n"
        "QUAND on saisit un palindrome \n"
        "ALORS %s est renvoyé ensuite"


    def test_palindrome(self):
        palindrome = "radar"

        ohce = Ohce()



        resultat = ohce.palindrome(palindrome)

        self.assertIn(palindrome, resultat)

        # ET 'Bien dit' est renvoyé ensuite
        resultat_apres_palindrome = resultat[len(palindrome):len(resultat)]
        self.assertIn(ohce.bien_dit(), resultat_apres_palindrome)

    def test_non_palindrome(self):
        #spy_langue = LangueSpy()
        ohce = Ohce()

        ohce.palindrome("toto")

        self.assertEqual(0, LangueSpy.nombre_appels_a_bien_dit)
if __name__ == '__main__':
    unittest.main()