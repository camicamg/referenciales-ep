# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class PersonaDao:

    def getPersonas(self):

        personaSQL = """
        SELECT id, descripcion
        FROM personas
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(personaSQL)
            personas = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': persona[0], 'descripcion': persona[1]} for persona in personas]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las personas: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getPersonaById(self, id):

        personaSQL = """
        SELECT id, descripcion
        FROM personas WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(personaSQL, (id,))
            personaEncontrada = cur.fetchone() # Obtener una sola fila
            if personaEncontrada:
                return {
                        "id": personaEncontrada[0],
                        "descripcion": personaEncontrada[1]
                    }  # Retornar los datos de la persona
            else:
                return None # Retornar None si no se encuentra la persona
        except Exception as e:
            app.logger.error(f"Error al obtener persona: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarPersona(self, descripcion):

        insertPersonaSQL = """
        INSERT INTO personas(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertPersonaSQL, (descripcion,))
            persona_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return persona_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar persona: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updatePersona(self, id, descripcion):

        updatePersonaSQL = """
        UPDATE personas
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updatePersonaSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar persona: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deletePersona(self, id):

        updatePersonaSQL = """
        DELETE FROM personas
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updatePersonaSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar persona: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()