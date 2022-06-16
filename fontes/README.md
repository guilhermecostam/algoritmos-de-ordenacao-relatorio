
# Passo a passo para executar os algoritmos

## Ferramentas

Estas são as ferramentas que utilizei no desenvolvimento dos algoritmos.

- **Python** — Linguagem de programação de alto nível

## Preparando para rodar:

Para rodar basta fazer a instalação do python na máquina e rodar o seguinte comando:

```bash
# Onde nome_do_arquivo é o nome do algoritmo que deseja rodar
$ python3 nome_do_arquivo.py
```

##  Algoritmos

- Os algoritmos utilizados são:
  - Insertion Sort;
  - Merge Sort;
  - Quick Sort.

## Observações

1. O código está escrito inteiramente em inglês.

2. Os programas retornam apenas os tamanhos dos vetores utilizados e os tempos de execução dos algoritmos. Essas informações são para poder plotar os gráficos.

3. Como os algoritmos Quick Sort e Insertion Sort possuem melhor, pior e médio caso, a versão principal possibilita que seja escolhida o caso que deseja rodar. Por isso, deixei uma pasta com versões de cada caso do Insertion Sort e do Quick Sort separados.

4. Caso deseje mais eficiência é possível rodar os casos separados e já passar o retorno direto para um arquivo de texto com o comando:
```bash
$ python3 nome_do_arquivo.py >> arquivo.txt
```
