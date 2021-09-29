

class ObjetoVariavel(object):

    def __init__(self):

        self.exec_string = ""
    
    def transpilar(self, nome, operador ,valor):
        
        self.exec_string += nome + "" + operador + valor
        return self.exec_string