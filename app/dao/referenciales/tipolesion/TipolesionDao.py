# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class TipolesionDao:

    def getTipolesiones(self):

        tipolesionSQL = """
        SELECT id, descripcion
        FROM tipolesiones
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(tipolesionSQL)
            tipolesiones = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': tipolesion[0], 'descripcion': tipolesion[1]} for tipolesion in tipolesiones]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las tipolesiones: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getTipolesionById(self, id):

        tipolesionSQL = """
        SELECT id, descripcion
        FROM tipolesiones WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(tipolesionSQL, (id,))
            tipolesionEncontrada = cur.fetchone() # Obtener una sola fila
            if tipolesionEncontrada:
                return {
                        "id": tipolesionEncontrada[0],
                        "descripcion": tipolesionEncontrada[1]
                    }  # Retornar los datos del tipolesion
            else:
                return None # Retornar None si no se encuentra el tipolesion
        except Exception as e:
            app.logger.error(f"Error al obtener tipolesion: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarTipolesion(self, descripcion):

        insertTipolesionSQL = """
        INSERT INTO tipolesiones(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertTipolesionSQL, (descripcion,))
            tipolesion_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return tipolesion_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar tipolesion: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateTipolesion(self, id, descripcion):

        updateTipolesionSQL = """
        UPDATE tipolesiones
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateTipolesionSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar tipolesion: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteTipolesion(self, id):

        updateTipolesionSQL = """
        DELETE FROM tipolesiones
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateTipolesionSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar tipolesion: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()