print("Introduccion a clases")
class Animal:
    edad=3
    raza= "chihuas"
    comida="croquetas"
    def come(self):
        print(f"el perro come "+self.comida)
print(Animal)
print("Creando el objeto de la clase animal")
perro=Animal()

print(f"edad del perro {perro.edad}")
print(f"raza del perro {perro.raza}")
perro.come()
