# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class TipoconsultaDao:

    def getTipoconsultas(self):

        tipoconsultaSQL = """
        SELECT id, descripcion
        FROM tipoconsultas
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(tipoconsultaSQL)
            tipoconsultas = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': tipoconsulta[0], 'descripcion': tipoconsulta[1]} for tipoconsulta in tipoconsultas]

        except Exception as e:
            app.logger.error(f"Error al obtener todos los tipoconsultas: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getTipoconsultaById(self, id):

        tipoconsultaSQL = """
        SELECT id, descripcion
        FROM tipoconsultas WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(tipoconsultaSQL, (id,))
            tipoconsultaEncontrada = cur.fetchone() # Obtener una sola fila
            if tipoconsultaEncontrada:
                return {
                        "id": tipoconsultaEncontrada[0],
                        "descripcion": tipoconsultaEncontrada[1]
                    }  # Retornar los datos del tipoconsulta
            else:
                return None # Retornar None si no se encuentra el tipoconsulta
        except Exception as e:
            app.logger.error(f"Error al obtener tipoconsulta: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarTipoconsulta(self, descripcion):

        insertTipoconsultaSQL = """
        INSERT INTO tipoconsultas(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertTipoconsultaSQL, (descripcion,))
            tipoconsulta_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return tipoconsulta_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar tipoconsulta: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateTipoconsulta(self, id, descripcion):

        updateTipoconsultaSQL = """
        UPDATE tipoconsultas
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateTipoconsultaSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar tipoconsulta: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteTipoconsulta(self, id):

        updateTipoconsultaSQL = """
        DELETE FROM tipoconsultas
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateTipoconsultaSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar tipoconsulta: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()