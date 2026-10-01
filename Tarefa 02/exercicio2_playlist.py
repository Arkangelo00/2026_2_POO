from datetime import datetime, timedelta

class Musica:
    def __init__(self, id: int, titulo: str, artista: str, album: str, duracao: timedelta):
        self.__id = id
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__duracao = duracao

    def get_id(self) -> int: return self.__id
    def set_id(self, id: int): self.__id = id

    def get_titulo(self) -> str: return self.__titulo
    def set_titulo(self, t: str): self.__titulo = t

    def get_artista(self) -> str: return self.__artista
    def set_artista(self, a: str): self.__artista = a

    def get_album(self) -> str: return self.__album
    def set_album(self, alb: str): self.__album = alb

    def get_duracao(self) -> timedelta: return self.__duracao
    def set_duracao(self, d: timedelta): self.__duracao = d

    def __str__(self) -> str:
        return f"ID: {self.__id} | Título: {self.__titulo} | Artista: {self.__artista} | Álbum: {self.__album} | Duração: {self.__duracao}"


class PlayList:
    def __init__(self, id: int, nome: str, descricao: str):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao

    def get_id(self) -> int: return self.__id
    def set_id(self, id: int): self.__id = id

    def get_nome(self) -> str: return self.__nome
    def set_nome(self, n: str): self.__nome = n

    def get_descricao(self) -> str: return self.__descricao
    def set_descricao(self, d: str): self.__descricao = d

    def tempo_total(self, itens_playlist, lista_musicas) -> timedelta:
        total = timedelta(0)
        meus_itens = [item for item in itens_playlist if item.get_id_playlist() == self.__id]
        for item in meus_itens:
            for m in lista_musicas:
                if m.get_id() == item.get_id_musica():
                    total += m.get_duracao()
        return total

    def __str__(self) -> str:
        return f"ID: {self.__id} | Nome: {self.__nome} | Descrição: {self.__descricao}"


class PlayListItem:
    def __init__(self, id: int, id_playlist: int, id_musica: int, data_inclusao: datetime, sequencia: int):
        self.__id = id
        self.__id_playlist = id_playlist
        self.__id_musica = id_musica
        self.__data_inclusao = data_inclusao
        self.__sequencia = sequencia

    def get_id(self) -> int: return self.__id
    def set_id(self, id: int): self.__id = id

    def get_id_playlist(self) -> int: return self.__id_playlist
    def set_id_playlist(self, ip: int): self.__id_playlist = ip

    def get_id_musica(self) -> int: return self.__id_musica
    def set_id_musica(self, im: int): self.__id_musica = im

    def get_data_inclusao(self) -> datetime: return self.__data_inclusao
    def set_data_inclusao(self, d: datetime): self.__data_inclusao = d

    def get_sequencia(self) -> int: return self.__sequencia
    def set_sequencia(self, s: int): self.__sequencia = s

    def __str__(self) -> str:
        dt_str = self.__data_inclusao.strftime("%d/%m/%Y %H:%M")
        return f"Item ID: {self.__id} | Playlist ID: {self.__id_playlist} | Música ID: {self.__id_musica} | Seq: {self.__sequencia} | Incluso em: {dt_str}"


