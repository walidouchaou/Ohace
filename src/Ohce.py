


class Ohce:
    def __init__(self,maniere_de_dire_bonjour):
        self.maniere_de_dire_bonjour = maniere_de_dire_bonjour
    def palindrome(self,palindrome):
        miroir = palindrome[::-1]
        return self.maniere_de_dire_bonjour.dire_bonjour()\
               +miroir\
        + ("bien dit" if miroir==palindrome else "")\
        +"Au revoir "
