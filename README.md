# 📈 Graph-NER: Similaridade em Narrativas de Animes

Repositório do projeto final para a disciplina (Unidade 01).

## (i) Membros da Equipe
* **Joao Victor Moura** - *Discente/Desenvolvedor*

---

## (ii) Descrição Detalhada das Atividades
Este projeto tem como objetivo detectar padrões e plágios literários/temáticos em sinopses de animes usando a API oficial do **MyAnimeList** e algoritmos matemáticos de **Processamento de Linguagem Natural (NLP) e Grafos**.

As atividades seguiram a seguinte esteira de dados (Pipeline):
1. **Extração de Dados (Data Mining):** Uso do script `src/api_mal.py` para consultar iterativamente o ranking do *MyAnimeList* (API v2) contornando limites (*Rate Limits*), gerando um Dataset puro.
2. **Reconhecimento de Entidades (NER)** 
3. **Cálculo de Similaridade (Jaccard Index)** 
4. **Visualização por Grafo** 

---

## (iii) Apresentação dos Principais Resultados


---

## (iv) Análise e Discussão dos Achados
A aplicação do **Processamento de Linguagens Naturais** somado à **Teoria dos Grafos** se provou excepcional na área de recomendação de nicho e detecção de clichês:



---

## (v) Vídeo de Apresentação
📽️ **Acessar Pitch via Loom:** 
```
TBA
```

*(Máximo 10 Minutos - Apresentar: O problema abordado, modelagem técnica e resultados/limitações*).

---
### Instalação (Como rodar localmente)
1. Instale as dependências: `pip install -r requirements.txt`
2. Adicione seu Client-ID da API do MyAnimeList no arquivo `.env`.
3. Inicie o fluxo rodando: `python main.py`
