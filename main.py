class Aluno:
    universidade = "UniGrande"

    def __init__(self, matricula: int, nome: str) -> None:
        self.matricula = matricula
        self.nome = nome
        self.creditos_cursados = 0
        self.mgp = 0.0

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str) -> None:
        valor = valor.strip()
        if len(valor) < 3:
            raise ValueError("Nome inválido")
        self._nome = valor

    @property
    def mgp(self) -> float:
        return self._mgp

    @mgp.setter
    def mgp(self, valor: float) -> None:
        if not 0 <= valor <= 10:
            raise ValueError("MGP deve estar entre 0 e 10")
        self._mgp = valor

    @property
    def creditos_cursados(self):
        return self._creditos_cursados

    @creditos_cursados.setter
    def creditos_cursados(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("Créditos não podem ser negativos")
        self._creditos_cursados = valor

    def apresentar(self):
        return f"{self.matricula} - {self.nome}"


class Professor:
    def __init__(self, id_rh: int,
                 matricula: int,
                 nome: str, email: str) -> None:
        self.__id_rh = id_rh
        self.matricula = matricula
        self.nome = nome
        self.email = email

    @property
    def email(self) -> str:
        return self._email
    @email.setter
    def email(self, valor: str) -> None:
        valor = valor.strip().lower()
        if "@" not in valor:
            raise ValueError("E-mail inválido")
        usuario, dominio = valor.split("@", 1)
        if not usuario or "." not in dominio:
            raise ValueError("E-mail inválido")
        self._email = valor


    def payload_integracao_rh(self) -> dict[str, object]:
        return {
                "id_rh": self.__id_rh,
                "matricula": self.matricula,
                "nome": self.nome
        }

    def resumo(self) -> str:
        return f"{self.matricula} - {self.nome} < {self.email}"

class Curso:
    def __init__(self, codigo: int, nome: str,
                 total_creditos: int) -> None:
        self.codigo = codigo
        self.nome = nome
        self.total_creditos = total_creditos

# 1. Criação com sucesso
aluno_1 = Aluno(20260001, "David Leite")
aluno_2 = Aluno(20260002, "Carlinhos Maia")

# 2. Atualizações válidas via setter
aluno_1.mgp = 8.5
aluno_1.creditos_cursados = 24

# 3. Tentativas inválidas (lançam ValueError)
aluno_1.mgp = 11.0               # ValueError: MGP deve estar entre 0 e 10
aluno_1.nome = "Ed"              # ValueError: Nome inválido
aluno_1.creditos_cursados = -4   # ValueError: Créditos não podem ser negativos

print(aluno_1.apresentar())
print(aluno_2.apresentar())

professor_1 = Professor(1, 'Elisrenan',
                        'elisrenan@gmail.com')
professor_2 = Professor(2, 'Mariano',
                        "marilindo@gmail.com")

print(professor_1.resumo())
print(professor_2.resumo())

curso_1 = Curso(4340, "ADS", 40)
curso_2 = Curso(35, "SI", 200)

