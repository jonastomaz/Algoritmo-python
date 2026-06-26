#Crie um programa em Python que simule um sistema de login. Defina um nome de usu´ario e
#uma senha correta no programa. Solicite ao usu´ario que insira o nome de usu´ario e a senha. Se
#ambos estiverem corretos, o programa deve exibir a mensagem “Login bem-sucedido”, caso
#contr´ario, deve exibir a mensagem “Login inv´alido”.

nome_usuario = 'jonas'
senha = 'senha'

nome_dig = input('qual o nome do usuario? ')
senha_dig = input('qual a senha? ')

while (nome_dig != nome_usuario) or (senha_dig != senha):
    print('login invalido')
    nome_dig = input('qual o nome do usuario? ')
    senha_dig = input('qual a senha? ')

else:
    print('login bem sucedido')