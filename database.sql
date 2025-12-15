CREATE DATABASE bioskop;
USE bioskop;

CREATE TABLE film (
    id INT AUTO_INCREMENT PRIMARY KEY,
    judul VARCHAR(100),
    genre VARCHAR(50),
    durasi INT
);

CREATE TABLE tiket (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_pemesan VARCHAR(100),
    jumlah INT,
    film_id INT,
    FOREIGN KEY (film_id) REFERENCES film(id)
);