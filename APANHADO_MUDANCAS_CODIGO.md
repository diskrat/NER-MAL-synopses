# Linha do Tempo — Mudanças de Código (detalhado por commit)

**Fonte:** histórico de commits do repositório (`git log`)
**Ordem:** cronológica (mais antigo → mais recente)

---

## 2026-04-06 — 27a7a83 — Initial commit
Mensagem: "Initial commit"

Resumo técnico:
- Arquivos adicionados: `.gitignore`, `LICENSE`.
- Objetivo: criar a estrutura inicial do repositório. Nenhuma funcionalidade de pipeline presente neste commit.

Impacto: base do repositório; ponto de partida para commits subsequentes.

---

## 2026-04-06 — 5afb117 — Add MyAnimeList API integration and requirements file
Mensagem: "Add MyAnimeList API integration and requirements file"

Mudanças e detalhes:
- Adicionado `src/api_mal.py`: módulo com cliente/funcionalidades para baixar e salvar dados da API MyAnimeList (funções HTTP, parsing JSON e persistência em `data/raw/`).
- Adicionados 30 arquivos JSON em `data/raw/` (`animes-0001.json` … `animes-0030.json`) contendo dumps de dados obtidos via API.
- `requirements.txt` incluído para registrar dependências necessárias ao cliente e scripts de ingestão.
- `README.md` inicial inserido com instruções básicas.

Impacto técnico:
- Introdução de uma fonte de dados externa (MyAnimeList) e código de ingestão. Estrutura de dados brutos em `data/raw/` utilizada para testes e experimentos iniciais.

---

## 2026-04-12 — 0549f5d — Refactor code structure for improved readability and maintainability
Mensagem: "Refactor code structure for improved readability and maintainability"

Mudanças e detalhes:
- Adicionado `main.py`: primeiro runner do pipeline com funções para leitura e transformação de dados e geração de grafos (`networkx` exports em GEXF).
- Incluídos artefatos de exemplo em `output/` (`graph.gexf`) e arquivo de documentação/entrada `data/docs/U1T1.pdf`.
- Adicionados arquivos em `data/processed/` (primeiras versões de datasets processados e pares de similaridade) para estruturar saídas padronizadas.

Impacto técnico:
- `main.py` provê a primeira versão executável do pipeline, permitindo processar dados e gerar grafos, servindo como base para refatorações posteriores.

---

## 2026-04-13 — 962fb71 — fix: ajuste geral
Mensagem: "fix: ajuste geral"

Mudanças e detalhes:
- Remoção do dataset de animes (arquivos JSON em `data/raw/`), indicando mudança de direção para documentos PDF.
- Inclusão massiva de PDFs em `data/raw/` (diversos TCCs e documentos acadêmicos) e respectivos textos extraídos em `data/processed/raw_texts/`.
- Atualizações no `main.py` para adaptar a extração/limpeza de texto a partir de PDFs e gerar saídas esperadas pelo pipeline.
- Inclusão de `tests/test_main.py` para cobrir comportamentos centrais do runner.
- Removido `src/api_mal.py` (integração MyAnimeList retirada do fluxo principal).

Impacto técnico:
- Transição clara na fonte de dados: de JSONs para PDFs, exigindo parsers de PDF e rotinas de extração de texto. Esse commit prepara o código para processamento de documentos acadêmicos.

---

## 2026-04-15 — 3f8f12b — Refactor code structure for improved readability and maintainability
Mensagem: "Refactor code structure for improved readability and maintainability"

Mudanças e detalhes:
- Refatoração e modularização do `main.py`: extração de funções reutilizáveis como `extract_pdf_text`, `load_raw_pdfs`, `append_entities_jsonl`, `build_entity_cooccurrence_graph`, `segment_text_by_paragraph`, entre outras. Essas funções tornam o fluxo mais testável e orientado a streaming por documento.
- Criação/atualização de `data/processed/entities.jsonl` e `data/processed/performance_metrics.json` para armazenamento incremental de entidades e métricas de execução.
- Adicionado `notebooks/graph_ner_pipeline.ipynb` com notebooks de exploração e geração das visualizações em `output/` (multiplicidade de `graph_*.gexf` e SVGs).

Impacto técnico:
- Migração para um processamento por documento (streaming), append-only para resultados e métricas. Menor uso de memória e maior resiliência a falhas/parada parcial.

---

## 2026-04-16 — 2d6e40e — Add pipeline for extracting entities from PDFs using spaCy and Hugging Face NER
Mensagem: "Add pipeline for extracting entities from PDFs using spaCy and Hugging Face NER"

Mudanças e detalhes:
- Integração inicial de NER baseado em Transformers:
  - Adicionado `pytorch_to_spacy.ipynb` com experimentos para usar `AutoTokenizer` + `AutoModelForTokenClassification` e para conectar modelos HF ao tokenizador/pipeline do spaCy (ex.: mapeamento de subtokens para tokens spaCy, componente `HuggingFaceNERWrapper`).
  - Alternativas experimentadas no notebook: uso direto do `pipeline('ner')` do HF e componente que alinha labels de subtokens com tokens do spaCy para gerar entidades coerentes com a tokenização local.
- `main.py` foi atualizado para suportar cache de extração de texto: checagem de `data/processed/raw_texts/{stem}.txt` antes de reprocessar PDFs, reduzindo re-extrações desnecessárias.
- Atualizações em `data/processed/entities.jsonl` e `data/processed/performance_metrics.json` para registrar resultados do NER e métricas.
- Adicionado `PLAN.md` e documentação complementar no `README.md` explicando o fluxo streaming e artefatos gerados.

Problemas observados (documentados nos notebooks):
- Erro de inicialização de `senter` em spaCy em certos envs — notebook inclui fallback para `sentencizer` e chamadas a `nlp.initialize()` onde necessário.
- Possíveis discrepâncias entre execuções por causa de caches em `data/processed/raw_texts/` (arquivos pré-extraídos contendo texto de teste); recomendado verificar timestamps/validade do cache.

Impacto técnico:
- Este commit introduz a ponte entre modelos Transformers e o pipeline local, permitindo avaliar acurácia e consistência entre abordagens (HF-as-is vs HF integrado ao tokenizador do spaCy). Também formaliza o uso de cache para extração de textos.

---

### Observações e fontes
- O apanhado foi construído a partir do histórico de commits (`git log --name-status`) e inspeção dos arquivos adicionados/modificados listados nos commits.
- Se desejar, posso agora:
  - Incluir trechos de diff (linhas alteradas) para arquivos-chave (`main.py`, notebooks e `README.md`) por commit — atenção ao tamanho;
  - Adicionar hashes completos dos commits e instruções para revisar cada commit localmente;
  - Gerar um resumo temático (por exemplo: "Extração de PDFs", "NER / Transformers", "Refatorações") agrupando commits relacionados.

---

*Fim da linha do tempo detalhada.*
