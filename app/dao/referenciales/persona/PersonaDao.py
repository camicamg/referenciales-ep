# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class PersonaDao:

    def getPersonas(self):
        #id_persona nombres apellidos fecha_ingreso
        personaSQL = """
        SELECT id_persona, nombres, apellidos, fecha_ingreso, ci
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
            return [{'id': persona[0],'nombres_completo': f"{persona[1]} {persona[2]}", 'nombres': persona[1], 'apellidos': persona[2], 'fecha_ingreso': persona[3].strftime('%d/%m/%Y'), 'ci': persona[4]} for persona in personas]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las personas: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getPersonaById(self, id):
        #id_persona nombres apellidos fecha_ingreso ci
        personaSQL = """
        SELECT id_persona, nombres, apellidos, telefono, correo, direccion, ci
        FROM personas WHERE id_persona=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(personaSQL, (id,))
            personaEncontrada = cur.fetchone()  # Obtener una sola fila
            if personaEncontrada:
                return {
                    "id": personaEncontrada[0],
                    "nombre": personaEncontrada[1],
                    "apellido": personaEncontrada[2],
                    "telefono": personaEncontrada[3],
                    "correo": personaEncontrada[4],
                    "direccion": personaEncontrada[5],
                    "ci":personaEncontrada[6]
                }  # Retornar los datos de persona
            else:
                return None  # Retornar None si no se encuentra la persona
        except Exception as e:
            app.logger.error(f"Error al obtener persona: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarPersona(self, nombre, apellido, telefono, correo, direccion,ci):
        usuId = 1
        insertPersonaSQL = """
        INSERT INTO personas(nombres, apellidos, telefono, correo, direccion, ci, creacion_fecha, creacion_hora, creacion_usuario ) VALUES(%s, %s, %s, %s, %s, %s, CURRENT_DATE, NOW(), %s) RETURNING id_persona
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertPersonaSQL, (nombre, apellido, telefono, correo, direccion, ci, usuId))
            persona_id = cur.fetchone()[0]
            con.commit()  # se confirma la insercion
            print("Commit ejecutado correctamente!!!", persona_id)

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

    def updatePersona(self, id, nombre, apellido, telefono, correo, direccion):
        updatePersonaSQL = """
        UPDATE personas
        SET nombreS=%s, apellidoS=%s, telefono=%s, correo=%s, direccion=%s
        WHERE id_persona=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updatePersonaSQL, (nombre, apellido, telefono, correo, direccion, id))
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
        WHERE id_persona=%s
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