import re
import unicodedata
from typing import Union
from datetime import datetime

just_numbers = lambda a: ''.join(re.findall("\d+", a))


def retira_vazios(param):
  ret = {}
  for i in param:
    if not (len(str(param[i])) == 0  or param[i] is None):
      ret.update({i: param[i]})

  return ret

def formatar_data_ptbr(data: Union[str, datetime]) -> str:
  """
  Converte uma data datetime ou string ISO 8601 para o formato pt-BR: dd/mm/yyyy HH:MM:SS
  """
  if isinstance(data, datetime):
    return data.strftime("%d/%m/%Y %H:%M:%S")
  elif isinstance(data, str):
    try:
      data_obj = datetime.fromisoformat(data)
      return data_obj.strftime("%d/%m/%Y %H:%M:%S")
    except ValueError:
      return data
  else:
    return str(data)

def fun_remove_acentos(texto: str) -> str:
  """
  Remove acentos de uma string e retorna apenas os caracteres ASCII.
  
  Exemplo:
  >>> FUN_REMOVE_ACENTOS("ação")
  'acao'
  """
  
  texto_normalizado = unicodedata.normalize('NFKD', texto)
  texto_sem_acentos = ''.join([c for c in texto_normalizado if not unicodedata.combining(c)])
  return texto_sem_acentos

def processar_parametros(user: dict) -> dict:
  for chave, valor in user.items():
    if isinstance(valor, str):
      user[chave] = fun_remove_acentos(valor)
  return user

def trata_retorno_oracle(self, value, msgSuccess, msgError):
  saida = {
    'sucesso': False,
    'mensagem': msgError
  }

  if 'IsRowEffected' in value:
    saida['sucesso'] = value['IsRowEffected']

    if value['RowsEffected'] > 0:
      saida['mensagem'] = msgSuccess
    else:
      saida['mensagem'] = msgError

  else:
    saida['mensagem'] = msgError

  if 'Mensagem' in value:
    if 'ORA-20002' in value['Mensagem']:
      saida['mensagem'] = self.retorna_msg_oracle(value['Mensagem'])

  return saida