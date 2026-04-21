# Apanhado Detalhado do Projeto NER-Eng-comp

**Data:** 2026-04-16

---

## 1. Visão Geral da Conversa

Este documento resume todo o trabalho feito no repositório `NER-Eng-comp` durante a sessão de colaboração: decisões de agente, alterações no código, notebooks, problemas encontrados e próximos passos.

Principais objetivos abordados:
- Registrar comportamento e preferências do agente (`.agent.md`).
- Refatorar a pipeline para processamento streaming por documento e persistência incremental de entidades em JSONL.
- Integrar modelos de NER do Hugging Face (ex.: `wikineural-multilingual-ner`) com tokenização/pipe do spaCy (várias estratégias: HF-as-is e HF alinhado a tokens do spaCy).
- Evitar reprocessamento de PDFs através de cache de texto extraído.

---

## 2. Decisões do Usuário (configurações do agente)

- Não criar branches nem executar `git push` automaticamente.
- Estilo de commit: Conventional Commits.
- Execução de testes automáticos: não automática (apenas sob demanda).

---

## 3. Ações Executadas

- Criação/atualização de `.agent.md` com preferências e plano detalhado.
- Leitura de `PLAN.md` para gerar plano de trabalho e aplicar alterações de documentação.
- Atualização de `README.md` para refletir design de streaming por documento, caminhos de artefatos e instruções de execução.
- Edição e experimentação em `notebooks/pytorch_to_spacy.ipynb`:
  - Carregamento explícito de `AutoTokenizer` e `AutoModelForTokenClassification`.
  - Implementação de componentes spaCy que usam HF (duas variantes: alinhamento por tokens spaCy + mapeamento de subtokens e versão HF "as-is").
  - Wrapper `HuggingFaceNERWrapper` e helper `extract_entities_hf` em variantes do notebook.
  - Adição de lógica de segmentação por sentença com `senter` e fallback para `sentencizer`, incluindo chamada a `nlp.initialize()` para evitar E109.
- Alterações em `main.py`:
  - `extract_pdf_text` agora verifica `data/processed/raw_texts/{stem}.txt` e reutiliza o texto extraído quando disponível (cache).
  - Manutenção da estratégia de escrita incremental em `data/processed/entities.jsonl` via `append_entities_jsonl`.
- Coleta do histórico de commits e geração de um resumo/timeline parcial dos commits importantes.

---

## 4. Inventário Técnico

- Linguagens / Bibliotecas: Python, spaCy, Hugging Face `transformers`, PyTorch, networkx, PyPDF (ou pypdf), pytest.
- Arquivos-chave:
  - `main.py` — runner da pipeline streaming por documento.
  - `notebooks/pytorch_to_spacy.ipynb` — desenvolvimento e experimentação HF↔spaCy.
  - `README.md`, `PLAN.md`, `.agent.md` — documentação e metadados.
  - `data/processed/entities.jsonl` — arquivo append-only com entidades extraídas.
  - `data/processed/raw_texts/` — cache dos textos extraídos dos PDFs.
  - `output/*.gexf` — grafos de coocorrência exportados.

---

## 5. Estado Atual do Código (resumo por arquivo)

- `main.py`:
  - Streaming por documento implementado.
  - `extract_pdf_text` com leitura/escrita de cache em `data/processed/raw_texts/`.
  - Funções de segmentação, análise e construção do grafo mantidas.
  - Integração HF no `main.py` está parcial — a maior parte da experimentação está no notebook.
- `notebooks/pytorch_to_spacy.ipynb`:
  - Contém implementações experimentais:
    - Carregamento explícito de tokenizer/model HF.
    - `hf_ner_component` (alinhamento token-wise) e versão HF-as-is.
    - Tratamento de `senter` com `nlp.initialize()` e fallback `sentencizer`.
- `.agent.md` e `README.md`:
  - Atualizados para registrar decisões e documentar pipeline streaming.

---

## 6. Problemas Encontrados e Soluções Aplicadas

- Erro `ValueError [E109]` ao adicionar `senter` no pipeline spaCy: resolvido chamando `nlp.initialize()` e implementando fallback para `sentencizer` quando `senter` falha na inicialização.
- Divergência entre comportamento do notebook e `main.py` no `pdf_iter`: possivelmente causada por arquivos de cache contendo texto de teste (ex.: string de exemplo "Naruto..."). Ações tomadas:
  - `extract_pdf_text` passou a reutilizar/expor o cache em `data/processed/raw_texts/`.
  - Adicionado logging nas rotinas do notebook para diagnosticar arquivos detectados e cache usado.
- Recuperação de `git diff` muito grande: saída foi armazenada em recurso temporário, leitura parcial devido ao tamanho; não afeta estado do repositório, apenas a exibição do diff completo foi truncada.

---

## 7. Progresso e Itens Concluídos

- Concluído:
  - `.agent.md` criado/atualizado com decisões do usuário.
  - `README.md` atualizado.
  - Notebooks atualizado com experimentos HF↔spaCy.
  - `extract_pdf_text` passou a usar cache de extração.
  - Histórico de commits coletado.
- Em andamento / pendente:
  - Portar o `HuggingFaceNERWrapper` do notebook para `main.py` (integração completa em runner).
  - Reconciliar comportamento notebook vs `main.py` (resolver causa raiz do cache de texto de teste).
  - Opção: implementar invalidação de cache via comparação de `mtime` do PDF vs. `mtime` do arquivo de texto extraído.

---

## 8. Estado de Trabalho Atual e Prioridades

Prioridade imediata:
1. Verificar conteúdo de `data/processed/raw_texts/` para detectar caches com texto de teste.
2. Portar e centralizar o carregamento do tokenizer + modelo HF para carregar uma única vez (evitar recarregamentos repetidos em execução streaming).
3. Decidir estratégia final de NER para produção: HF-as-is (pipeline HF) vs HF alinhado a tokens spaCy (melhor integração com tokens/sentenças do pipeline).

---

## 9. Recomendações de Ações Imediatas (comandos)

Inspecionar um arquivo de texto cache suspeito (PowerShell):

```powershell
Get-Content data/processed/raw_texts\NOME_DO_ARQUIVO.txt -TotalCount 50
```

Para forçar reextração (exemplo): renomear ou remover o cache antes de rodar o pipeline:

```powershell
# remover cache para um PDF específico
Remove-Item data/processed/raw_texts\NOME_DO_ARQUIVO.txt
```

Executar o `main.py` (ambiente virtual ativado):

```powershell
python main.py
```

---

## 10. Próximos Passos Sugeridos

- Confirmar se deseja que eu porte as implementações HF do notebook para `main.py` agora (posso fazê-lo e incluir carregamento único do modelo/tokenizer).
- Implementar verificação de validade do cache (comparo de timestamps) se desejar evitar reprocessamentos inválidos.
- Opcional: adicionar comando `--invalidate-cache` ao runner para facilitar testes.

---

## 11. Referências Rápidas

- Artefatos:
  - `data/processed/entities.jsonl` — entidades extraídas (append-only).
  - `data/processed/raw_texts/` — extrações cacheadas por PDF.
  - `output/*.gexf` — grafos de coocorrências exportados.
- Arquivos de interesse: `main.py`, `notebooks/pytorch_to_spacy.ipynb`, `README.md`, `.agent.md`.

---

*Fim do apanhado.*
