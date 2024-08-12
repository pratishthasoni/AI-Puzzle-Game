import collections
import os
import glob

class Meastro:
    def __init__(self, folder_path):
        """
        Initializes the Meastro class with the folder path.
        """
        self.folder_path = folder_path

    def process_files(self):
        """
        Processes all .txt files in the folder to count puzzle of ones.
        """
        txt_files = glob.glob(os.path.join(self.folder_path, '*.txt')) 

        for txt_file in txt_files:
            file_name = os.path.basename(txt_file)
            print(f"Processing file: {file_name}")

            with open(txt_file, 'r') as file:
                grid_text = file.readlines()
                grid = [list(line.strip()) for line in grid_text]

                if not grid:
                    print(0)
                    continue

                num_of_connected_shapes = self.count_connected_shapes(grid)
                print(num_of_connected_shapes)

    def count_connected_shapes(self, grid):
        """
        Counts the number of puzzle of 1 in the given grid.
        """
        rows, cols = len(grid), len(grid[0])            #length of the grid
        visited_ones = set()                            #declaring set to mark the visited 1's in the puzzle
        puzzle_count = 0                                #initializing the total count of 1's with 0

        def bfs(r, c):                                  #using breadth first search approach
            q = collections.deque()                     #using queue data structure to store the values in the memory
            visited_ones.add((r, c))
            q.append((r, c))    
            while q:                                    #expanding and checking the puzzle
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]    #checking all the adjacent locations (right,left,top,below)
                for dr, dc in directions:               
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and nc in range(cols) and             #the coordinates should be in the range of rows & cols and if it is 1 and is already not visited.
                        grid[nr][nc] == '1' and (nr, nc) not in visited_ones):
                        q.append((nr, nc))                                      #doing the bfs on that particular coordinate as well
                        visited_ones.add((nr, nc))                               #adding the values in set so we dont iterate through them once again

        for r in range(rows):                           #iterating through rows and columns
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited_ones:  #checking if the value is 1 and making sure we are not going through the same coordinates
                    bfs(r, c)                                          #calling the bfs approach 
                    puzzle_count += 1

        return puzzle_count


folder_path = '/Users/pratishthasoni/Downloads/Meastro'
puzzle_counter = Meastro(folder_path)
puzzle_counter.process_files()