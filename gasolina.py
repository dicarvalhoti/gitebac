
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_gasolina = pd.read_csv('./gasolina.csv', sep=',', encoding='utf-8')

plt.figure(figsize=(10, 6))
grafico_gasolina = sns.lineplot(x="dia", y="venda", data=df_gasolina, marker='o')
grafico_gasolina.set_xticklabels(labels=df_gasolina['dia'], rotation=45)

plt.title('Preço Médio da Gasolina em São Paulo - Julho 2021', fontsize=16)
plt.xlabel('Dia', fontsize=12)
plt.ylabel('Preço (R$)', fontsize=12)

plt.legend(['Preço da Gasolina'], loc='upper right')

plt.tight_layout()
plt.savefig('gasolina.png')
plt.show()
