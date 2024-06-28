from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', examples='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereco do centro de treinamento', examples='Rua X, 002', max_length=20)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', examples='Marcos', max_length=20)]