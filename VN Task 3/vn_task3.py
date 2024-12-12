class WordGrid():
    def __init__(self):
        self.initial_grid = [ 
            ['C', 'L', 'T', 'D'],
            ['A', 'L', 'A', 'T'],
            ['M', 'O', 'C', 'O'],
            ['D', 'E', 'S', 'K']
        ]
    
    def generate_line_list(self, line_type, iteration_counter, is_reverse):
        line = []
        grid = self.initial_grid
        reversed_grid = list(reversed(self.initial_grid))
        if line_type == 'horizontal' and not is_reverse:
            line = grid[iteration_counter]
        elif line_type == 'horizontal' and is_reverse:
            line = list(reversed(grid[iteration_counter]))
        elif line_type == 'vertical' and not is_reverse:
            for inner_array in grid:
                line.append(inner_array[iteration_counter])
        elif line_type == 'vertical' and is_reverse:
            for inner_array in reversed_grid:
                line.append(inner_array[iteration_counter])
        elif line_type == 'diagonal':
            print("damn...")
        return line
    
    def replace_sublist(self, line_list, word_list):
        new_list = line_list.copy()
        sublist_replace = ['*'] * len(word_list)
        i = 0
        while i < len(new_list):
            if new_list[i:i+len(word_list)] == word_list:
                new_list[i:i+len(word_list)] = sublist_replace
                i += len(sublist_replace)
            else:
                i += 1
        return new_list
    
    def find_word_in_list(self, word_list, line_list):
        return any(map(lambda x: line_list[x:x + len(word_list)] == word_list, range(len(line_list) - len(word_list) + 1)))

    def guess_word(self):
        for line in self.initial_grid:
            print("  ".join(map(str, line)))
        user_input = input("Hi, enter words that you think are in the grid: ")
        user_input_list = list(user_input.upper())

        line = []
        founded_words = []
        iteration_counter = 0
        search_direction = ''
        is_reverse = False

        for iteration in range(16):
            if iteration <= 3:
                search_direction = 'horizontal'
            elif iteration == 4:
                search_direction = 'vertical'
                iteration_counter = 0
            elif iteration == 8:
                search_direction = 'vertical'
                is_reverse = True
                iteration_counter = 3
            elif iteration == 12:
                search_direction = 'horizontal'
                is_reverse = True
                iteration_counter = 3
            
            line = self.generate_line_list(search_direction, iteration_counter, is_reverse)

            if not is_reverse:
                iteration_counter += 1
            else:
                iteration_counter -= 1
            
            is_word_found = self.find_word_in_list(user_input_list, line)
            if is_word_found:
                founded_words.append(user_input)
                print(self.replace_sublist(line, user_input_list))

        print(f'''Founded words: {founded_words} ({len(founded_words)})''')
        
word_grid = WordGrid()
word_grid.guess_word()