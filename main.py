import pandas as pd
#lire le fichier csv
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(e)
    raise Exception 

<<<<<<< HEAD
=======
# lire le fichier avec le moteur 'odf'
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    print("file not found")
>>>>>>> 9166aee43e9ffd1f9fbb1e0ddb7f87cb56f1f16b

# afficher le nombre de colonne et ligne du tableaux
print(df.shape)
print(df.columns)

df["Revenue"] = df["quantity"] * df["unit_price"] - df["discount"]
print("Chiffre d'affaires total :", df["Revenue"].sum())

print(f"produit moyen vendu: {df['unit_price'].mean()}")
print(f"nombre de categorie  ou il y a de l electronique {(df["category"]== "Electronics").sum()}")
print(f"nombre de categorie ou il y a furniture {(df['category'] == 'Furniture').sum()}")


print(f"la moyen des age est de {df['customer_age'].mean()}")
f=(df["gender"]== "F").sum()
m=(df["gender"]== "M").sum()
print(f"il y a {f} femme et {m} homme")

print(df[df["customer_age"]<25].sum())
print(df[(df["customer_age"] > 25) & (df["customer_age"] < 50)])
print((df["customer_age"]==50).sum())

print(f"{((df['returned']=='Yes').sum()/len(df))*100}des utilisateur on renvoyer")
print(f"{((df['returned']=='No').sum()/len(df))*100}des utilisateur n'on renvoyer")

note_retours = df[df["returned"] == "Yes"]["rating"].mean()
note_sans_retours = df[df["returned"] == "No"]["rating"].mean()

print("Note moyenne des clients qui retournent :", note_retours)
print("Note moyenne des clients qui ne retournent pas :", note_sans_retours)
print(df["rating"].mean())

print(df[df["category"] == "Electronics"]["rating"].mean())
print(df[df["category"] == "Furniture"]["rating"].mean())
print(df["unit_price"].corr(df["rating"]))
df["unit_price"].dropna()
donnee=df["unit_price"].max()
print(f"le print le plus �lev� est {donnee}")
