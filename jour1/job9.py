nom="pc portable"
prix_unitaire=900
quantité_de_stock=10
print(nom, prix_unitaire, quantité_de_stock)
client=int(input("Combien de pc portable voulez vous ?"))
quantité_de_stock=quantité_de_stock-client
print(quantité_de_stock)
prix_unitaire=prix_unitaire*1.1
print(nom, prix_unitaire, quantité_de_stock)