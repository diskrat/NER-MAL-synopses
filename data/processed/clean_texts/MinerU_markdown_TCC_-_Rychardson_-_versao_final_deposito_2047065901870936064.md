<!-- source: data\processed\md\MinerU_markdown_TCC_-_Rychardson_-_versao_final_deposito_2047065901870936064.md -->

# Resumo

Empresas juniores são associações sem fins lucrativos, formadas e geridas por estudantes de graduação de instituições de ensino superior, possuindo como principal objetivo proporcionar a vivência de um ambiente empresarial e aprendizado para os alunos por meio da realização de projetos. Nesse contexto, uma dificuldade enfrentada é a gestão de processos, devido à descentralização das atividades em múltiplas ferramentas de gerenciamento, o que dificulta o acompanhamento por parte dos gestores. Para solucionar essa problemática, este trabalho propõe o Prisma, um sistema web desenvolvido especificamente para o contexto das empresas juniores, reunindo em uma única plataforma as funcionalidades necessárias ao gerenciamento de seus principais processos. Em vez de integrar ferramentas externas, o Prisma implementa módulos próprios que substituem soluções dispersas, oferecendo padronização, rastreabilidade e maior eficiência na gestão organizacional. O Prisma oferece módulos de gerenciamento para Processo Seletivo, permitindo administrar candidatos, etapas, notas, avisos; Projetos, com a gestão de riscos, metas e membros; Board, entregando uma gerência de atividades; Metas para acompanhamento de indicadores e Itens para inventário. O sistema é acessível a partir de dispositivos conectados à internet e foi desenvolvido com o framework Spring Boot e a biblioteca React do JavaScript. Ao final do projeto, espera-se disponibilizar uma solução que auxilie os gestores das empresas juniores no monitoramento e na melhoria de seus processos. Palavras-chave: empresas juniores; gestão de processos; sistema web; Spring Boot; React.

# 1 Introdução 1

1.1 Problema e motivação . . 1 1.2 Objetivos 2 1.3 Metodologia . . 2 1.4 Organização do trabalho 3

# 2 Fundamentação Teórica 5

2.1 Gestão de Processos em Empresas Juniores . . 5 2.2 Sistemas Web e sua Relevância Organizacional 6 2.3 Framework Spring Boot . . . 6 2.4 Banco de Dados PostgreSQL . 6 2.5 Biblioteca React . 7 2.6 Linguagem TypeScript . . . 7 2.7 Estilização com TailwindCSS . . 8 2.8 Metodologias Ágeis e o Desenvolvimento do Prisma 8 2.9 Modelagem UML . . 8 2.9.1 Diagramas Estruturais . . 9 2.9.2 Diagramas Comportamentais . . . . . 9 2.10 Modelo C4 para Visualização de Arquitetura de Software . . 10 2.10.1 Princípios e objetivos . . . . 10 2.10.2 Os quatro níveis do C4 . . 10 2.10.3 Benefícios práticos . . . . . . 11 2.10.4 C4 e UML: papéis complementares . . . 11 2.10.5 Boas práticas e limitações . . . 11 2.11 Síntese do Capítulo 11

# 3 Trabalhos Relacionados 13

3.1 Sistemas de Gestão e Ferramentas Integradas 13 3.2 Trabalhos Acadêmicos e Sistemas Open Source . . . 14 3.3 Contribuições e Diferenciais do Prisma 15 3.3.1 Comparativo entre Prisma, Trello e Notion . . 16

# 4 Prisma 19

4.1 Objetivos da Solução Proposta . . 19 4.2 Metodologia de Desenvolvimento 20 4.3 Levantamento de Requisitos 20 4.3.1 Escopo e Perfis de Usuário . . . . 20 4.3.2 Regras de Negócio . . . 21 4.3.3 Requisitos Funcionais 21 4.3.4 Requisitos Não Funcionais . . . . 22 4.4 Relação com a Especificação Técnica do Capítulo 5 . . . 23 4.5 Modelagem de Casos de Uso . 23 4.6 Arquitetura do Sistema com C4 Model . 24 4.6.1 Diagrama de Contexto . . 24 4.6.2 Diagrama de Contêineres . . . . 25 4.6.3 Diagrama de Componentes . . . . . 26 4.6.4 Diagrama de Deployment . . . . 26 4.7 Modelagem de Classes 27 4.8 Síntese do Capítulo 29

