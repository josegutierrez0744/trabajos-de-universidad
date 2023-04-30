 CREATE DATABASE diccionario;
USE diccionario;

 CREATE TABLE palabras (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    palabra VARCHAR(50) NOT NULL,
    significado TEXT NOT NULL
)
