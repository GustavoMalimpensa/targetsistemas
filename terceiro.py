import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

faturamento = [dia['valor'] for dia in dados]

menor = min(faturamento)
maior = max(faturamento)

media = sum(faturamento)/len(faturamento)
superiores_media = sum(1 for valor in faturamento if valor > media)

print(f'Menor faturamento: {menor:.2f}')
print(f'Maior faturamento: {maior:.2f}')
print(f'Número de dias com faturamento acima da média: {superiores_media}')
