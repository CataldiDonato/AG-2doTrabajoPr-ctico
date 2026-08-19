pesos = [1800, 600, 1200]
valores = [72, 36, 60]
pesoMaximo = 3000

mejorValor = 0
mejores = [0] * 3

# 3 bucles for: cada variable vale 0 (no llevar) o 1 (llevar)
for x0 in range(2):
    for x1 in range(2):
        for x2 in range(2):
            pesoTotal = x0*pesos[0] + x1*pesos[1] + x2*pesos[2]

            if pesoTotal <= pesoMaximo:
                valor = x0*valores[0] + x1*valores[1] + x2*valores[2]

                if valor > mejorValor:
                    mejorValor = valor
                    mejores = [x0, x1, x2]

# Reconstruir qué pesos se eligieron (los que quedaron en 1)
pesos_elegidos = [pesos[i] for i in range(3) if mejores[i] == 1]

print("El valor máximo es:", mejorValor)
print("Con los pesos:", pesos_elegidos)