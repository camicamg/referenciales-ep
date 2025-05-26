# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class LoginDao:

    def buscarUsuario(self, usu_nick: str):

        buscar_usuario_sql = """
        SELECT 
            id_usuario AS usu_id,
            nickname AS usu_nick,
            clave AS usu_clave,
            estado AS usu_estado
        FROM 
            usuarios
        WHERE 
            nickname = %s 
            AND estado IS TRUE;"""

        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(buscar_usuario_sql, (usu_nick,))
            usuario_encontrado = cur.fetchone() # Obtener una sola fila
            if usuario_encontrado:
                return {
                        "usu_id": usuario_encontrado[0]
                        , "usu_nick": usuario_encontrado[1]
                        , "usu_clave": usuario_encontrado[2]
                        , "usu_estado": usuario_encontrado[3]
                        }  # Retornar los datos de la usuario
            else:
                return None # Retornar None si no se encuentra el usuario
        except Exception as e:
            app.logger.error(f"Error al obtener usuario: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()