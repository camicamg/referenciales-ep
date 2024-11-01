# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class PersonaDao:

    def getPersonas(self):

        personaSQL = """
        SELECT id, nombre, direccion, telefono, correo_electronico, sexo
        FROM personas
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(personaSQL)
            personas = cur.fetchall()  # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': persona[0], 'nombre': persona[1], 'direccion': persona[2], 
                     'telefono': persona[3], 'correo_electronico': persona[4], 'sexo': persona[5] } for persona in personas]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las personas: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getPersonaById(self, id):

        personaSQL = """
        SELECT id, nombre, direccion, telefono, correo_electronico, sexo
        FROM personas WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(personaSQL, (id,))
            personaEncontrado = cur.fetchone()  # Obtener una sola fila
            if personaEncontrado:
                return {
                    "id": personaEncontrado[0],
                    "nombre": personaEncontrado[1],
                    "direccion": personaEncontrado[2],
                    "telefono": personaEncontrado[3],
                    "correo_electronico": personaEncontrado[4],
                    "sexo": personaEncontrado[5]
                }  # Retornar los datos de la persona
            else:
                return None  # Retornar None si no se encuentra la persona
        except Exception as e:
            app.logger.error(f"Error al obtener persona: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarPersona(self, nombre, direccion, telefono, correo_electronico, sexo):

        insertPersonaSQL = """
        INSERT INTO personas(nombre, direccion, telefono, correo_electronico, sexo) 
        VALUES(%s, %s, %s, %s, %s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertPersonaSQL, (nombre, direccion, telefono, correo_electronico, sexo,))
            persona_id = cur.fetchone()[0]
            con.commit()  # se confirma la insercion
            return persona_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar persona: {str(e)}")
            con.rollback()  # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updatePersona(self, id, nombre, direccion, telefono, correo_electronico, sexo):

        updatePersonaSQL = """
        UPDATE personas
        SET nombre=%s, direccion=%s, telefono=%s, correo_electronico=%s, sexo=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updatePersonaSQL, (nombre, direccion, telefono, correo_electronico, sexo, id,))
            filas_afectadas = cur.rowcount  # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0  # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar persona: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deletePersona(self, id):

        deletePersonaSQL = """
        DELETE FROM personas
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deletePersonaSQL, (id,))
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