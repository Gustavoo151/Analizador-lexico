from tag import tokens, symbols

tokensInOrder = [] # Resultados dos tokens gerados pelo analisador léxico

identifierTable = [] # Lista para fazer armazenamento do todos os identificadores. Com seus respectivos dados ou não

# Buscando um mach com token usando o parâmetro de entrada
def searchTokens(valueOrSymbol):
    for searchToken in tokens:  # Buscando um mach com token usando o parâmetro de entrada
    
        if searchToken['lexeme'] == valueOrSymbol:
            tokensInOrder.append(searchToken)
            return True
        
        # Pegando os operadores lógigos relacionais
        elif valueOrSymbol in ['==', '>=', '<=', '!=']:
            if valueOrSymbol == '==' and searchToken['tag'] == 261:
                tokensInOrder.append(searchToken)
                return True

            elif valueOrSymbol == '>=' and searchToken['tag'] == 263:
                tokensInOrder.append(searchToken)
                return True
            
            elif valueOrSymbol == '<=' and searchToken['tag'] == 267:
                tokensInOrder.append(searchToken)
                return True
                
            elif valueOrSymbol == '!=' and searchToken['tag'] == 269:
                tokensInOrder.append(searchToken)
                return True


# Condicional para receber valores inteiro/float
def tokensInteger(valueOrSymbol):
    if isinstance(valueOrSymbol, int) or isinstance(valueOrSymbol, float):  # Usando a função isinstance() verifica se um objeto pertence à subclasse especificada
        token = {'tag': 270, 'value': valueOrSymbol}  # Gerando o token da tag 270 que representa um valor int ou float
        tokensInOrder.append(token)
        return True


#FUNÇÃO PRINCIPAL
# Buscando um mach com token usando o parâmetro de entrada 
def machToken(valueOrSymbol):
        for searchSymbol in symbols:        
            if searchSymbol['tag'] == valueOrSymbol:
                tokensInOrder.append(searchSymbol)
                return True


 #Função que recebe um valor e retorna em forma de token
def find_symb_value_in_table(valueOrSymbol): 
    
    if searchTokens(valueOrSymbol) == True:
        return None

    # Buscando um mach com token usando o parâmetro de entrada 
    elif tokensInteger(valueOrSymbol) == True:
        return None
    
    # Buscando um mach com token usando o parâmetro de entrada 
    elif machToken(valueOrSymbol) == True:
        return None
    
    # Gerando o token da tag 264 que representa qualquer parte do código que o nome pode ser alterado pelo programador    (Após ter passado por todos os condicionais acima só sobraram os identificadores)
    token = {'tag': 264, 'lexeme': f'{valueOrSymbol}'} 
    tokensInOrder.append(token)
    
    # Verificando se o símbolo já está na tabela de símbolos
    if token not in identifierTable:
        identifierTable.append(token)


######################### CÓDIGO TESTE ####################################################
'''
    float altura = 1.75;
    float peso = 80;
    int idade = 30;
    float imcNormal = 22.5;
    float meuImc;
    float imc;

    imc = peso / (altura * altura)
    if imcNormal == imc;
        meuImc = imc;
'''
# LISTA COM PALAVRA POR PALAVRA DO CÓDIGO
casoTesteLista = ['float','altura', '=', 1.75, ';', 'float', 'peso', '=', 80.0, ';', 'int', 'idade', 30, ';', 'float', 'imcNormal', '=', 22.5, ';', 'float', 'meuImc', ';', 'float', 'imc', ';', 'imc', '=', 'peso', '/', '(', 'altura', '*', 'altura', ')', ';', 'if', 'imcNormal', '==', 'imc', ';', 'meuImc', '=', 'imc', ';',]

##############################################################################################

# Usando List Comprehensions para passar valor por valor na função principal
[find_symb_value_in_table(dados) for dados in casoTesteLista]

print("-="*25)
print("\tTOKENS EM ORDEM")
print("-="*25)
# Usando List Comprehensions para printar os tokens em ordem
[print(tokens) for tokens in tokensInOrder]
print(""*20)
print('')
print("-="*20)
print('\tTABELA DE SÍMBOLOS')
print("-="*20)
# Usando List Comprehensions para printar a tabela se símbolos
[print(tokens) for tokens in identifierTable]
print("-="*20)