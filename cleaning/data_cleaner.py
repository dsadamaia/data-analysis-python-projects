import pandas as pd

def clean_data(file):
    df = pd.read_csv(file)

    print("\nRemovendo duplicatas...")
    df = df.drop_duplicates()

    print("Preenchendo valores nulos...")
    df = df.fillna(method="ffill")

    print("Convertendo colunas numéricas...")
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass

    df.to_csv("cleaned_output.csv", index=False)
    print("\nArquivo limpo salvo como cleaned_output.csv")

if __name__ == "__main__":
    file = input("Arquivo CSV: ")
    clean_data(file)
