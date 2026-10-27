import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.__id = id 
        self.__nome = nome
        self.__email = email
        self.__fone = fone

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone

    def set_id(self, id):
        if id == "": raise ValueError("ID deve ser informado.")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado.")
        self.__nome = nome
    def set_email(self, email):
        if email == "": raise ValueError("Email deve ser informado.")
        self.__email = email
    def set_fone(self, fone):
        if fone == "": raise ValueError("Telefone deve ser informado.")
        self.__fone = fone

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Email: {self.__email} | Fone: {self.__fone}"

class ClienteDAO:
    objetos = []

    @classmethod
    def Inserir(cls, obj):
        cls.Abrir()
        cls.objetos.append(obj)
        cls.Salvar()

    @classmethod
    def Listar(cls):
        cls.Abrir()
        return cls.objetos

    @classmethod
    def Listar_Id(cls, id):
        cls.Abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def Atualizar(cls, obj):
        cls.Abrir()
        for i, x in enumerate(cls.objetos):
            if x.get_id() == obj.get_id():
                cls.objetos[i] = obj
                cls.Salvar()
                return

    @classmethod
    def Excluir(cls, obj):
        cls.Abrir()
        cls.objetos.remove(obj)
        cls.Salvar()

    @classmethod
    def Abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", "r") as arquivo:
                dados = json.load(arquivo)
                for item in dados:
                    c = Cliente(item["id"], item["nome"], item["email"], item["fone"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def Salvar(cls):
        dados = []
        for obj in cls.objetos:
            dados.append({
                "id": obj.get_id(),
                "nome": obj.get_nome(),
                "email": obj.get_email(),
                "fone": obj.get_fone()
            })
        with open("clientes.json", "w") as arquivo:
            json.dump(dados, arquivo, indent=4)

class UI:
    @staticmethod
    def Menu():
        print("\n-- SISTEMA DE COMÉRCIO ELETRÔNICO - CLIENTES --")
        print("1 - Listar clientes")
        print("2 - Inserir cliente")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("5 - Sair")
        return int(input("Digite um número: "))

    @staticmethod
    def Main():
        ClienteDAO.Abrir()
        while True:
            try:
                op = UI.Menu()
                if op == 1:
                    UI.Cliente_Listar()
                elif op == 2:
                    UI.Cliente_Inserir()
                elif op == 3:
                    UI.Cliente_Atualizar()
                elif op == 4:
                    UI.Cliente_Excluir()
                elif op == 5:
                    print("Saindo do sistema...")
                    break
                else:
                    print("Opção inválida!")
            except ValueError as erro:
                print(f"Erro: {erro}")
            except Exception as erro:
                print(f"Ocorreu um erro inesperado: {erro}")

    @staticmethod
    def Cliente_Listar():
        clientes = ClienteDAO.Listar()
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            print("\n-- Lista de Clientes --")
            for c in clientes:
                print(c)

    @staticmethod
    def Cliente_Inserir():
        id = int(input("Informe o ID: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o telefone: ")
        c = Cliente(id, nome, email, fone)
        ClienteDAO.Inserir(c)
        print("Cliente cadastrado com sucesso!")

    @staticmethod
    def Cliente_Atualizar():
        UI.Cliente_Listar()
        clientes = ClienteDAO.Listar()
        if clientes:
            id = int(input("Informe o ID do cliente que deseja atualizar: "))
            c = ClienteDAO.Listar_Id(id)
            if c is not None:
                nome = input("Informe o novo nome: ")
                email = input("Informe o novo email: ")
                fone = input("Informe o novo telefone: ")
                c_novo = Cliente(id, nome, email, fone)
                ClienteDAO.Atualizar(c_novo)
                print("Cliente atualizado com sucesso!")
            else:
                print("Cliente não encontrado.")

    @staticmethod
    def Cliente_Excluir():
        UI.Cliente_Listar()
        clientes = ClienteDAO.Listar()
        if clientes:
            id = int(input("Informe o ID do cliente que deseja excluir: "))
            c = ClienteDAO.Listar_Id(id)
            if c is not None:
                ClienteDAO.Excluir(c)
                print("Cliente excluído com sucesso!")
            else:
                print("Cliente não encontrado.")

if __name__ == "__main__":
    UI.Main()

