USE [ControlGastos_PROD]
GO

INSERT INTO [dbo].[Gasto_Mes]
           ([idGasto]
           ,[idPeriodo]
           ,[monto])
     VALUES
           (<idGasto, int,>
           ,<idPeriodo, int,>
           ,<monto, decimal(10,2),>)
GO

