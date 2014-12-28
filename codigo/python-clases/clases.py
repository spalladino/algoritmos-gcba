# Definimos la clase persona con atributos nombre, apellido, dni y fechaNacimiento
class Persona:

    # Init es el constructor, en esta funcion vamos a pasar como parametro los valores iniciales de los atributos
    # Recordar siempre pasar self como primer parametro
    def __init__(self, nombre, apellido, dni, fechaNacimiento):
        # Asignamos a cada atributo el valor del parametro
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fechaNacimiento = fechaNacimiento
        
    # Str nos devuelve un string que indica informalmente que es esta entidad
    # De nuevo, siempre self debe ser un primer parametro
    # Lo ejecutamos haciendo str(instancia)
    def __str__(self):
        # String formatting: donde aparece %s indica que se va a reemplazar por el contenido de esa posicion de la tupla
        # Por ejemplo: "Este %s un %s" % ("es", "ejemplo") == "Este es un ejemplo"
        return "%s %s, DNI %s, %s" % (self.nombre, self.apellido, self.dni, self.fechaNacimiento)

    # Repr deberia devolver una expresion python valida que genere esta instancia
    # Nuevamente, self siempre va como primer parametro
    # Lo ejecutamos haciendo repr(instancia), y va a ser llamado cada vez que se quiera mostrar el valor de la instancia actual por ejemplo dentro de una lista
    def __repr__(self):
        return "Persona(%s, %s, %s, %s)" % (self.nombre, self.apellido, self.dni, self.fechaNacimiento)

# Metodo para pedir los atributos de una persona por consola y crear una nueva instancia
def pedir_persona():
    # Con raw_input() levantamos lo que escribio el usuario, similar al cin de C++, pero nos devuelve siempre string
    print "Ingrese nombre:"
    nombre = raw_input()
    print "Apellido:"
    apellido = raw_input()
    # Como queremos que el DNI sea entero, lo convertimos de string a entero usando int()
    print "DNI:"
    dni = int(raw_input())
    # Lo mismo con el anio de nacimiento
    print "Anio nacimiento:"
    year = int(raw_input())
    
    # Creamos una nueva instancia de la clase persona con los valores que le pedimos al usuario
    nuevaPersona = Persona(nombre, apellido, dni, year)
    
    # Y la devolvemos
    return nuevaPersona


def main():
    # Pedimos la nueva persona
    persona = pedir_persona()
    print
    
    # Mostramos que es str(persona)
    print "str(persona)" 
    print str(persona)
    print
    
    # Lo mismo para repr
    print "repr(persona)" 
    print repr(persona)
    print
    
    # Podemos acceder a un atributo en particular y mostrarlo
    print "persona.apellido"
    print persona.apellido
    print
    
    # Podemos modificarlo y mostrar el nuevo valor
    print "persona.apellido = 'Nuevoapellido'"
    persona.apellido = 'Nuevoapellido'
    print "persona.apellido"
    print persona.apellido
    print

    # Y mostramos nuevamente la representacion despues de haber modificado la persona, notar que no hace falta el str()
    print "str(persona)" 
    print persona
    print


if __name__ == '__main__':
    main()

