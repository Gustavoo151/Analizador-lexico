from tag import tokens, symbols

tokensInOrder = [] # Resultados dos tokens gerados pelo analisador léxico

identifierTable = [] # Lista para fazer armazenamento do todos os identificadores. Com seus respectivos dados ou não

 #Função que recebe um valor e retorna em forma de token
def find_symb_value_in_table(valueOrSymbol): 
    for seachToken in tokens:  # Buscando um mach com token usando o parâmetro de entrada
        if seachToken['lexeme'] == valueOrSymbol:
            tokensInOrder.append(seachToken)
            return None

    # Condicional para receber valores inteiro/float
    if isinstance(valueOrSymbol, int) or isinstance(valueOrSymbol, float):  # Usando a função isinstance() verifica se um objeto pertence à subclasse especificada
        token = {'tag': 270, 'value': valueOrSymbol}  # Gerando o token da tag 270 que representa um valor int ou float
        tokensInOrder.append(token)
        return None

    # Buscando um mach com token usando o parâmetro de entrada 
    for seachSymbol in symbols:        
        if seachSymbol['tag'] == valueOrSymbol:
            tokensInOrder.append(seachSymbol)
            return None

    # Gerando o token da tag 264 que representa qualquer parte do código que o nome pode ser alterado pelo programador    (Após ter passado por todos os condicionais acima só sobraram os identificadores)
    token = {'tag': 264, 'lexeme': f'{valueOrSymbol}'} 
    tokensInOrder.append(token)
    identifierTable.append(token)



'''
    float altura = 1.75;
    float peso = 80;
    int idade;

    imc = peso / (altura * altura)
'''

casoTesteLista = ['float','altura', '=', 1.75, ';', 'float', 'peso', '=', 80.0, ';', 'int', 'idade', 30, ';', 'imc', '=', 'peso', '/', '(', 'altura', '*', 'altura',')', ';']

[find_symb_value_in_table(dados) for dados in casoTesteLista]

print("-="*25)
print("\tTOKENS EM ORDEM")
print("-="*25)
[print(tokens) for tokens in tokensInOrder]
print(""*20)
print('')
print("-="*20)
print('\tTABELA DE SÍMBOLOS')
print("-="*20)
[print(tokens) for tokens in identifierTable]
print("-="*20)