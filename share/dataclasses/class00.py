import inspect
from dataclasses import dataclass, field, asdict, astuple
from uuid import UUID, uuid4
from datetime import datetime

@dataclass(frozen=True, order=True)
class User:
    name: str = field(default= "test")
    birth_date: datetime = field(default = "01/01/1974")
    cpf: str = field(default = "17261704890")
    # O ID não entra na ordenação de comparação do order=True
    id: UUID = field(default_factory=uuid4, compare=False)

    def __post_init__(self):
        # 1. Normalização (Burlamos o 'frozen' com object.__setattr__)
        object.__setattr__(self, 'name', self.name.title())
        object.__setattr__(self, 'cpf', self.cpf.replace(".", "").replace("-", ""))

        # 2. Validação básica de CPF
        if len(self.cpf) != 11 or not self.cpf.isdigit():
            raise ValueError("CPF inválido! Deve conter exatamente 11 dígitos numéricos.")

    @property
    def age(self) -> int:
        """Calcula a idade dinamicamente baseada na data atual."""
        today = datetime.today()
        # Subtrai os anos e checa se o aniversário já passou este ano
        passed_birthday = (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        return today.year - self.birth_date.year - passed_birthday



def main():
   # print("Digite os dados separados por vírgula (Nome, Data Nasc DD/MM/AAAA, CPF):")
    try:
        #dados = input().split(",")

        dados = {
            "name": "Yuji",
            "birth_date": "28/08/2000",
            "cpf": '44233494859',
        }
        
        # Coletando e limpando os inputs básicos
        name = dados.get("name")
        # Tratando a string para virar um datetime válido (ajustado o formato %m%Y para %Y)
        birth_date = datetime.strptime(dados.get("birth_date"), "%d/%m/%Y")
        cpf = dados.get("cpf")

        # Instanciando a Dataclass
        user_test = User(name=name, birth_date=birth_date, cpf=cpf)
        
        print("\n✅ Usuário criado com sucesso!")
        print(f"\nIdade calculada dinamicamente: {user_test.age} anos")
        print(f"\nDicionário completo: {asdict(user_test)}")
        print(f"Tupla de valores: {astuple(user_test)}\n")
        print(f"Inspeção: \n {inspect.getmembers(User, inspect.isfunction)} ")
    except (IndexError, ValueError) as e:
        print(f"\n❌ Erro ao processar os dados. Verifique o formato inserido.")
        print(f"Detalhes do erro: {e}")

if __name__ == "__main__":
    main()
