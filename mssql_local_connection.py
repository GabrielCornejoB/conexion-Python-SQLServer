# Instalarlo si no se tiene: 'pip install pyodbc'
import pyodbc   

# Ej: ODBC Driver 17 for SQL Server (esto depende de la versión que se tenga instalada del driver)
# Pasos para encontrar la versión:
#   1. En el buscador de windows buscar la aplicación llamada: 'ODBC Data Sources' (tambien puede aparecer como
#   'Orígnenes de Datos ODBC')
#   2. Se abrirá una ventana, en esta debemos buscar la sección de 'Drivers' o 'Controladores'
#   3. Aquí en la columna 'Nombre' buscaremos la que diga 'ODBC Driver XX for SQL Server, y este es el 
#   parametro que necesitamos
param_driver = ""      

# Se obtiene entrando en la base de datos y colocando el comando SQL: "SELECT @@SERVERNAME;"
param_server = ""    

# El nombre de la base de datos a la que se va a acceder
param_database = ""                 

conn_params = "Driver={"+param_driver+"};Server="+param_server+";Database="+param_database+";Trusted_Connection=yes;"

conn = pyodbc.connect(conn_params)
cursor = conn.cursor()

# La query SQL que se quiera realizar en la base de datos específicada anteriormente
sql_query = "";                      
cursor.execute(sql_query)                  

# El resultado de la consulta queda almacenado en la variable 'cursor', y debemos usar la función fetchall()
# Para imprimirlo usamos un for, ya que estos resultados quedan almacenados como un arreglo
# Si queremos acceder solamente a una de las columnas del resultado de la consulta podemos colocar 'row[1]'
# y así acceder a los elementos en el indice 1 del resultado

for row in cursor.fetchall():
    print(row)