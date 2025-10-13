from core.games.keywords import KeywordsGame

class KeywordsScene():
    def __init__(self, player, length, n):
        self.game = KeywordsGame(length, n)
        self.game.start()

        while True:
            if player.life == 0:
                print("Game Over")
                break
            elif self.game.is_over():
                if self.game.get_failed_attempts() > 0:
                    print("Game Over")
                else:
                    print("You won!!!")
                break
            else:
                print(self.game.get_current_keyword())
                key = input("")
                if self.game.play(key):
                    print("Bien")
                else:
                    player.decrement_life()
                    print("Life: " + str(player.life))
