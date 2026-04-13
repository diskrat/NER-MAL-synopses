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
   - Carrega documentos PDF presentes em `data/raw/` como entrada principal.
2. **Extração de texto**
   - Converte os PDFs em texto bruto utilizando `PyPDF2`.
3. **Exportação de texto**
   - Salva os textos extraídos em `data/processed/raw_texts/` como `.txt`.
4. **Processamento de texto**
   - Limpeza e normalização dos textos extraídos.
5. **NER e co-ocorrência**
   - Extração de entidades nomeadas com spaCy e construção de grafos de co-ocorrência.
6. **Análise de desempenho**
   - Comparação entre granulações: sentença, parágrafo e blocos de caracteres.
7. **Visualização e análise crítica**
   - Salvamento de grafos em `output/graph.gexf` e `output/graph.svg`, além de métricas em `data/processed/`.

---

## (iii) Situação Atual
### O que já está implementado
- Pipeline de extração de texto de PDFs diretamente em `data/raw/` usando `PyPDF2`.
- Extração de entidades nomeadas via spaCy e geração de grafo de co-ocorrência.
- Comparação de desempenho entre segmentação por sentença, parágrafo e blocos de caracteres.
- Exportação de resultados em `output/graph.gexf`, `output/graph.svg` e `data/processed/performance_metrics.json`.
- Fallback para processamento de registros JSON em `data/raw/` quando não há PDFs.

### O que falta implementar
- Documentar resultados qualitativos finais e conclusões.
- Produzir a apresentação assíncrona Loom.

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
3. Coloque os PDFs de entrada em `data/raw/`.
4. Execute o pipeline completo de análise: `python main.py`

## Testes
1. Instale as dependências: `pip install -r requirements.txt`
2. Execute os testes: `pytest`

> Se o modelo spaCy não estiver instalado, o `main.py` irá baixar automaticamente `en_core_web_sm` na primeira execução.

---

## Observações
- O PDF em `data/docs/U1T1.pdf` é o guia do trabalho e não a fonte de entrada principal do pipeline.
- O pipeline agora processa os PDFs em `data/raw/`, extrai texto, identifica entidades e gera grafos de co-ocorrência.
- O resultado do grafo é salvo em `output/graph.gexf` e `output/graph.svg`; as métricas de segmentação são gravadas em `data/processed/performance_metrics.json`.
