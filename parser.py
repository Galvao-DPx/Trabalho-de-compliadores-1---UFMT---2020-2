

class Parser(object):

    def __init__(self, tokens):
        
        self.tokens = tokens

        self.tokens_index = 0

        self.codigo_transpilado = ""

    def parse(self):

        while self.tokens_index < len(self.tokens):
            #Aqui será representado o tipo de token
            token_tipo = self.tokens[self.tokens_index][0]
            #Aqui será representado o valor do token
            token_valor = self.tokens[self.tokens_index][1]
            
            if token_tipo == "IDENTIFICADOR" and (token_valor != "Integer" or 
                token_valor != "Real" or token_valor != "read" or token_valor != "write" 
                or token_valor != "real" or token_valor != "integer" or token_valor != "if" 
                or token_valor != "then" or token_valor != "else" or token_valor != "being" or
                token_valor != "end."):
                    self.parse_declaracao_variavel(self.tokens[self.tokens_index:len(self.tokens)])
            
            self.tokens_index += 1

    def parse_declaracao_variavel(self, token_corrente):
        
        tokens_checados = 0

        for token in range(0, len(token_corrente)):
            
            token_tipo = token_corrente[tokens_checados][0]
            token_valor = token_corrente[tokens_checados][1]
            
            #Lista de tokens que o parser indentifica
            if token == 0:
                print("Tipo_variavel " + token_valor , "\n")
            
            elif token == 1 and (token_valor == "real" or token_valor == "integer"):
                print("Tipo_dado_num " + token_valor , "\n")
            elif token == 1 and (token_valor != "real" or token_valor != "integer"):
                print("ERRO: VARIAVEL INVALIDA " + token_valor + "\n")
                quit()
            
            elif token == 2 and (token_valor == "read" or token_valor == "write" or token_valor == "if" or token_valor == "then" or token_valor == "else"):
                print("Tipo_comando " + token_valor , "\n")
            elif token == 2 and (token_valor != "read" or token_valor != "write" or token_valor != "if" or token_valor != "then" or token_valor != "else"):
                print("ERRO: COMANDO INVALIDO " + token_valor + "\n")
                quit()
            
            elif token == 3 and (token_valor == "+" or token_valor == "-" or token_valor == "*" or token_valor == "/"):
                print("Tipo_opMAT " + token_valor , "\n")
            elif token == 3 and (token_valor != "+" or token_valor != "-" or token_valor != "*" or token_valor != "/"):
                print("ERRO: OPERACAO MATEMATICA INVALIDO " + token_valor + "\n")
                quit()

            elif token == 4 and (token_valor == ">" or token_valor == "<" or token_valor == "=" or token_valor == ">=" or token_valor == "<=" or token_valor == "<>"):
                print("Tipo_opREL " + token_valor , "\n")
            elif token == 4 and (token_valor != ">" or token_valor != "<" or token_valor != "=" or token_valor != ">=" or token_valor != "<=" or token_valor != "<>"):
                print("ERRO: OPERACAO RELACIONAL INVALIDO " + token_valor + "\n")
                quit()
            
            elif token == 5 and token_valor == "begin":
                print("Tipo_InicioCodigo" + token_valor , "\n")
            elif token == 5 and token_valor != "begin":
                print("ERRO: ESPERAVA " + token_valor + " PARA MARCAR O INICIO DO CODIGO" "\n")
                quit()

            elif token == 6 and token_valor == "end.":
                print("Tipo_FimCodigo" + token_valor , "\n")
            elif token == 6 and token_valor != "end.":
                print("ERRO: ESPERAVA " + token_valor + " PARA MARCAR O FINAL DO CODIGO" "\n")
                quit()

            elif token == 7 and token_valor == ":":
                print("op_atribuicaoVAR" + token_valor , "\n")
            elif token == 7 and token_valor != ":":
                print("ERRO: ESPERAVA ':' " + token_valor + " PARA ATRIBUIR VALOR PARA VARIAVEL" "\n")
                quit()
            
            elif token == 8 and token_valor == ":=":
                print("op_atribuicaoExpMAT" + token_valor , "\n")
            elif token == 8 and token_valor != ":=":
                print("ERRO: ESPERAVA ':=' " + token_valor + " PARA ATRIBUIR VALOR PARA VARIAVEL EM EXPRESSAO MATEMATICA" "\n")
                quit()
            
            elif token == 9 and (token_valor == ";" or token_valor == "$;"):
                print("op_FimLinha" + token_valor , "\n")
            elif token == 9 and (token_valor != ";" or token_valor != "$;"):
                print("ERRO: ESPERAVA ';' OU '$;' " + token_valor + " PARA MARCAR O FINAL DA LINHA" "\n")
                quit()
            
            elif token == 10 and token_valor == ",":
                print("op_Separador" + token_valor , "\n")

            tokens_checados =+ 1
        
        self.tokens_index =+ tokens_checados