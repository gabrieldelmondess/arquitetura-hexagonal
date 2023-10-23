if __name__ == '__main__':
    from domain import Musician, Album
    from repositories import MusicianRepository, AlbumRepository
    from use_cases import CreateMusician, CreateAlbum

    # configuração de repositórios
    musician_repository = MusicianRepository()
    album_repository = AlbumRepository()

    # exemplo de uso de casos de uso
    create_musician = CreateMusician(musician_repository)
    create_musician.execute("John", "Doe", "Guitar")

    create_album = CreateAlbum(album_repository)
    create_album.execute(Musician("John", "Doe", "Guitar"), "Album 1", "2023-10-17", 5)