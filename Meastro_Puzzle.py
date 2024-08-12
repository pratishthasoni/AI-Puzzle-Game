import collections
import os
import glob

class Meastro:
    def __init__(self, folder_path):
        """
        Initializes the Meastro class with the folder path.
        """
        self.folder_path = folder_path

    def read_input_files(self):
        """
        Processes all .txt files in the folder to count puzzle of ones.
        """
        input_text_files = glob.glob(os.path.join(self.folder_path, '*.txt')) 
        print(input_text_files)

        for input_file in input_text_files:
            file_name = os.path.basename(input_file)
            print(f"Processing file: {file_name}")

            with open(input_file, 'r') as file:
                input_grid_text = file.readlines()
                grid = [list(line.strip()) for line in input_grid_text]

                if not grid:
                    print(0)
                    continue

                num_of_connected_shapes = self.get_count_connected_shapes(grid)
                print(num_of_connected_shapes)

    def get_count_connected_shapes(self, grid):
        """
        Counts the number of puzzle of 1 in the given grid.
        """
        rows, cols = len(grid), len(grid[0])             #length of the grid
        visited_cells = set()                            #declaring set to mark the visited 1's in the puzzle
        total_count_shapes = 0                           #initializing the total count of 1's with 0

        def bfs(row_, cell_):                                   #using breadth first search approach
            data_queue = collections.deque()                      #using queue data structure to store the values in the memory
            visited_cells.add((row_, cell_))
            data_queue.append((row_, cell_))    
            while data_queue:                                     #expanding and checking the puzzle
                row, col = data_queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]                 #checking all the adjacent locations (right,left,top,below)
                for direct_row, direct_col in directions:               
                    n_row, n_col = row + direct_row, col + direct_col
                    if (n_row in range(rows) and n_col in range(cols) and             #the coordinates should be in the range of rows & cols and if it is 1 and is already not visited.
                        grid[n_row][n_col] == '1' and (n_row, n_col) not in visited_cells):
                        data_queue.append((n_row, n_col))                                      #doing the bfs on that particular coordinate as well
                        visited_cells.add((n_row, n_col))                               #adding the values in set so we dont iterate through them once again

        for row_ in range(rows):                           #iterating through rows and columns
            for cell_ in range(cols):
                if grid[row_][cell_] == '1' and (row_, cell_) not in visited_cells:  #checking if the value is 1 and making sure we are not going through the same coordinates
                    bfs(row_, cell_)                                          #calling the bfs approach 
                    total_count_shapes += 1

        return total_count_shapes


folder_path = ''            #empty path so that it searches in current directory
puzzle_counter = Meastro(folder_path)
puzzle_counter.read_input_files()
