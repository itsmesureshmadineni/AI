
class Puzzle:

    def __init__(self, board, parent, id, depth):

        # Setup puzzle.
        self.board = board
        self.parent = parent
        self.id = id
        self.depth = depth

    def __lt__(self, puzzle):

        # Comparator for two puzzles.
        return self.id < puzzle.id

class EightPuzzle:

    def __init__(self, start, goal):

        # Setup the class.
        self.start = start
        self.goal = goal
        self.movements = [(-1, 0),(1, 0),(0, -1),(0, 1)]

    def is_goal(self, config):

        # Check if the given puzzle is same as goal.
        for i in range(3):
            for j in range(3):
                if self.goal[i][j] != config[i][j]:
                    return False

        return True

    def look_for_blank(self, config):

        # Look for the blank symbol in the puzzle.
        for i in range(3):

            for j in range(3):

                if config[i][j] == 0:

                    return (i, j)

    def show_puzzle(self, config):

        # Show the puzzle in the output.

        for i in range(3):
            for j in range(3):
                print(config[i][j], end = ' ')
            print('')


    def show_path(self, config, algorithm='BFS'):

        puzzle = []

        while config != None:

            puzzle.append(config)

            config = config.parent

        i = len(puzzle) - 1

        print('Steps taken for %s algorithm are as follows (%d steps):' % (algorithm, len(puzzle) - 1))
        while i >= 0:

            self.show_puzzle(puzzle[i].board)
            print('')

            i = i - 1


    def breadth_first_search(self):

        # BFS implementation of the 8-puzzle.

        # Puzzle count.
        puzzle_count = 0

        # Create parent puzzle.
        parent = Puzzle(self.start, None, puzzle_count, 0)

        # setup queue.
        queue = [parent]

        while len(queue) > 0:

            # get element from queue.
            top = queue.pop()

            # Get the depth.
            new_depth = top.depth + 1

            # get the board.
            board = top.board

            # find blank.
            blank = self.look_for_blank(board)

            for i in range(4):

                p = blank[0]
                q = blank[1]
                r = p + self.movements[i][0]
                s = q + self.movements[i][1]

                # If the indicies are valid.
                if (r < 3 and r >= 0) and (s >= 0 and s < 3):

                    # get the new board.
                    new_board = [[cell for cell in row] for row in board]

                    # swap the blank with the new element.
                    new_board[p][q], new_board[r][s] = new_board[r][s], new_board[p][q]

                    # increment puzzle count.
                    puzzle_count = puzzle_count + 1

                    # create child puzzle.
                    child = Puzzle(new_board, top, puzzle_count, new_depth)

                    if self.is_goal(new_board):

                        # Show the path to the goal.
                        self.show_path(child, algorithm='BFS')

                        # clear the contents of the queue.
                        queue.clear()
                        break

                    # add the child in the queue.
                    queue.insert(0, child)



# initial configuration.
initial = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

goal = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

# the goal configuration
goal = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

# initialize.
solver = EightPuzzle(initial, goal)

# run algorithms.
solver.breadth_first_search()

