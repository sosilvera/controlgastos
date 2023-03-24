-- Crear la tabla Bancos
CREATE TABLE Bancos (
    IdBanco INT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL
);

-- Crear la tabla Banco_Limites
CREATE TABLE Banco_Limites (
    Id INT PRIMARY KEY,
    IdBancoLimites INT NOT NULL,
    Limite_total DECIMAL(18,2) NOT NULL,
    Limite_actual DECIMAL(18,2) NOT NULL,
    FOREIGN KEY (IdBancoLimites) REFERENCES Bancos(IdBanco)
);

-- Crear la tabla Periodos
CREATE TABLE Periodos (
    IdPeriodo INT PRIMARY KEY,
    NumeroMes INT NOT NULL,
    NumeroAnio INT NOT NULL
);

-- Crear la tabla DeudaBCRA
CREATE TABLE DeudaBCRA (
    idDeuda INT PRIMARY KEY,
    idBanco INT NOT NULL,
    Total DECIMAL(18,2) NOT NULL,
    Situacion VARCHAR(50) NOT NULL,
    FOREIGN KEY (idBanco) REFERENCES Bancos(IdBanco)
);

-- Crear la tabla Gastos
CREATE TABLE Gastos (
    IdGasto INT PRIMARY KEY,
    Descripcion VARCHAR(50) NOT NULL,
    Monto DECIMAL(18,2) NOT NULL,
    idBanco INT NOT NULL,
    FechaCompra DATE NOT NULL,
    CuotasTotales INT NOT NULL,
    CuotasPagas INT NOT NULL,
    Intereses BIT NOT NULL, -- -> Bool
    ValorCuota DECIMAL(18,2) NOT NULL,
    MesPrimeraCuota INT NOT NULL, -- idPeriodo
    MesUltimaCuota INT NOT NULL, -- IdPeriodo + cuotas totales
    FOREIGN KEY (idBanco) REFERENCES Bancos(IdBanco),
    FOREIGN KEY (MesPrimeraCuota) REFERENCES Periodos(IdPeriodo),
    FOREIGN KEY (MesUltimaCuota) REFERENCES Periodos(IdPeriodo)
);