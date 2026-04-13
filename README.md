# 📈 Graph-NER: Similaridade em Narrativas de Animes

Repositório do projeto final para a disciplina (Unidade 01) com base na descrição do trabalho e no documento de apoio em `data/docs/U1T1.pdf`.

## (i) Membros da Equipe
* **Joao Victor Moura** - *Discente/Desenvolvedor*

---

## (ii) Descrição Detalhada das Atividades
Este trabalho investiga similaridades temáticas e padrões de co-ocorrência em sinopses de animes usando técnicas de **Processamento de Linguagem Natural (NLP)** e **Teoria dos Grafos**.

O objetivo é analisar o conteúdo textual das sinopses para extrair entidades nomeadas, gerar grafos de co-ocorrência e identificar relações entre obras. O projeto está alinhado com os requisitos do trabalho da Unidade 01, incluindo:

- **Reconhecimento de Entidades (NER)**
- **Grafo de co-ocorrência de NER**
- **Análise de desempenho** por sentença, parágrafo e blocos de caracteres
- **Visualização gráfica** de relacionamentos
- **Documentação estruturada** e apresentação assíncrona em Loom

### Pipeline esperado
1. **Extração de dados**
   - Coleta de animes do MyAnimeList com `src/api_mal.py`.
2. **Processamento de texto**
   - Limpeza e normalização das sinopses.
3. **NER e co-ocorrência**
   - Extração de entidades e construção de grafos de relacionamento.
4. **Cálculo de similaridade**
   - Medidas como Jaccard entre conjuntos de entidades ou tokens.
5. **Visualização e análise crítica**
   - Interpretação de resultados e comparação de diferentes granularidades de análise.

---

## (iii) Situação Atual
### O que já está implementado
- `src/api_mal.py`: script de extração de animes do MyAnimeList com paginação e salvamento em `data/raw/`.
- Dados brutos armazenados em `data/raw/animes-XXXX.json`.
- Estrutura inicial de projeto e dependências listadas.

### O que falta implementar
- Pipeline de NER para as sinopses.
- Cálculo de similaridade entre animes.
- Construção do grafo de co-ocorrência e visualizações.
- Análise comparativa de desempenho por sentença, parágrafo e blocos de caracteres.
- Preenchimento de resultados e conclusão no relatório.

---

## (iv) Análise e Discussão dos Achados (Em desenvolvimento)
O trabalho está em fase inicial: os dados foram extraídos, mas ainda falta desenvolver a camada de NLP e a visualização em grafo. O caminho segue pelo uso de entidades nomeadas e medidas de similaridade para mapear relações entre sinopses de animes.

---

## (v) Vídeo de Apresentação
📽️ **Acessar Pitch via Loom:**
```
TBA
```

*(Máximo 10 minutos - apresentar: problema abordado, modelagem técnica, resultados e limitações.)* 

---

## Instalação (Como rodar localmente)
1. Ative o ambiente virtual: `source venv/bin/activate`
2. Instale as dependências: `pip install -r requirements.txt`
3. Configure `MAL_CLIENT_ID` no arquivo `.env`.
4. Execute a extração de dados: `python src/api_mal.py`
5. Execute o pipeline completo de análise: `python main.py`

> Se o modelo spaCy não estiver instalado, o `main.py` irá baixar automaticamente `en_core_web_sm` na primeira execução.

---

## Observações
- O PDF em `data/docs/U1T1.pdf` reforça o escopo do projeto: NER, grafos de co-ocorrência e análise de desempenho.
- O repositório agora inclui um pipeline inicial para processar as sinopses, extrair entidades e gerar um grafo de similaridade.
- O resultado do grafo será salvo em `output/graph.svg` e os pares de similaridade em `data/processed/similarity_pairs.json`.
