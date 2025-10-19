from core.games.numbers.sequential_numbers import SequentialNumbersGame


class SequentialNumbersScene():
    def __init__(self, player, width, height, numbers):
        self.game = SequentialNumbersGame(width, height, numbers)
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
                x = int(input("X: "))
                y = int(input("Y: "))

                if self.game.play(x, y):
                    print("Bien")
                else:
                    player.decrement_life()
                    print("Life: " + str(player.life))
