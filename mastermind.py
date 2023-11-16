import random

class MastermindGame:
    def __init__(self):
        self.num_color = random.randint(1,8)
        self.num_position = random.randint(1, 10)
        self.generate_puzzle()

    def generate_puzzle(self):
        color_option = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'][:self.num_color]
        self.puzzle = random.sample(color_option * self.num_position, self.num_position)
        self.puzzle_clue = ['*'] * self.num_position


    def provide(self, guess):
        clue = []
        for i in range(len(self.puzzle)):
            if guess[i] == self.puzzle[i]:
                clue.append('*')
            elif guess[i] in self.puzzle:
                clue.append('o')
            else:
                clue.append(' ')
        return clue


game = MastermindGame()
print(f'Playing Mastermind with {game.num_color} colors and {game.num_position} positions')
attempt = 0

while True:
    user_guess = input('What is your guess: ')
    game.puzzle_clue = game.provide(user_guess)
    if game.puzzle_clue == game.puzzle:
        print("Congratulation! You've won")
        break
    print(f'Your guess is {user_guess}')


    print("Clue: ", *game.puzzle_clue, sep='')
    attempt += 1

print(f'You solve it after {attempt} rounds')


