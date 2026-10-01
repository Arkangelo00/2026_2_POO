from datetime import datetime, timedelta

class Treino:
    def __init__(self, id: int, dt: datetime, ds: float, t: timedelta):
        self.__id = id
        self.__data = dt
        self.__distancia = ds
        self.__tempo = t

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_data(self) -> datetime:
        return self.__data

    def set_data(self, dt: datetime):
        self.__data = dt

    def get_distancia(self) -> float:
        return self.__distancia

    def set_distancia(self, ds: float):
        self.__distancia = ds

    def get_tempo(self) -> timedelta:
        return self.__tempo

    def set_tempo(self, t: timedelta):
        self.__tempo = t

    def pace(self) -> timedelta:
        if self.__distancia <= 0:
            return timedelta(0)
        segundos_totais = self.__tempo.total_seconds()
        segundos_por_km = segundos_totais / self.__distancia
        return timedelta(seconds=segundos_por_km)

    def __str__(self) -> str:
        pace_td = self.pace()
        total_segundos = int(pace_td.total_seconds())
        minutos = total_segundos // 60
        segundos = total_segundos % 60
        data_str = self.__data.strftime("%d/%m/%Y %H:%M")
        return (f"ID: {self.__id} | Data: {data_str} | "
                f"Distância: {self.__distancia:.2f} km | Tempo: {self.__tempo} | "
                f"Pace: {minutos:02d}:{segundos:02d} min/km")


class TreinoUI:
    treinos = []

    @classmethod
    def menu(cls) -> int:
        print("\n=== MENU TREINOS ===")
        print("1. Inserir treino")
        print("2. Listar todos os treinos")
        print("3. Listar treino por ID")
        print("4. Atualizar treino")
        print("5. Excluir treino")
        print("6. Treino mais rápido (menor pace)")
        print("0. Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    @classmethod
    def inserir(cls):
        print("\n--- Inserir Treino ---")
        try:
            id_t = int(input("ID: "))
            data_str = input("Data e Hora (dd/mm/aaaa hh:mm): ")
            dt = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
            ds = float(input("Distância (km): "))
            minutos = int(input("Tempo de corrida (em minutos): "))
            t = timedelta(minutes=minutos)

            novo_treino = Treino(id_t, dt, ds, t)
            cls.treinos.append(novo_treino)
            print("Treino inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir treino: {e}")

    @classmethod
    def listar(cls):
        print("\n--- Lista de Treinos ---")
        if not cls.treinos:
            print("Nenhum treino cadastrado.")
            return
        for t in cls.treinos:
            print(t)

    @classmethod
    def listar_id(cls):
        print("\n--- Buscar Treino por ID ---")
        try:
            id_t = int(input("Informe o ID do treino: "))
            for t in cls.treinos:
                if t.get_id() == id_t:
                    print(t)
                    return
            print("Treino não encontrado.")
        except ValueError:
            print("ID inválido.")

    @classmethod
    def atualizar(cls):
        print("\n--- Atualizar Treino ---")
        try:
            id_t = int(input("Informe o ID do treino a atualizar: "))
            for t in cls.treinos:
                if t.get_id() == id_t:
                    data_str = input("Nova Data e Hora (dd/mm/aaaa hh:mm): ")
                    dt = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
                    ds = float(input("Nova Distância (km): "))
                    minutos = int(input("Novo Tempo (minutos): "))
                    
                    t.set_data(dt)
                    t.set_distancia(ds)
                    t.set_tempo(timedelta(minutes=minutos))
                    print("Treino atualizado com sucesso!")
                    return
            print("Treino não encontrado.")
        except Exception as e:
            print(f"Erro ao atualizar: {e}")

    @classmethod
    def excluir(cls):
        print("\n--- Excluir Treino ---")
        try:
            id_t = int(input("Informe o ID do treino a excluir: "))
            for t in cls.treinos:
                if t.get_id() == id_t:
                    cls.treinos.remove(t)
                    print("Treino excluído com sucesso!")
                    return
            print("Treino não encontrado.")
        except ValueError:
            print("ID inválido.")

    @classmethod
    def mais_rapido(cls):
        print("\n--- Treino Mais Rápido (Menor Pace) ---")
        if not cls.treinos:
            print("Nenhum treino cadastrado.")
            return
        treino_rapido = min(cls.treinos, key=lambda t: t.pace())
        print(treino_rapido)

    @classmethod
    def main(cls):
        op = -1
        while op != 0:
            op = cls.menu()
            if op == 1:
                cls.inserir()
            elif op == 2:
                cls.listar()
            elif op == 3:
                cls.listar_id()
            elif op == 4:
                cls.atualizar()
            elif op == 5:
                cls.excluir()
            elif op == 6:
                cls.mais_rapido()
            elif op == 0:
                print("Encerrando a aplicação...")
            else:
                print("Opção inválida!")


if __name__ == "__main__":
    TreinoUI.main()