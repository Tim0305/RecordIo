# Clase que representa a un jugador, con registro de vidas, victorias y fallos.
class Player():
    '''
    Nombre: __init__
    Parámetros: wins (int, opcional), fails (int, opcional)
    Descripción: Inicializa las estadísticas del jugador con valores predeterminados o dados.
    '''
    def __init__(self, wins: int = 0, fails: int = 0) -> None:
        self.__wins = wins
        self.__fails = fails
        self.__life = 3  # Vida inicial del jugador

    '''
    Nombre: decrement_life
    Descripción: Resta una vida al jugador.
    '''
    def decrement_life(self) -> None:
        self.__life -= 1

    '''
    Nombre: reset
    Descripción: Restablece la vida del jugador a su valor inicial.
    '''
    def reset(self) -> None:
        self.__life = 3

    '''
    Nombre: get_life
    Descripción: Retorna la cantidad actual de vidas del jugador.
    '''
    def get_life(self) -> int:
        return self.__life
    
    '''
    Nombre: increment_wins
    Descripción: Incrementa en uno el número de victorias del jugador.
    '''
    def increment_wins(self) -> None:
        self.__wins += 1

    '''
    Nombre: increment_fails
    Descripción: Aumenta en uno el número de partidas perdidas del jugador.
    '''
    def increment_fails(self) -> None:
        self.__fails += 1

    '''
    Nombre: get_wins
    Descripción: Retorna el número total de victorias acumuladas.
    '''
    def get_wins(self) -> int:
        return self.__wins

    '''
    Nombre: get_fails
    Descripción: Retorna el número total de partidas perdidas acumuladas.
    '''
    def get_fails(self) -> int:
        return self.__fails
