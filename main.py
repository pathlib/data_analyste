import pandas as pd

# lire le fichier avec le moteur 'odf'
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    print("file not found")

# afficher les 5 premières lignes
print(df.shape)

df["Revenue"] = df["quantity"] * df["unit_price"] - df["discount"]
print("Chiffre d'affaires total :", df["Revenue"].sum())


print(f" produit moyen vendu:  {df["unit_price"].mean()}")
print((df["category"]== "Electronics").sum())
print((df["category"] == "Furniture").sum())


print(df["customer_age"].mean())
f=(df["gender"]== "F").sum()
m=(df["gender"]== "M").sum()
print(f,m)

print(df["customer_age"]<25)
print((df["customer_age"] > 25) & (df["customer_age"] < 50))
print(df["customer_age"]>=50)

print(((df["returned"]=="Yes").sum()/len(df))*100)
print(((df["returned"]=="No").sum()/len(df))*100)

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
print(f"le print le plus haut est {donnee}")
