from utilities.LangueStub import LangueStub


class Ohce:

    def __bien_dit(self):
        return LangueStub.bien_dit()

    def __bonjour(self):
        return LangueStub.dire_bonjour()

    def __au_revoir(self):
        return "Au revoir"

    def palindrome(self,palindrome):
        miroir = palindrome[::-1]
        return self.__bonjour() \
               + miroir \
               + (self.__bien_dit() if miroir == palindrome else "") \
               + self.__au_revoir()
