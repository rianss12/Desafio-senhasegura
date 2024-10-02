import matplotlib
matplotlib.use('Agg')  # Backend sem interface gráfica

import matplotlib.pyplot as plt

# Exemplo de gráfico
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.savefig('grafico.png')  # Salva o gráfico em um arquivo