CREATE DATABASE articulos;

USE articulos;

CREATE TABLE usuarios ( id INT NOT NULL AUTO_INCREMENT, usuario VARCHAR(50) NULL, password VARCHAR(50) NULL, PRIMARY KEY (id));

DELIMITER $$
CREATE PROCEDURE spCrearUsuario (IN pusuario VARCHAR(50), IN ppassword VARCHAR(50))
       BEGIN
         IF EXISTS (SELECT (1) FROM usuarios WHERE usuario = pusuario) THEN
             SELECT "Usuario Existente!";
         ELSE
             INSERT INTO usuarios
             (
                 usuario,
                 password
             )
             VALUES (
                 pusuario,
                 ppassword
             );
         END IF;
       END$$
DELIMITER ;


DELIMITER //
CREATE PROCEDURE spAutenticarUsuario (IN pusuario VARCHAR(50))
    BEGIN
        SELECT * FROM usuarios WHERE usuario = pusuario;
    END//
DELIMITER ;


CREATE TABLE articulo (
    id INT NULL AUTO_INCREMENT PRIMARY KEY,
    id_usuario VARCHAR(50) NULL,
    articulo VARCHAR(50) NULL
)

DELIMITER $$
CREATE PROCEDURE spAgregarArticulos (
IN pusuario INT,
IN particulo VARCHAR(50)
)
BEGIN
    INSERT INTO articulo(id_usuario, articulo)
    VALUES(pusuario, particulo);
END$$
DELIMITER ;