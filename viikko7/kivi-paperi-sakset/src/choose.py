from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

def choosegame(vastaus):
    
    if vastaus.endswith("a"): 
        peli = KPSPelaajaVsPelaaja()

    elif vastaus.endswith("b"):
        peli = KPSTekoaly(Tekoaly())

    elif vastaus.endswith("c"):
        peli = KPSParempiTekoaly(TekoalyParannettu(10))

    else:
        peli = None

    return peli