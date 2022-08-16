from tag import tag, symbs  # Módulo para pegar todas as tags

tableSymb = [] # Tabela da símbolos para armazenar todos os identificadores do código. (Tudo que o programador tem liberade de mudar, recebe o nome de ID na tabela de símbolos).

tableTokens = [] # Lista para fazer armazenamento do todos os tokens com seus respectivos dados

symb = []

def find_symb_value_in_table(lexeme,valueOrSymb):    #Função que recebe um token com seu lexema
    lexeme = lexeme.upper()  # Usamos a função uppe() para padronizar todos as entradas de lexemes com letras maiúsculas

    for tags in tag:  # Pegando todas as tags um por uma do módulo tag, para fazer as verificações
        if tags['lexeme'] == lexeme and tags not in tableTokens: # Na primeira parte antes do and verificamos se o lexeme recebido está dentro de alguma tag e se tiver verificamos se ele já foi adicionado anteriormente na tableTokens.
            return tableTokens.append(tags)  # Adicionado um a tag na tableTokens 

        elif tags['tag'] == 264:  # A tag 262 sever para adicionar os identificadores na lista tableSymb. Lembrando que no módulo tag à tag 264 recebe o parâmetro lexeme para formar seu token.
            return tableSymb.append(tags) 
        elif valueOrSymb in symbs:
            return symb.append({'tag': valueOrSymb})



find_symb_value_in_table('int', None) #função teste passando a palavra reserveda INT
find_symb_value_in_table('do', None)  # Testando com a palavra chave DO
find_symb_value_in_table('do', None)  # Verficando se está adicinando arquivos duplicados
find_symb_value_in_table('Altura', '')  # Adicionado uma variável para ser transformada em identificador
find_symb_value_in_table('Altura', '')  # Adicionado uma variável para ser transformada em identificador
find_symb_value_in_table('', '[')
find_symb_value_in_table('', '=')
find_symb_value_in_table('', '{')


[print(x) for x in tableSymb] # printando a tabela de simbolos
print("-="*40)
[print(x) for x in tableTokens] # printando a tabela de tokens
print("-="*40)
[print(x) for x in symb] # printando os symb