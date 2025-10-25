# Importar la clase Player para manejar los datos del jugador
from player.player import Player


'''
Nombre: write_game_data
Parámetros: player (Player)
Descripción: Escribe los datos del jugador en un archivo de texto llamado "data.txt".
Guarda el número total de partidas jugadas, las ganadas y las perdidas. 
Si el archivo ya existe, su contenido se sobrescribe con la información más reciente del jugador.
'''
def write_game_data(player: Player) -> None:
    # Abrir el archivo en modo escritura (si no existe, lo crea)
    with open("data.txt", "w") as f:
        # Escribir la información
        f.write(f"Total Games: {player.get_wins() + player.get_fails()}\n")
        f.write(f"Wins: {player.get_wins()}\n")
        f.write(f"Fails: {player.get_fails()}\n")


'''
Nombre: get_game_data
Descripción: Lee los datos guardados en el archivo "data.txt" y devuelve un diccionario con las estadísticas del jugador.
Si el archivo no existe u ocurre un error durante la lectura, se devuelven valores por defecto en cero. 
El diccionario contiene las claves "total_games", "wins" y "fails" con los valores correspondientes a las partidas jugadas, ganadas y perdidas.
'''
def get_game_data() -> dict[str, int]:
    data = {"total_games": 0, "wins": 0, "fails": 0}  # Valores por defecto

    # Detectar errores
    try:
        # Abrir el archivo en modo lectura
        with open("data.txt", "r") as f:
            # Obtener la información (separada por ":"})
            data["total_games"] = int(f.readline().split(":")[1])
            data["wins"] = int(f.readline().split(":")[1])
            data["fails"] = int(f.readline().split(":")[1])
    except FileNotFoundError:
        print("Archivo 'data.txt' no encontrado. Se usarán valores por defecto.")
    except Exception as e:
        print(f"Error leyendo el archivo: {e}")

    return data
