import psycopg2

class Conexion:

    """Metodo constructor
    """
    def __init__(self):
        # https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.parse_dsn
        dbname = "mi Bd"
        user = "postgres"
        password = "Amanece.1"
        host = "localhost"
        port = 5432
        #self.con = psycopg2.connect("dbname=veterinaria-db user=juandba host=localhost password=admin")
        self.con = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

    """getConexion

        retorna la instancia de la base de datos
    """
    def getConexion(self):
        return self.con