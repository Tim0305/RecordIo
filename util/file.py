from player.player import Player


def write_game_data(player: Player) -> None:
    with open("data.txt", "w") as f:
        f.write(f"Total Games: {player.get_wins() + player.get_fails()}\n")
        f.write(f"Wins: {player.get_wins()}\n")
        f.write(f"Fails: {player.get_fails()}\n")


def get_game_data() -> dict[str, int]:
    data = {"total_games": 0, "wins": 0, "fails": 0}  # valores por defecto
    try:
        with open("data.txt", "r") as f:
            data["total_games"] = int(f.readline().split(":")[1])
            data["wins"] = int(f.readline().split(":")[1])
            data["fails"] = int(f.readline().split(":")[1])
    except FileNotFoundError:
        print("Archivo 'data.txt' no encontrado. Se usarán valores por defecto")
    except Exception as e:
        print(f"Error leyendo el archivo: {e}")

    return data
