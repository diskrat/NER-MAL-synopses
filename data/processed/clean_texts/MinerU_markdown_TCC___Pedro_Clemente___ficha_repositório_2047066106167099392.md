<!-- source: data\processed\md\MinerU_markdown_TCC___Pedro_Clemente___ficha_repositório_2047066106167099392.md -->

# Resumo

Este trabalho apresenta o desenvolvimento e a implementação de uma pipeline de segurança automatizada integrada ao processo de Integração e Entrega Contínuas (CI/CD) do sistema PoP-ERP, com o objetivo de fortalecer o desenvolvimento seguro e mitigar vulnerabilidades ao longo de todo o ciclo de vida do software. A solução adota princípios de DevSecOps e combina três camadas complementares de verificação: análise estática do código-fonte (SAST, abreviação para o inglês Static Application Security Testing), análise da cadeia de suprimentos de software e testes dinâmicos de segurança (DAST, do inglês Dynamic Application Security Testing). A metodologia empregada compreende levantamento bibliográfico, modelagem arquitetural, implementação incremental, execu-ção experimental e avaliação crítica dos resultados obtidos. Os experimentos demonstraram a efetividade da pipeline na identificação de vulnerabilidades estruturais, falhas em dependências e comportamentos inseguros em tempo de execução, evidenciando a importância da automação e da integração de segurança no processo de desenvolvimento. Como contribuição, o trabalho estabelece uma abordagem reprodutível e aplicável a outros ambientes CI/CD, reforçando a maturidade em segurança do PoP-ERP e promovendo a consolidação de práticas DevSecOps na instituição. Palavras-chave: DevSecOps; CI/CD; SAST; DAST; cadeia de suprimentos de software; PoP-ERP.

# 1 Introdução 1

1.1 Contexto e motivação de trabalho . . 2 1.1.1 Incidentes de segurança com sistemas ERP . . . . 3 1.2 Objetivo 3 1.3 Contribuições 4 1.4 Estrutura do Trabalho . . 4

# 2 Fundamentação Teórica 7

2.1 Vulnerabilidades de Software: Conceitos e Formas de Classificação . . . 7 2.1.1 O que é uma vulnerabilidade? . . 7 2.1.2 Classificações de vulnerabilidades . . . . . . 8 2.2 Teste Estático de Segurança de Aplicações . . 8 2.3 Análise da cadeia de suprimentos de software 9 2.4 Teste Dinâmico de Segurança de Aplicações . . 10 2.5 Exemplos de vulnerabilidades detectadas por SAST, SBOM e DAST . . . 11 2.6 Tecnologias que compõem o sistema PoP-ERP 11 2.6.1 Linguagem de Programação Python . . . . . 11 2.6.2 Framework Django . . . . . 12 2.6.3 Banco de Dados PostgreSQL . . . . . . . 12

# 3 Revisão de literatura 13

3.1 Estudo precursor 13 3.2 Metodologia de pesquisa . . 14 3.3 Artigos relevantes ao tema 15 3.4 Produção científica sobre o tema 17 3.5 Metanálise dos Resultados da Revisão Bibliográfica . . . 18

# 4 Solução Proposta 19

4.1 Metodologia . . . 19 4.2 Arquitetura 22 4.2.1 Análise Estática de Código com Bandit . . . . . . . . . . . . 23 4.2.2 Análise de Vulnerabilidades com Trivy . . . . . 23 4.2.3 Análise Dinâmica com OWASP ZAP . . . 24 4.3 Integração ao pipeline de CI/CD 25 4.3.1 Fase 1: Integração do Bandit (SAST) . . . 26 4.3.2 Fase 2: Integração do Trivy para análise de dependências . . . . . 26 4.3.3 Fase 3: Integração do OWASP ZAP (DAST) . . . . . . . . . . . 27 4.3.4 Pipeline final integrada . . . . . 28 4.3.5 Conclusão da integração . . . 29

# 5 Avaliação do Pipeline de Segurança 31

5.1 Descrição do Ambiente Experimental 31 5.1.1 Configurações 31 5.2 Avaliação da Análise Estática (SAST) 32 5.2.1 Resultados Gerais do SAST 32 5.2.2 Discussão e Ações Corretivas no SAST . . . . . . . . . . 32 5.3 Avaliação da Análise de SBOM (Trivy) . . 33 5.3.1 Resultados da Análise SBOM . . . 34 5.3.2 Discussão e Ações Corretivas SBOM . . . . 34 5.4 Avaliação do Teste Dinâmico (DAST) . . 35 5.4.1 Resultados Obtidos . . 35 5.4.2 Discussão e Ações Corretivas DAST . . . . . . 35 5.4.3 Síntese Geral da Ferramenta OWASP ZAP . . . . 37 5.5 Síntese Integrada da Avaliação . 37

# 6 Conclusão 39

6.1 Síntese dos Resultados 39 6.2 Dificuldades Técnicas e Organizacionais . . . 39 6.3 Impacto na Cultura de Desenvolvimento . . . 40 6.4 Trabalhos Futuros . . 40 6.5 Considerações Finais 41