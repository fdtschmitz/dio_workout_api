from pydantic import Field, PositiveFloat
from typing import Annotated
from workout_api.contrib.models import BaseModel


class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do atleta', examples='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', examples='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', examples=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', examples=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', examples=1.70)]
    sexo: Annotated[str, Field(description='Sexo do atleta', examples='M', max_length=1)]