import pyodbc

# Ej: ODBC Driver 17 for SQL Server (esto depende de la versión que se tenga instalada del driver)
param_driver = ""      

# Se obtiene entrando en la base de datos y colocando el comando SQL: "SELECT @@SEVERNAME;"
param_server = ""    

# El nombre de la base de datos a la que se va a acceder
param_database = ""                 

conn_params = "Driver={"+param_driver+"};Server="+param_server+";Database="+param_database+";Trusted_Connection=yes;"

conn = pyodbc.connect(conn_params)
cursor = conn.cursor()

# La query SQL que se quiera realizar en la base de datos específicada anteriormente
sql_query = ""                      
cursor.execute(sql_query)                  

# En cursor queda el output del Query, toca imprimirlo línea a línea
for i in cursor:
    print(i)