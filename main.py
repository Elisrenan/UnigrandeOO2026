class Aluno:
    universidade = "UniGrande"

    def __init__(self, matricula: int, nome: str) -> None:
        self.matricula = matricula
        self.nome = nome
        self.creditos_cursados = 0
        self.mgp = 0.0

    def apresentar(self):
        return f"{self.matricula} - {self.nome}"


class Professor:
    def __init__(self, matricula: int,
                 nome: str, email: str) -> None:
        self.matricula = matricula
        self.nome = nome
        self.email = email

    def resumo(self) -> str:
        return f"{self.matricula} - {self.nome} < {self.email}"

class Curso:
    def __init__(self, codigo: int, nome: str,
                 total_creditos: int) -> None:
        self.codigo = codigo
        self.nome = nome
        self.total_creditos = total_creditos

aluno_1 = Aluno(20260001, "David Leite")
aluno_2 = Aluno(20260002, "Carlinhos Maia")

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

