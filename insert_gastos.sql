USE [ControlGastos_PROD]
GO

INSERT INTO [dbo].[Gastos]
           ([descripcion]
           ,[monto]
           ,[idBanco]
           ,[fechaCompra]
           ,[cuotasTotales]
           ,[cuotasPagas]
           ,[intereses]
           ,[valorCuota]
           ,[mesPrimeraCuota]
           ,[mesUltimaCuota])
     VALUES
           (<descripcion, varchar(50),>
           ,<monto, decimal(18,2),>
           ,<idBanco, int,>
           ,<fechaCompra, date,>
           ,<cuotasTotales, int,>
           ,<cuotasPagas, int,>
           ,<intereses, bit,>
           ,<valorCuota, decimal(18,2),>
           ,<mesPrimeraCuota, int,>
           ,<mesUltimaCuota, int,>)
GO

