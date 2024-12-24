import requests
import json
import pandas as pd
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from pathlib import Path

CAMINHO_AULA = Path(__file__).parent
CAMINHO_ARQUIVO = CAMINHO_AULA / 'Cep.xlsx'


def obter_endereco_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    
    if response.status_code == 200:
        endereco = response.json()
        return endereco
    else:
        print('Erro', {response.status_code})

cep = '17055180'

resultado = obter_endereco_cep(cep)

formatacao = pd.DataFrame([resultado])

workbook = Workbook()
worksheet: Worksheet = workbook.active
worksheet.append(formatacao.columns.tolist())


for row in formatacao.itertuples(index=False, name=None):
    worksheet.append(row)
    print('Success.')

workbook.save(CAMINHO_ARQUIVO)