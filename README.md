# Trabalho Prático – DGT2823 Tecnologias para desenv. de soluções de big data

**Aluno:** Bryan David Leite Oliveira – Matrícula 202308032828
**Curso:** Desenvolvimento FullStack – Polo Venda Nova – Turma 9001 – Semestre 2026.3 FLEX

Limpeza de um conjunto de dados (CSV) com Python e a biblioteca Pandas.

## Arquivos

| Arquivo | Conteúdo |
| --- | --- |
| `dados.csv` | Conjunto de dados do roteiro (separador `;`) |
| `microatividades.py` / `.ipynb` | Microatividades 1 a 5 (leitura, subconjunto, `max_rows`, `head`/`tail`, `info`) |
| `trabalho_pratico.py` / `.ipynb` | Trabalho prático: leitura, verificação e limpeza dos dados (passos 1 a 13) |
| `saida_microatividades.txt` | Saída da execução das microatividades |
| `saida_trabalho_pratico.txt` | Saída da execução do trabalho prático |

Os notebooks (`.ipynb`) já têm as saídas da execução gravadas.

## Como executar

```
pip install pandas numpy
python microatividades.py
python trabalho_pratico.py
```

Execute dentro da pasta do projeto, para o `dados.csv` ser encontrado. Os `.ipynb` abrem no JupyterLab, Jupyter Notebook ou Google Colab (envie também o `dados.csv`).

## Resumo do tratamento dos dados

1. Leitura do CSV com `sep=';'`, `engine='python'` e `encoding='utf-8'`.
2. Verificação com `info()`, `head(10)` e `tail(10)`: 32 linhas, 6 colunas; `Calories` tem 2 nulos (linhas 18 e 28) e `Date` tem 1 nulo (linha 22).
3. Cópia do conjunto original (`df.copy()`).
4. `Calories`: nulos substituídos por 0.
5. `Date`: nulos substituídos por `'1900/01/01'`; a conversão com `to_datetime` falha porque o valor não segue o formato dos demais. O valor é trocado por `NaN`.
6. Nova tentativa de conversão: falha por causa do valor `20201226` (linha 26). Ele é trocado por `'2020/12/26'` com `replace`.
7. `to_datetime` aplicado em toda a coluna `Date`, que passa a ser `datetime`.
8. `dropna()` remove o registro com `Date` nulo (linha 22).
9. Resultado final: 31 linhas, 0 valores nulos, `Date` em `datetime`.
