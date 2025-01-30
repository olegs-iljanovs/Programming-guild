class WordGrid:
    def __init__(self):
        self.grid = [
            ['C', 'L', 'T', 'D'],
            ['A', 'L', 'A', 'T'],
            ['M', 'O', 'C', 'O'],
            ['D', 'E', 'S', 'K']
        ]

    '''creates array of chars for each line direction'''
    def get_line(self, line_type, index, reverse=False):
        if line_type == 'horizontal':
            return self.grid[index][::-1] if reverse else self.grid[index]
        elif line_type == 'vertical':
            return [row[index] for row in (self.grid[::-1] if reverse else self.grid)]
        elif line_type == 'diagonal-main':
            return [self.grid[i][i] for i in (range(len(self.grid) - 1, -1, -1) if reverse else range(len(self.grid)))]
        elif line_type == 'diagonal-side':
            return [self.grid[len(self.grid) - 1 - i][i] for i in (range(len(self.grid) - 1, -1, -1) if reverse else range(len(self.grid)))]

    '''replaces chars in line with * if word was found'''
    def replace_sublist(self, line, word):
        line = line[:]
        start = 0
        while start < len(line):
            if line[start:start + len(word)] == word:
                line[start:start + len(word)] = ['*'] * len(word)
                start += len(word)
            else:
                start += 1
        return line

    '''checks if word is found in line array'''
    def find_word_in_list(self, word, line):
        return word in ''.join(line)

    '''main function'''
    def guess_word(self):
        #prints initial grid
        for row in self.grid:
            print(' '.join(row))

        user_input = input("Hi, enter words that you think are in the grid: ").upper().split()

        found_words = []
        for word in user_input:
            #iterates through each direction of the grid, creating line and searching for word in it
            for i in range(4):
                for reverse in (False, True):
                    line = self.get_line('horizontal', i, reverse)
                    if self.find_word_in_list(word, line):
                        found_words.append(word)
                        print(self.replace_sublist(line, list(word)))
                        break
                    line = self.get_line('vertical', i, reverse)
                    if self.find_word_in_list(word, line):
                        found_words.append(word)
                        print(self.replace_sublist(line, list(word)))
                        break
                    line = self.get_line('diagonal-main', i, reverse)
                    if self.find_word_in_list(word, line):
                        found_words.append(word)
                        print(self.replace_sublist(line, list(word)))
                        break
                    line = self.get_line('diagonal-side', i, reverse)
                    if self.find_word_in_list(word, line):
                        found_words.append(word)
                        print(self.replace_sublist(line, list(word)))
                        break

        print(f"Founded words: {', '.join(found_words)} ({len(found_words)})")

word_grid = WordGrid()
word_grid.guess_word()