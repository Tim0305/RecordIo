from core.games.invisible_road import InvisibleRoadGame

class InvisibleRoadScene:
    def __init__(self, player, width, height):
        self.game = InvisibleRoadGame(width, height)
        self.game.start()

        while True:
            if player.life == 0:
                print("Game Over")
                break
            elif self.game.is_over():
                print(self.game.get_failed_attempts())
                if self.game.get_failed_attempts() > 0:

                    print("Game Over")
                else:
                    print("You won!!!")
                break
            else:
                x = int(input("X: "))
                y = int(input("Y: "))

                if self.game.play((x, y)):
                    print("Bien")
                else:
                    player.decrement_life()
                    print("Life: " + str(player.life))
