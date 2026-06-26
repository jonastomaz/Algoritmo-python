class Eleitor:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @mudar_nome.setter
    def mudar_nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self.__idade

    @mudar_idade.setter
    def mudar_idade(self, nova_idade):
        self.__validar_idade
        self._idade = nova_idade

    def tipo_eleitor(self):
        if 16 <= self.idade < 18 or self.idade >= 70:
            return "Eleitor Facultativo"
        elif self.idade >= 18:
            return "Eleitor Obrigatório"

    
    def __validar_idade(self, nova_idade):
        if nova_idade < 16:
            raise ValueError("A idade do eleitor deve ser maior ou igual a 16 anos.")