class UI:
    playlists = []
    musicas = []
    playlist_itens = []

    @classmethod
    def menu(cls) -> int:
        print("\n================ MENU PLAYLIST ===============")
        print("--- GESTÃO DE MÚSICAS ---")
        print("1. Cadastrar Música           2. Listar Músicas")
        print("3. Atualizar Música           4. Excluir Música")
        print("--- GESTÃO DE PLAYLISTS ---")
        print("5. Criar Playlist             6. Listar Playlists")
        print("7. Atualizar Playlist         8. Excluir Playlist")
        print("9. Ver Tempo Total de uma Playlist")
        print("--- ITENS DA PLAYLIST ---")
        print("10. Adicionar Música à Playlist")
        print("11. Listar Músicas de uma Playlist")
        print("12. Remover Música de uma Playlist")
        print("0. Sair")
        try:
            return int(input("Opção: "))
        except ValueError:
            return -1

    @classmethod
    def inserir_musica(cls):
        print("\n--- Inserir Música ---")
        try:
            id_m = int(input("ID da Música: "))
            titulo = input("Título: ")
            artista = input("Artista: ")
            album = input("Álbum: ")
            dur_seg = int(input("Duração (em segundos): "))
            m = Musica(id_m, titulo, artista, album, timedelta(seconds=dur_seg))
            cls.musicas.append(m)
            print("Música cadastrada com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    @classmethod
    def listar_musicas(cls):
        print("\n--- Lista de Músicas ---")
        if not cls.musicas:
            print("Nenhuma música cadastrada.")
        for m in cls.musicas:
            print(m)

    @classmethod
    def inserir_playlist(cls):
        print("\n--- Inserir Playlist ---")
        try:
            id_p = int(input("ID da Playlist: "))
            nome = input("Nome: ")
            desc = input("Descrição: ")
            p = PlayList(id_p, nome, desc)
            cls.playlists.append(p)
            print("Playlist criada com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    @classmethod
    def listar_playlists(cls):
        print("\n--- Lista de Playlists ---")
        if not cls.playlists:
            print("Nenhuma playlist cadastrada.")
        for p in cls.playlists:
            print(p)

    @classmethod
    def tempo_total_playlist(cls):
        print("\n--- Tempo Total da Playlist ---")
        try:
            id_p = int(input("ID da Playlist: "))
            p = next((x for x in cls.playlists if x.get_id() == id_p), None)
            if p:
                tempo = p.tempo_total(cls.playlist_itens, cls.musicas)
                print(f"Playlist: {p.get_nome()} | Duração Total: {tempo}")
            else:
                print("Playlist não encontrada.")
        except Exception as e:
            print(f"Erro: {e}")

    @classmethod
    def inserir_item_playlist(cls):
        print("\n--- Adicionar Música à Playlist ---")
        try:
            id_item = int(input("ID do Item: "))
            id_p = int(input("ID da Playlist: "))
            id_m = int(input("ID da Música: "))
            seq = int(input("Sequência/Ordem na Playlist: "))

            if not any(p.get_id() == id_p for p in cls.playlists):
                print("Playlist não encontrada.")
                return
            if not any(m.get_id() == id_m for m in cls.musicas):
                print("Música não encontrada.")
                return

            item = PlayListItem(id_item, id_p, id_m, datetime.now(), seq)
            cls.playlist_itens.append(item)
            print("Música adicionada à playlist com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    @classmethod
    def listar_itens_playlist(cls):
        print("\n--- Músicas da Playlist ---")
        try:
            id_p = int(input("ID da Playlist: "))
            itens = [i for i in cls.playlist_itens if i.get_id_playlist() == id_p]
            itens.sort(key=lambda x: x.get_sequencia())

            if not itens:
                print("Nenhuma música nesta playlist.")
                return

            for item in itens:
                musica = next((m for m in cls.musicas if m.get_id() == item.get_id_musica()), None)
                if musica:
                    print(f"Ordem: {item.get_sequencia()} | {musica}")
        except Exception as e:
            print(f"Erro: {e}")

    @classmethod
    def main(cls):
        op = -1
        while op != 0:
            op = cls.menu()
            if op == 1: cls.inserir_musica()
            elif op == 2: cls.listar_musicas()
            elif op == 5: cls.inserir_playlist()
            elif op == 6: cls.listar_playlists()
            elif op == 9: cls.tempo_total_playlist()
            elif op == 10: cls.inserir_item_playlist()
            elif op == 11: cls.listar_itens_playlist()
            elif op == 0: print("Saindo da aplicação...")

if __name__ == "__main__":
    UI.main()