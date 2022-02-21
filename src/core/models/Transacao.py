from dataclasses import dataclass
from datetime import datetime
from pandas import Timestamp as pd
from src.core.models.Cliente import Cliente

@dataclass
class Transacao:
    id: int
    id_cliente: Cliente
    valor: float
    data: datetime

    @classmethod
    def dadoBruto(cls,dado):
        return cls(
            id=dado['id'],
            cliente_id=dado['cliente_id'],
            valor=dado['valor'],
            data_cadastro= str(pd(dado['data_cadastro']).to_pydatetime()),
        )