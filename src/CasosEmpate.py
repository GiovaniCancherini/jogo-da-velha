import pandas as pd

data_path = "Data/tic-tac-toe.csv"
new_data_path = "Data/tic-tac-toe-updated.csv"

# Carregar o dataset original
df = pd.read_csv(data_path, sep=",", header=None)
df.columns = ['L1C1', 'L1C2', 'L1C3', 'L2C1', 'L2C2', 'L2C3', 'L3C1', 'L3C2', 'L3C3', 'RESULTADO']

# Adicionar novos casos de empate
new_data = [
    ['x', 'o', 'x', 'o', 'x', 'o', 'o', 'x', 'o', 'empate'],
    ['o', 'x', 'o', 'x', 'o', 'x', 'x', 'o', 'x', 'empate'],
    ['x', 'o', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'empate'],
    ['x', 'x', 'o', 'o', 'x', 'x', 'x', 'o', 'o', 'empate'],
    ['o', 'x', 'x', 'x', 'o', 'o', 'x', 'o', 'x', 'empate'],
    ['x', 'x', 'o', 'o', 'o', 'x', 'x', 'o', 'x', 'empate'],
    ['o', 'o', 'x', 'x', 'x', 'o', 'o', 'x', 'x', 'empate'],
    ['x', 'o', 'o', 'o', 'x', 'x', 'x', 'x', 'o', 'empate'],
    ['o', 'x', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'empate'],
    ['x', 'o', 'x', 'x', 'x', 'o', 'o', 'o', 'x', 'empate']
]
new_df = pd.DataFrame(new_data, columns=['L1C1', 'L1C2', 'L1C3', 'L2C1', 'L2C2', 'L2C3', 'L3C1', 'L3C2', 'L3C3', 'RESULTADO'])
df = pd.concat([df, new_df], ignore_index=True)


print("Primeiras linhas do dataframe atualizado:")
print(df.head())

# Salvar o dataset atualizado
df.to_csv(new_data_path, index=False, header=False)

print(f"Dataset atualizado salvo em: {new_data_path}")
