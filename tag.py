lexeme = ''

tag = [
    {'tag': 256, 'lexeme': 'AND'},

    {'tag': 257, 'lexeme': 'BASIC'},               # ??? 
    {'tag': 257, 'lexeme': 'INT', 'width': 4},     # int
    {'tag': 257, 'lexeme': 'FLOAT', 'width': 8},   # float

    {'tag': 258, 'lexeme': 'BREAK'},
    {'tag': 259, 'lexeme': 'DO'},
    {'tag': 260, 'lexeme': 'ELSE'},
    {'tag': 261, 'lexeme': 'EQ'},  # ????
    {'tag': 262, 'lexeme': 'FALSE'},
    {'tag': 263, 'lexeme': 'GE'},  # ????
    {'tag': 264, 'lexeme': f'{lexeme}'},
    {'tag': 265, 'lexeme': 'IF'},
    {'tag': 266, 'lexeme': 'INDEX'},
    {'tag': 267, 'lexeme': 'LE'},  # ????
    {'tag': 268, 'lexeme': 'MINUS'}, # ???
    {'tag': 269, 'lexeme': 'NE'},
    # {'tag': 270, 'value': f'{lexeme}'},
    {'tag': 271, 'lexeme': 'OR'},
    {'tag': 272, 'lexeme': 'REAL'},
    {'tag': 273, 'lexeme': 'TEMP'},
    {'tag': 274, 'lexeme': 'TRUE'},
    {'tag': 275, 'lexeme': 'WHILE'}
]

symbs = ['[',']', '=', '*', '{', '}']