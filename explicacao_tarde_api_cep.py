'''

Explicação sobre API

'''

import requests

def consulta_cep_(cep):
    url = f'https:\\viacep.com.br\ws\{cep}\json\'     

resposta = requests.get(url)

if resposta.status_code == 200:

    dados = resposta.json()
    
    return dados

else:

    return ' Error na consulta'

print ('Aula de API com Python:Consulta de CEP =')

meu_cep = '05349000'

resultado = consulta_cep(meu_cep)

if isinstance(resultado, dict):

    print(f'Endereço:{resultado['logradouro']}')
    print(f'Bairro:{resultado['Bairro']}')
    print(f'Cidade{resultado['localidade']}')