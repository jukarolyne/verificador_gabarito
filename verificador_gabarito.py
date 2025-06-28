'''Leitura Ótica'''

def capturar_gabarito(n_questoes, guarda_letra: str ='', letras: list =['A', 'B', 'C', 'D', 'E']):
  '''captura as opcoes marcadas pelo avaliado'''
  lista = []
  if n_questoes == 0:
      return lista
  for i in range(n_questoes):
      cont = 0
      questao = input(f'Digite a {i+1}ª questão: ').split(" ")
      for j in range(len(questao)):
          if int(questao[j]) <= 127:
              guarda_letra = letras[j]
              cont +=1
      if cont == 1:
          lista.append(guarda_letra)
      else:
          lista.append('*')
  return lista

def verificar_gabarito(gabarito: list, marcadas: list, contar_acertos = 0):
  '''compara gabarito com opcoes marcadas'''
  for i, q in enumerate(gabarito):
    if q == marcadas[i]:
      marcadas[i] = 'V'
      contar_acertos += 1
    else:
      marcadas[i] = 'F'
  return contar_acertos, marcadas
  
if __name__ == '__main__':
  print('-+-'*30)
  gabarito_base = input('Digite o gabarito da prova: ').split(" ")
  qtde_avaliados = int(input('Digite quantos gabaritos deseja corrigir: '))
  print('As letras presentes no gabarito padrão são {A, B, C, D, E}')
  letras = input('Deseja mudar? \nSe sim, digite a seguir as letras do seu gabarito \nSe não, aperte ENTER para pular\n').split()
  print('-+-'*30)

  resultados_salvos = []
  for gabarito in range(qtde_avaliados): 
    nome_avaliado = input('Digite nome do avaliado: ')
    if letras == [None]:
      marcadas = capturar_gabarito(len(gabarito_base))
    else:
      marcadas = capturar_gabarito(len(gabarito_base), letras)
    print('-+-'*30)
    resultados_salvos.append([nome_avaliado, verificar_gabarito(gabarito_base, marcadas)])

  for resultado in resultados_salvos:
    print(f'{resultado[0]} | {resultado[1][0]} acerto(s) | conferência com o gabarito: {resultado[1][1]}')



'''EXEMPLO DE SAÍDA:
-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-
Digite o gabarito da prova: A D
Digite quantos gabaritos deseja corrigir: 2
As letras presentes no gabarito padrão são {A, B, C, D, E}
Deseja mudar? 
Se sim, digite a seguir as letras do seu gabarito 
Se não, aperte ENTER para pular
A B C D
-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-
Digite nome do avaliado: MARIA
Digite a 1ª questão: 1 222 222 222
Digite a 2ª questão: 222 222 222 1
-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-
Digite nome do avaliado: ANA
Digite a 1ª questão: 1 222 222 1
Digite a 2ª questão: 222 222 222 1
-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-
MARIA | 2 acerto(s) | conferência com o gabarito: ['V', 'V']
ANA | 1 acerto(s) | conferência com o gabarito: ['F', 'V']'''
