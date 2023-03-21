import os
import math
from tqdm import*
from colorama import Back
from colorama import Fore
from colorama import init
from colorama import * 
from stdiomask import *
import string
import re
import time 
import datetime
import random


usuarios = []
username = "a"      
password = "a"
intentos = 0
tiempo = 2

# Asistencia y Manuales ( INTERFACES )

def manual_usuario():
    palma()
    print(Fore.BLACK+
     """
     \t\t\t\t ꧁═════════════════════════════|| Las Palmas || - || Manual ||═════════════════════════════꧂
     \t\t\t\t 
     \t\t\t\t
     \t\t\t\t       >> Bienvenido/a al manual de usuario del simulador de cajero automático.
     \t\t\t\t           A continuación se presentan los pasos necesarios para utilizar el software:
     \t\t\t\t
     \t\t\t\t           
     \t\t\t\t           1. -Inicio de sesión: El primer paso es iniciar sesión en el sistema. 
     \t\t\t\t               Para hacerlo, introduzca su cédula y PIN. Si es la primera vez que             
     \t\t\t\t               utiliza el software, deberá registrarse solicitandolo a un administrador.
     \t\t\t\t
     \t\t\t\t           2. -Seleccion de transacción: A continuación, se le presentarán las opciones 
     \t\t\t\t               disponibles.
     \t\t\t\t  
     \t\t\t\t               >> Retiro de efectivo.
     \t\t\t\t               >> Deposito de efectivo.
     \t\t\t\t               >> Transferencias.
     \t\t\t\t               >> Camabios de PIN.
     \t\t\t\t 
     \t\t\t\t               Si ha seleccionado alguna de las opciones el software mostrará un menú 
     \t\t\t\t               intuitivo y dependiendo de lo que seleccione se procesará la operación 
     \t\t\t\t               y se mostrará un mensaje indicando que la operación se puede continuar
     \t\t\t\t               con o sin una emisión de voucher del estado de su cuenta y por último  
     \t\t\t\t               un mensaje que se ha completado con éxito su operación.              
     """
    )
    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
    

def manual_admin():
    palma()
    print(Fore.BLACK+
     """
     \t\t\t\t ꧁═════════════════════════════|| Las Palmas || - || Manual ||═════════════════════════════꧂
     \t\t\t\t 
     \t\t\t\t
     \t\t\t\t       >> Bienvenido/a al manual de administrador del simulador de cajero automático.
     \t\t\t\t           A continuación se presentan los pasos necesarios para utilizar el software:
     \t\t\t\t
     \t\t\t\t           
     \t\t\t\t           1. -Inicio de sesión: El primer paso es iniciar sesión en el sistema. 
     \t\t\t\t               Para hacerlo, introduzca sus creedenciales predeterminadas en el inicio
     \t\t\t\t               de sesión.
     \t\t\t\t
     \t\t\t\t           2. -Menú << CRUD >>: A continuación, se le presentarán las opciones 
     \t\t\t\t               disponibles.
     \t\t\t\t               
     \t\t\t\t               >> CREATED ( Crear ) : Opción para registrar usuarios.
     \t\t\t\t
     \t\t\t\t                  Al registrar un nuevo usuario el software pedirá los sigueintes datos:
     \t\t\t\t                  Cédula, Nombres Completos, Dinero y PIN. Asegúrese de rellenar los 
     \t\t\t\t                  campos correctamente. 
     \t\t\t\t
     \t\t\t\t               >> READ ( Leer ) : Opcion para mostrar usuarios registrados.
     \t\t\t\t                   
     \t\t\t\t                  Esta opción desplegará todos los usuarios registrados en el sistema.
     \t\t\t\t
     \t\t\t\t               >> UPDATE ( Actualizar ) : Opción para editar datos de usuarios registrados.
     \t\t\t\t               
     \t\t\t\t                  Esta opción permite editar datos del usuario: Nombres Completos y Monto.
     \t\t\t\t
     \t\t\t\t               >> DELETE ( Eliminar ) : Opcion para eliminar datos de usuarios registrados.
     \t\t\t\t 
     \t\t\t\t                  Esta opción permite elimar todos los datos de un usuario registrado.
     \t\t\t\t                   
     """
    )
    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")


# Logo banco e interfaces 

def bienvenido():
    os.system("cls")
    print(Fore.GREEN+f"""
\t\t\t\t       ||  ꧁═════════════════════════════|| Las Palmas || - || Usuario ||═════════════════════════════꧂
\t\t\t\t       ||                                                                      
\t\t\t\t       ||                             BIENVENIDO AL BANCO LAS PALMAS                                                                       
\t\t\t\t       ||  ░░░░░░░░░░░░☼░░░░░░░░░                                                             
\t\t\t\t       ||  ░░▄▀▀▀▄░▄▄░░░░░░╠▓░░░░     BIENVENIDO: {usuarios[psind + 1]} 
\t\t\t\t       ||  ░░░▄▀▀▄█▄░▀▄░░░▓╬▓▓▓░░
\t\t\t\t       ||  ░░▀░░░░█░▀▄░░░▓▓╬▓▓▓▓░     ¡Que gusto tenerte aquí! 
\t\t\t\t       ||  ░░░░░░▐▌░░░░▀▀███████▀
\t\t\t\t       ||  ▒▒▄██████▄▒▒▒▒▒▒▒▒▒▒▒▒                                                                
\t\t\t\t       ||                                 
\t\t\t\t       ||                                         
\t\t\t\t       ||                                                                  
\t\t\t\t       ||                                                                  
\t\t\t\t       ||  ═════════════════════════════||Estamos cargando sus datos..||═════════════════════════════                                                            
    """)
    input(Fore.LIGHTMAGENTA_EX+"\n\n\t\t\t\t\t\t\tPresione Enter para continuar")

def palma():
    

    os.system("cls")
    init()
    
    print(Fore.RED +
        """
                                                                        ░░░░░░░░░░░░☼░░░░░░░░░                                                                  
                                                                        ░░▄▀▀▀▄░▄▄░░░░░░╠▓░░░░
                                                                        ░░░▄▀▀▄█▄░▀▄░░░▓╬▓▓▓░░
                                                                        ░░▀░░░░█░▀▄░░░▓▓╬▓▓▓▓░
                                                                        ░░░░░░▐▌░░░░▀▀███████▀
                                                                        ▒▒▄██████▄▒▒▒▒▒▒▒▒▒▒▒▒

        """+Fore.RESET
    )



def logo_banco1():
    

    os.system("cls")
    init()
    
    print(Fore.RED +
        """
        \t\t                                      || B || || A || || N || C || O ||
        \t\t                 _____________________________________________________________________________
        \t\t 
        \t\t          
        \t\t             ██▓     ▄▄▄        ██████     ██▓███   ▄▄▄       ██▓     ███▄ ▄███▓ ▄▄▄        ██████ 
        \t\t             ▓██▒    ▒████▄    ▒██    ▒    ▓██░  ██▒▒████▄    ▓██▒    ▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ 
        \t\t             ▒██░    ▒██  ▀█▄  ░ ▓██▄      ▓██░ ██▓▒▒██  ▀█▄  ▒██░    ▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   
        \t\t             ▒██░    ░██▄▄▄▄██   ▒   ██▒   ▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██░    ▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒
        \t\t             ░██████▒ ▓█   ▓██▒▒██████▒▒   ▒██▒ ░  ░ ▓█   ▓██▒░██████▒▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒
        \t\t             ░ ▒░▓  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░   ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░
        \t\t             ░ ░ ▒  ░  ▒   ▒▒ ░░ ░▒  ░ ░   ░▒ ░       ▒   ▒▒ ░░ ░ ▒  ░░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░
        \t\t             ░ ░     ░   ▒   ░  ░  ░     ░░         ░   ▒     ░ ░   ░      ░     ░   ▒   ░  ░  ░  
        \t\t                 ░  ░      ░  ░      ░                    ░  ░    ░  ░       ░         ░  ░      ░  
        \t\t 
                                                                        ░░░░░░░░░░░░☼░░░░░░░░░                                                                  
                                                                        ░░▄▀▀▀▄░▄▄░░░░░░╠▓░░░░
                                                                        ░░░▄▀▀▄█▄░▀▄░░░▓╬▓▓▓░░
                                                                        ░░▀░░░░█░▀▄░░░▓▓╬▓▓▓▓░
                                                                        ░░░░░░▐▌░░░░▀▀███████▀
                                                                        ▒▒▄██████▄▒▒▒▒▒▒▒▒▒▒▒▒

        """+Fore.RESET
    )

