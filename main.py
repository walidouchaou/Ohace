import locale


from src.Langues.LangueAnglais import LangueAnglaise
from src.Langues.LangueFrancaise import LangueFrancaise
from src.Ohce import Ohce
from src.PeriodeDeLaJournee import PeriodeDeLaJournee


class SystemLangAdapter():
    def __init__(self):
        langue_systeme = locale.getdefaultlocale()[0]
        self.__langue = LangueAnglaise() \
            if langue_systeme == "en_GB" \
            else LangueFrancaise()





if __name__ == '__main__':
    ohce = Ohce(SystemLangAdapter(), PeriodeDeLaJournee.NUIT)

while True:
    user_input = input("> ")
    if ohce.palindrome(user_input):
        ohce.__bien_dit()
    else:
        print(user_input[::-1])