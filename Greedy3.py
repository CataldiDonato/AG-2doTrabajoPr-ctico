#1.CREACION DE LA CLASE---------------------
# Creacion de la clase Objeto para encapsular las propiedades de cada elemento.
class Objeto:
    def __init__(self, id_objeto, volumen, valor):

        self.id_objeto = id_objeto
        self.volumen = volumen
        self.valor = valor
        # Calculo la densidad al momento de instanciar el objeto.
        self.densidad = valor / volumen 

#2. CARGA DE OBJETOS---------------------
# Carga de los 3 objetos exactamente como figuran en la tabla del enunciado.
lista_objetos = [
    Objeto(1, 1800, 72),
    Objeto(2, 600, 36),
    Objeto(3, 1200, 60)
]

volumen_maximo = 3000 # Límite de la mochila

#3.ORDENAMIENTO DE OBJETOS---------------------
# Ordenamiento de la lista de objetos de mayor a menor basándonos en su 'densidad' esto permite obtener el mejor resultado en relacion precio/volumen.
# Uso de una función lambda para indicarle a Python qué atributo mirar para ordenar.
objetos_ordenados = sorted(lista_objetos, key=lambda obj: obj.densidad, reverse=True)

# 4. PREPARACION DE VARIABLES---------------------
# Prepacion de las variables para monitorear el llenado de la mochila.
mochila_seleccionada = []
volumen_acumulado = 0
valor_total_acumulado = 0

# 5.EL CICLO DE SELECCIÓN-----------------
# Recorrido de la lista de objetos que ya está ordenada por rentabilidad.
for obj in objetos_ordenados:
    
    # Se verifica si el objeto actual entra en el espacio restante de la mochila.
    if volumen_acumulado + obj.volumen <= volumen_maximo:
        
        # Si entra, se agrega a la mochila y se actualiza los contadores.
        mochila_seleccionada.append(obj.id_objeto)
        volumen_acumulado += obj.volumen
        valor_total_acumulado += obj.valor
        
    # Si no entra, el ciclo simplemente lo ignora y pasa al siguiente de la lista.


# 6. RESULTADOS---------------------
# Se muestra en consola cómo quedó conformada la solución.
print("--- RESULTADO DEL ALGORITMO GREEDY ---")
print(f"Objetos seleccionados (IDs): {mochila_seleccionada}")
print(f"Volumen total ocupado: {volumen_acumulado} cm³ (Límite: {volumen_maximo} cm³)")
print(f"Valor total obtenido: ${valor_total_acumulado}")