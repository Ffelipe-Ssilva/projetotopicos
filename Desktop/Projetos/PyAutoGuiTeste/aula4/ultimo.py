import pandas as pd
import sklearn
tabela=pd.read_csv("advertising.csv")
print(tabela)
print("------------------------------------------------------------------------")
#tem que importar plot lib pra usar seaborn
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(tabela.corr(),cmap="Wistia",annot=True)
plt.show()

x=tabela[["TV","Radio","Jornal"]]
y=tabela["Vendas"]
#remover random state de train test parentesis
from sklearn.model_selection import train_test_split
xtreino,xteste,ytreino,yteste = train_test_split(x,y,test_size=0.3,random_state=1)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

#cria ia
modelo_regressaolinear=LinearRegression()
modelo_arvoredecisao=RandomForestRegressor()

#treina ia
modelo_regressaolinear.fit(xtreino,ytreino)
modelo_arvoredecisao.fit(xtreino,ytreino)

previsao_regressaolinear=modelo_regressaolinear.predict(xteste)
previsao_arvoredecisao=modelo_arvoredecisao.predict(xteste)

from sklearn.metrics import r2_score

print(r2_score(yteste,previsao_regressaolinear))
print(r2_score(yteste,previsao_arvoredecisao))


tabela_auxiliar=pd.DataFrame()
tabela_auxiliar["y_test"]=yteste
tabela_auxiliar["arvore de decisao"]=previsao_arvoredecisao
tabela_auxiliar["regressao linear"]=previsao_regressaolinear

plt.figure(figsize=(15,6))
sns.lineplot(data=tabela_auxiliar)
plt.show()

novos=pd.read_csv("novos.csv")
print(novos)

print(modelo_arvoredecisao.predict(novos))