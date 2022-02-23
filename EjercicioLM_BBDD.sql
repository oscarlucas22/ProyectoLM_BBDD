CREATE TABLE SOCIOS (
    DNI VARCHAR (10) PRIMARY KEY NOT NULL,
    Nombre VARCHAR (20) NOT NULL,
    Direccion VARCHAR (20)
);

CREATE TABLE PELICULAS (
    RefPelicula VARCHAR (10) NOT NULL,
    NombrePelicula VARCHAR (20) NOT NULL,
    Genero VARCHAR (10) NOT NULL,
    Director VARCHAR (20),
    AnoEstreno DATE,
    Nacionalidad VARCHAR (20) NOT NULL,
    CONSTRAINT anoestreno_check CHECK (YEAR(AnoEstreno) > 1900)
);

CREATE TABLE PRESTAMOS (
    DNI_fk VARCHAR (10) NOT NULL,
    RefPelicula_fk VARCHAR (10) NOT NULL,
    FechaPrestamo DATE NOT NULL,
    Importe INT (3) NOT NULL DEFAULT (400),
    CONSTRAINT pri PRIMARY KEY (DNI_fk,RefPelicula_fk,FechaPrestamo),
    CONSTRAINT DNI_ajena FOREIGN KEY DNI_fk REFERENCES SOCIOS(DNI),
    CONSTRAINT RefPelicula_ajena FOREIGN KEY RefPelicula_fk REFERENCES PELICULAS(RefPelicula)
);