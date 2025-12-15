from config.db import get_connection

class CrudService:

    def tambah_film(self, film):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO film (judul, genre, durasi) VALUES (%s,%s,%s)",
            (film.judul, film.genre, film.durasi)
        )
        db.commit()
        print("Film berhasil ditambahkan")

    def lihat_film(self):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM film")
        print("\nID | Judul | Genre | Durasi")
        print("-" * 40)
        for f in cursor.fetchall():
            print(f"{f[0]:<3}| {f[1]:<12}| {f[2]:<8}| {f[3]} menit")

    def pesan_tiket(self, tiket):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO tiket (nama_pemesan, jumlah, film_id) VALUES (%s,%s,%s)",
            (tiket.nama, tiket.jumlah, tiket.film_id)
        )
        db.commit()
        print("Tiket berhasil dipesan")

    def lihat_tiket(self):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT tiket.id, tiket.nama_pemesan, tiket.jumlah, film.judul
            FROM tiket
            JOIN film ON tiket.film_id = film.id
        """)

        print("\n=== DAFTAR PESANAN TIKET ===")
        print("ID | Nama Pemesan | Jumlah | Judul Film")
        print("-" * 45)
        for t in cursor.fetchall():
            print(f"{t[0]:<3}| {t[1]:<13}| {t[2]:<7}| {t[3]}")
