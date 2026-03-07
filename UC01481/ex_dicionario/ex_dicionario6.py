vendas = {
    "Janeiro": 1000,
    "Fevereiro": 1500,
    "Março": 1200
}

totalVendas = 0

for valor in vendas.values():
    totalVendas += valor

print("Total de vendas do trimestre:", totalVendas)