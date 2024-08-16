from sudoku_generator import SudokuGenerator


class SudokuRunner:

    def __init__(self):
        self.possible_sizes = [3, 4, 9, 16]

        self.possible_chars = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,
                               'A', 'B', 'C', 'D', 'E', 'F',
                               'G', 'H']
    
    def run_game(self):
        print("Size of the puzzle is the length of one row. Default size is 9.")
        print("Possible sizes: 3, 4, 9, 16")
        char_size = input("Enter the desired size of the puzzle: ")

        try:
            char_size = int(char_size)

        except:
            char_size = 9

        if char_size not in self.possible_sizes:
            char_size = 9

        print("Puzzle size will be " + str(char_size))

        print("Difficulty of the puzzle ranges from 1-5, where 1 is the easiest and 5 is the most difficult. Default difficulty is 3")
        difficulty = input("Enter the desired difficulty of the puzzle: ")

        try:
            difficulty = int(difficulty)
        
        except:
            difficulty = 3
        
        if difficulty < 1:
            difficulty = 1

        if difficulty > 5:
            difficulty = 5

        print("Puzzle difficulty will be " + str(difficulty))

        chars = self.possible_chars[0: char_size]

        generator = SudokuGenerator(chars, difficulty)

        puzzles = generator.generate_puzzle()

        unsolved_puzzle = puzzles[0]
        solution = puzzles[1]

        generator.print_puzzle(unsolved_puzzle)


r = SudokuRunner()
r.run_game()