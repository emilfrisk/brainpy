
class Brainfuck:

    def __init__(self):
        self.data_pointer = 0
        self.instruction_pointer = 0
        self.data_cells = [0]
    
    def get_commands(self, code):
        return [command for command in list(code) if command in list('><+-.,[]')]

    def get_parenthese_pairs(self, code):
        pairs = {}
        stack = []

        for index, command in enumerate(self.get_commands(code)):
            if command == '[':
                stack.append(index)
            if command == ']':
                if len(stack) == 0:
                    raise Exception('Brackets do not match.')

                opening_bracket_index = stack.pop()
                closing_bracket_index = index

                pairs[opening_bracket_index] = closing_bracket_index
                pairs[closing_bracket_index] = opening_bracket_index

        if len(stack) > 0:
            raise Exception('Brackets do not match.')
        
        return pairs



    def evaluate(self, code):

        pairs = self.get_parenthese_pairs(code)

        while self.instruction_pointer < len(self.get_commands(code)):
        
            command = self.get_commands(code)[self.instruction_pointer]

            if command == '>':
                self.data_pointer += 1
                if self.data_pointer == len(self.data_cells):
                    self.data_cells.append(0)

            if command == '<':
                self.data_pointer -= 1 if self.data_pointer > 0 else 0

            if command == '+':
                self.data_cells[self.data_pointer] += 1 if self.data_cells[self.data_pointer] < 255 else 0

            if command == '-':
                self.data_cells[self.data_pointer] -= 1 if self.data_cells[self.data_pointer] > 0 else 255

            if command == '.':
                print(chr(self.data_cells[self.data_pointer]), end='')

            if command == '[':
                if self.data_cells[self.data_pointer] == 0:
                    self.instruction_pointer = pairs[self.instruction_pointer]

            if command == ']':
                if self.data_cells[self.data_pointer] != 0:
                    self.instruction_pointer = pairs[self.instruction_pointer]

            self.instruction_pointer += 1

        self.__init__()



bf = Brainfuck()
bf.evaluate('''++++++++++[>+++++++>++++++++++>+++>+<<<<-]
>++.>+.+++++++..+++.>++.<<+++++++++++++++.
>.+++.------.--------.>+.>.''')
