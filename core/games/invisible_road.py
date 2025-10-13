import random

class InvisibleRoadGame():
    def __init__(self, width = 3, height = 3):
        self.width = width
        self.height = height
        self.__board = []
        self.__road = []
        self.__current_position = 0
        self.__fails = 0

    def start(self):
        # Reset variables
        self.__board = []
        self.__road = []
        self.__current_position = 0
        self.__fails = 0

        # Create the board
        for _ in range(self.height):
            self.__board.append([0] * self.width)
        
        self.__init_road()
        print(self.__road)
        self.print_board()

    def __init_road(self):
        # Create the road randomly
        # 0 -> up, 1 -> right; 2 -> down (never left)
        
        # Set the initial position
        x = 0
        y = random.randint(0, self.height - 1)
        position = (x, y)
        self.__road.append(tuple(position))
        self.__board[y][x] = 1

        while(x < self.width - 1):
            move = random.randint(0, 2)

            if move == 0:
                # Move up
                if y == 0:
                    y = 0
                else:
                    y -= 1
            elif move == 1:
                # Move right
                x += 1
            else:
                # Move down
                if y == self.height - 1:
                    y = self.height - 1
                else:
                    y += 1

            position = (x, y)
            if (position not in self.__road):
                self.__road.append(position)
                self.__board[y][x] = 1
            else:
                # Reset the position
                x = self.__road[-1][0]
                y = self.__road[-1][1]

    def print_board(self):
        for i in range(self.height):
            print(self.__board[i])

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height 
    
    def play(self, position):
        if (position == self.__road[self.__current_position]):
            self.__current_position += 1
            return True
        else:
            self.__fails += 1
            return False
    
    def is_over(self):
        return self.__current_position == len(self.__road)
    
    def get_failed_attempts(self):
        return self.__fails