def logo_salir():
        os.system("cls")
        print(Fore.RED +
        """
        \t\t                                      || B || || A || || N || C || O ||
        \t\t                 _____________________________________________________________________________
        \t\t                                                                                                                                                                                                                                                    
        \t\t                                                                                                        
        \t\t             ██▓     ▄▄▄        ██████     ██▓███   ▄▄▄       ██▓     ███▄ ▄███▓ ▄▄▄        ██████ 
        \t\t             ▓██▒    ▒████▄    ▒██    ▒    ▓██░  ██▒▒████▄    ▓██▒    ▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ 
        \t\t             ▒██░    ▒██  ▀█▄  ░ ▓██▄      ▓██░ ██▓▒▒██  ▀█▄  ▒██░    ▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   
        \t\t             ▒██░    ░██▄▄▄▄██   ▒   ██▒   ▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██░    ▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒
        \t\t             ░██████▒ ▓█   ▓██▒▒██████▒▒   ▒██▒ ░  ░ ▓█   ▓██▒░██████▒▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒
        \t\t             ░ ▒░▓  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░   ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░
        \t\t             ░ ░ ▒  ░  ▒   ▒▒ ░░ ░▒  ░ ░   ░▒ ░       ▒   ▒▒ ░░ ░ ▒  ░░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░
        \t\t             ░ ░     ░   ▒   ░  ░  ░     ░░         ░   ▒     ░ ░   ░      ░     ░   ▒   ░  ░  ░  
        \t\t                 ░  ░      ░  ░      ░                    ░  ░    ░  ░       ░         ░  ░      ░  
        \t\t 
                                                                        ░░░░░░░░░░░░☼░░░░░░░░░                                                                  
                                                                        ░░▄▀▀▀▄░▄▄░░░░░░╠▓░░░░
                                                                        ░░░▄▀▀▄█▄░▀▄░░░▓╬▓▓▓░░
                                                                        ░░▀░░░░█░▀▄░░░▓▓╬▓▓▓▓░
                                                                        ░░░░░░▐▌░░░░▀▀███████▀
                                                                        ▒▒▄██████▄▒▒▒▒▒▒▒▒▒▒▒▒

        """
    )
        
        print(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\tGracias por preferirnos")
        time.sleep(tiempo)


def logo_banco():

    os.system("cls")
    init()
    
    print(Fore.RED +
        """
        \t\t                                      || B || || A || || N || C || O ||
        \t\t                 _____________________________________________________________________________
        \t\t                                                                                                                                                                                                                                                    
        \t\t                                                                                                        
        \t\t             ██▓     ▄▄▄        ██████     ██▓███   ▄▄▄       ██▓     ███▄ ▄███▓ ▄▄▄        ██████ 
        \t\t             ▓██▒    ▒████▄    ▒██    ▒    ▓██░  ██▒▒████▄    ▓██▒    ▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ 
        \t\t             ▒██░    ▒██  ▀█▄  ░ ▓██▄      ▓██░ ██▓▒▒██  ▀█▄  ▒██░    ▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   
        \t\t             ▒██░    ░██▄▄▄▄██   ▒   ██▒   ▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██░    ▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒
        \t\t             ░██████▒ ▓█   ▓██▒▒██████▒▒   ▒██▒ ░  ░ ▓█   ▓██▒░██████▒▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒
        \t\t             ░ ▒░▓  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░   ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░
        \t\t             ░ ░ ▒  ░  ▒   ▒▒ ░░ ░▒  ░ ░   ░▒ ░       ▒   ▒▒ ░░ ░ ▒  ░░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░
        \t\t             ░ ░     ░   ▒   ░  ░  ░     ░░         ░   ▒     ░ ░   ░      ░     ░   ▒   ░  ░  ░  
        \t\t                 ░  ░      ░  ░      ░                    ░  ░    ░  ░       ░         ░  ░      ░  
        \t\t 
                                                                        ░░░░░░░░░░░░☼░░░░░░░░░                                                                  
                                                                        ░░▄▀▀▀▄░▄▄░░░░░░╠▓░░░░
                                                                        ░░░▄▀▀▄█▄░▀▄░░░▓╬▓▓▓░░
                                                                        ░░▀░░░░█░▀▄░░░▓▓╬▓▓▓▓░
                                                                        ░░░░░░▐▌░░░░▀▀███████▀
                                                                        ▒▒▄██████▄▒▒▒▒▒▒▒▒▒▒▒▒

        """
    )

def progress_bar():

    logo_banco()
    print(
    Fore.GREEN + Style.BRIGHT +
    """
    \t\t\t\t         _____________________________________________________________________________
    \t\t\t\t                                                      
    \t\t\t\t                                     
    \t\t\t\t                                        CARGANDO SISTEMA                                                        
    \t\t\t\t                                                                                     
    \t\t\t\t         _____________________________________________________________________________
        
    """
    )
    

    for i in tqdm(range(70), bar_format="{l_bar}{bar}", postfix="%"):
        time.sleep(0.02)

def menu_crud():
    print( 
    Fore.LIGHTGREEN_EX + Style.BRIGHT +
    """
    \t\t\t                  _____________________________________________________________________________
    \t\t\t 
    \t\t\t 
    \t\t\t                                        || C || || R || U || D || 
    \t\t\t 
    \t\t\t 
    \t\t\t                                                                 
    \t\t\t                                        1. - Ingresar datos de Usuario
    \t\t\t                                        2. - Mostrar datos de usuarios
    \t\t\t                                        3. - Editar datos de usuario
    \t\t\t                                        4. - Eliminar datos de usuario
    \t\t\t                                        5. - Consultar datos de Usuario
    \t\t\t                                        6. - Salir
    \t\t\t                                                                                                                                                                                                                                                                                                                                                                   
    \t\t\t                  _____________________________________________________________________________
                                                                                    
    """)
    
def menu_usuarios():
    print( 
    Fore.LIGHTGREEN_EX + Style.BRIGHT +
    f"""
    \t\t\t                  _____________________________________________________________________________
    \t\t\t 
    \t\t\t 
    \t\t\t                                        || M || || E || N || U || 
    \t\t\t 
    \t\t\t 
    \t\t\t                                   Saldo Disponible:$ {usuarios[psind + 2]}                        
    \t\t\t                                        1. - Retirar
    \t\t\t                                        2. - Depositar
    \t\t\t                                        3. - Transferir
    \t\t\t                                        4. - Cambiar PIN
    \t\t\t                                        5. - Salir
    \t\t\t                                                                                                                                                                                                                                                                                                                                                                    
    \t\t\t                  _____________________________________________________________________________
                                                                                    
    """)
def volver():
    palma()
    print( 
    Fore.LIGHTGREEN_EX + Style.BRIGHT +
    """
    \t\t\t                  _____________________________________________________________________________
    \t\t\t 
    \t\t\t 
    \t\t\t                                        || M || || E || N || U || 
    \t\t\t                                                                 
    \t\t\t                                        1. - Continuar
    \t\t\t                                        2. - Salir                                                                                                                                                                                                                                                                                                                                                                  
    \t\t\t                  _____________________________________________________________________________
                                                                                    
    """)


def menu_retiros():
    print( 
    Fore.LIGHTGREEN_EX + Style.BRIGHT +
    f"""
    \t\t\t                  _____________________________________________________________________________
    \t\t\t 
    \t\t\t 
    \t\t\t                                        || - RETIRO RÁPIDO - || 
    \t\t\t 
    \t\t\t                                         
    \t\t\t                                        Saldo Disponible:$ {usuarios[psind + 2]}                 
    \t\t\t                                               1. - $10
    \t\t\t                                               2. - $20
    \t\t\t                                               3. - $50
    \t\t\t                                               4. - $100
    \t\t\t                                               5. - Otra Cantidad (Especificar)
    \t\t\t                                               6. - Salir
    \t\t\t
    \t\t\t                                                                                                                                                                                                                                                                                                                                                                    
    \t\t\t                  _____________________________________________________________________________
                                                                                    
    """)

def menu_depo():
    print( 
    Fore.LIGHTGREEN_EX + Style.BRIGHT +
    f"""
    \t\t\t                  _____________________________________________________________________________
    \t\t\t 
    \t\t\t 
    \t\t\t                                        || - DEPÓSITO RÁPIDO - || 
    \t\t\t 
    \t\t\t                                        
    \t\t\t                                        Saldo Disponible:$ {usuarios[psind + 2]}                         
    \t\t\t                                               1. - $10
    \t\t\t                                               2. - $20
    \t\t\t                                               3. - $50
    \t\t\t                                               4. - $100
    \t\t\t                                               5. - Otra Cantidad (Especificar)
    \t\t\t                                               6. - Salir
    \t\t\t
    \t\t\t                                                                                                                                                                                                                                                                                                                                                                    
    \t\t\t                  _____________________________________________________________________________
                                                                                    
    """)

def voucher():
    print( 
    Fore.LIGHTGREEN_EX + Style.BRIGHT +
    f"""
    \t\t\t                  _____________________________________________________________________________
    \t\t\t              
    \t\t\t 
    \t\t\t                                        || - DEPÓSITO RÁPIDO - || 
    \t\t\t 
    \t\t\t                                        
    \t\t\t                                        Saldo Disponible:$ {usuarios[psind + 2]}                      
    \t\t\t                                               1. - $10
    \t\t\t                                               2. - $20
    \t\t\t                                               3. - $50
    \t\t\t                                               4. - $100
    \t\t\t                                               5. - Otra Cantidad (Especificar)
    \t\t\t                                               6. - Salir
    \t\t\t
    \t\t\t                                                                                                                                                                                                                                                                                                                                                                    
    \t\t\t                  _____________________________________________________________________________
                                                                                    
    """)

def opcion_v():
    input(Fore.RED+"\n\n\t\t\t\t\t\t\t\t     || INGRESE UNA OPCIÓN VÁLIDA ||")
 

def impresion_retiro():

    numeros = ''.join(random.choices(string.digits, k=6))
    codigo =  numeros 

    fecha_hora_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    
    
    print(
        Fore.BLACK+
        f"""
        \t\t                         ═════════════════|| LAS PALMAS ||═════════════════
        \t\t                         ||
        \t\t                         || >> RETIRO
        \t\t                         ||
        \t\t                         ||        Cuenta...: {usuarios[psind][8:10]}XXXXXX{usuarios[psind][-2:]}
        \t\t                         ||        Nombre...: {usuarios[psind+1]}
        \t\t                         ||        Documento: {codigo}
        \t\t                         ||        Efectivo.: {valor}.00
        \t\t                         ||        Cargo....: 0.35
        \t\t                         ||        Moneda...: USD
        \t\t                         ||        Fecha....: {fecha_hora_actual}
        \t\t                         ||        Saldo....: {retiro} 
        \t\t                         ||                                                      
        \t\t                         ||              **GUARDE SU RECIBO***
        \t\t                         ||        *Cuidar la clave es su responsabilidad
        \t\t                         ||         Cliente
        \t\t                         ||
        \t\t                         ════════════════════════════════════════════════



        """+ Fore.RESET  
    )

def user_not_found():
    os.system("cls")
    print(Fore.RED+"""\n\n\n\n\n
    \t\t                       _________________________________________________________________________________
    \t\t                       |                                                                               |
    \t\t                       |                          USUARIO NO ENCONTRADO                                |
    \t\t                       |_______________________________________________________________________________|
        
    """)
    input(Fore.LIGHTMAGENTA_EX+"\n\n\t\t\t\t\t\t\t\tPresione Enter para volver a intentar")

    


def impresion_retiro1():

    numeros = ''.join(random.choices(string.digits, k=6))
    codigo =  numeros 

    fecha_hora_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    
    
    print(
        Fore.BLACK+
        f"""
        \t\t                         ═════════════════|| LAS PALMAS ||═════════════════
        \t\t                         ||
        \t\t                         || >> RETIRO
        \t\t                         ||
        \t\t                         ||        Cuenta...: {usuarios[psind][8:10]}XXXXXX{usuarios[psind][-2:]}
        \t\t                         ||        Nombre...: {usuarios[psind+1]}
        \t\t                         ||        Documento: {codigo}
        \t\t                         ||        Efectivo.: {saldo}
        \t\t                         ||        Cargo....: 0.35
        \t\t                         ||        Moneda...: USD
        \t\t                         ||        Fecha....: {fecha_hora_actual}
        \t\t                         ||        Saldo....: {retiro} 
        \t\t                         ||                                                      
        \t\t                         ||              **GUARDE SU RECIBO***
        \t\t                         ||        *Cuidar la clave es su responsabilidad
        \t\t                         ||         Cliente
        \t\t                         ||
        \t\t                         ════════════════════════════════════════════════



        """+ Fore.RESET  
    )

def impresion1():
    print(
        Fore.BLACK +
        f"""
        \t\t                         ═══════════════|| IMPRESION ||════════════════
        \t\t                         ||                                          
        \t\t                         ||        Saldo de la Cuenta:  {saldo}                   
        \t\t                         ||        Saldo Retirado:      -20.35                                     
        \t\t                         ||        Saldo Actual:        {retiro}        
        \t\t                         ||                                          
        \t\t                         ══════════════════════════════════════════════


        """ + Fore.RESET 
    )



def depositos():
    numeros = ''.join(random.choices(string.digits, k=6))
    codigo =  numeros 
    fecha_hora_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
   
    print(
        Fore.BLACK+
        f"""
        \t\t                         ═════════════════|| LAS PALMAS ||═════════════════
        \t\t                         ||
        \t\t                         || >> DEPÓSITO
        \t\t                         ||
        \t\t                         ||        Cuenta...: {usuarios[psind][8:10]}XXXXXX{usuarios[psind][-2:]}
        \t\t                         ||        Nombre...: {usuarios[psind+1]}
        \t\t                         ||        Documento: {codigo}                                                 
        \t\t                         ||        Deposito.:  {dep}                                                           
        \t\t                         ||        Cargo....: 0.35
        \t\t                         ||        Moneda...: USD
        \t\t                         ||        Fecha....: {fecha_hora_actual}
        \t\t                         ||        Saldo....: {saldo + dep} 
        \t\t                         ||                                                      
        \t\t                         ||        *Cuidar la clave es su responsabilidad
        \t\t                         ||         Cliente
        \t\t                         ||
        \t\t                         ════════════════════════════════════════════════

        """+ Fore.RESET  
    )



def depositos_manu():
    print(
        Fore.BLACK+
        f"""
        \t\t                         ═════════════════|| IMPRESIÓN ||═════════════════
        \t\t                         ||                                          
        \t\t                         ||        Saldo de la Cuenta:  {saldo}   
        \t\t                         ||        Valor del Depósito:  {datos}
        \t\t                         ||        Saldo de la Cuenta:  {saldo + datos}                         
        \t\t                         ||        Valor del Voucher:  -{0.35}                                
        \t\t                         ||        Saldo Actual:        {retiro}
        \t\t                         ||
        \t\t                         ════════════════════════════════════════════════



        """+ Fore.RESET  
    )



def generar_tabla(datos):
    
    for i in range(0, len(datos), 4):
        codigo = datos[i]
        nombre = datos[i+1]
        cedula = datos[i+2]
        monto = datos[i+3]
        
        
        # Imprimir la fila de la tabla
        #print(Fore.GREEN+"  │                        |                          |                |                       |")
        print(Fore.GREEN+"    \t\t                   |  {:<20}  |{:<25} | ${:<15}| #{:<15}     |".format(codigo, nombre,cedula,monto))
        print("    \t\t                   |════════════════════════════════════════════════════════════════════════════════════════════|")

def list():   
    os.system("cls")
    palma()
    print(Fore.MAGENTA+"    \t\t                   ꧁═════════════════════════════|| Las Palmas || - || Usuarios ||═════════════════════════════꧂")
    print("    \t\t                   |════════════════════════════════════════════════════════════════════════════════════════════|")
    print("    \t\t                   |    {:20}| {:<25}| {:<15} |  {:<15}    |".format("Cédula", "Nombre Completo","Monto", "PIN de Cuenta"))
    print("    \t\t                   |════════════════════════════════════════════════════════════════════════════════════════════|")
    for i  in range(len(usuarios)):
        if i % 4 == 0:
            codigo = usuarios[i]
            nombre = usuarios[i+1]
            cedula = usuarios[i+2]
            monto = usuarios[i+3]
            
            datos = [codigo, nombre,cedula,  monto]
            generar_tabla(datos)
    
    os.system("pause")

def check_password(passw,intentos):
    if passw != password:
        return False
    else:
        return True



def check_user(admin):
    if  admin != username:
        os.system("cls")
        print(Fore.RED+"""\n\n\n\n\n
        \t                      _________________________________________________________________________________
        \t                      |                                                                               |
        \t                      |                          USUARIO NO ENCONTRADO                                |
        \t                      |_______________________________________________________________________________|
            
        """)
        input(Fore.LIGHTMAGENTA_EX+"\n\n\t\t\t\t\t\t\t\tPresione Enter para volver a intentar")
        return False
    else:
        return True

def menu_voucher():
    print(Fore.GREEN+
        """
    \t\t\t\t                  _________________________________________________________
    \t\t\t\t                                  MENU DE IMPRESIÓN DE VOUCHER
    \t\t\t\t                  
    \t\t\t\t                      1. Desea continuar con la impresión del voucher || $0.35
    \t\t\t\t                      2. Continuar sin voucher
    \t\t\t\t                      3. Salir
    \t\t\t\t                  _________________________________________________________
    
"""  )

def loadData():
    with open('users_admins.txt', 'r') as file:
        usuarios.clear()
        data = file.read().splitlines()
        usuarios.extend(data)

def saveData():
    with open("users_admins.txt", "w") as txt_file:
        for line in usuarios:
            txt_file.write(line+ "\n")

def eliminar():
    palma()
    cedula = input(str(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese el número de cuenta que desea eliminar: ")) 
    if "Cédula: " + cedula in usuarios:
        pos = usuarios.index("Cédula: " + cedula)
        usuarios.pop(pos+3)
        usuarios.pop(pos+2)
        usuarios.pop(pos+1)
        usuarios.pop(pos)
        palma()
        print(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tUsuario eliminado correctamente!")
        saveData()
        os.system("pause")
    else:
        palma()
        print(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tUsuario no registrado!")
        os.system("pause")

def user_list(code):
    os.system("cls")
    palma()
    print(Fore.MAGENTA+"    \t\t                   ꧁═════════════════════════════|| Las Palmas || - || Usuario ||═════════════════════════════꧂")
    print("    \t\t                   |════════════════════════════════════════════════════════════════════════════════════════════|")
    print("    \t\t                   |    {:20}| {:<25}| {:<15} |  {:<15}    |".format("Cédula", "Nombre Completo","Monto", "PIN de Cuenta"))
    print("    \t\t                   |════════════════════════════════════════════════════════════════════════════════════════════|")
    psind = usuarios.index("Cédula: " + code)
    codigo = usuarios[psind]
    nombre = usuarios[psind+1]
    cedula = usuarios[psind+2]
    monto = usuarios[psind+3]                                       
    
            
    datos = [codigo, nombre,cedula, monto]
    generar_tabla(datos)
    os.system("pause")

def loadData():
    with open('users_admins.txt', 'r') as file:
        usuarios.clear()
        data = file.read().splitlines()
        usuarios.extend(data)

def validar_cedula(cedula):
    # Verificar que la cédula tenga 10 dígitos numéricos
    if not cedula.isdigit() or len(cedula) != 10:
        return False
    # Verificar que los dos primeros dígitos correspondan a la provincia
    provincia = int(cedula[:2])
    if provincia < 1 or provincia > 24:
        return False
    
    # Comprobar que el tercer dígito sea un número válido para el género
    genero = int(cedula[2])
    if genero not in [0, 1, 2, 3, 4, 5, 6]:
        return False
    
    # Aplicar el algoritmo de Luhn para validar los últimos siete dígitos
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    total = 0
    digito_verificador = int(cedula[-1])
    for i in range(9):
        digito = int(cedula[i])
        coeficiente = coeficientes[i]
        producto = digito * coeficiente
        if producto >= 10:
            producto -= 9
        total += producto
    total %= 10
    if total != 0:
        total = 10 - total
    if total != digito_verificador:
        return False
    
    # Si pasó todas las verificaciones, la cédula es válida
    return True

def saveData():
    with open("users_admins.txt", "w") as txt_file:
        for line in usuarios:
            txt_file.write(line+ "\n")

try:
    print(Back.LIGHTYELLOW_EX +"Inicializando logo del banco...")
    logo_banco()
    time.sleep(2)
    progress_bar()
    loadData()
except:
    opcion_v()
inicio=True
while inicio:
    try:
        palma()
        print( 
        Fore.LIGHTGREEN_EX + Style.NORMAL +
            """\n\n
            \t                    _____________________________________________________________________________
            \t   
            \t   
            \t                                          || M || || E || N || U || 
            \t   
            \t   
            \t                                                                   
            \t                                          1. - Ingresar como usuario
            \t                                          2. - Ingresar como admin
            \t                                          3. - Salir
            \t
            \t 
            \t                                   ||  Ingrese << ? >> para ayuda e información  ||                                                                                                                                                                                                                                                                       
            \t                    _____________________________________________________________________________
                                                                                            
            """)
            
        opci=input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\t\tIngrese una opción: ")
        match opci:
            case '1':
                progress_bar()
                cedula_val=True
                while cedula_val:
                    try: 
                        logo_banco()
                        cedula = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese su cédula: ")
                        if "Cédula: " + cedula in usuarios:
                            psind = usuarios.index("Cédula: " + cedula)
                            datos = []
                            datos.append(usuarios[psind])
                            datos.append(usuarios[psind + 1])
                            datos.append(usuarios[psind + 2])
                            datos.append(usuarios[psind + 3])
                            cedula_val=False
                            codigo_val =True
                            while codigo_val:
                                logo_banco()
                                texto = getpass(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese el PIN: ", "*")
                                if texto == "":
                                    print("Ingrese algún valor")
                                    time.sleep(tiempo)
                                    continue
                                if datos[3] == texto:
                                    codigo_val = False
                                    menu_edit = True
                                    bienvenido()
                                    while menu_edit:
                                        palma()
                                        menu_usuarios()
                                        opci=input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese una opción: ")
                                        match opci:
                                            case '1':
                                                while True:
                                                    logo_banco()
                                                    menu_retiros()
                                                    reti=input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSeleccione una opción: ")
                                                    match reti:
                                                        case '1':
                                                            try:
                                                                palma()
                                                                psind = usuarios.index("Cédula: " + cedula)
                                                                usuarios[psind]
                                                                usuarios[psind + 1]
                                                                usuarios[psind + 2]
                                                                usuarios[psind + 3]
                                                                saldo = float(usuarios[psind + 2])
                                                                

                                                                if saldo > 10:
                                                                    
                                                                    menu_voucher()
                                                                    voucher = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\t Seleccione una opción: ")

                                                                    match voucher:
                                                                        case '1':

                                                                            if saldo >= 10.35:

                                                                            
                                                                                
                                                                                

                                                                                valor = 10

                                                                                
                                                                                retiro = saldo - 10.35
                                                                                retiro=round(retiro,2)
                                                                                usuarios[psind + 2] = str(retiro)
                                                                                
                                                                                impresion_retiro()
                                                                                

                                                                                print(usuarios[psind])
                                                                                print(usuarios[psind + 1])
                                                                                input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                                saveData()

                                                                            else:
                                                                                os.system("cls")
                                                                                print("\t\t\t\t\t\t\t\tSaldo insuficiente para la impresión del voucher")
                                                                                input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")


                                                                            
                                                                        
                                                                        case '2':
                                                                            palma()

                                                                            retiro = saldo - 10
                                                                            retiro=round(retiro,2)
                                                                            usuarios[psind + 2] = str(retiro)
                                                                            
                                                                            input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tOPERACIÓN EXITOSA")
                                                                            input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                            saveData()
                                                                            os.system("cls")
                                                                            
                                                                            
                                                                        case '3':
                                                                            palma()
                                                                            input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla pata continuar")
                                        
                                                                        case _:
                                                                            palma()
                                                                            opcion_v()

                                                                    

                                                                else:
                                                                    palma()
                                                                    input(Fore.RED+"\t\t\t\t\t\t\t\tSaldo insuficiente")
                                                            
                                                            except:
                                                                palma()
                                                                print(Fore.RED+"\t\t\t\t\t\t\t\tFormato inválido")
                                                                input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")


                                                        case '2':
                                                            palma()
                                                            psind = usuarios.index("Cédula: " + cedula)
                                                            usuarios[psind]
                                                            usuarios[psind + 1]
                                                            usuarios[psind + 2]
                                                            usuarios[psind + 3]
                                                            saldo = float(usuarios[psind + 2])
                                                            
                                                            if saldo > 20:
                                                                menu_voucher()
                                                                voucher = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSeleccione una opción: ")

                                                                match voucher:
                                                                    case '1':
                                                                        palma()

                                                                        if saldo >= 20.35:
                                                                            valor = 20
                                                                            retiro = saldo - 20.35
                                                                            retiro=round(retiro,2)
                                                                            usuarios[psind + 2] = str(retiro)
                                                                            impresion_retiro()
                                                                            input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")

                                                                            
                                                                            saveData()

                                                                        else:
                                                                            palma()
                                                                            print(Fore.RED+"\t\t\t\t\t\t\t\tSaldo insuficiente para la impresión del voucher")
                                                                            input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")


                                                                        
                                                                    
                                                                    case '2':
                                                                        palma()

                                                                        retiro = saldo - 20
                                                                        retiro=round(retiro,2)
                                                                        usuarios[psind + 2] = str(retiro)
                                                                        
                                                                        input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tOPERACIÓN EXITOSA")
                                                                        input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                        saveData()
                                                                        os.system("cls")
                                                                        
                                                                    
                                                                    case '3':
                                                                        palma()
                                                                        input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                    case _:
                                                                        palma()
                                                                        opcion_v()
                                                                

                                                            else:
                                                                palma()
                                                                input(Fore.RED+"\t\t\t\t\t\t\t\tSaldo insuficiente")
                                                        

                                                            
                                                        case '3':
                                                            palma()
                                                            psind = usuarios.index("Cédula: " + cedula)
                                                            usuarios[psind]
                                                            usuarios[psind + 1]
                                                            usuarios[psind + 2]
                                                            usuarios[psind + 3]
                                                            saldo = float(usuarios[psind + 2])
                                                            if saldo > 50:
                                                                menu_voucher()
                                                                voucher = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSeleccione una opción: ")

                                                                match voucher:
                                                                    case '1':
                                                                        palma()

                                                                        if saldo >= 50.35:
                                                                            valor = 50
                                                                            retiro = saldo - 50.35
                                                                            retiro=round(retiro,2)
                                                                            usuarios[psind + 2] = str(retiro)
                                                                            impresion_retiro()
                                                                        
                                                                            input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                            saveData()

                                                                        else:
                                                                            palma()
                                                                            print(Fore.RED+"\t\t\t\t\t\t\t\tSaldo insuficiente para la impresión del voucher")
                                                                            input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")


                                                                        
                                                                    
                                                                    case '2':
                                                                        palma()

                                                                        retiro = saldo - 50
                                                                        retiro=round(retiro,2)
                                                                        usuarios[psind + 2] = str(retiro)
                                                                        
                                                                        input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tOPERACIÓN EXITOSA")
                                                                        input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                        saveData()
                                                                        os.system("cls")
                                                                        
                                                                        
                                                                    case '3':
                                                                        palma()
                                                                        input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                        
                                                                    case _:
                                                                        palma()
                                                                        opcion_v()

                                                                

                                                            else:
                                                                palma()
                                                                input(Fore.RED+"\t\t\t\t\t\t\t\tSaldo insuficiente")
                                                        
                                                        
                                                
                                                        case '4':
                                                            palma()
                                                            psind = usuarios.index("Cédula: " + cedula)
                                                            usuarios[psind]
                                                            usuarios[psind + 1]
                                                            usuarios[psind + 2]
                                                            usuarios[psind + 3]
                                                            saldo = float(usuarios[psind + 2])
                                                            if saldo > 100:
                                                                menu_voucher()
                                                                voucher = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSeleccione una opción: ")

                                                                match voucher:
                                                                    case '1':
                                                                        palma()

                                                                        if saldo >= 100.35:

                                                                            valor = 100
                                                                            retiro = saldo - 100.35
                                                                            retiro=round(retiro,2)
                                                                            usuarios[psind + 2] = str(retiro)
                                                                            impresion_retiro()
                                                                    
                                                                            input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                            saveData()

                                                                        else:
                                                                            palma()
                                                                            print(Fore.RED+"\t\t\t\t\t\t\t\tSaldo insuficiente para la impresión del voucher")
                                                                            input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")


                                                                        
                                                                    
                                                                    case '2':
                                                                        palma()

                                                                        retiro = saldo - 100
                                                                        retiro=round(retiro,2)
                                                                        usuarios[psind + 2] = str(retiro)
                                                                        
                                                                        input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tOPERACIÓN EXITOSA")
                                                                        input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                        saveData()
                                                                        os.system("cls")
                                                                        
                                                                        break
                                                                    case '3':
                                                                        palma()
                                                                        input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                        
                                                                    case _:
                                                                        palma()
                                                                        opcion_v()

                                                                

                                                            else:
                                                                palma()
                                                                input(Fore.RED+"\t\t\t\t\t\t\t\tSaldo insuficiente")
                                                        
                                                        
                                                        case '5':
                                                            palma()
                                                            try:
                                                                
                                                                psind = usuarios.index("Cédula: " + cedula)
                                                                usuarios[psind]
                                                                usuarios[psind + 1]
                                                                usuarios[psind + 2]
                                                                usuarios[psind + 3]
                                                                datos=float(input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese la cantidad entera:"))
                                                                if datos< 5 or datos>1000:
                                                                    palma()
                                                                    print(Fore.RED+"\t\t\t\t\t\t\t\tSolo se acepta desde $5 hasta $1000")
                                                                    input(Fore.RED+"\t\t\t\t\t\t\t\t============== || CANTIDAD ERRONEA || ===========")


                                                                else:
                                                                    palma()
                                                                    saldo = float(usuarios[psind + 2])
                                                                

                                                                    if saldo > datos:
                                                                    
                                                                        palma()
                                                                        menu_voucher()
                                                                        voucher = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSeleccione una opción: ")

                                                                        match voucher:
                                                                            case '1':
                                                                                palma()
                                                                                if saldo > (datos+0.35):
                                                                                    
                                                                                    retiro = saldo - datos -0.35
                                                                                    retiro=round(retiro,2)

                                                                                    usuarios[psind + 2] = str(retiro)

                                                                                    impresion_retiro1()


                                                                                    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                                    saveData()
                                                                                else:
                                                                                    palma()
                                                                                    print(Fore.RED+"\t\t\t\t\t\t\t\tSaldo insuficiente para la impresión del voucher")
                                                                                    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                            case '2':
                                                                                palma()
                                                                                retiro = saldo - datos
                                                                                retiro=round(retiro,2)

                                                                                usuarios[psind + 2] = str(retiro)

                                                                                input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tOPERACIÓN EXITOSA")
                                                                                input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                                saveData()
                                                                            case '3':
                                                                                palma()
                                                                                input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                            case _:
                                                                                palma()
                                                                                opcion_v()
                                                                    else:
                                                                        palma()
                                                                        input(Fore.RED+"\t\t\t\t\t\t\t\tSaldo insuficiente")
                                                                
                                                            except:
                                                                palma()
                                                                print(Fore.RED+"\t\t\t\t\t\t\t\tFormato inválido")
                                                                input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                        case '6':
                                                            palma()
                                                            saveData()
                                                            break
                                                        case _:
                                                            palma()
                                                            opcion_v()
                                                            
                                                            
                                            case '2':
                                                while True:
                                                    logo_banco()
                                                    menu_depo()
                                                    reti=input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSeleccione una opcion: ")
                                                    match reti:
                                                        case '1':
                                                            os.system("cls")
                                                            psind = usuarios.index("Cédula: " + cedula)
                                                            usuarios[psind]
                                                            usuarios[psind + 1]
                                                            usuarios[psind + 2]
                                                            usuarios[psind + 3]
                                                            saldo = float(usuarios[psind + 2])
                                                            menu_voucher()
                                                            voucher = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSeleccione una opción: ")

                                                            match voucher:
                                                                case '1':
                                                                    palma()

                                                                    #variable de deposito
                                                                    dep = 10

                                                                    retiro = saldo + dep
                                                                    
                                                                    retiro = retiro-0.35
                                                                    
                                                                    retiro=round(retiro,2)

                                                                    usuarios[psind + 2] = str(retiro)
                                                                    depositos()


                                                                    input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tOPERACIÓN EXITOSA")
                                                                    saveData()
                                                                case '2':
                                                                    palma()
                                                                    #variable de deposito
                                                                    dep = 10

                                                                    
                                                                    retiro = saldo + dep
                                                                    retiro=round(retiro,2)

                                                                    
                                                                    usuarios[psind + 2] = str(retiro)

                                                                    
                                                                    input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tOPERACIÓN EXITOSA")
                                                                    saveData()

                                                                case '3':
                                                                    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                    

                                                                case _:
                                                                    opcion_v()
                                                                
                                                        case '2':
                                                            os.system("cls")
                                                            psind = usuarios.index("Cédula: " + cedula)
                                                            usuarios[psind]
                                                            usuarios[psind + 1]
                                                            usuarios[psind + 2]
                                                            usuarios[psind + 3]
                                                            saldo = float(usuarios[psind + 2])
                                                            menu_voucher()
                                                            voucher = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSeleccione una opción: ")

                                                            match voucher:
                                                                case '1':
                                                                    palma()

                                                                    #variable de deposito
                                                                    dep = 20

                                                                    retiro = saldo + dep
                                                                    
                                                                    retiro = retiro-0.35
                                                                    
                                                                    retiro=round(retiro,2)

                                                                    usuarios[psind + 2] = str(retiro)

                                                                    depositos()
                                                                    input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tOPERACIÓN EXITOSA")
                                                                    saveData()
                                                                case '2':
                                                                    palma()
                                                                    
                                                                    #variable de deposito
                                                                    dep = 20

                                                                    
                                                                    retiro = saldo + dep
                                                                    retiro=round(retiro,2)

                                                                    
                                                                    usuarios[psind + 2] = str(retiro)

                                                                    
                                                                    input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tOPERACIÓN EXITOSA")
                                                                    saveData()
                                                                case '3':
                                                                    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")

                                                                case _:
                                                                    opcion_v()
                                                        case '3':
                                                            os.system("cls")
                                                            psind = usuarios.index("Cédula: " + cedula)
                                                            usuarios[psind]
                                                            usuarios[psind + 1]
                                                            usuarios[psind + 2]
                                                            usuarios[psind + 3]
                                                            saldo = float(usuarios[psind + 2])
                                                            menu_voucher()
                                                            voucher = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSeleccione una opción: ")

                                                            match voucher:
                                                                case '1':
                                                                    palma()

                                                                    #variable de deposito
                                                                    dep = 50

                                                                    retiro = saldo + dep
                                                                    
                                                                    retiro = retiro-0.35
                                                                    
                                                                    retiro=round(retiro,2)

                                                                    usuarios[psind + 2] = str(retiro)
                                                                    depositos()


                                                                    input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tOPERACIÓN EXITOSA")
                                                                    saveData()
                                                                case '2':
                                                                    palma()
                                                                    #variable de deposito
                                                                    dep = 50

                                                                    
                                                                    retiro = saldo + dep
                                                                    retiro=round(retiro,2)

                                                                    
                                                                    usuarios[psind + 2] = str(retiro)

                                                                    
                                                                    input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tOPERACIÓN EXITOSA")
                                                                    saveData()

                                                                case '3':
                                                                    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")

                                                                case _:
                                                                    opcion_v()
                                                        case '4':
                                                            os.system("cls")
                                                            psind = usuarios.index("Cédula: " + cedula)
                                                            usuarios[psind]
                                                            usuarios[psind + 1]
                                                            usuarios[psind + 2]
                                                            usuarios[psind + 3]
                                                            saldo = float(usuarios[psind + 2])
                                                            menu_voucher()
                                                            voucher = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSeleccione una opción: ")

                                                            match voucher:
                                                                case '1':
                                                                    palma()

                                                                    #variable de deposito
                                                                    dep = 100

                                                                    retiro = saldo + dep
                                                                    
                                                                    retiro = retiro-0.35
                                                                    
                                                                    retiro=round(retiro,2)

                                                                    usuarios[psind + 2] = str(retiro)
                                                                    depositos()


                                                                    input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tOPERACIÓN EXITOSA")
                                                                    saveData()
                                                                case '2':
                                                                    palma()
                                                                    #variable de deposito
                                                                    dep = 100

                                                                    
                                                                    retiro = saldo + dep
                                                                    retiro=round(retiro,2)

                                                                    
                                                                    usuarios[psind + 2] = str(retiro)

                                                                    
                                                                    input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tOPERACIÓN EXITOSA")
                                                                    saveData()

                                                                case '3':
                                                                    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")

                                                                case _:
                                                                    opcion_v()
                                                        case '5':
                                                            try:
                                                                palma()
                                                                psind = usuarios.index("Cédula: " + cedula)
                                                                usuarios[psind]
                                                                usuarios[psind + 1]
                                                                usuarios[psind + 2]
                                                                usuarios[psind + 3]
                                                                datos=float(input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese la cantidad entera: "))
                                                                if datos< 5 or datos>1000:
                                                                    palma()
                                                                    print(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSolo se acepta mayores a $5 hasta $1000")
                                                                    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\t============== || CANTIDAD ERRÓNEA || ===========")

                                                                else:
                                                                    palma()
                                                                    saldo = float(usuarios[psind + 2])
                                                                    retiro = saldo + datos   
                                                                    retiro=round(retiro,2)                                             
                                                                    usuarios[psind + 2] = str(retiro)
                                                                    menu_voucher()
                                                                    voucher = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSeleccione una opción: ")
                                                                    match voucher:
                                                                        case '1':
                                                                            palma()
                                                                            if saldo > 0.35:
                                                                                retiro = (saldo + datos)
                                                                                retiro=retiro-0.35
                                                                                retiro=round(retiro,2)

                                                                                usuarios[psind + 2] = str(retiro)
                                                                                depositos_manu()


                                                                                input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                                saveData()
                                                                        case '2':
                                                                            palma
                                                                            retiro = saldo + datos
                                                                            retiro=round(retiro,2)

                                                                            usuarios[psind + 2] = str(retiro)

                                                                            input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tOPERACIÓN EXITOSA")
                                                                            input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                            saveData()
                                                                        case '3':
                                                                        
                                                                            input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                        case _:
                                                                            opcion_v()
                        

                                                                    
                                                            except:
                                                                palma()
                                                                print(Fore.RED+"\t\t\t\t\t\t\t\tFormato inválido")
                                                                input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                            saveData()
                                                        case '6':
                                                            palma()
                                                            saveData()
                                                            break
                                                        case _:
                                            
                                                            opcion_v()
                                                            
                                            case '3':
                                                
                                                repetir=True
                                                while repetir:
                                                    volver()
                                                    op=input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSeleccione una opcion: ")
                                                    match op:
                                                        case '1':
                                        
                                                            transf=True
                                                            while transf:
                                                                palma()
                                                                print(Fore.GREEN+"""
                            \t\t\t                      _____________________________________________________________
                            \t\t\t                      |                     Menú de Transacción                      
                            \t\t\t                      |    Cuenta Destino:                                                
                            \t\t\t                      |    Dinero a Transferir:                                                
                            \t\t\t                      |    Cuenta:                                                
                            \t\t\t                      |    PIN:                                             
                            \t\t\t                      _____________________________________________________________
                        
                        
                        
                        """)
                                                                cedula = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese la cédula para la cuenta que desea realizar el deposito: ")
                                                                if "Cédula: " + cedula in usuarios:
                                                                    psind = usuarios.index("Cédula: " + cedula)
                                                                    datos = []
                                                                    datos.append(usuarios[psind])
                                                                    datos.append(usuarios[psind + 1])
                                                                    datos.append(usuarios[psind + 2])
                                                                    datos.append(usuarios[psind + 3])
                                                                    
                                                                        
                                                                    os.system("cls")
                                                                    usuarios[psind]
                                                                    usuarios[psind + 1]
                                                                    usuarios[psind + 2]
                                                                    usuarios[psind + 3]
                                                                    compro=True
                                                                    while compro:
                                                                        palma()
                                                                        try:
                                                                            palma()
                                                                            print(Fore.GREEN+f"""
                            \t\t\t                      _____________________________________________________________
                            \t\t\t                      |                     Menú de Transacción                      
                            \t\t\t                      |    Cuenta Destino: {cedula}                                               
                            \t\t\t                      |    Dinero a Transferir:                                                
                            \t\t\t                      |    Cuenta:                                                
                            \t\t\t                      |    PIN:                                             
                            \t\t\t                      _____________________________________________________________
                        
                        
                        
                        """)                                                      
                                                                            dato=float(input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese la cantidad que desea transferir: "))
                                                                            compro=False
                                                                        except:
                                                                            palma()
                                                                            print(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tDebe ingresar una cantidad")
                                                                            input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                        


                                                                    
                                                                    if dato< 5 or dato>1000:
                                                                        palma()
                                                                        print(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tCantidad errónea tiene que ser mayor de $5 y menor a $1000")
                                                                        input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                        compro=True
                                                                        

                                                                    else:
                                                                        palma()
                                                                        saldo = float(usuarios[psind + 2])
                                                                        retiro = saldo + dato
                                                                        retiro=round(retiro,2)
                                                                        usuarios[psind + 2] = str(retiro)
                                                                        
                                                                        while True:
                                                                            palma()
                                                                            print(Fore.GREEN+f"""
                            \t\t\t                      _____________________________________________________________
                            \t\t\t                      |                     Menú de Transacción                      
                            \t\t\t                      |    Cuenta Destino(Cédula): {cedula}                                               
                            \t\t\t                      |    Dinero a Transferir:${dato}                                                
                            \t\t\t                      |    Cédula:                                                
                            \t\t\t                      |    PIN:                                             
                            \t\t\t                      _____________________________________________________________
                        
                        
                        
                        """)
                                                                            cedula = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese su cédula para confirmar: ")
                                                                            if "Cédula: " + cedula in usuarios:
                                                                                psind = usuarios.index("Cédula: " + cedula)
                                                                                datos = []
                                                                                datos.append(usuarios[psind])
                                                                                datos.append(usuarios[psind + 1])
                                                                                datos.append(usuarios[psind + 2])
                                                                                datos.append(usuarios[psind + 3])
                                                                                palma()
                                                                                print(Fore.GREEN+f"""
                            \t\t\t                      _____________________________________________________________
                            \t\t\t                      |                     Menú de Transacción                      
                            \t\t\t                      |    Cuenta Destino(Cédula) {cedula}                                               
                            \t\t\t                      |    Dinero a Transferir:${dato}                                                
                            \t\t\t                      |    Cédula:{cedula}                                                
                            \t\t\t                      |    PIN:                                             
                            \t\t\t                      _____________________________________________________________
                        
                        
                        
                        """)
                                                                                texto = getpass(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese el PIN: ", "*")
                                                                                if datos[3] == texto:
                                                                                    palma()
                                                                                    usuarios[psind]
                                                                                    usuarios[psind + 1]
                                                                                    usuarios[psind + 2]
                                                                                    usuarios[psind + 3]

                                                                                    saldo = float(usuarios[psind + 2])
                                                                                    if saldo > dato:

                                                                                        
                                                                                        retiro =  saldo-dato 
                                                                                        retiro=round(retiro,2)                                               
                                                                                        usuarios[psind + 2] = str(retiro)
                                                                                        os.system("cls")
                                                                                        print(Fore.GREEN+f"""
                            \t\t\t                      _____________________________________________________________
                            \t\t\t                      |                     Menú de Transacción                      
                            \t\t\t                      |    Cuenta Destino(Cédula): {cedula}                                               
                            \t\t\t                      |    Dinero a Transferir:${dato}                                                
                            \t\t\t                      |    Cédula:{cedula}                                                
                            \t\t\t                      |    PIN:{'*' * len(texto)}                                             
                            \t\t\t                      _____________________________________________________________
                        
                        
                        
                        """)
                                                                                        print(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tTransferencia Exitosa")
                                                                                        input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                                        compro=False
                                                                                        transf=False
                                                                                        repetir=False
                                                                                        menu_edit =True
                                                                                        saveData()
                                                                                        break
                                                                                    
                                                                                    else:
                                                                                        print(Fore.RED+"\t\t\t\t\t\t\t\tNo tiene suficiente dinero o fondos")
                                                                                        input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                                        compro=True
                                                                                        break
                                                                                else:
                                                                                    palma()
                                                                                    print(Fore.LIGHTGREEN_EX+"""
                                                                                    _________________________________
                                                                                    |       Contraseña Incorrecta     |
                                                                                    |_________________________________|""")
                                                                                    input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tPresione Enter para volver ")
                                                                                
                                                                                
                                                                                
                                                                            else:
                                                                                palma()
                                                                                print(Fore.LIGHTGREEN_EX+"""
                                                                                    _________________________________
                                                                                    |       Usuario Incorrecto        |
                                                                                    |_________________________________|""")
                                                                                input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tPresione Enter para volver ")
                                                                                
                                                                else:
                                                                    palma()
                                                                    user_not_found()
                                                                    saveData()
                                                        case '2':
                                                            break
                                                        case _:
                                                            input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngreso una opcion no valida")
                                            case '4':
                                                texto = getpass(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese su PIN: ", "*")    
                                                if  datos[3] == texto:
                                                    pin= getpass(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese su nuevo PIN: ", "*")
                                                    if not len(pin) == 4 or not pin.isdigit():
                                                        palma()
                                                        print (Fore.RED+"\t\t\t\t\t\t\t\tError de PIN: Ingrese solamente 4 Números")
                                                        input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione Enter para continuar")
                                                    else:
                                                        usuarios[psind + 3] = str(pin)
                                                        input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tGuardado Exitoso")
                                                        saveData()
                                                        print(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tContraseña Actualizada. Vuelva a Ingresar Nuevamente Porfavor")
                                                        input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione Enter para Continuar")
                                                        break

                                                else:
                                                    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPIN Incorrecto")                                              

                                                

                                                        
                                            case '5':
                                                menuu=False
                                                inicio=True
                                                break

                                            case _:
                                                palma()
                                                opcion_v()
                                                
                                                

                            
                                else:
                                        intentos += 1
                                        palma()
                                        print(Fore.RED+f"""
                                _______________________________________________________________________________
                                |       Contraseña Incorrecta    Intentos:{intentos}                            |
                                |_______________________________________________________________________________|
                                        """)
                                        if intentos == 3:
                                            palma()
                                            print(Fore.RED+f"""
                                _______________________________________________________________________________
                                |       Contraseña Incorrecta    Intentos:{intentos}                            |
                                |       Se Volverá Al Menú Principal                                            |
                                |_______________________________________________________________________________|
                                        """)

                                            codigo_val = False
                                            intentos = 0
                                            inicio = True
                                        os.system("pause")

                        else:
                            user_not_found()
                    except:
                       opcion_v()
                       cedula_val = True
                
            case '2':

                progress_bar()
                loadData()
                menu = True
                while menu:
                    try:
                        logo_banco()
                        admin = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\t Ingrese el usuario:  \n\t\t\t\t\t\t\t\t ")
                        if check_user(admin):
                            menu = False
                            menu_contraseña = True
                            while menu_contraseña:
                                logo_banco()
                                passw = getpass(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\t Ingrese contraseña:  \n\t\t\t\t\t\t\t\t ", "*")
                                if passw == "":
                                    input (Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese algún Valor Porfavor... Espere y Vuelva a Ingresar")
                                    
                                    continue
                                if check_password(passw,intentos):
                                        menu_contraseña = False
                                        menu_opciones_alumnos = True
                                        while menu_opciones_alumnos:
                                                    palma()
                                                    menu_crud()
                                                    op = input(str(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSeleccione una opción: "))
                                                    match op:
                                                        case '1':
                                                            menu = False
                                                            menu_add_user = True
                                                            while menu_add_user:
                                                                palma()
                                                                print(Fore.GREEN+"""
                \t\t\t                      _____________________________________________________________
                \t\t\t                      |                     Menú de Creación                      
                \t\t\t                      |    Cédula:                                                
                \t\t\t                      |    Nombre:                                                
                \t\t\t                      |    Dinero:                                                
                \t\t\t                      |    PIN:                                             
                \t\t\t                      _____________________________________________________________
            
            
            
            """)
                                                                
                                                                cedula = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese la Cédula de Identidad: ")
                                                                if validar_cedula(cedula):
                                                                    palma()
                                                                    print(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tCédula Ecuatoriana Detectada")
                                                                    os.system("pause")
                                                                elif len(cedula) != 10 and not cedula.isdigit():
                                                                    palma()
                                                                    print(Fore.RED+"\t\t\t\t\t\t\t\tError de Cédula: Ingrese Solamente 10 Caractéres Máximo y Números")
                                                                    os.system("pause")
                                                                    break
                                                                elif not cedula.isdigit():
                                                                    palma()
                                                                    print(Fore.RED+"\t\t\t\t\t\t\t\tError de Cédula: Solo Se Aceptan Números")
                                                                    os.system("pause")
                                                                    break
                                                                else:
                                                                    palma()
                                                                    print(Fore.RED+"\t\t\t\t\t\t\t\tError de Cédula: Cédula Ecuatoriana No Detectada")
                                                                    os.system("pause")
                                                                    menu_edit = False
                                                                    me2u = True
                                                                    break
                                                                palma()
                                                                print(Fore.GREEN+f"""
                \t\t\t                      _____________________________________________________________
                \t\t\t                      |                     Menú de Creación                      
                \t\t\t                      |    Cédula:{cedula}                                                
                \t\t\t                      |    Nombre:                                                
                \t\t\t                      |    Dinero:                                                
                \t\t\t                      |    PIN:                                             
                \t\t\t                      _____________________________________________________________
            
            
            
            """)
                                                                nombre = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese su Nombre y Apellido: ")
                                                                palma()
                                                                print(Fore.GREEN+f"""
                \t\t\t                      _____________________________________________________________
                \t\t\t                      |                     Menú de Creación                      
                \t\t\t                      |    Cédula:{cedula}                                        
                \t\t\t                      |    Nombre:{nombre}                                        
                \t\t\t                      |    Dinero:                                                
                \t\t\t                      |    PIN:                                             
                \t\t\t                      _____________________________________________________________
            
            
            
            """)
                                                                
                                                                try:
                                                                    monto=float(input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese la cantidad entera: "))
                                                                    if monto >=5 and monto <=5000:
                                                                        
                                                                        palma()
                                                                        print(Fore.GREEN+f"""
                        \t\t\t                      _____________________________________________________________
                        \t\t\t                      |                     Menú de Creación                      
                        \t\t\t                      |    Cédula:{cedula}                                        
                        \t\t\t                      |    Nombre:{nombre}                                        
                        \t\t\t                      |    Dinero:{monto}                                         
                        \t\t\t                      |    PIN:                                             
                        \t\t\t                      _____________________________________________________________
                    
                    
                    
                    """)
                                                                    else:
                                                                        menu_add_user = True
                                                                        input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngreso una cantida erronea")
                                                                        input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tDebe ser mayor a 4 y menor que 5001 ")
                                                                        break
                                                                except:
                                                                    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tFormato invalido")
                                                                    menu_add_user = True
                                                                    break        

                                                                pin= input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese su PIN: ")
                                                                palma()
                                                                print(Fore.GREEN+f"""
                \t\t\t                      _____________________________________________________________
                \t\t\t                      |                     Menú de Creación                      
                \t\t\t                      |    Cédula:{cedula}                                        
                \t\t\t                      |    Nombre:{nombre}                                        
                \t\t\t                      |    Dinero: {monto}                                        
                \t\t\t                      |    PIN:{pin}  
                \t\t\t                      _____________________________________________________________
            
            
            
            """)
                                                                input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                if not nombre.replace(" ","").isalpha():
                                                                    palma()
                                                                    print(Fore.RED+"\t\t\t\t\t\t\t\tError de Nombre: Ingrese solamente letras.")
                                                                    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                if not len(pin) == 4 or not pin.isdigit():
                                                                    palma()
                                                                    print (Fore.RED+"\t\t\t\t\t\t\t\tError de PIN: Ingrese solamente 4 Números")
                                                                    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                if len(cedula) != 10:
                                                                    palma()
                                                                    print(Fore.RED+"\t\t\t\t\t\t\t\tError de Cédula: Ingrese Solamente Números y 10 caractéres Máximo")
                                                                    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                if "Cédula: " + cedula in usuarios:
                                                                    palma()
                                                                    print(Fore.RED+"\t\t\t\t\t\t\t\tError de Cédula: Ese número de cédula ya esta registrado!")
                                                                    input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                else:
                                                                    if cedula.isdigit() and nombre.replace(" ","").isalpha() and len(pin) == 4 and pin.isdigit():
                                                                        monto = str(round(float(monto), 2))
                                                                        usuarios.append("Cédula: " + cedula)
                                                                        usuarios.append(nombre)
                                                                        usuarios.append(monto)
                                                                        usuarios.append(pin)
                                                                        saveData()
                                                                        menu_add_user = False
                                                                        menu = True
                                                                
                                                        case '2':
                                                    
                                                            list()
                                                            
                                                        case '3':
                                                            palma()
                                                            cedula = input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese la Cédula a editar: ")
                                                            if "Cédula: " + cedula in usuarios:
                                                                psind = usuarios.index("Cédula: " + cedula)
                                                                usuarios[psind]
                                                                usuarios[psind + 1]
                                                                usuarios[psind + 2]
                                                                usuarios[psind + 3]
                                                                menu = False
                                                                menu_edit = True
                                                                while menu_edit:
                                                                    palma()
                                                                    print(Fore.GREEN+"""
                                                                _____________________________
                                                                                        
                                                                    Menú Editar Datos      
                                                                                        
                                                                    1.Nombres              
                                                                    2.Monto
                                                                    3.Salir     
                                                                ___________________________
                                                                    
                                                                    """)
                                                                    op_edit = input(str(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSeleccione una opción: "))
                                                                    match op_edit:
                                                                        case '1':
                                                                            dato= str(input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese el nuevo nombre: "))
                        
                                                                            if not dato.replace(" ","").isalpha():
                                                                                palma()
                                                                                print(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tError de Nombre: Ingrese solamente letras.")
                                                                                os.system("pause")
                                                                            else:
                                                                                usuarios[psind + 1] = dato
                                                                                saveData()
                                                                                input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tGuardado Exitoso")
                                                                        case '2':
                                                                            monto= str(input(Fore.RED+"\t\t\t\t\t\t\t\tIngrese el Nuevo Monto: "))                                                                       
                                                                            if not (monto.isdigit() or re.match(r'^\d+(\.\d+)?$', monto)):
                                                                                print(Fore.RED+"\t\t\t\t\t\t\t\tIngrese correctamente el valor")
                                                                                input(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tPresione una tecla para continuar")
                                                                            else:
                                                                                monto = str(round(float(monto), 2))                                                                     
                                                                                usuarios[psind + 2] = monto
                                                                                saveData()
                                                                                input(Fore.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tGuardado Exitoso")
                                                                        case '3':
                                                                            palma()
                                                                            menu_edit = False
                                                                            me2u = True
                                                                            break
                                                                        case _:
                                                                            palma()
                                                                            opcion_v()
                                                            else:
                                                                palma()
                                                                user_not_found()
                                                                os.system("pause") 
                                                            os.system("cls")

                                                        case'4': 
                                                            palma()
                                                            eliminar()  
                                                        case '5':
                                                            os.system("cls")
                                                            palma()
                                                            str_codigo = input(str(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tIngrese el número de cédula que desea consultar: "))
                                                            if "Cédula: " + str_codigo in usuarios:
                                                            
                                                                user_list(str_codigo)
                                                            else:
                                                                os.system("cls")
                                                                print("Usuario no Registrado!")
                                                                os.system("pause")
                                                        case '6':
                                                            palma()
                                                            print (Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tSE ABANDONARÁ EL SISTEMA. GRACIAS POR PREFEFIRNOS")
                                                            menu=False
                                                            inicio=True
                                                            break

                                                        case _:
                                                            opcion_v()                              
                                else:
                                        intentos += 1
                                        palma()
                                        print(Fore.RED+f"""
                                _______________________________________________________________________________
                                |       Contraseña Incorrecta    Intentos:{intentos}                            |
                                |_______________________________________________________________________________|
                                        """)
                                        if intentos == 3:
                                            palma()
                                            print(Fore.RED+f"""
                                _______________________________________________________________________________
                                |       Contraseña Incorrecta    Intentos:{intentos}                            |
                                |                                                                               |
                                |_______________________________________________________________________________|
                                        """)

                                            menu_contraseña = False
                                            intentos = 0
                                            inicio = True
                                        os.system("pause")
                            else:
                                os.system("pause")
                    except:
                        opcion_v()
                        menu = True
            case "?":
                manual = True
                while manual:
                    try:
                        palma()
                        print(Fore.BLACK +
                        """
                            \t                  _____________________________________________________________________________
                            \t 
                            \t 
                            \t                                        || M || || E || N || Ú || 
                            \t 
                            \t 
                            \t                                                                 
                            \t                                        1. - Manual Usuario
                            \t                                        2. - Manual Administrador
                            \t                                        3. - Salir
                            \t
                            \t                                                                                                                                                                                                                                                                                                                                                                    
                            \t                  _____________________________________________________________________________
                        """)
                        op = input("Seleccione una opción: ")

                        match op:
                            case "1":
                                manual_usuario()
                                  
                            case "2":
                                manual_admin()
                            
                            case "3":
                                break
                            case _:
                                opcion_v()
                    except:
                        opcion_v()


            case '3':
                logo_salir()
                break
            case _:
                opcion_v()
                
    except:
        opcion_v()
        inicio=True