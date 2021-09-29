import re

class Lexer(object):
    def __init__(self, codigo_fonte):
        self.codigo_fonte = codigo_fonte

    def tokenizar(self): 
        
        tokens = []

        codigo_fonte = self.codigo_fonte.split()

        fonte_index = 0

        while fonte_index < len(codigo_fonte):
            
            palavra = (codigo_fonte[fonte_index])
            #Lista de Tokens para analisador lexico baseado no exemplo
            if re.match('[a-z]', palavra) or re.match('[A-Z]', palavra):
                if palavra[len(palavra) - 1] == ";" or palavra[len(palavra) - 1] == ":" : 
                    tokens.append(["IDENTIFICADOR", palavra[0:len(palavra) - 1]])
                    print("\n")
                else: 
                    tokens.append(["IDENTIFICADOR", palavra])
                    print("\n")
            
            elif re.match('[0-9]', palavra):
                if palavra[len(palavra) - 1] == ";":
                    tokens.append(["Integer", palavra[0:len(palavra) - 1]])
                    print("\n")
                else:
                    tokens.append(["Integer", palavra])
                    print("\n")
            
            elif re.match("^[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?$", palavra):
                if palavra[len(palavra) - 1] == ";":
                    tokens.append(["Real", palavra[0:len(palavra) - 1]])
                    print("\n")
                else:
                    tokens.append(["Real", palavra])
                    print("\n")

            elif (palavra == "<" or palavra == ">" or palavra == ">=" or palavra == "<=" or palavra == "="): tokens.append(["OPERADOR_Relacional", palavra])
            
            if (palavra == "real:") or (palavra == "integer:" ): 
                    tokens.append(["DECLARACAO_Tipo", palavra[0:len(palavra) - 1]])
                    print("\n")
            
            if palavra == "read" or palavra == "write" or palavra == "if" or palavra == "then" or palavra == "else": 
                    tokens.append(["DECLARACAO_Comando", palavra[0:len(palavra) - 1]])
                    print("\n")
            
            if (palavra == ","):
                     tokens.append(["SEPARADOR", palavra])  
                     print("\n")

            if (palavra == "end."):
                     tokens.append(["DECLARACAO_FimCodigo", palavra])  
                     print("\n")
            
            if (palavra == "begin"): 
                    tokens.append(["DECLARACAO_InicioCodigo", palavra])
                    print("\n")
            
            if (palavra == ":"):
                tokens.append(["OPERADOR_Atribuicao_VAR", ":"])
                print("\n")
            
            if (palavra == ":="):
                tokens.append(["OPERADOR_Atribuicao_ExpressãoMAT", ":="])
                print("\n")
            
            elif (palavra == "+" or palavra == "-" or palavra == "*" or palavra == "/"): 
                tokens.append(["OPERADOR_Matematico", palavra])
                print("\n")
            
            if (palavra[len(palavra) - 1] == "$" or palavra[len(palavra) - 1] == ";" ): 
                tokens.append(["OPERADOR_FimDeLinha", ";"])
                print("\n")
                
            
            fonte_index += 1
        
        print(tokens)


        return tokens



