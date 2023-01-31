from enum import Enum
import datetime




class PeriodeDeLaJournee(Enum):
    DEFAULT = 1  # Quand on ne sait pas à quel moment nous sommes
    MATIN=2
    APRES_MIDI = 3
    SOIR = 4
    NUIT = 5

class PeriodeActuel():
    def PeriodeActuel(self):
        current_time = datetime.datetime.now().time()
        heurs = current_time.strftime("%H")
        if heurs>=6 and heurs<=12:
            return "MATIN"
        elif heurs >= 12 and heurs<=17:
            return "APRES_MIDI"
        elif heurs>=17 and heurs <= 22 :
            return "SOIR"
        elif heurs>=22 and heurs <=6:
            return "NUIT"
        else:
            return "DEFAULT"