from src.PeriodeDeLaJournee import PeriodeActuel
from src.PeriodeDeLaJournee import PeriodeDeLaJournee
from src.Langues.Constantes import Constantes
import parameterized.parameterized
import locale


class LangueStub:
    @parameterized.parameterized.expand(
        [[PeriodeActuel]],
        lambda _, __, args:
        str(type(args.args[0]).__name__))
    def dire_bonjour(self):
        system_language = locale.getdefaultlocale()[0]
        if system_language == "en-US":
            if PeriodeActuel.PeriodeActuel() == "MATIN":
                return Constantes.Anglais.GOOD_MORNING
            elif PeriodeActuel.PeriodeActuel()=="APRES_MIDI":
                return Constantes.Anglais.GOOD_AFTERNOON
            elif PeriodeActuel.PeriodeActuel()=="SOIR":
                return Constantes.Anglais.GOOD_EVENING
            elif PeriodeActuel.PeriodeActuel()== "NUIT":
                return Constantes.Anglais.GOOD_NIGHT
            else:
                return Constantes.Anglais.HELLO
        else:
            if PeriodeActuel.PeriodeActuel() == "MATIN":
                return Constantes.Francais.BONJOUR
            elif PeriodeActuel.PeriodeActuel()=="APRES_MIDI":
                return Constantes.Francais.BONJOUR
            elif PeriodeActuel.PeriodeActuel()=="SOIR":
                return Constantes.Francais.BONSOIR
            elif PeriodeActuel.PeriodeActuel()== "NUIT":
                return Constantes.Francais.BONSOIR
            else:
                return Constantes.Francais.BONJOUR

    def bien_dit(self):
        system_language = locale.getdefaultlocale()[0]
        if system_language == "en-US":
            return Constantes.Anglais.WELL_DONE
        else:
            return Constantes.Francais.BIEN_DIT
