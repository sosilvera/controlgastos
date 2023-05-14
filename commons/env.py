DBNAME = 'ControlGastos_PROD'
TRUSTED_CONNECTION = 'yes'
LOCAL = False

if LOCAL:
    SERVER = 'DESKTOP-0NB8DVB\SQLEXPRESS' #Server Seba 
    STRING_CONNECTION = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+SERVER+';DATABASE='+DBNAME+';Trusted_Connection='+TRUSTED_CONNECTION
else:
    STRING_CONNECTION='DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:dbcontrolgastos.database.windows.net,1433;Database=controlgastosdb;Uid=controlgastosad;Pwd=123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
