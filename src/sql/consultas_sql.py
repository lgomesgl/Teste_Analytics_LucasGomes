import pandas as pd
import sqlite3
import os
from pathlib import Path

root = Path(os.path.abspath('')).parent.parent
csv_path = root / "data" / "data_clean_analyse.csv"
df = pd.read_csv(csv_path)

df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

conn = sqlite3.connect("sales_dataset.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tabela_vendas (
    ID INTEGER PRIMARY KEY,
    Data DATE,
    Produto TEXT,
    Categoria TEXT,
    Quantidade REAL,
    Preço REAL
);
""")

df.to_sql('tabela_vendas', conn, if_exists='replace', index=False)

query1 = """
SELECT 
    Produto AS NomeProduto,
    Categoria,
    SUM(Quantidade * Preço) AS TotalVendas
FROM 
    tabela_vendas
GROUP BY 
    Produto, Categoria
ORDER BY 
    TotalVendas DESC;
"""

result1 = pd.read_sql_query(query1, conn)
print(result1)

query2 = """
SELECT 
    Produto AS NomeProduto,
    SUM(Quantidade) AS TotalQuantidadeVendida
FROM 
    tabela_vendas
WHERE 
    strftime('%m', Data) = '06' 
GROUP BY 
    Produto
ORDER BY 
    TotalQuantidadeVendida ASC
LIMIT 10;
"""

result2 = pd.read_sql_query(query2, conn)
print(result2)

conn.close()