-- First query: " Listar o nome do produto, categoria e a soma total de vendas (Quantidade * Preço) para cada produto. 
-- Ordene o resultado pelo valor total de vendas em ordem decrescente."
-- Tabela Gerada -> data_clean.csv = tabela_vendas

SELECT
    Produto,
    Categoria,
    SUM(Quantidade * Preço) AS TotalVendas -- Criar uma colunas total de vendas 
FROM 
    tabela_vendas -- data: data_clean.csv
GROUP BY
    Produto, Categoria -- Agrupar por Produto e Categoria
ORDER BY
    TotalVendas DESC; -- Ordenar de forma descrescente a coluna TotalVendas

SELECT 
    Produto AS NomeProduto,
    SUM(Quantidade) AS TotalQuantidadeVendida -- Somar as quantidades
FROM 
    tabela_vendas -- data: data_clean.csv
WHERE 
    strftime('%m', Data) = '06' AND strftime('%Y', Data) = '2024' -- Filtro para pegar só o mês de junho de 2024
GROUP BY 
    Produto -- Agrupar por Produto 
ORDER BY 
    TotalQuantidadeVendida ASC -- Ordenar de forma crescente a coluna TotalVendas
LIMIT 10; -- Pegar só os 10 primeiros