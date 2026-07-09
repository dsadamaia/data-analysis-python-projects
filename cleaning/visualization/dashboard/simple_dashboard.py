import pandas as pd
import plotly.express as px

def dashboard(file, column):
    df = pd.read_csv(file)
    fig = px.line(df, y=column, title=f"Dashboard - {column}")
    fig.show()

if __name__ == "__main__":
    file = input("CSV: ")
    column = input("Coluna: ")
    dashboard(file, column)
