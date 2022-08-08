#Iniciando projeto pela função "menu"



def menu():
  #Retorno ao menu facilitado com a lista voltarMenu
  voltarMenu = 's'
  while voltarMenu == 's':
    opcao = input('''
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
                  Atividade Ativa:
                 (Agenda em Python)
Menu:

1 - (((Cadastrar contato)))
2 - (((Listar contato)))
3 - (((Excluir contato)))
4 - (((Buscar contato pelo Email)))
5 - (((Sair)))
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
Escolha a opção desejada: 
''')
    #Escolher um numero para realizar a tarefa desejada
    if opcao == '1':
      cadastrar()
    elif opcao == '2':
      listar()
    elif opcao == '3':
      excluir()
    elif opcao == '4':
      buscarContatoPeloEmail()
    elif opcao == '5':
      sair()
    else:
      print('Funçao invalida... Volte ao menu!')
    voltarMenu = input('Deseja voltar ao menu ? (s/n)').lower()

    #Fim do menu
def cadastrar():
  #Função para adicionar contatos a lista
  email = input('Digite o Email do contato: ')
  nome = input('Digite o nome do contato: ')
  telefone = input('Digite o telefone do contato:')
  twitter = input('Digite o twitter do contato: ')
  instagram = input('Digite o instagram do contato: ')
  try:
    agenda = open('agenda.txt','a')
    dados = f'{email},{nome},{telefone},{twitter},{instagram}\n'
    agenda.write(dados)
    agenda.close()
    print(f'Contato Gravado!!!')
  except:
    print ('ERRO fatal... Revise o codigo!')

def listar():
  #Função para listar os contatos que ja foram adicionados
  agenda = open ('agenda.txt','r')
  for contato in agenda:
    print(contato)
  agenda.close()

def excluir():
  #Função para deletar contatos da lista a partir do email
  emailDel = input('Digite o email a ser deletado: ')
  agenda = open ('agenda.txt','r')
  auxiliar = []
  auxiliar1 =[]
  for i in agenda:
    auxiliar.append(i)
  for i in range(0, len(auxiliar)):
    if emailDel not in auxiliar[i]:
      auxiliar1.append(auxiliar[i])
  agenda = open('agenda.txt','w')
  for i in auxiliar1:
    agenda.write(i)
  listarContato()
  print(f'Deletado com sucesso!')

def buscarContatoPeloEmail():
  #Função para buscar contatos atravez do email de identificação
  email =input(f'Digite o Email a ser buscado: ')
  agenda = open ('agenda.txt','r')
  for contato in agenda:
    if email in contato.split(';')[0]:
      print(contato)
  agenda.close()

def sair():
  #Função sair
  print('Saindo do programa!!!')

def main():
  menu()


main()
