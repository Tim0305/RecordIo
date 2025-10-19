from core.games.memory.memory import MemoryGame

class MemoryScene():
    def __init__(self, player, width, height):
        self.game = MemoryGame(width, height)
        self.game.start()

        while True:
            if player.get_life() == 0:
                print("Game Over")
                break
            elif self.game.is_over():
                print("You won!!!")
                break
            else:
                self.game.print_board()
                x1 = int(input("X1: "))
                y1 = int(input("Y1: "))
                x2 = int(input("X2: "))
                y2 = int(input("Y2: "))

                if self.game.play(x1, y1, x2, y2):
                    print("Bien")
                else:
                    player.decrement_life()
                    print("Life: " + str(player.get_life()))
