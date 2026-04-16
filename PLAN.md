# Extração e Armazenamento Otimizado de Entidades

Para diminuir o overhead de memória e simplificar a implementação, o pipeline será refatorado para operar em **streaming** (processando um arquivo por vez) e os extraídos serão iterados numa única passagem, evitando carregar e manter o texto de todos os documentos na memória (o que escalaria muito mal com múltiplos PDFs longos).

## Proposed Changes

### [MODIFY] main.py

Em vez de carregar todos os PDFs em uma lista de `records`, vamos processar documento a documento da seguinte maneira simplificada:

1. **Iterar pelos PDFs**: Para cada PDF encontrado:
   - Extrair o texto.
   - Salvar o texto bruto no disco imediatamente.
   - Extrair as entidades nomeadas uma única vez usando o `spaCy`.
   - Salvar as entidades em um arquivo único JSON Lines (`data/processed/entities.jsonl`), **anexando** (`append`) linha a linha para não precisar manter toda a lista em memória.
   - Atualizar o grafo de co-ocorrência em memória.
   - Executar as três metodologias de análise de segmentação para computar as métricas, adicionando-as a um acumulador.
2. **Ao final do loop**:
   - Salvar o Grafo em GEXF e SVG.
   - Salvar as métricas agregadas na forma json.

### Simplificações na Implementação
- Remover a construção e retenção do objeto complexo `records`, substituindo-o por um pipeline de processamento e consumo por lote ou arquivo individual. Isso simplifica bastante as funções que agora recebem os dados unitários de `text` e `entities` ao invés de listas longas.
- Diminuir iterações repetitivas do `spaCy` convertendo a checagem das métricas para uma forma acumulativa muito mais rápida, reduzindo a complexidade de algoritmos O(N) que percorriam multiplas vezes a mesma lista.
- Gravar as entidades como JSONL possibilita "buscar e guardar" conforme seu pedido original e de forma imediata.

## Open Questions

- A alteração para um arquivo `entities.jsonl` (uma linha de JSON por PDF) atende a sua necessidade? É o padrão mais robusto para consumo sem estourar memória posteriormente.
- Se concordar, prosseguirei imediatamente com as edições no código para finalizar esta implementação.

## Implementation Status

- **main.py**: Implemented streaming processing per document; extracts text per PDF, saves raw text files to `data/processed/raw_texts/`, extracts named entities once per document with spaCy, appends entities to `data/processed/entities.jsonl`, updates co-occurrence graph in memory and saves graph outputs to `output/graph.gexf` and `output/graph.svg`.
- **Segmentation analysis**: Converted to a single-pass accumulator to support streaming and avoid multiple spaCy runs.
- **Tests**: Unit tests executed in the project's virtualenv and passed (`6 passed, 1 warning`).
- **Requirements**: Pinned `pytest` to a compatible `8.4.2` to ensure installation in the project's venv.

If you'd like, I can open a PR with these changes or update the `README.md` with usage and run instructions.
