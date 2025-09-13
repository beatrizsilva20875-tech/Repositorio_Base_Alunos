import csv  # importamos o csv

# Abre o arquivo para escrita no formato TSV
with open('lista_de_compras.tsv', 'w', newline='', encoding='utf-8') as csvFile:
    csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n')

    csvWriter.writerow(['maçãs', 'bananas', 'morango'])
    csvWriter.writerow(['leite', 'iorgute', 'queijo'])
    csvWriter.writerow(['sabão', 'detergente', 'esponja'])
