from fila_base import FilaBase
from typing import Dict
from constants import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'Cliente atual: {cliente_atual}. Dirija-se ao caixa {caixa}')

    def estatistica(self, dia: str, agencia: int, retorna_estatistica) -> Dict:
        estatistica = retorna_estatistica(dia, agencia)
        return estatistica.roda_estatistica(self.clientes_atendidos)
