import sys

# Mock submission that will return valid path
class ReferenceMazeRunner:
    def run(self, start, end):
        # print(f"we're in ReferenceMazeRunner self = {self}")
        path = []
        # check if start room has valid exits
        if start.exits:
            # iterate over each possible next room
            for possibility in start.exits:
                # print(possibility)
                # get maze square object related to each possible exit
                next = start.get_square(possibility)
                # print(next.name)
                if next:
                    if next.exits:
                        # print(next.exits)
                        for exit in next.exits:
                            # print(exit)
                            next_next = next.get_square(exit)
                            # print(next_next.name)
                            # print(end)
                            if next_next.name == end.name:
                                path.append(possibility)
                                # path.append()
                            # if possibility name equals start, then pass
                            # if possibility name equals end:
        
            # print(f"path = {path}")
                
            
    
        return path

class MazeLoader:
    def __init__(self):
        self.master_list = {}
        
        try:
            with open(sys.argv[1], 'r') as f:
                cell_nums = int(f.readline())
                for _ in range(cell_nums):
                    curr_line = f.readline()
                    parts = curr_line.split(' ', 2)
                    name = parts[0]
                    if name not in self.master_list:
                        self.master_list[name] = MazeSquare(name)
                    square = self.master_list.get(name)
                    exits = parts[1].split(',')
                    for exit in exits:
                        direction, next_square = exit.split(':')
                        if next_square not in self.master_list:
                            self.master_list[next_square] = MazeSquare(next_square)
                        square.add_exit(self.master_list.get(next_square), direction)
                start, end = f.readline().split(' ')
                
                current = self.master_list.get(start)
                # print(current.exits.get('North').name)
                runners = [ReferenceMazeRunner()]
                for runner in runners:
                    result = runner.run(self.master_list.get(start), self.master_list.get(end))
                    print(result)
                    for step in result:
                        current = current.get_square(step)
                        if current == None:
                            print('Invalid path returned')
                            break
                    print('Returned ' + ('valid' if self.master_list.get(end).get_name() == current.get_name() else 'invalid') + ' path')
        except FileNotFoundError:
            print('Location of maze file was not found')
        except IOError:
            print('IO Exception reading from maze file')
                
class MazeSquare:
    def __init__(self, name):
        self.name = name
        self.exits = {}
        
    def add_exit(self, square, direction):                            
        self.exits[direction] = square
    
    def get_name(self):
        return self.name
    
    def get_exists(self):
        return self.exits.keys()
                    
    def get_square(self, direction):
        return self.exits.get(direction, None)                     
        
MazeLoader()

# call simple.maze in Command Line:
# python3 MazeLoader.py /home/mauratee/src/maze_dist/src/samples/simple.maze