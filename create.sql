-- Crear la tabla Bancos
CREATE TABLE Bancos (
    IdBanco INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(50) NOT NULL
);

-- Crear la tabla Banco_Limites
CREATE TABLE Banco_Limites (
    Id INT PRIMARY KEY IDENTITY(1,1),
    IdBancoLimites INT NOT NULL,
    Limite_total DECIMAL(18,2) NOT NULL,
    Limite_actual DECIMAL(18,2) NOT NULL,
    FOREIGN KEY (IdBancoLimites) REFERENCES Bancos(IdBanco)
);

-- Crear la tabla Periodos
CREATE TABLE Periodos (
    IdPeriodo INT PRIMARY KEY IDENTITY(1,1),
    NumeroMes INT NOT NULL,
    NumeroAnio INT NOT NULL,
    descripcion VARCHAR(20)
);

-- Crear la tabla DeudaBCRA
CREATE TABLE DeudaBCRA (
    idDeuda INT PRIMARY KEY IDENTITY(1,1),
    idBanco INT NOT NULL,
    Total DECIMAL(18,2) NOT NULL,
    Situacion VARCHAR(50) NOT NULL,
    FOREIGN KEY (idBanco) REFERENCES Bancos(IdBanco)
);

-- Crear la tabla Gastos
CREATE TABLE Gastos (
    idGasto INT PRIMARY KEY IDENTITY(1,1),
    descripcion VARCHAR(50) NOT NULL,
    monto DECIMAL(18,2) NOT NULL,
    idBanco INT NOT NULL,
    fechaCompra DATE NOT NULL,
    cuotasTotales INT NOT NULL,
    cuotasPagas INT NOT NULL,
    intereses BIT NOT NULL, -- -> Bool
    valorCuota DECIMAL(18,2) NOT NULL,
    mesPrimeraCuota INT NOT NULL, -- idPeriodo
    mesUltimaCuota INT NOT NULL, -- IdPeriodo + cuotas totales
    FOREIGN KEY (idBanco) REFERENCES Bancos(IdBanco),
    FOREIGN KEY (MesPrimeraCuota) REFERENCES Periodos(IdPeriodo),
    FOREIGN KEY (MesUltimaCuota) REFERENCES Periodos(IdPeriodo)
);

CREATE TABLE Gasto_Mes (
    idGasto_Mes INT PRIMARY KEY IDENTITY(1,1),
    idGasto INT NOT NULL,
    idPeriodo INT NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    CONSTRAINT FK_Gasto_Mes_Gastos FOREIGN KEY (idGasto) REFERENCES Gastos (IdGasto),
    CONSTRAINT FK_Gasto_Mes_Periodos FOREIGN KEY (idPeriodo) REFERENCES Periodos (IdPeriodo)
);