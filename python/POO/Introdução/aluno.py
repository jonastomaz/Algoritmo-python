class Aluno:
    def __init__(self, aulas_dadas, faltas, media_anual):
        self.__aulas_dadas = aulas_dadas
        self.__faltas = faltas
        self.__media_anual = media_anual
        self.__indice_falta_global = self.__calcular_indece_falta
        self.__aprovado_ou_nao = self.__aprovado_ou_reprovado

    @property
    def indice_falta_global(self):
        return self.__indice_falta_global

    @property
    def aprovado_ou_nao(self):
        return self.__aprovado_ou_nao

    
    def __calcular_indece_falta(self, aulas_dadas, faltas):
        total_aulas = sum(self.aulas_dadas)
        total_faltas = sum(self.faltas)
        return (total_faltas / total_aulas) * 100
    
    def __aprovado_ou_reprovado(self, media_anual):
        if self.media_anual < 50 or self.__indice_falta_global >= 50:
            return "Reprovado"
        else:
            return "Aprovado"