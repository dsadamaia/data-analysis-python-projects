import pandas as pd
import matplotlib.pyplot as plt

def plot_column(file, column):
    df = pd.read_csv(file)

    plt.figure(figsize=(10,5))
    plt.plot(df[column], marker='o')
    plt.title(f"Gráfico da coluna: {column}")
    plt.xlabel("Index")
    plt.ylabel(column)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    file = input("CSV: ")
    column = input("Coluna para plotar: ")
    plot_column(file, column)
