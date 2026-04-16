# 📈 Graph-NER: Similaridade em Narrativas de Animes

Repositório do projeto final para a disciplina (Unidade 01). O pipeline processa PDFs/textos para extrair entidades nomeadas, gerar grafos de co-ocorrência e calcular métricas de segmentação.

## (i) Membros da Equipe
- **Joao Victor Moura** - *Discente/Desenvolvedor*

---

## Descrição resumida
Este projeto explora similaridades temáticas e padrões de co-ocorrência em sinopses usando técnicas de NLP (spaCy) e teoria dos grafos (networkx). O foco atual é um pipeline eficiente e escalável por documento (streaming), que evita manter todos os textos em memória.

### Pipeline atual (streaming por documento)
1. Itera arquivos PDF em `data/raw/` um por um.
2. Para cada documento:
   - Extrai o texto (via `pypdf`/`PyPDF2`) e salva imediatamente em `data/processed/raw_texts/{id}.txt`.
   - Processa o texto com `spaCy` (modelo PT configurável) e extrai entidades uma vez por documento.
   - Anexa uma linha JSON em `data/processed/entities.jsonl` com `{"id": <doc_id>, "entities": [...]}`.
   - Atualiza grafos de co-ocorrência incrementalmente por estratégia de segmentação (sentença, parágrafo, k_chars).
   - Atualiza acumuladores de métricas de segmentação (single-pass).
3. Ao final do processamento, o pipeline salva os grafos em `output/graph_<strategy>.gexf` e as métricas agregadas em `data/processed/performance_metrics.json`.

---

## Situação Atual (implementado)
- Processamento streaming por documento (`main.py`).
- Salvamento imediato de textos extraídos em `data/processed/raw_texts/`.
- Extração de entidades por documento e append em `data/processed/entities.jsonl` (JSONL).
- Construção incremental de grafos de co-ocorrência por estratégia e exportação para GEXF em `output/`.
- Agregação de métricas de segmentação e exportação para `data/processed/performance_metrics.json`.

## O que falta / próximos passos
- Refinar testes automatizados e cobertura.
- Documentar achados qualitativos e produzir apresentação final.

---

## Instalação (Como rodar localmente)

Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Coloque os PDFs de entrada em `data/raw/` antes de executar.

---

## Testes
- Instale dependências: `pip install -r requirements.txt`
- Execute: `pytest`

Observação: o agente automatizado não executa testes por padrão — execute manualmente quando desejar validar alterações.

---

## Caminhos e artefatos importantes
- PDFs de entrada: `data/raw/`
- Textos extraídos (por documento): `data/processed/raw_texts/{id}.txt`
- Entidades (JSONL, 1 documento por linha): `data/processed/entities.jsonl`
- Métricas agregadas: `data/processed/performance_metrics.json`
- Grafos exportados (GEXF): `output/graph_sentence.gexf`, `output/graph_paragraph.gexf`, `output/graph_k_chars.gexf`

---

## Notas de implementação rápidas
- O arquivo `main.py` contém parâmetros úteis no topo: `FILE_LIMIT` (limita documentos durante testes), `CHAR_BLOCK_SIZE` (tamanho de blocos por caracteres), e `ENTITIES_PER_DOC`.
- Para gerar SVGs a partir dos GEXF, use Gephi ou ferramentas de conversão externa.

---

Se precisar, posso: (1) atualizar este README com mais detalhes de execução, (2) adicionar exemplos de saída, ou (3) abrir um PR com alterações agrupadas.
