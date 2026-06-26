class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
    
    def adicionar_tarefa(self, descricao):
        self.tarefas.append({'descricao': descricao, 'concluida': False})
        print(f'Tarefa "{descricao}" adicionada!')
    
    def listar_tarefas(self):
        if not self.tarefas:
            print('Nenhuma tarefa pendente.')
        else:
            for i, tarefa in enumerate(self.tarefas):
                status = '✔' if tarefa['concluida'] else '✖'
                print(f'{i + 1}. [{status}] {tarefa["descricao"]}')
    
    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]['concluida'] = True
            print(f'Tarefa "{self.tarefas[indice]["descricao"]}" concluída!')
        else:
            print('Índice inválido!')
    
    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            tarefa = self.tarefas.pop(indice)
            print(f'Tarefa "{tarefa["descricao"]}" removida!')
        else:
            print('Índice inválido!')


gerenciador = GerenciadorTarefas()
gerenciador.adicionar_tarefa("Comprar pão")
gerenciador.adicionar_tarefa("Ler um livro")
gerenciador.listar_tarefas()
gerenciador.concluir_tarefa(0)
gerenciador.listar_tarefas()
gerenciador.remover_tarefa(1)
gerenciador.listar_tarefas()