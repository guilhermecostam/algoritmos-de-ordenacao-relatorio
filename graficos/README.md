
# Passo a passo para plotar os gráficos

## Ferramentas

Estas são as ferramentas que utilizei no desenvolvimento dos algoritmos.

- **GNUPlot** — Programa para plotar gráficos de funções matemáticas

## Preparando para rodar:

Após ter rodado os algoritmos, basta colocar os retornos obtidos de cada algoritmo em um arquivo de texto (como os que estão neste diretório) e seguir os passos a seguir.

Fazer a instalação do GNUPlot na máquina, iniciar o programa e rodar os comandos:

```bash
# O comando a seguir plota o gráfico, com ponto e linhas
$ plot "merge_sort.txt" w lp

# Para rodar mais de um resultado, basta seguir o seguinte passo:
$ plot "merge_sort.txt" w lp, "quick_sort_middle_case.txt" w lp
```

## Observações

É indicado que os algoritmos e os gráficos sejam plotados no sistema operacional Linux. Nele o GNUPlot já vem instalado e apresenta pouca oscilação em relação aos dados obtidos pelos algoritmos, tornando o relatório mais fiel.
