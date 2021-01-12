from funcionario_model import FuncionarioModel
model = FuncionarioModel()

def CadastrarFuncionario():
    nome = input('Digite seu nome: ')
    salario = input('Digite o valor do seu salario: ')
    funcao = input('Digite sua função:')

    funcionario={
        "nome":nome,
        "salario":salario,
        "funcao":função
    
    }
    if model.salvar(funcionario):
        print("Funcionario Cadastrado com sucesso!")
        return 0
    else:
        print("Funcionario não Cadastrado")

def ListarFuncionarios():
    funcionarios = model.get.all()
    for funcionario in funcionarios:
        print(funcionario)
