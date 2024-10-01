import pandas as pd
import seaborn as sns

df_gasolina = pd.read_csv('./gasolina.csv', sep=',', encoding='utf-8')
df_gasolina.head(n=10)

grafico_gasolina = sns.lineplot(x="dia", y="venda", data=df_gasolina)
_ = grafico_gasolina.set_xticklabels(labels=df_gasolina['dia'], rotation=90)