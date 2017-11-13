#!/usr/bin/env python
# Compilers - LR Parsing Program

# LR_table columns
columns = {'i' : 0, '+' : 1, '-' : 2, '*' : 3, '/' : 4, '(' : 5, ')' : 6, '$' : 7,
'E' : 8, 'T' : 9, 'F' : 10}

# Uses RHS rule length to determine how many characters to pop from the stack.
rules = [  # CFG:
('E', 3),  # 'E+T'
('E', 3),  # 'E-T'
('E', 1),  # 'T'
('T', 3),  # 'T*F'
('T', 3),  # 'T/F'
('T', 1),  # 'F'
('F', 3),  # '(E)'
('F', 1)   # 'i'
]

LR_table = [
['S5', -1, -1, -1, -1, 'S4', -1, -1, 1, 2, 3],
[-1, 'S6', 'S7', -1, -1, -1, -1, 'acc', -1, -1, -1],
[-1, 'R3', 'R3', 'S8', 'S9', -1, 'R3', 'R3', -1, -1, -1],
[-1, 'R6', 'R6', 'R6', 'R6', -1, 'R6', 'R6', -1, -1, -1],
['S5', -1, -1, -1, -1, 'S4', -1, -1, 10, 2, 3],
[-1, 'R8', 'R8', 'R8', 'R8', -1, 'R8', 'R8', -1, -1, -1],
['S5', -1, -1, -1, -1, 'S4', -1, -1, -1, 11, 3],
['S5', -1, -1, -1, -1, 'S4', -1, -1, -1, 12, 3],
['S5', -1, -1, -1, -1, 'S4', -1, -1, -1, -1, 13],
['S5', -1, -1, -1, -1, 'S4', -1, -1, -1, -1, 14],
[-1, 'S6', 'S7', -1, -1, -1, 'S15', -1, -1, -1, -1],
[-1, 'R1', 'R1', 'S8', 'S9', -1, 'R1', 'R1', -1, -1, -1],
[-1, 'R2', 'R2', 'S8', 'S9', -1, 'R2', 'R2', -1, -1, -1],
[-1, 'R4', 'R4', 'R4', 'R4', -1, 'R4', 'R4', -1, -1, -1],
[-1, 'R5', 'R5', 'R5', 'R5', -1, 'R5', 'R5', -1, -1, -1],
[-1, 'R7', 'R7', 'R7', 'R7', -1, 'R7', 'R7', -1, -1, -1],
]

def trace_str(word):
    stack = [0]
    i = 0  # string iterator
    character = word[i]

    while True:
        state = stack[-1]
        column = columns.get(character)
        action = LR_table[state][column]  # action == terminal/nonterminal

	# If we have reached an invalid character
        if action == -1:
            return "Reject"

	# If we have concluded a word is accepted
        elif action == 'acc':
            return "Accept"

	# If we have reached a shift
        elif action[0] == 'S':
            stack.append(int(action[1:]))
            i += 1
            character = word[i]

	# If we have reached a reduce
        elif action[0] == 'R':
            action = int(action[1:])
            rule_length = rules[action - 1][1]
            while rule_length > 0:
                stack.pop()
                rule_length -= 1

            lhs = rules[action - 1][0]
            column = columns.get(lhs)
            state = stack[-1]

            non_terminal = LR_table[state][column]
            stack.append(non_terminal)

def main():
    word1 = '(i+i)*i$'
    word2 = '(i*)$'

    print trace_str(word1) # Accept
    print trace_str(word2) # Reject 

if __name__ == '__main__':
    main()
