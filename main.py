from models.film import Film
from models.tiket import Tiket
from services.crud_service import CrudService

service = CrudService()

while True:
    print("\n=== MENU BIOSKOP ===")
    print("1. Tambah Film")
    print("2. Lihat Film")
    print("3. Pesan Tiket")
    print("4. Lihat Pesanan Tiket")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        judul = input("Judul Film: ")
        genre = input("Genre: ")
        durasi = int(input("Durasi (menit): "))
        service.tambah_film(Film(judul, genre, durasi))

    elif pilihan == '2':
        service.lihat_film()

    elif pilihan == '3':
        nama = input("Nama Pemesan: ")
        jumlah = int(input("Jumlah Tiket: "))
        film_id = int(input("ID Film: "))
        service.pesan_tiket(Tiket(nama, jumlah, film_id))

    elif pilihan == '4':
        service.lihat_tiket()

    elif pilihan == '5':
        print("Terima kasih")
        break

    else:
        print("Pilihan tidak valid")
