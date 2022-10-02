import pyodbc

class Conexion:
    server = "DESKTOP"
    bd = "gymUdeM"
    usuario = "sa"
    contrasena = "sqlserver2008*"

    conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL server}; SERVER="+server+
                            f";DATABASE={bd}; UID={usuario};PWD={contrasena}")

##Seleccionar datos
    def select_in_database(self, consulta):
        habitaciones = []
        cursorSelect = self.conexion.cursor()

        cursorSelect.execute(consulta)


        Habitacion = cursorSelect.fetchone()

        while Habitacion:

            habitaciones.append(Habitacion)
            Habitacion = cursorSelect.fetchone()

        cursorSelect.close()

        return habitaciones
##Insertar datos
    def insert_in_database(self,consulta):
        """
        Inserta un nuevo objeto en la base de datos
        :arg Consulta: instrucciones para insertar en la base de datos
        """
        cursorInsert = self.conexion.cursor()

        cursorInsert.execute(consulta)
        cursorInsert.commit()
        cursorInsert.close()

##Actualizar datos
    def update_in_database(self, consulta):
        cursorUpdate = self.conexion.cursor()


        cursorUpdate.execute(consulta)

        cursorUpdate.commit()
        cursorUpdate.close()

##Elimiar datos
    def delete_in_database(self, consulta):
        cursorEliminar = self.conexion.cursor()


        cursorEliminar.execute(consulta)

        cursorEliminar.commit()
        cursorEliminar.close()




