class Cliente:
    def __init__(self, nome, cpf, limite):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_limite(limite)
        self.__socio = None
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def set_cpf(self, cpf):
        if cpf == "": raise ValueError("CPF deve ser informado")
        self.__cpf = cpf
    def set_limite(self, limite):
        if limite < 0: raise ValueError("Limite deve ser positivo")
        self.__limite = limite
    def set_socio(self, c):
        a = self  # primeiro cliente
        b = c     # segundo cliente

        # sa é o sócio atual de a
        sa = a.__socio
        # a tem algum sócio? Se sim, o sócio (sa) dele não é mais a
        if sa != None: sa.__socio = None

        # sb é o sócio atual de b
        sb = b.__socio
        if sb != None: sb.__socio = None

        a.__socio = b
        b.__socio = a

        #self.__socio = c
        #c.__socio = self
    def get_nome(self) : return self.__nome
    def get_cpf(self) : return self.__cpf
    def get_limite(self) : 
        if self.__socio == None: return self.__limite
        return self.__limite + self.__socio.__limite 
    def get_socio(self): return self.__socio
    def __str__(self):
        return f"{self.__nome} - {self.__cpf} - {self.__limite:.2f} - {self.get_limite():.2f}"

c1 = Cliente("Eduardo", "123456", 1000)
c2 = Cliente("Jorgiano", "654321", 2000)
c1.set_socio(c2)
print(c1, "sócio:", c1.get_socio().get_nome())
print(c2, "sócio:", c2.get_socio().get_nome())

#print(c1.get_socio().get_socio().get_nome())

c3 = Cliente("Danielle", "112233", 3000)
c4 = Cliente("Silvia", "332211", 4000)
c3.set_socio(c4)
print(c3, "sócio:", c3.get_socio().get_nome())
print(c4, "sócio:", c4.get_socio().get_nome())

# antes
# c1 é sócio de c2
# c2 é sócio de c1
# c3 é sócio de c4
# c4 é sócio de c3

# depois
# c1 é sócio de c3
# c2 tem que ficar sem sócio
# c3 é sócio de c1
# c4 tem que ficar sem sócio

# quando for ligar c1 a c3
# c1 tem algum sócio? 
# sócio de c1: s1 = c1.__socio
# if s1 != None: s1.__socio = None  

# quando for ligar c3 a c1
# c3 tem algum sócio? 
# s3 = c3.__socio
# if s3 != None: s3.__socio = None  

c1.set_socio(c3)
print(c1, "sócio:", c1.get_socio())
print(c2, "sócio:", c2.get_socio())
print(c3, "sócio:", c3.get_socio())
print(c4, "sócio:", c4.get_socio())





