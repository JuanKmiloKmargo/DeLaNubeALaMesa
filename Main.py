"""
Created on Sat Oct  7 14:27:11 2023

@author: USUARIO
"""

#from Interfaces.PanelLogo import PanelCentral
from Interfaces.InicioSesionRestaurante import Constructor as LogInConstructor
#from Interfaces.Interfaz_de_cajero_DefiPOO import RestauranteApp as icdp

def MainLoop(ventana_Inicial:int):
    valor = ventana_Inicial
    while valor != 0:
        Estructura = LogInConstructor(valor)
        valor = Estructura.destino
        #if valor == 5:
            #icdp()
        print(valor)

MainLoop(1)