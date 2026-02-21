import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/titanic_dataset.csv')#leitura do arquivo csv

df.head()
print(df.info()) #vendo todos os tipos de dados
df.describe() #imprimindo as estatisticas
print(df.isnull().sum()) #contagemdos valores nulos
df.duplicated().sum()

#remove os dados duplicados
df= df.drop_duplicates()  

#trata valores nulos (177) em idade substituindo pela mediana
df['Age'] = df['Age'].fillna(df['Age'].median()) 

#identificando crianças
df['Child'] = df['Age'] < 12

#substituo os valores nulos (687) das cabines com unknown
df["Cabin"] = df["Cabin"].fillna("Unknown") 

#preenchendo os valores nulos(2) com os mais frequentes
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])


#agrupamento por sexo
df_por_sexo = df.groupby('Sex')['Survived'].mean().reset_index() 

plt.figure(figsize=(8,6))
sns.barplot(data=df_por_sexo, x='Sex', y='Survived', palette=['red', 'blue'])
plt.title('Sobrevivência por sexo')
plt.savefig('images/por_sexo.png')
plt.show()

#Sobrevivência de crianças

df_por_crianca = df.groupby('Child')['Survived'].mean().reset_index()

plt.figure(figsize=(6,8))
sns.barplot(data= df_por_crianca, x='Child', y= 'Survived', palette='pastel')
plt.title('Taxa de sobrevivência Crianças x Adultos')
plt.savefig('images/por_criancas.png')
plt.show()

#sobrevivencia por classe
df_por_classe = df.groupby('Pclass')['Survived'].mean().reset_index() 

plt.figure(figsize=(8,6))
sns.barplot(data=df_por_classe, x='Pclass', y='Survived', palette='Set2')
plt.title('Taxa de sobreviventes por classe')
plt.savefig('images/por_classe.png')
plt.show()

#idade sobreviventes

sns.histplot(data=df, x="Age", hue="Survived", kde=True)
plt.title("Faixa etáriade sobreviventes")
plt.savefig('images/por_idade.png')
plt.show()