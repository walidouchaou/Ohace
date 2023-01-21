


class Ohce:
    def palindrome(self,palindrome):
        miroir = "".join(reversed(palindrome))
        return "Bonjour " + miroir + ("Bien dit " if miroir == palindrome else "") + "Au revoie "
