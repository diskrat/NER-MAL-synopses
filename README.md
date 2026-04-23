# Análise de Entidades Nomeadas e Grafos de Co-ocorrência
## O que este repositório contém (resumo técnico atual)
Este repositório implementa um pipeline de extração e análise de entidades nomeadas a partir de documentos (PDF/Markdown), construção de grafos de co-ocorrência e geração de artefatos para análise.

- `scripts/extract_main_content.py`: limpeza e extração preservando estrutura de arquivos Markdown; produz `data/processed/clean_texts/*.md` e `data/processed/clean_texts/clean_texts.jsonl`.
- `scripts/main_spacy.py`: pipeline leve que consome `.md` limpos e gera `data/processed/entities.jsonl`, `data/processed/performance_metrics.json` e grafos GEXF em `output/`.
- `scripts/export_graph_svg.py`: exporta GEXF → SVG com fallback puro-SVG se o Matplotlib falhar.
- `main.py`: runner histórico que orquestra extração, NER e geração de grafos (mantido para referência).

### Artefatos gerados

- Textos extraídos: `data/processed/raw_texts/`
- Textos limpos (Markdown): `data/processed/clean_texts/`
- Entidades (JSONL): `data/processed/entities.jsonl`
- Métricas: `data/processed/performance_metrics.json`
- Grafos (GEXF): `output/graph_sentence.gexf`, `output/graph_paragraph.gexf`, `output/graph_k_chars.gexf`

## Instruções rápidas para rodar localmente

Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
# executar pipeline de extração/limpeza de Markdown
python scripts/extract_main_content.py --input data/processed/md --out data/processed/clean_texts
# executar pipeline spaCy a partir dos .md limpos
python scripts/main_spacy.py --input data/processed/clean_texts --out data/processed
# gerar SVG a partir dos grafos (fallback se matplotlib falhar)
python scripts/export_graph_svg.py --input output/graph_paragraph.gexf --out output/graph_paragraph.svg
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/extract_main_content.py --input data/processed/md --out data/processed/clean_texts
python scripts/main_spacy.py --input data/processed/clean_texts --out data/processed
python scripts/export_graph_svg.py --input output/graph_paragraph.gexf --out output/graph_paragraph.svg
```

Coloque os PDFs/MDs de entrada nos diretórios apropriados antes de executar.

## Membros do grupo
- **Joao Victor Moura** 

## Descrição detalhada das atividades realizadas
- Implementação do pipeline de extração e limpeza de Markdown com preservação de headings e trimming de seções (`RESUMO` → `INTRODUÇÃO`).
- Integração com `spaCy` para extração de entidades e estratégias de segmentação para construir grafos de co-ocorrência.
- Exportação de grafos em GEXF e geração de SVGs com fallback robusto.

## Principais resultados e imagens
- Principais artefatos gerados estão em `output/` (GEXF e SVG).


## Vídeo de apresentação
- Link para vídeo Loom: \[TBA\]