# 5 Implementação 31

5.1 Visão Geral de Implementação . . 31 5.2 Desafios Técnicos . 31 5.3 Requisitos do Sistema . 32 5.3.1 Requisitos Funcionais (RF) . . . . 32 5.3.2 Requisitos Não Funcionais (RNF) . . . . 33 5.3.3 Rastreabilidade (RF → Módulos/Artefatos) . . . . . . . . . . . . 34 5.4 Padrões de Navegação e Comportamento do Sistema . . 34 5.5 Detalhamento do Sistema e Módulos Implementados 34 5.5.1 Navegação por sidebar com ações consistentes . . . . . 35 5.5.2 Soft delete e entidade abstrata de auditoria . . . . 35 5.5.3 Listagens paginadas e desempenho 36 5.5.4 Módulo de Usuários e Autenticação . . . 36 5.5.4.1 Acesso e autenticação (login) . . . . . . . 36 5.5.4.2 Registro externo (autocadastro) . . . . . . . . . . . . . 37 5.5.4.3 Cadastro interno (administradores) . . . . . . . . . . . 37 5.5.4.4 Listagem paginada e operações . . . . . 38 5.5.4.5 Arquitetura e rastreabilidade . . 38 5.5.5 Módulo: Processo Seletivo . . 39 5.5.5.1 Cadastro de processo . . . 39 5.5.5.2 Listagem de processos . . . . 39 5.5.5.3 Cadastro de candidatos . . . . 40 5.5.5.4 Listagem de candidatos . . . . . 40 5.5.5.5 Lançamento de notas . . . 41 5.5.5.6 Notícias do processo . . . . 41 5.5.6 Projetos . . . . 42 5.5.7 Indicadores e Metas BJ (Dashboard) . . . . . . . . . 44 5.5.8 Board (Quadro de Atividades) . . . . 46 5.5.9 Itens (Inventário) . . . . 47 5.6 Decisões de Projeto e Padrões Utilizados . . . . 49 5.7 Diagramas de Classe — Módulos Principais . . 49 5.7.1 Autenticação e Usuários . . . . . 49 5.7.2 Processo Seletivo . . . . . 50 5.7.3 Projetos . . . . 51 5.7.4 Metas BJ e Indicadores . . 53 5.7.5 Board (colunas e cartões) . . . 54 5.7.6 Atividades (itens / controle de estoque) . . . . . . . 55 5.8 Exemplo de Implementação em Código 57 5.8.1 Backend . . . . 57 5.8.1.1 Controller: criação com DTO, Swagger e resposta padronizada . . 57 5.8.1.2 Service: construção da entidade, validações e persistência 58 5.8.1.3 Repository: consultas com native queries . . . . . . . . 58 5.8.1.4 Modelo: entidade estendendo AbstractEntity . . . . . . 59 5.8.2 Frontend 59 5.8.2.1 Formulário React com TypeScript . . . . . . . . . 59 5.8.2.2 Requisição usando React Query . . . . . . . 60 5.8.2.3 Interface da entidade no frontend . . . . 60 5.8.3 Síntese 60 5.9 Implantação e Integrações 61 5.10 Síntese do Capítulo 61

# 6 Estudo de Caso e Resultados 6 3

6.1 Objetivos de avaliação 63 6.2 Contexto e linha de base (antes do Prisma) . . . . 63 6.3 Desenho do estudo 64 6.4 Resultados por módulo 64 6.4.1 Processo Seletivo . . . . 64 6.4.2 Projetos . . . . 64 6.5 Indicadores observados . . . 65 6.6 Discussão 65 6.7 Ameaças à validade . 66 6.8 Síntese . 66

# 7 Conclusão 67

7.1 Síntese das contribuições . 67 7.2 Validação e principais resultados . . . 67 7.3 Implicações práticas . . 68 7.4 Limitações . . . 68 7.5 Trabalhos futuros 68 7.6 Considerações finais 68