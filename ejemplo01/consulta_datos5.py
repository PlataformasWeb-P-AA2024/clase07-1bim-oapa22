from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

registros = session.query(Club, Jugador).join(Jugador).\
         filter(Jugador.nombre.like("%Da%")).all()
 
print("Consulta 2 ")
# print(registros)
"""

Consulta 2 

Club: nombre=Barcelona deporte=Fútbol fundación=1920
Jugador: Damian Diaz - dorsal:10 - posición: mediocampo


Club: nombre=Barcelona deporte=Fútbol fundación=1920
Jugador: Dario Aymar - dorsal:2 - posición: defensa
"""
for registro in registros: 
#     # el registro continen 
#     # dos valores en un tupla
#     # posición 0 el club
#     # posición 1 el jugador 
#     # que cumplen con la condición
    club = registro[0] #objeto de tipo Club
    jugador = registro[1] #objeto de tipo Jugador
    print(club.nombre) # El club
    print(jugador.nombre) # El jugador
    print("------------------")


















