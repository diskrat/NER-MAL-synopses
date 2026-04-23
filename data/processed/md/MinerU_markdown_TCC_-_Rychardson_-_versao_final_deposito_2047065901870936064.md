# Prisma: Desenvolvimento de um Sistema Web para Gerenciamento de Empresas Juniores

Rychardson Ribeiro de Souza 

Orientador: Prof. Dr. Itamir de Morais Barroca Filho 

# Prisma: Desenvolvimento de um Sistema Web para Gerenciamento de Empresas Juniores

# Rychardson Ribeiro de Souza

Orientador: Prof. Dr. Itamir de Morais Barroca Filho 

Trabalho de Conclusão de Curso de Graduação na modalidade Monografia, submetido como parte dos requisitos necessários para conclusão do curso de Engenharia de Computação pela Universidade Federal do Rio Grande do Norte (UFRN/CT). 

# Universidade Federal do Rio Grande do Norte - UFRN

# Sistema de Bibliotecas - SISBI

# Catalogação de Publicação na Fonte. UFRN - Biblioteca Central Zila Mamede

Souza, Rychardson Ribeiro de. 

Prisma: desenvolvimento de um sistema Web para gerenciamento de empresas juniores / Rychardson Ribeiro de Souza. - 2025. 

94 f.: il. 

Monografia (graduação) - Universidade Federal do Rio Grande do Norte, Centro de Tecnologia, Graduação em Engenharia de Computação, Natal, RN, 2025. 

Orientação: Prof. Dr. Itamir de Morais Barroca Filho. 

1. Empresas juniores - Monografia. 2. Gestão de processos - Monografia. 3. Sistema web - Monografia. 4. Spring Boot - Monografia. 5. React - Monografia. I. Barroca Filho, Itamir de Morais. II. Título. 

RN/UF/BCZM 

CDU 658 

# Prisma: Desenvolvimento de um Sistema Web para Gerenciamento de Empresas Juniores

# Rychardson Ribeiro de Souza

Monografia aprovada em 28 de novembro de 2025, pela banca examinadora composta pelos seguintes membros: 

Prof. Dr. Itamir de Morais Barroca Filho . . . . . . IMD/UFRN 

Prof. Dr. Jean Mário Moreira de Lima . . IMD/UFFN 

Prof. Dr. André Morais Gurgel IMD/UFRN 

A minha família e amigos ...... 

# Agradecimentos

A minha mãe e ao meu pai pelo apoio durante o andamento do curso. 

A Pedro Leandro, amigo que me apoiou na reta final do curso. 

A Empresa Júnior Include Engenharia, por se disponibilizarem a colaborar com minha monografia. 

Ao meu orientador professor Dr. Itamir de Morais Barroca Filho, sou grato pela orienta-ção. 

Aos demais colegas de graduação, pelas críticas e sugestões. 

# Resumo

Empresas juniores são associações sem fins lucrativos, formadas e geridas por estudantes de graduação de instituições de ensino superior, possuindo como principal objetivo proporcionar a vivência de um ambiente empresarial e aprendizado para os alunos por meio da realização de projetos. 

Nesse contexto, uma dificuldade enfrentada é a gestão de processos, devido à descentralização das atividades em múltiplas ferramentas de gerenciamento, o que dificulta o acompanhamento por parte dos gestores. Para solucionar essa problemática, este trabalho propõe o Prisma, um sistema web desenvolvido especificamente para o contexto das empresas juniores, reunindo em uma única plataforma as funcionalidades necessárias ao gerenciamento de seus principais processos. Em vez de integrar ferramentas externas, o Prisma implementa módulos próprios que substituem soluções dispersas, oferecendo padronização, rastreabilidade e maior eficiência na gestão organizacional. 

O Prisma oferece módulos de gerenciamento para Processo Seletivo, permitindo administrar candidatos, etapas, notas, avisos; Projetos, com a gestão de riscos, metas e membros; Board, entregando uma gerência de atividades; Metas para acompanhamento de indicadores e Itens para inventário. 

O sistema é acessível a partir de dispositivos conectados à internet e foi desenvolvido com o framework Spring Boot e a biblioteca React do JavaScript. Ao final do projeto, espera-se disponibilizar uma solução que auxilie os gestores das empresas juniores no monitoramento e na melhoria de seus processos. 

Palavras-chave: empresas juniores; gestão de processos; sistema web; Spring Boot; React. 

# Abstract

Junior enterprises are non-profit associations managed by undergraduate students whose main purpose is to provide practical business experience and learning through project development. 

In this context, a recurring challenge is process management, often hindered by the decentralization of activities across multiple independent tools, which makes it difficult for managers to effectively monitor and coordinate operations. To address this issue, this work proposes Prisma, a web system designed specifically for the reality of junior enterprises, bringing together in a single platform the functionalities required to manage their core processes. Rather than integrating external tools, Prisma implements its own modules to replace fragmented solutions, offering standardization, traceability, and greater organizational efficiency. 

Prisma includes management modules for the Selection Process (candidates, stages, grades, and notices), Projects (risks, goals, and members), Board (kanban-style activity management), Goals (indicator tracking), and Items (inventory). 

The system is accessible from internet-connected devices and was developed using the Spring Boot framework and the React JavaScript library. The project aims to provide a solution that supports junior-enterprise managers in monitoring and improving their organizational processes. 

Keywords: junior enterprises; process management; web system; Spring Boot; React. 

# Lista de Figuras

3.1 Interface principal do Trello, com estrutura baseada em quadros e cartões. 13 

3.2 Interface principal do Notion, utilizada para organização e documentação colaborativa. . 14 

3.3 Interface do OpenProject, sistema open source para gestão colaborativa de projetos. 15 

3.4 Interface do sistema Prisma, integrando múltiplos módulos de gestão em uma única plataforma. 16 

4.1 Diagrama de casos de uso do sistema Prisma 23 

4.2 Diagrama de contexto (C1) do sistema Prisma . . 24 

4.3 Diagrama de contêineres (C2) do sistema Prisma . 25 

4.4 Diagrama de componentes (C3) do sistema Prisma . . 26 

4.5 Diagrama de deployment (C4) do sistema Prisma 27 

4.6 Diagrama geral de classes do sistema Prisma 28 

5.1 Padrão de navegação na sidebar: subitens Cadastrar/Listar (e Dashboard em Projetos). 35 

5.2 Tela de login do Prisma. 36 

5.3 Registro externo com validações e consentimento. . . . 37 

5.4 Cadastro interno: definição de papéis e permissões por módulo. . . . . . . 38 

5.5 Listagem administrativa de usuários (paginação e ações rápidas). . . . . . 38 

5.6 Cadastro de processo seletivo com definição e ordenação de etapas. . . . . 39 

5.7 Lista de processos seletivos com ações de atalho. 40 

5.8 Cadastro de candidato associado a um processo. . . . 40 

5.9 Candidatos de um processo seletivo (listagem paginada). . . . . . . . 41 

5.10 Lançamento de notas por etapa e cálculo automático de médias. . . . . . 41 

5.11 Publicação de notícias do processo seletivo com suporte a Markdown. . . 42 

5.12 Listagem de projetos com badges de status, paginação e ações rápidas. . . 43 

5.13 Fluxo de cadastro em quatro passos: dados gerais, metas, membros e riscos. 43 

5.14 Detalhes do projeto com seções de Metas, Membros e Riscos. . . . . . . 44 

5.15 Dashboard do módulo de Projetos com indicadores e busca por alocações. 44 

5.16 Receitas e Metas — visão Faturamento x Meta. 45 

5.17 Receitas e Metas — visão Faturamento colaborativo x Meta. . . 46 

5.18 Receitas e Metas — visão Composição (mensal e acumulados). . . . . . . 46 

5.19 Board com colunas e modal para criação de nova coluna (título e cor). . . 47 

5.20 Cadastro de item com título, quantidade e descrição opcional. . . . . 48 

5.21 Listagem de itens (paginação, quantidade em destaque e ações de edi-ção/remoção). . 48 

5.22 Modelo de classes para autenticação e usuários 49 

5.23 Modelo de classes para processo seletivo (candidatos, notas, estágios e notícias) . 51 

5.24 Modelo de classes para projetos (metas, riscos e membros) . . . . . . . 52 

5.25 Modelo de classes para metas/indicadores (integração BJ) . . . . . 53 

5.26 Modelo de classes do Board (colunas e cartões). . . . 55 

5.27 Modelo de classes de Itens (inventário/estoque). . . . 56 

# Lista de Tabelas

3.1 Comparativo entre Prisma, Trello e Notion . . . 16 

5.1 Requisitos Funcionais (RF) . . 32 

5.2 Requisitos Não Funcionais (RNF) 33 

5.3 Matriz de Rastreabilidade (resumo $\mathrm { R F } $ artefatos) . . 34 

# LISTA DE ABREVIATURAS E SIGLAS

<table><tr><td>ABNT</td><td>Associação Brasileira de Normas Técnicas</td></tr><tr><td>API</td><td>Application Programming Interface</td></tr><tr><td>BJ</td><td>Brasil Júnior</td></tr><tr><td>C4</td><td>C4 Model (modelo de visualização arquitetural)</td></tr><tr><td>CRUD</td><td>Create, Read, Update e Delete</td></tr><tr><td>DTO</td><td>Data Transfer Object</td></tr><tr><td>EJ</td><td>Empresa Júnior</td></tr><tr><td>JPA</td><td>Java Persistence API</td></tr><tr><td>JWT</td><td>JSON Web Token</td></tr><tr><td>KPI</td><td>Key Performance Indicator (indicador-chave de desempenho)</td></tr><tr><td>PS</td><td>Proteso Seletivo</td></tr><tr><td>REST</td><td>Representational State Transfer</td></tr><tr><td>SPA</td><td>Single/Page Application</td></tr><tr><td>SSO</td><td>Single Sign-On</td></tr><tr><td>UI</td><td>User Interface (interface do usoário)</td></tr><tr><td>UML</td><td>Unified Modeling Language</td></tr><tr><td>UX</td><td>User Experience (experiência do usoário)</td></tr></table>

# Sumário

# Lista de Figuras i

# Lista de Tabelas iii

# Lista de abreviaturas e siglas v

# Sumário vii

# 1 Introdução 1

1.1 Problema e motivação . . 1 

1.2 Objetivos 2 

1.3 Metodologia . . 2 

1.4 Organização do trabalho 3 

# 2 Fundamentação Teórica 5

2.1 Gestão de Processos em Empresas Juniores . . 5 

2.2 Sistemas Web e sua Relevância Organizacional 6 

2.3 Framework Spring Boot . . . 6 

2.4 Banco de Dados PostgreSQL . 6 

2.5 Biblioteca React . 7 

2.6 Linguagem TypeScript . . . 7 

2.7 Estilização com TailwindCSS . . 8 

2.8 Metodologias Ágeis e o Desenvolvimento do Prisma 8 

2.9 Modelagem UML . . 8 

2.9.1 Diagramas Estruturais . . 9 

2.9.2 Diagramas Comportamentais . . . . . 9 

2.10 Modelo C4 para Visualização de Arquitetura de Software . . 10 

2.10.1 Princípios e objetivos . . . . 10 

2.10.2 Os quatro níveis do C4 . . 10 

2.10.3 Benefícios práticos . . . . . . 11 

2.10.4 C4 e UML: papéis complementares . . . 11 

2.10.5 Boas práticas e limitações . . . 11 

2.11 Síntese do Capítulo 11 

# 3 Trabalhos Relacionados 13

3.1 Sistemas de Gestão e Ferramentas Integradas 13 

3.2 Trabalhos Acadêmicos e Sistemas Open Source . . . 14 

3.3 Contribuições e Diferenciais do Prisma 15 

3.3.1 Comparativo entre Prisma, Trello e Notion . . 16 

# 4 Prisma 19

4.1 Objetivos da Solução Proposta . . 19 

4.2 Metodologia de Desenvolvimento 20 

4.3 Levantamento de Requisitos 20 

4.3.1 Escopo e Perfis de Usuário . . . . 20 

4.3.2 Regras de Negócio . . . 21 

4.3.3 Requisitos Funcionais 21 

4.3.4 Requisitos Não Funcionais . . . . 22 

4.4 Relação com a Especificação Técnica do Capítulo 5 . . . 23 

4.5 Modelagem de Casos de Uso . 23 

4.6 Arquitetura do Sistema com C4 Model . 24 

4.6.1 Diagrama de Contexto . . 24 

4.6.2 Diagrama de Contêineres . . . . 25 

4.6.3 Diagrama de Componentes . . . . . 26 

4.6.4 Diagrama de Deployment . . . . 26 

4.7 Modelagem de Classes 27 

4.8 Síntese do Capítulo 29 

# 5 Implementação 31

5.1 Visão Geral de Implementação . . 31 

5.2 Desafios Técnicos . 31 

5.3 Requisitos do Sistema . 32 

5.3.1 Requisitos Funcionais (RF) . . . . 32 

5.3.2 Requisitos Não Funcionais (RNF) . . . . 33 

5.3.3 Rastreabilidade (RF → Módulos/Artefatos) . . . . . . . . . . . . 34 

5.4 Padrões de Navegação e Comportamento do Sistema . . 34 

5.5 Detalhamento do Sistema e Módulos Implementados 34 

5.5.1 Navegação por sidebar com ações consistentes . . . . . 35 

5.5.2 Soft delete e entidade abstrata de auditoria . . . . 35 

5.5.3 Listagens paginadas e desempenho 36 

5.5.4 Módulo de Usuários e Autenticação . . . 36 

5.5.4.1 Acesso e autenticação (login) . . . . . . . 36 

5.5.4.2 Registro externo (autocadastro) . . . . . . . . . . . . . 37 

5.5.4.3 Cadastro interno (administradores) . . . . . . . . . . . 37 

5.5.4.4 Listagem paginada e operações . . . . . 38 

5.5.4.5 Arquitetura e rastreabilidade . . 38 

5.5.5 Módulo: Processo Seletivo . . 39 

5.5.5.1 Cadastro de processo . . . 39 

5.5.5.2 Listagem de processos . . . . 39 

5.5.5.3 Cadastro de candidatos . . . . 40 

5.5.5.4 Listagem de candidatos . . . . . 40 

5.5.5.5 Lançamento de notas . . . 41 

5.5.5.6 Notícias do processo . . . . 41 

5.5.6 Projetos . . . . 42 

5.5.7 Indicadores e Metas BJ (Dashboard) . . . . . . . . . 44 

5.5.8 Board (Quadro de Atividades) . . . . 46 

5.5.9 Itens (Inventário) . . . . 47 

5.6 Decisões de Projeto e Padrões Utilizados . . . . 49 

5.7 Diagramas de Classe — Módulos Principais . . 49 

5.7.1 Autenticação e Usuários . . . . . 49 

5.7.2 Processo Seletivo . . . . . 50 

5.7.3 Projetos . . . . 51 

5.7.4 Metas BJ e Indicadores . . 53 

5.7.5 Board (colunas e cartões) . . . 54 

5.7.6 Atividades (itens / controle de estoque) . . . . . . . 55 

5.8 Exemplo de Implementação em Código 57 

5.8.1 Backend . . . . 57 

5.8.1.1 Controller: criação com DTO, Swagger e resposta padronizada . . 57 

5.8.1.2 Service: construção da entidade, validações e persistência 58 

5.8.1.3 Repository: consultas com native queries . . . . . . . . 58 

5.8.1.4 Modelo: entidade estendendo AbstractEntity . . . . . . 59 

5.8.2 Frontend 59 

5.8.2.1 Formulário React com TypeScript . . . . . . . . . 59 

5.8.2.2 Requisição usando React Query . . . . . . . 60 

5.8.2.3 Interface da entidade no frontend . . . . 60 

5.8.3 Síntese 60 

5.9 Implantação e Integrações 61 

5.10 Síntese do Capítulo 61 

# 6 Estudo de Caso e Resultados 6 3

6.1 Objetivos de avaliação 63 

6.2 Contexto e linha de base (antes do Prisma) . . . . 63 

6.3 Desenho do estudo 64 

6.4 Resultados por módulo 64 

6.4.1 Processo Seletivo . . . . 64 

6.4.2 Projetos . . . . 64 

6.5 Indicadores observados . . . 65 

6.6 Discussão 65 

6.7 Ameaças à validade . 66 

6.8 Síntese . 66 

# 7 Conclusão 67

7.1 Síntese das contribuições . 67 

7.2 Validação e principais resultados . . . 67 

7.3 Implicações práticas . . 68 

7.4 Limitações . . . 68 

7.5 Trabalhos futuros 68 

7.6 Considerações finais 68 

# Referências bibliográficas 71

# Capítulo 1 Introdução

No Brasil, as empresas juniores (EJs) são reconhecidas por lei como associações civis sem fins lucrativos que funcionam no âmbito de instituições de ensino superior, com gestão estudantil e finalidade educativa (BRASIL, 2016). Na prática, realizam projetos e serviços alinhados às suas áreas de formação, desenvolvendo competências profissionais e empreendedoras, sob orientação acadêmica quando aplicável (PARANÁ, s.d.). Em ní- vel nacional, a Confederação Brasil Júnior consolida dados e iniciativas do movimento, registrando expansão contínua do ecossistema (JÚNIOR, 2023). 

Em termos de escala, o movimento reúne milhares de estudantes e um número expressivo de EJs em todo o país, o que ajuda a dimensionar o potencial de impacto de ferramentas que padronizem a operação e consolidem informações nessas organizações, especialmente em contextos de alta rotatividade de membros e múltiplos projetos em paralelo (JÚNIOR, 2023). 

A gestão eficiente de processos é um dos pilares fundamentais para o bom funcionamento e a evolução de qualquer organização. No ambiente das empresas juniores, esse desafio se torna ainda mais evidente devido à rotatividade de membros e à necessidade de documentar operações administrativas e estratégicas. A ausência de ferramentas centralizadoras frequentemente resulta em dificuldade de acompanhamento das atividades e de tomada de decisão pelos gestores. 

# 1.1 Problema e motivação

A Brasil Júnior reporta expansão contínua do movimento, com milhares de estudantes envolvidos e um número expressivo de EJs em funcionamento, chegando a quase 1500 empresas juniores (JÚNIOR, 2023). Esse crescimento constante também aumenta a complexidade operacional, com várias frentes de trabalho — projetos, processo seletivo e comunicação —, alta rotatividade natural de membros e necessidade de prestação de contas a orientadores e diretoria. 

Na prática, a operação cotidiana de uma EJ costuma envolver diversas frentes: execução de projetos, condução de processos seletivos, planejamento estratégico, gestão de indicadores, comunicação interna e prestação de contas à diretoria e aos orientadores. Diante dessa diversidade, é comum que as atividades sejam distribuídas em planilhas, documentos dispersos, trocas de mensagens e ferramentas desacopladas (como Trello, 

Notion e formulários). Isso gera efeitos recorrentes, tais como: (i) retrabalho e duplicidade de dados; (ii) dificuldade para acompanhar prazos, status e entregas; (iii) ausência de trilhas históricas; e (iv) perda de contexto sempre que ocorre troca de gestão — realidade comum nas EJs, que renovam grande parte do seu quadro anualmente. 

Essas fragilidades se tornam ainda mais perceptíveis em momentos críticos, como períodos de inscrição no Processo Seletivo, execução simultânea de projetos ou fechamento de semestres. A falta de centralização e padronização aumenta o esforço manual, reduz a eficiência e compromete a tomada de decisão, uma vez que informações relevantes precisam ser buscadas em diferentes arquivos e plataformas. 

A motivação deste trabalho é disponibilizar uma ferramenta única de gestão de processos no contexto das EJs, reduzindo o esforço manual e elevando a transparência dos processos mais frequentes (Processo Seletivo e Projetos), sem perder de vista práticas de governança (status padronizados, indicadores e histórico consultável), promovendo uma gestão mais eficiente e escalável ao longo das transições de gestão estudantil. 

# 1.2 Objetivos

Desenvolver o sistema Prisma, uma plataforma web que centralize e automatize os principais processos internos de empresas juniores, oferecendo uma plataforma única capaz de reduzir retrabalho, aumentar a rastreabilidade e apoiar a tomada de decisão dos gestores. O Prisma deve oferecer uma interface intuitiva e recursos de acompanhamento de tarefas, metas e indicadores de desempenho para solucionar as problemáticas operacionais das EJs. 

Quanto às funcionalidades esperadas, o Prisma deve disponibilizar aos seus usuários: 

• a consolidação, em um único sistema, das funcionalidades de Processo Seletivo, Projetos, Board, Metas e Itens, eliminando o uso de planilhas e ferramentas paralelas; 

• histórico consultável, padronização de status e indicadores, permitindo a compara-ção entre diferentes períodos de gestão; 

• redução do esforço operacional em atividades repetitivas, como o lançamento de notas no Processo Seletivo e a comunicação entre frentes; 

• APIs REST seguras (JWT) para integrações e automações pontuais, com controle de acesso baseado em perfis de usuário. 

# 1.3 Metodologia

O desenvolvimento é fundamentado em: (i) elicitação e especificação de requisitos; (ii) desenho arquitetural e modelagem (UML e modelo C4); (iii) implementação incremental; e (iv) validação em campo com coleta de métricas (tempo/esforço). 

Na primeira etapa, para elencar os requisitos, considerou-se a realidade das EJs, seguida de reuniões com lideranças da Include Engenharia para validar os requisitos apresentados e definir prioridades e novas demandas. Na sequência, foram realizados os de-

senhos arquiteturais e a modelagem UML e C4, a fim de compreender como os diferentes usuários interagem com o sistema. 

Com os requisitos e a modelagem estabelecidos, definiram-se os critérios e as tecnologias a serem utilizadas. Optou-se pelo seguinte stack: no backend, Spring Boot com camadas Controller–Service–Repository e PostgreSQL para persistência; no frontend, React com TypeScript. A interface emprega Tailwind CSS e bibliotecas de componentes. React favorece interfaces responsivas; Spring Boot simplifica a criação de APIs REST seguras (por exemplo, com JSON Web Token — JWT), integra bem testes e oferece estabilidade; e o PostgreSQL proporciona consistência no armazenamento de dados. 

Na implementação incremental, elaborou-se um diagrama de casos de uso para explicitar a relação entre as entidades do sistema, com foco nos módulos prioritários (Processo Seletivo e Projetos), definidos em (i). 

Por fim, com os módulos prioritários implementados, procedeu-se à validação junto aos interessados na Include Engenharia, para posterior coleta de dados e mensuração de tempo e esforço alocado. 

# 1.4 Organização do trabalho

Esta monografia está estruturada nos seguintes capítulos, respectivamente: 

• Capítulo 2 — Fundamentação Teórica: apresenta conceitos e tecnologias que embasam a monografia, discutindo a importância da gestão de processos em EJs e as tecnologias empregadas no desenvolvimento do Prisma, como Spring Boot, PostgreSQL, React, TypeScript e Tailwind CSS. 

• Capítulo 3 — Trabalhos Relacionados: realiza uma comparação de sistemas semelhantes ao Prisma, privados ou open source, mostrando o que oferecem e os diferenciais do Prisma. 

• Capítulo 4 — Prisma: contextualiza o problema, apresenta os objetivos da solu-ção, os requisitos funcionais e não funcionais, bem como restrições e critérios de aceitação. 

• Capítulo 5 — Implementação: descreve as estratégias utilizadas na arquitetura do sistema, com os modelos e mapeamentos $\mathrm { ( D T O  }$ entidade), endpoints, persistência, decisões de engenharia e a descrição dos módulos (Processo Seletivo, Projetos, Board, Metas, Itens) e seus fluxos. 

• Capítulo 6 — Estudo de Caso e Resultados: apresenta o plano de avaliação, métricas e procedimentos de coleta, os resultados por módulo, os indicadores observados, pontos de melhoria e ameaças à validade. 

• Capítulo 7 — Conclusão: traz as considerações finais, com a síntese das contribuições, limitações e possíveis trabalhos futuros. 

Espera-se que o Prisma contribua para a melhoria da organização interna, o aumento da eficiência operacional e o fortalecimento da transparência nos processos das EJs, tornando a gestão mais ágil, integrada e confiável. 

# Capítulo 2

# Fundamentação Teórica

Este capítulo apresenta os principais conceitos e tecnologias que servem de base para o desenvolvimento do sistema Prisma. São abordados aspectos relacionados à gestão de processos nas empresas juniores, às características dos sistemas web e às ferramentas tecnológicas utilizadas na implementação do projeto. 

# 2.1 Gestão de Processos em Empresas Juniores

A gestão de processos é uma disciplina da administração voltada para o mapeamento, análise e melhoria contínua dos fluxos de trabalho organizacionais. Segundo Rummler e Brache (2010), a gestão por processos visa alinhar as atividades operacionais à estraté- gia organizacional, otimizando recursos e reduzindo redundâncias (RUMMLER GEARY A.; BRACHE, 2010). Hammer e Champy (1993) complementam que o redesenho de processos é uma ferramenta essencial para aumentar a competitividade e eficiência das organizações (HAMMER; CHAMPY, 1993). 

No contexto das empresas juniores — associações civis sem fins lucrativos, formadas e geridas por estudantes de graduação — a gestão de processos assume um papel ainda mais estratégico. Conforme a Confederação Brasileira de Empresas Juniores (Brasil Jú- nior, 2023), o Movimento Empresa Júnior (MEJ) conta atualmente com mais de 1.700 empresas distribuídas em todas as regiões do país, atuando na capacitação empreendedora de mais de 30 mil estudantes universitários (JÚNIOR, 2023). 

Entretanto, o caráter rotativo das diretorias e o curto ciclo de permanência dos membros dificultam a consolidação de práticas administrativas eficazes e o registro de conhecimento organizacional (OLIVEIRA, 2019). Além disso, o uso fragmentado de múltiplas ferramentas digitais — como planilhas, e-mails e plataformas de gestão isoladas — gera perda de dados e retrabalho. Nesse cenário, a adoção de sistemas integrados de gestão se torna fundamental para centralizar informações, manter a continuidade administrativa e melhorar a governança interna. 

O Prisma surge como resposta a essa necessidade, propondo um ambiente unificado em que os gestores das empresas juniores possam acompanhar processos internos, indicadores e tarefas de forma estruturada, transparente e acessível. 

# 2.2 Sistemas Web e sua Relevância Organizacional

Com o avanço das tecnologias de rede na década de 1990 e a consolidação da internet comercial, os sistemas web passaram a substituir os softwares locais, oferecendo maior portabilidade e facilidade de manutenção. De acordo com Pressman e Maxim (2016), as aplicações web modernas são caracterizadas pela sua arquitetura distribuída, pela atualização centralizada e pela independência de plataforma, o que reduz custos operacionais e amplia o alcance do software (PRESSMAN ROGER S.; MAXIM, 2016). 

A arquitetura de três camadas (three-tier architecture) — composta por apresentação, lógica de negócio e banco de dados — consolidou-se como padrão no desenvolvimento de sistemas web corporativos (SOMMERVILLE, 2011). Essa separação de responsabilidades facilita a manutenção, promove a escalabilidade e possibilita a substituição de componentes individuais sem comprometer o funcionamento geral. 

No ambiente das empresas juniores, os sistemas web desempenham papel crucial ao permitir a integração entre setores, a comunicação em tempo real e o acompanhamento simultâneo das operações. Além disso, o acesso multiplataforma, por meio de navegadores e dispositivos móveis, amplia a usabilidade e favorece a continuidade das atividades mesmo em regimes híbridos ou remotos (LAUDON KENNETH C.; LAUDON, 2019). 

# 2.3 Framework Spring Boot

O Spring Boot é um framework de código aberto lançado pela Pivotal Software em 2014, como uma evolução do ecossistema Spring. Ele tem como principal objetivo simplificar o processo de configuração e implantação de aplicações Java, reduzindo o chamado boilerplate code — código repetitivo que não agrega valor direto à lógica de negócio (WALLS, 2016). 

A popularidade do Spring Boot está associada à sua abordagem de convenção sobre configuração (convention over configuration), que facilita a criação de aplicações produtivas e seguras com mínima configuração manual. Segundo o relatório JetBrains (2023), o Spring Boot é atualmente o framework mais utilizado para desenvolvimento backend em Java no mundo, presente em mais de $60 \%$ dos projetos corporativos (JETBRAINS, 2023). 

Entre suas principais vantagens estão o suporte nativo a APIs REST, a integração simplificada com bancos de dados e a compatibilidade com arquiteturas baseadas em microserviços. No projeto Prisma, o Spring Boot é responsável pela camada de back-end, lidando com o processamento de requisições, aplicação das regras de negócio e persistência de dados, garantindo segurança e desempenho na manipulação das informações. 

# 2.4 Banco de Dados PostgreSQL

O PostgreSQL é um sistema gerenciador de banco de dados relacional (SGBD) de código aberto, desenvolvido originalmente na Universidade da Califórnia em Berkeley 

no final da década de 1980, a partir do projeto POSTGRES, liderado por Michael Stonebraker (STONEBRAKER, 1986). Considerado um dos bancos de dados mais avançados do mundo, o PostgreSQL é reconhecido por sua aderência ao padrão SQL, estabilidade e suporte a extensões, funções definidas pelo usuário e controle transacional robusto (GROUP, 2024). 

Pesquisas de mercado, como o ranking DB-Engines (2024), colocam o PostgreSQL entre os três SGBDs mais utilizados globalmente, ao lado do MySQL e do Oracle Database (DB-ENGINES, 2024). Sua natureza open source e sua forte comunidade de desenvolvimento fazem dele uma alternativa competitiva e segura para aplicações corporativas e acadêmicas. 

A escolha do PostgreSQL para o sistema Prisma se deve à sua estabilidade, desempenho e compatibilidade com o Spring Boot, possibilitando integração direta via JPA/Hibernate e garantindo integridade e eficiência na persistência dos dados. 

# 2.5 Biblioteca React

O React é uma biblioteca JavaScript criada pelo engenheiro Jordan Walke, do Facebook, em 2013, com o propósito de otimizar o desenvolvimento de interfaces dinâmicas e reativas (PLATFORMS, 2023). Seu diferencial está no uso do conceito de Virtual DOM, que reduz a necessidade de renderização completa da página, tornando o desempenho mais eficiente e a interação mais fluida para o usuário. 

De acordo com o relatório Stack Overflow Developer Survey (2023), o React é a biblioteca de front-end mais popular entre os desenvolvedores há seis anos consecutivos, utilizada em cerca de $40 \%$ dos projetos analisados (OVERFLOW, 2023). Sua arquitetura baseada em componentes promove modularidade, reutilização e manutenção facilitada do código. 

No projeto Prisma, o React foi utilizado para garantir uma interface moderna, responsiva e intuitiva. A integração entre React e Spring Boot permitiu a construção de um sistema completo, com comunicação eficiente entre cliente e servidor, resultando em uma experiência de uso consistente e de alto desempenho. 

# 2.6 Linguagem TypeScript

O TypeScript é uma linguagem desenvolvida pela Microsoft em 2012, projetada como um superconjunto do JavaScript que adiciona tipagem estática e recursos de orientação a objetos (CORPORATION, 2023). Essa abordagem aumenta a robustez do código, reduz erros em tempo de execução e melhora a legibilidade e manutenção em grandes aplica-ções. 

Segundo a pesquisa State of JavaScript (2023), o TypeScript é utilizado por mais de $80 \%$ dos desenvolvedores de front-end em aplicações modernas (JS, 2023). Sua integra-ção com o React proporciona um ambiente de desenvolvimento mais confiável e eficiente, especialmente em projetos colaborativos e de longa duração. 

# 2.7 Estilização com TailwindCSS

Para o design da interface, foi adotado o TailwindCSS, um framework utilitário que permite construir layouts responsivos de forma rápida e padronizada (LABS, 2024). Baseandose em classes utilitárias, o TailwindCSS favorece consistência visual, reduz dependências de arquivos CSS extensos e acelera o processo de desenvolvimento. 

Complementarmente, foram utilizadas bibliotecas de componentes, como shadcn/ui, que se integram ao TailwindCSS e possibilitam uma prototipagem mais ágil. Essa combinação assegura uma interface moderna, consistente e adequada às demandas de usabilidade do Prisma. 

# 2.8 Metodologias Ágeis e o Desenvolvimento do Prisma

As metodologias ágeis surgiram no início dos anos 2000 como uma alternativa aos modelos tradicionais de desenvolvimento, como o Waterfall. O marco inicial foi a publicação do Manifesto Ágil em 2001 por um grupo de 17 especialistas, incluindo Kent Beck e Martin Fowler, que enfatizaram a importância da colaboração, da entrega contínua de valor e da capacidade de adaptação às mudanças (BECK; FOWLER, 2001). 

Atualmente, práticas como Scrum e Kanban são amplamente adotadas em equipes de software, permitindo um ciclo de desenvolvimento iterativo e incremental. Conforme Schwaber e Sutherland (2020), o Scrum é particularmente eficaz para ambientes que exigem inovação constante, pois promove feedback rápido e comunicação contínua entre os membros (SCHWABER KEN; SUTHERLAND, 2020). 

No desenvolvimento do Prisma, essas metodologias foram aplicadas com o intuito de garantir entregas regulares, revisões frequentes e alinhamento contínuo com os objetivos do projeto. Essa abordagem favorece a experimentação, o aprendizado constante e a melhoria contínua — elementos essenciais em projetos acadêmicos e colaborativos. 

# 2.9 Modelagem UML

A Unified Modeling Language (UML) é uma linguagem padrão para a modelagem de sistemas orientados a objetos, amplamente utilizada para representar graficamente a estrutura e o comportamento de softwares (BOOCH; RUMBAUGH; JACOBSON, 2005). Segundo Booch, Rumbaugh e Jacobson (2005), a UML fornece uma notação visual unificada que facilita a comunicação entre desenvolvedores, analistas e demais stakeholders de um projeto, permitindo que diferentes visões do sistema sejam compreendidas de forma integrada. 

Os diagramas UML auxiliam na documentação, no entendimento e na manutenção do sistema, promovendo uma visão abstrata das suas camadas, componentes e relacionamentos. A linguagem é composta por dois grandes grupos de diagramas: estruturais e comportamentais. 

# 2.9.1 Diagramas Estruturais

Os diagramas estruturais descrevem os elementos estáticos do sistema, ou seja, sua arquitetura, classes, objetos e relacionamentos. Entre eles, destacam-se: 

• Diagrama de classes: mostra a estrutura do sistema em termos de classes, atributos, métodos e associações; 

• Diagrama de objetos: ilustra instâncias concretas das classes em um determinado momento; 

• Diagrama de componentes: representa os módulos físicos do sistema; 

• Diagrama de implantação: evidencia a distribuição do software e seus artefatos em infraestrutura física; 

• Diagrama de pacotes: organiza as classes e componentes em agrupamentos lógicos. 

Esses diagramas permitem visualizar a organização e os relacionamentos internos de um sistema, fornecendo uma base sólida para o desenvolvimento orientado a objetos. 

# 2.9.2 Diagramas Comportamentais

Já os diagramas comportamentais descrevem como o sistema reage a eventos e interações, enfatizando o fluxo de atividades e a comunicação entre os elementos. Entre os principais estão: 

• Diagrama de casos de uso: demonstra as interações entre os atores externos e o sistema, definindo o escopo funcional; 

• Diagrama de atividades: detalha o fluxo de processos e decisões lógicas; 

• Diagrama de sequência: representa a troca de mensagens entre objetos ou componentes ao longo do tempo; 

• Diagrama de estados: mostra as transições de estados de um objeto conforme as ações do sistema. 

Esses diagramas auxiliam na compreensão do comportamento dinâmico do sistema, permitindo representar de forma clara a lógica de execução e as interações entre os componentes. 

No desenvolvimento do sistema Prisma, foram utilizados principalmente os diagramas de casos de uso, classes e atividades. Esses diagramas permitem compreender tanto as funcionalidades oferecidas aos usuários quanto a estrutura interna e os fluxos de informação do sistema. Essa abordagem contribuiu para uma modelagem consistente e alinhada aos princípios da orientação a objetos, servindo como base para a implementação das funcionalidades nas camadas de back-end e front-end. 

# 2.10 Modelo C4 para Visualização de Arquitetura de Software

O C4 Model é uma abordagem proposta por brown2018 para visualizar arquiteturas de software por meio de um conjunto pequeno e coerente de diagramas, com diferentes níveis de detalhe. Seu objetivo é reduzir a ambiguidade de diagramas ad hoc e fornecer uma linguagem visual simples, voltada à comunicação entre públicos com graus distintos de conhecimento técnico (BROWN, s.d.). Diferentemente da UML — uma linguagem ampla, com múltiplos tipos de diagramas — o C4 tem foco no o que comunicar (o nível de abstração) e em para quem comunicar (o público), favorecendo consistência e alinhamento de expectativas. 

# 2.10.1 Princípios e objetivos

Os princípios norteadores do C4 incluem: (i) hierarquia de abstração, permitindo ir do todo ao detalhe progressivamente; (ii) consistência visual, com um vocabulário reduzido de elementos (pessoas, sistemas, contêineres e componentes); (iii) independência de notação, podendo ser desenhado em ferramentas diversas, desde quadros brancos até geradores automáticos; e (iv) documentação enxuta, em que cada diagrama responde a perguntas específicas sobre o sistema (BROWN, 2018; BROWN, s.d.). 

# 2.10.2 Os quatro níveis do C4

O modelo estabelece quatro níveis principais de visualização (BROWN, s.d.): 

• C1 — Contexto do Sistema (System Context): apresenta o sistema como uma “caixa” e suas interações externas (pessoas, outros sistemas, integrações). Responde à pergunta: quem usa o sistema e com o que ele se conecta? 

• C2 — Contêineres (Containers): mostra os blocos executáveis e/ou implantáveis que compõem a solução (por exemplo, SPA, API, banco de dados, filas), além dos protocolos de comunicação entre eles. Responde: como o sistema é executado tecnicamente? 

• C3 — Componentes (Components): decompõe um contêiner (p. ex., a API) em componentes de software (controladores, serviços, repositórios), destacando responsabilidades e dependências. 

• C4 — Código (Code): opcional; detalha uma parte do componente (p. ex., um diagrama de classes de um módulo) quando for útil à compreensão de implementações específicas. 

Além desses níveis, brown2018 sugere diagramas suplementares, como Deployment (para infraestrutura/ambiente) e System Landscape (para mapear múltiplos sistemas de uma organização), frequentemente utilizados em conjunto com C1–C3 quando a execução em produção e a integração organizacional são relevantes. 

# 2.10.3 Benefícios práticos

Entre os benefícios reportados pelo uso do C4 estão: (i) comunicação clara com equipes técnicas e não técnicas; (ii) trilha de rastreabilidade entre visão macro e decisões de baixo nível; (iii) facilidade de manutenção dos diagramas, pela simplicidade da notação; e (iv) complementaridade com outras técnicas (p. ex., UML para detalhes estruturais) (BROWN, 2018). No contexto deste trabalho, o C4 foi empregado para apresentar, de forma progressiva, a visão do Prisma — do contexto externo (C1) aos contêineres (C2) e componentes do back-end (C3) — além de um diagrama de deployment para explicitar a infraestrutura de execução. 

# 2.10.4 C4 e UML: papéis complementares

Enquanto a UML dispõe de 14 tipos de diagramas para diferentes perspectivas, o C4 privilegia poucos diagramas, cada qual associado a um nível de abstração. Assim, o C4 comunica o “mapa” arquitetural (quem interage, como é implantado, como as partes se conectam), e a UML é particularmente útil para detalhar estrutura (p. ex., diagrama de classes) e comportamento (p. ex., sequência/atividades) de partes selecionadas. A combinação de ambos favorece documentação enxuta, porém suficientemente precisa, alinhada às necessidades de comunicação deste projeto (BROWN, 2018; BROWN, s.d.). 

# 2.10.5 Boas práticas e limitações

Boas práticas recomendadas incluem: (i) manter legendas e descrições sucintas diretamente nos diagramas; (ii) padronizar formas e cores para papéis (pessoas), sistemas, contêineres e componentes; (iii) evitar excesso de elementos em um mesmo diagrama; e (iv) sincronizar os diagramas com o repositório de código e com a infraestrutura (quando possível, por geração automática) (BROWN, s.d.). Como limitação, o C4 não prescreve notação formal ou semântica executável; quando for necessária modelagem precisa de baixo nível, recomenda-se complementar com UML, ADRs e documentação de APIs. 

# 2.11 Síntese do Capítulo

Neste capítulo, discutiram-se os conceitos fundamentais que sustentam o desenvolvimento do sistema Prisma. A gestão de processos em empresas juniores foi apresentada como o contexto motivador, enquanto as tecnologias Spring Boot, PostgreSQL, React e TypeScript foram descritas como ferramentas essenciais para a implementação de um sistema web moderno, eficiente e escalável. Por fim, as metodologias ágeis foram destacadas como a base de organização e planejamento do desenvolvimento, alinhando-se aos objetivos de otimização, eficiência e transparência propostos por este trabalho. 

# Capítulo 3

# Trabalhos Relacionados

Este capítulo apresenta trabalhos e sistemas existentes com objetivos semelhantes ao do sistema Prisma, destacando suas abordagens, limitações e contribuições. A análise desses sistemas permite compreender as estratégias tecnológicas nas quais o Prisma se insere, identificando lacunas que justificam sua proposta de desenvolvimento. 

# 3.1 Sistemas de Gestão e Ferramentas Integradas

Existem diversas soluções no mercado, amplamente utilizadas no gerenciamento de processos e atividades organizacionais. Destacam-se sistemas como o Trello e o ClickUp, plataformas em nuvem que permitem organizar tarefas e acompanhar o progresso das atividades, colaborando com a equipe em tempo real (ATLASSIAN, 2025; TECH-NOLOGIES, 2023). Embora essas ferramentas sejam robustas, apresentam limitações na personalização dos fluxos internos, dificultando a adaptação às necessidades específicas de empresas juniores, como a gestão de processos seletivos e controle de metas e riscos nos projetos. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/cbc79273ad620addbf4a0885b69be205727813b879230a9ced87c86dd3c56625.jpg)



Figura 3.1 – Interface principal do Trello, com estrutura baseada em quadros e cartões.



Adaptado de Atlassian (2025). Disponível em:


<https://trello.com/home?wvideo $\ulcorner$ uy8s1pjm2i#video>. Acesso em: 9 out. 2025. 

Observa-se que o Trello adota uma abordagem visual simples e intuitiva, centrada na gestão de tarefas individuais e colaborativas. Embora eficiente para controle operacional, sua limitação está na ausência de módulos integrados voltados para metas, processos ou indicadores institucionais, essenciais para o contexto de empresas juniores. 

Já sistemas como o Notion e o Monday.com também centralizam a gestão de informa-ções. Contudo, a maioria dessas plataformas adota modelos pagos, o que representa um fator limitante para empresas juniores com recursos reduzidos. Outro fator limitante é a adaptatividade aos usuários, devido à natureza abrangente dessas plataformas com diversas funcionalidades para atender o público geral, causando um maior esforço para adequar esses ambientes às necessidades das empresas juniores. Nesse contexto, o Prisma surge como uma solução alternativa, customizada para empresas juniores e desenvolvida com tecnologias modernas, oferecendo melhor custo-benefício. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/317b51e1e719418b266730319db0edcc63c9a6b1e505a147ebef0b363ed7778b.jpg)



Figura 3.2 – Interface principal do Notion, utilizada para organização e documentação colaborativa.


Adaptado de Notion Labs (2025). Disponível em: <https://www.notion.com/pt/help/guides/the-ultimate-guide-to-notion-templates>. Acesso em: 9 out. 2025. 

# 3.2 Trabalhos Acadêmicos e Sistemas Open Source

No âmbito acadêmico, diversos trabalhos apresentaram soluções voltadas à automatização e integração de processos organizacionais, como SILVA M. R.; PEREIRA (2021), que desenvolveu um sistema web de gestão de projetos acadêmicos utilizando o framework Django, com foco na comunicação entre equipes e no acompanhamento de metas. 

SOUZA T. A.; CARVALHO (2020) apresentaram uma aplicação construída com Spring 

Boot e Angular para o gerenciamento de fluxos administrativos em universidades, destacando a importância da modularidade e da escalabilidade no design da aplicação. 

Projetos de código aberto, como o OpenProject e o Redmine, também oferecem funcionalidades semelhantes, permitindo a gestão colaborativa de tarefas e indicadores de desempenho (GMBH, 2024; COMMUNITY, 2024). Entretanto, tais soluções apresentam uma curva de aprendizado elevada e demandam recursos de infraestrutura mais complexos, o que pode inviabilizar sua adoção por organizações menores. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/8d177056efb6475740dbcdbfb2fe924d3c6dd32b38abd88ffb856796453aa56e.jpg)



Figura 3.3 – Interface do OpenProject, sistema open source para gestão colaborativa de projetos. Adaptado de OpenProject Foundation (2025). Disponível em: <https: //www.openproject.org/docs/release-notes/9/9-0-0/improved-design-9a94857a.png>. Acesso em: 9 out. 2025.


# 3.3 Contribuições e Diferenciais do Prisma

Em comparação com as soluções apresentadas, o sistema Prisma, que será apresentado no Capítulo 4, é voltado especificamente para empresas juniores, unificando em uma única plataforma funcionalidades de gestão de metas, atividades, processos seletivos, projetos e usuários. Utilizando as tecnologias Spring Boot, React, TypeScript e TailwindCSS, garante um ambiente moderno e seguro, promovendo a transparência e a eficiência organizacional. 

O Prisma também oferece integração com o sistema da Confederação Brasileira de Empresas Juniores (Brasil Júnior), disponível em: <https://portal.brasiljunior.org.br/>, permitindo que a empresa júnior utilize os dados de faturamento cadastrados no sistema para atualização automática no Prisma. 

Com uma interface intuitiva e de fácil navegação, o Prisma reduz a complexidade de uso, tornando-o prático para gestores, membros e colaboradores de diferentes níveis técnicos. Além disso, por adotar uma arquitetura modular e escalável, a expansão para novos módulos e integrações futuras torna-se mais acessível. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/83e6ed7816963c82b6e2898f309e05803cda6eed4ae9138e15a106e02421ce9a.jpg)



Figura 3.4 – Interface do sistema Prisma, integrando múltiplos módulos de gestão em uma única plataforma.


Elaborado pelo autor (2025). 

# 3.3.1 Comparativo entre Prisma, Trello e Notion

A Tabela 3.1 apresenta uma análise comparativa entre o Prisma e duas ferramentas amplamente utilizadas no mercado — Trello e Notion — destacando funcionalidades relacionadas à gestão organizacional e ao contexto de empresas juniores. 


Tabela 3.1 – Comparativo entre Prisma, Trello e Notion


<table><tr><td>Funcionalidade / Módulo</td><td>Prisma</td><td>Trello</td><td>Notion</td></tr><tr><td>Gestão de Processo Se-letivo (multiplas etapas,notas, candidatos)</td><td>Sim —[módulocompletto e automatizzato</td><td>Não (exige adaptaçao por quadros e cartões)</td><td>Parcial (possívelvia templates, semlingica nativa)</td></tr><tr><td>Envio automático de e-mails para candidatos do PS</td><td>Sim —integradoao[módulo de PS</td><td>Não</td><td>Não</td></tr><tr><td>Gestão de Projetos (metas, riscos, membros,directorship)</td><td>Sim —[módulointegrado e especializados</td><td>Parcial (organizaçao via quadros,sem metas e riscos nativos)</td><td>Parcial (possívelvia bancos dedados, mas semlingica aplicada)</td></tr><tr><td>Dashboard interativocom visão geral dos projetos</td><td>Sim</td><td>Limitado (somentePower-Upsguided or plugins)</td><td>Parcial (requer criacão manual de visualizações)</td></tr><tr><td>Gestão de Metas do PortalBJ (integração externa)</td><td>Sim —integrazionenativeacom dadosda Brasil Júnior</td><td>Não</td><td>Não</td></tr></table>

Continua na próxima página 

<table><tr><td>Funcionalidade / Módulo</td><td>Prisma</td><td>Trello</td><td>Notion</td></tr><tr><td>Gestão de Itens (estoque / inventorário)</td><td>Sim —[móduloproprio]</td><td>Não</td><td>Parcial (possível via tabelas criadasmanualmente)</td></tr><tr><td>Gestão de Usuários com permissões poredly</td><td>Sim — controle de acesso granular</td><td>Parcial (perfis基本情况; restricções apenas em planos半导res)</td><td>Parcial (控制器 avançado somente em planos半导res)</td></tr><tr><td>Board de Atividades (kanban)</td><td>Sim — integrado aos processos internos</td><td>Sim — funcionalidade principal</td><td>Sim — via templatese bancos de da-dos</td></tr><tr><td>Customização para em-presas juniores</td><td>Alta —desenvolvimento especialamente para EJs</td><td>Baixa —solution genérica</td><td>Baixa —solution genérica</td></tr><tr><td>Custo</td><td>Baixo custo —adaptavelporedlyoferecido</td><td>Freemium (recur-los avançados são半导res)</td><td>Freemium (recur-los avançados são半导res)</td></tr><tr><td>Curva de aprendizado para EJs</td><td>Baixa —[móculos orientados aos processos共振idas EJs</td><td>Baixa</td><td>Média (alto nivende flexibilitadede exigecfgenera-çao)</td></tr><tr><td>Rastreabilidade e histori-rico de operações</td><td>Sim — registros completenessporedly</td><td>Parcial (logs limitados; plugins ne-cessários)</td><td>Parcial (configura-vel manualmente)</td></tr><tr><td>Padronização de proces-sos internos</td><td>Alta — PS, proje-tos, metas, ativi-dades</td><td>Baixa</td><td>Média (dependedoriskyarioncriar os fluxos)</td></tr></table>

Observa-se que, embora Trello e Notion sejam ferramentas consolidadas para organização geral, ambas carecem de módulos específicos para empresas juniores. O Prisma diferencia-se ao oferecer integração nativa com o Portal Brasil Júnior, gestão completa de processos seletivos, módulos dedicados a metas, projetos e estoque, além de uma arquitetura desenhada especificamente para o fluxo operacional das EJs. 

Dessa forma, o Prisma posiciona-se como uma solução intermediária entre ferramentas de alto custo disponíveis no mercado e sistemas open source de difícil manutenção, oferecendo uma alternativa acessível e adaptada à realidade das empresas juniores. 

# Capítulo 4

# Prisma

O desenvolvimento de sistemas de informação requer uma análise detalhada das necessidades dos usuários e do contexto em que a aplicação será inserida. Essa etapa é essencial para identificar os principais desafios, definir o escopo do projeto e propor solu-ções que atendam de forma eficiente aos objetivos pretendidos. 

No contexto do sistema Prisma, que tem por finalidade otimizar a gestão de atividades, metas e processos organizacionais, o principal problema está na ausência de um ambiente unificado que possibilite o acompanhamento eficiente das informações e a integração entre os diferentes módulos funcionais. 

A carência de ferramentas que permitam uma visão sólida do desempenho, assim como a falta de padronização nos processos, dificultam a comunicação entre as equipes e comprometem a tomada de decisões. Para promover a transparência dos dados e melhorar a experiência de uso para diferentes perfis de usuários do sistema, o desenvolvimento de uma solução tecnológica que automatize processos e centralize informações estratégicas torna-se essencial. 

A partir dessa definição do problema, foi elaborada a modelagem conceitual do sistema, contemplando as principais interações entre usuários e sistema, bem como a estrutura geral das entidades que compõem o domínio. Essa modelagem servirá de base para o planejamento da implementação, abordada no capítulo seguinte. 

# 4.1 Objetivos da Solução Proposta

O sistema Prisma foi concebido com o propósito de integrar diferentes áreas de gestão das empresas juniores, permitindo centralizar informações e automatizar rotinas administrativas. 

Entre seus objetivos principais, destacam-se: 

• Integração: Unificar módulos de atividades, metas, projetos e processos seletivos e estoque em uma única plataforma; 

• Automatização: Reduzir o retrabalho e a dependência de planilhas, otimizando fluxos internos; 

• Transparência: Facilitar o acompanhamento de dados e resultados por parte dos gestores e membros; 

• Escalabilidade: Permitir a expansão modular e futura integração com outras plataformas; 

• Usabilidade: Oferecer uma interface intuitiva e acessível a usuários com diferentes níveis de experiência técnica. 

Esses objetivos orientam a concepção da arquitetura do sistema e norteiam o desenvolvimento das funcionalidades apresentadas nas próximas seções. 

# 4.2 Metodologia de Desenvolvimento

O desenvolvimento do Prisma adotou uma abordagem com metodologias ágeis, combinando práticas do Scrum e do Kanban de forma adaptada à realidade do projeto, conduzido por um único desenvolvedor. Esse modelo híbrido permitiu organizar o fluxo de trabalho de maneira incremental, priorizando entregas contínuas e validação frequente com os usuários-alvo. 

Do Scrum, foram incorporados elementos como o planejamento iterativo, a definição de metas de curto prazo e a priorização de funcionalidades com base no valor percebido pelos usuários. Selecionavam-se módulos específicos, como Processo Seletivo ou Projetos, estabelecendo escopos reduzidos para implementação. 

Do Kanban, adotou-se o gerenciamento visual das tarefas e o controle do work in progress, permitindo acompanhar o fluxo das atividades desde a análise até a implementação e validação. Esse fluxo contínuo mostrou-se adequado ao desenvolvimento individual, reduzindo a necessidade de reuniões recorrentes. 

Essa combinação proporcionou um processo ágil para definir requisitos e incrementos funcionais, permitindo validar rapidamente as entregas com gestores e membros que utilizarão o sistema. Assim, a metodologia utilizada serviu de suporte direto ao levantamento e refinamento dos requisitos apresentados na subseção seguinte. 

# 4.3 Levantamento de Requisitos

O levantamento de requisitos teve como objetivo compreender as necessidades específicas do público-alvo — gestores e membros de empresas juniores — e traduzi-las em funcionalidades observáveis no sistema. 

Os requisitos foram classificados em duas categorias: funcionais e não funcionais. 

# 4.3.1 Escopo e Perfis de Usuário

O Prisma conta com três perfis: o Administrador que pode gerenciar usuários, metas, processos seletivos, projetos, atividades e inventário, representando todo o escopo de módulos do sistema e que, na realidade de uma empresa júnior, corresponderiam aos diretores da empresa; o Usuário comum, que seriam os gerentes designados, podendo gerenciar atividades, processos seletivos e projetos. 

Por fim, tem-se o último perfil de Candidato, que apenas pode participar do processo seletivo, cadastrado diretamente pelos perfis anteriores. 

Escopo funcional. O Prisma abrange: (i) usuários, autenticação e autorização (RF01- RF02), (ii) Processo Seletivo (RF03), (iii) Projetos, metas, riscos e membros (RF04), (iv) indicadores e dashboards (RF05), e (v) itens/board (RF06-RF07). 

# 4.3.2 Regras de Negócio

• RN-PS-01 (Etapas do PS): um Processo Seletivo é composto por etapas ordenadas; notas são sempre vinculadas a (candidato, etapa). Uma etapa só pode ser concluída se todas as notas obrigatórias forem lançadas (RF03). 

• RN-PS-02 (Avisos do PS): avisos/notícias devem registrar o público-alvo, que são os candidatos que ainda concorrem ao Processo Seletivo. 

• RN-PROJ-01 (Status de Projeto): os estados válidos são Não iniciado, Planejado, Em andamento, Em atenção/risco, Atrasado, Pausado, Concluído e Cancelado. Onde os gestores devem atualizar manualmente a situação do projeto para um maior controle. 

• RN-PROJ-02 (Metas): cada projeto tem metas com prazo e percentual de conclusão. 

• RN-PROJ-03 (Riscos): riscos possuem severidade, probabilidade, prazo e plano de mitigação, além de impactos. 

• RN-SEG-01 (Permissões): acesso a dados e ações é concedido por papel e módulo; toda ação sensível requer usuário autenticado e escopo válido (RF01, RF02). 

# 4.3.3 Requisitos Funcionais

Os requisitos funcionais descrevem o comportamento observável do sistema e estão alinhados aos módulos apresentados na Seção 4.3.1. A seguir, apresentam-se os RF de forma itemizada, à semelhança das regras de negócio: 

• RF01 — Autenticação JWT: o sistema deve autenticar usuários via login e senha, emitindo access token JWT com uma hora de duração, a ser enviado no cabeçalho das requisições protegidas. 

• RF02 — Usuários e Permissões: o sistema deve permitir CRUD de usuários (internos e externos) e atribuição de papéis por módulo. 

– criação/edição sem restrições para perfis administradores; 

– alteração de papel refletida instantaneamente nas rotas protegidas; 

– perfis não podem autoatribuir privilégios acima do próprio nível. 

• RF03 — Processo Seletivo: o sistema deve permitir CRUD de candidatos, etapas e notas; emissão de avisos e visão consolidada por candidato/etapa. 

– candidatos devem possuir notas em todas as etapas; 

– deve-se impedir duplicidade de nota para o mesmo par (candidato, etapa); 

– os avisos devem manter histórico com pré-visualização. 

• RF04 — Projetos, Metas, Riscos e Membros: o sistema deve permitir CRUD de projetos; definição de metas com prazos; cadastro e priorização de riscos; associa-ção de membros e funções. 

– o dashboard deve exibir a situação dos projetos, metas e riscos; 

– o projeto deve possuir, no mínimo, título, descrição, prazo, status e categoria. 

• RF05 — Indicadores e Dashboard: o sistema deve exibir indicadores consolidados com dados gerais da empresa. 

– carregamento gráfico de dados de faturamento e colaboração; 

– persistência dos dados deve considerar a empresa do usuário. 

• RF06 — Board (Kanban): o sistema deve permitir CRUD de colunas e cartões, com movimentação drag-and-drop. 

– campos mínimos do cartão: título, descrição, responsável, data-limite e status; 

– deve haver permissão de movimentar e ordenar colunas; 

– deve haver permissão de criar, movimentar e ordenar cartões em qualquer coluna. 

• RF07 — Itens / Inventário: o sistema deve permitir CRUD de itens da empresa. 

– campos mínimos: título, descrição e quantidade; 

– a quantidade deve ser positiva e o usuário deve ser opcional; 

# 4.3.4 Requisitos Não Funcionais

Os requisitos não funcionais definem os critérios de qualidade e restrições arquiteturais que garantem desempenho, segurança e manutenibilidade do Prisma: 

• RNF01 — Desempenho: operações comuns (login, lista de candidatos, lista de projetos) devem responder em até 3 s; o dashboard inicial deve carregar em até 10 s, considerando conexão estável. Páginas com mais de 10 itens devem ser paginadas. 

• RNF02 — Arquitetura e Escalabilidade: a solução deve adotar componentiza-ção por camadas (Controller–Service–Repository) e módulos independentes, permitindo a adição de novos módulos sem breaking changes nas APIs existentes; deve haver suporte futuro a múltiplas EJs via tenant id lógico. 

• RNF03 — Manutenibilidade e Qualidade: o código deve seguir boas práticas (Clean Code), padronização de arquitetura em camadas e padronização das respostas REST (incluindo traceId e mensagens claras). 

• RNF04 — Usabilidade e Acessibilidade: a interface deve ser responsiva e intuitiva, garantindo boa experiência de uso em diferentes dispositivos. 

• RNF05 — Segurança: o sistema deve operar sob HTTPS; senhas devem ser armazenadas com hash (BCrypt); o JWT deve possuir expiração; a autorização deve ser por escopos e papéis; deve haver rate limit em endpoints de autenticação. 

• RNF06 — Interoperabilidade e Documentação: as APIs RESTful devem ser documentadas via OpenAPI/Swagger, com versionamento de endpoints, CORS configurável e consumo desacoplado pelo frontend. 

# 4.4 Relação com a Especificação Técnica do Capítulo 5

As definições de requisitos apresentadas neste capítulo (funcionais, não funcionais, regras de negócio e escopo de usuários) servem como base conceitual para a formalização técnica mostrada no Cap. 5. No Capítulo 5, as Tabelas 5.1, 5.2 e 5.3 retomam estes mesmos requisitos e os organizam em um formato mais operacional, indicando módulo principal, prioridade e respectivos artefatos de implementação. 

Dessa forma, o que aqui foi descrito em termos de o que o sistema deve fazer (Se-ções 4.3.3 e 4.3.4) aparece no Cap. 5 em forma de tabelas de referência rápida. As regras de negócio listadas na Seção 4.3.2 são refletidas na matriz de rastreabilidade (Tabela 5.3), que vincula cada requisito aos pacotes e serviços implementados. A classificação por perfis de usuário (Seção 4.3.1) é mantida no Capítulo 5 ao associar cada requisito ao seu módulo correspondente. 

Assim, o Capítulo 4 estabelece a visão conceitual e de problema desses requisitos do Prisma, enquanto o Capítulo 5 apresenta essas mesmas necessidades em uma estrutura técnico-descritiva, adequada para implementação e validação junto aos usuários-alvo. 

# 4.5 Modelagem de Casos de Uso

Para representar as funcionalidades principais do sistema Prisma e as interações entre os usuários e a aplicação, elaborou-se um diagrama de casos de uso utilizando a linguagem UML. Esse diagrama fornece uma visão de alto nível das ações disponíveis e dos papéis que interagem com o sistema, servindo como referência para o levantamento de requisitos e a definição das fronteiras do projeto. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/3dd10a83d2d48a8660a9e484028fe9e8434fc2b6987417df93ff28592d40f858.jpg)



Figura 4.1 – Diagrama de casos de uso do sistema Prisma Elaborado pelo autor (2025).


O diagrama apresentado permite compreender como os diferentes atores interagem 

com o sistema, destacando os módulos principais e suas relações. Essa visão contribui para a identificação das funcionalidades essenciais e para a definição das prioridades de desenvolvimento. 

# 4.6 Arquitetura do Sistema com C4 Model

Com o objetivo de apresentar de forma hierárquica a estrutura de software do sistema Prisma, foi utilizado o C4 Model, proposto por Simon Brown. Esse modelo fornece quatro níveis de abstração — Contexto, Contêineres, Componentes e Deployment — que permitem compreender desde a visão geral até a decomposição técnica da aplicação. 

# 4.6.1 Diagrama de Contexto

O primeiro nível do modelo (C1) apresenta a visão geral do sistema e suas interações externas. A Figura 4.2 mostra como o usuário acessa o sistema via navegador e como o Prisma se comunica com seus serviços internos e externos. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/3bcb291234f69e6d4fd34ff7d3a44802157d5e77ae0c5983322ca3de1ee15158.jpg)



Figura 4.2 – Diagrama de contexto (C1) do sistema Prisma Elaborado pelo autor (2025).


# 4.6.2 Diagrama de Contêineres

O segundo nível (C2) detalha a composição tecnológica do sistema, descrevendo os principais contêineres e suas interações. A Figura 4.3 demonstra como o frontend, backend e banco de dados estão organizados, bem como as comunicações assíncronas via eventos e serviços externos. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/946ca30c1090773e23da479b593afc1cfe3ce587d8431c4f320b4abe040a24e7.jpg)



Figura 4.3 – Diagrama de contêineres (C2) do sistema Prisma Elaborado pelo autor (2025).


# 4.6.3 Diagrama de Componentes

O terceiro nível (C3) mostra a decomposição interna do backend, destacando os componentes principais do Spring Boot, como controladores, serviços, repositórios e utilitá- rios de autenticação. A Figura 4.4 ilustra a interação entre as classes responsáveis pelo processo de autenticação JWT no sistema. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/6f4ae6bcef1811e4a6abd3a2ac910100db017de6672bdc425e19c59a48808755.jpg)



Figura 4.4 – Diagrama de componentes (C3) do sistema Prisma Elaborado pelo autor (2025).


# 4.6.4 Diagrama de Deployment

O quarto nível (C4) representa a infraestrutura de implantação do sistema. A Figura 4.5 apresenta o ambiente distribuído de execução, com o frontend hospedado em nuvem, o backend em contêineres Docker e a comunicação com o banco de dados e serviço de e-mail. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/5c5e41d03b308c7bff15cb2a31a1529d850d3a83f20fb0f0718bbc1a3e56b7e7.jpg)



Figura 4.5 – Diagrama de deployment (C4) do sistema Prisma Elaborado pelo autor (2025).


# 4.7 Modelagem de Classes

Após a definição dos casos de uso e da arquitetura geral, elaborou-se a modelagem de classes do sistema, representando de forma abstrata as entidades, atributos e relacionamentos que compõem a estrutura interna do Prisma. Essa modelagem visa evidenciar a organização conceitual do sistema e o modo como os dados são estruturados e manipulados. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/0e574ca10cbdff5e5a9502f3be581d3ea0cc1c05d264176a29b696c22495f5fe.jpg)



Figura 4.6 – Diagrama geral de classes do sistema Prisma Elaborado pelo autor (2025).


O diagrama de classes contempla as principais entidades do sistema, como User, Activities, GoalsBJ, Company, SelectiveProcess, BoardColumn e Projetos. Cada uma delas representa um módulo funcional que será detalhado posteriormente no Capítulo 5. 

No centro do modelo, encontra-se a entidade User, responsável pela autenticação e associação aos dados pessoais representados por Person. No módulo de Atividades e Kanban, tem-se as classes BoardColumn e Cards compõem a estrutura do quadro, permitindo que cada coluna agregue múltiplos cartões, atribuídos a usuários. A classe 

Activities registra itens quantitativos associados a um usuário, permitindo um controle de estoque para o Prisma. 

O módulo de Projetos é formado pela classe Projects, que centraliza informações sobre status, cronograma e categoria. Cada projeto agrega metas (ProjectGoals), riscos (ProjectRiskItem) e membros (ProjectMembers), permitindo vincular responsabilidades e porcentagens de alocação de maneira estruturada. 

Na área de Processo Seletivo, a entidade SelectiveProcess agrupa os estágios de (StageSelectiveProcess), avisos (NoticeSelectiveProcess) e candidatos (Candidates). As notas lançadas em cada etapa são representadas por NoteStageSelectiveProcess, garantindo rastreabilidade por candidato e estágio. 

Por fim, o módulo de Empresa e Metas BJ reúne Company, GoalsBJ e Monthly-GoalBJ, permitindo o armazenamento de indicadores oficiais da Brasil Júnior associados à empresa, como metas anuais e faturamento mensal. 

Em conjunto, cada classe herda atributos de auditoria e deleção lógica de AbstractEntity, padrão compartilhado por todas as entidades persistentes do sistema. No diagrama evidencia-se a organização modular do Prisma e os relacionamentos entre suas principais entidades, servindo como base conceitual para a implementação detalhada apresentada no capítulo seguinte. 

Essa visão global da arquitetura fornece o alicerce para a construção das camadas ló- gicas e estruturais do software, permitindo que a implementação ocorra de forma coerente e modular. 

# 4.8 Síntese do Capítulo

Neste capítulo, foram apresentadas a contextualização do problema, as necessidades identificadas e a modelagem conceitual do sistema Prisma, composta pelos diagramas de casos de uso, arquitetura e classes. 

A inclusão dos diagramas do modelo C4 possibilitou compreender o sistema sob diferentes níveis de abstração — desde o contexto geral até a estrutura de componentes — complementando a visão estrutural oferecida pela modelagem UML. 

Esses elementos fornecem uma visão abrangente da proposta do sistema, preparando o terreno para o próximo capítulo, que aborda as decisões técnicas, a arquitetura de software e os diagramas específicos que detalham a implementação de cada módulo. 

# Capítulo 5

# Implementação

Este capítulo descreve as decisões de implementação do Prisma, relacionando a arquitetura apresentada no Cap. 4 com o desenvolvimento concreto do sistema. O foco aqui é: (i) consolidar os requisitos implementados, (ii) explicar as decisões de arquitetura e tecnológicas que materializam esses requisitos, e (iii) detalhar os principais módulos através de diagramas de classes específicos. 

# 5.1 Visão Geral de Implementação

A implementação segue a arquitetura em camadas vista no modelo C4: frontend (React $^ +$ TypeScript $^ +$ Tailwind), backend (Spring Boot, REST/JWT), banco de dados (PostgreSQL) e integrações assíncronas (eventos e envio de e-mails). O backend adota o padrão controller–service–repository, com mapeadores $\mathrm { ( D T O  }$ entidade) e componentes utilitários (p. ex., JWT), refletindo a organização de pacotes do projeto (controllers, service, repository, mappers, config, events). 

# 5.2 Desafios Técnicos

O principal desafio técnico do desenvolvimento do Prisma foi a necessidade de atuar simultaneamente em múltiplas frentes: elicitação de requisitos com os usuários, modelagem de domínio, implementação frontend e backend, configuração de segurança, integra-ção com serviços externos e implantação. 

Embora não houvesse limitações relacionadas ao domínio das tecnologias empregadas, o desenvolvimento dessas etapas por um único desenvolvedor exigiu organização rigorosa do fluxo de trabalho e priorização contínua, especialmente devido ao volume de atividades distribuídas entre diferentes áreas do sistema. Essa dinâmica reforçou a ado-ção de incrementos pequenos, validações frequentes e práticas ágeis, conforme descrito na metodologia. 

# 5.3 Requisitos do Sistema

O levantamento dos requisitos foi a etapa inicial do desenvolvimento do sistema Prisma. A partir de reuniões com os usuários-alvo — gestores e membros de empresas juniores —, foram identificadas as principais necessidades funcionais e restrições de qualidade do sistema. Também foi levada em conta a experiência pessoal como membro de empresa júnior. 

Na sequência, foi feita a modelagem de requisitos e uma análise dos módulos que compõem o sistema Prisma, então definiram-se as prioridades de implementação de modo a orientar o desenho da arquitetura e as decisões de implementação apresentadas neste capítulo. 

O processo seguiu três etapas principais: 

1. Elicitação e consolidação: identificação dos requisitos funcionais (RF) e não funcionais (RNF) a partir das necessidades do negócio. 

2. Priorização: definição dos módulos de requisitos com maior potencial de serem colocados em validação para os usuários-alvo, servindo de base ao planejamento das entregas. 

3. Desenvolvimento: criação dos módulos essenciais, como o de usuários e a segurança do sistema, em sequência iniciando os módulos definidos como prioritários no item anterior. 

As Tabelas 5.1, 5.2 e 5.3 apresentam o conjunto consolidado de requisitos, suas categorias e os respectivos elementos de implementação. Na Tabela 5.1, os requisitos definidos com maior prioridade são os elencados com maior potencial de utilizá-los em validação com os usuários, levando em consideração as necessidades das empresas juniores. 

# 5.3.1 Requisitos Funcionais (RF)

Os requisitos funcionais descrevem as funcionalidades observáveis pelo usuário e o comportamento esperado do sistema. 


Tabela 5.1 – Requisitos Funcionais (RF)


<table><tr><td>ID</td><td>Descrição</td><td>Módulo principal</td><td>Prioridade</td></tr><tr><td>RF01</td><td>Autentização baseada em token JWT; renovação automatística do token quando necessário.</td><td>Autentização / Segança</td><td>Alta</td></tr><tr><td>RF02</td><td>Gerenciamento de sistemas: cadastro in-terno/externo, papelis (admin, usoí) e PERMISSIONes por padrão.</td><td>Usuários e Permissões</td><td>Alta</td></tr></table>

Continua na próxima página 

<table><tr><td>ID</td><td>Descrição</td><td>Módulo principal</td><td>Prioridade</td></tr><tr><td>RF03</td><td>Processo seletivo (trainee): CRUD de candidatas, notas e noticias; acompanhamento por eta-pas.</td><td>Processo Seletivo</td><td>Alta</td></tr><tr><td>RF04</td><td>Projetos: CRUD; cadastro de metas, riscos e membros; dashboard de projetos.</td><td>Projetos</td><td>Média</td></tr><tr><td>RF05</td><td>Dashboard geral com指示ores e graficos (metas do Portal BJ, faturamento,的合作ação etc.).</td><td>Indicadores / Metas BJ</td><td>Baixa</td></tr><tr><td>RF06</td><td>Sistema de atividades: CRUD e movimentação entre colunas (kanban); Campos: título, descrição, responsavel, data-limite, status; colunas personalizadas (A Fazer, Fazendo, Concluído).</td><td>Atividades / Board</td><td>Baixa</td></tr><tr><td>RF07</td><td>Sistema de inventário: CRUD de itens; Campos: título, descrição, quantidade e usoário</td><td>Itens / Inventário</td><td>Baixa</td></tr></table>

# 5.3.2 Requisitos Não Funcionais (RNF)

Os requisitos não funcionais definem critérios de qualidade, desempenho e restrições arquiteturais que asseguram a robustez e a manutenibilidade do sistema. 


Tabela 5.2 – Requisitos Não Funcionais (RNF)


<table><tr><td>ID</td><td>Descrição</td><td>Categoria</td></tr><tr><td>RNF01</td><td>Desempenho: respostas comuns em até 3 s; dashboard em até 10 s.</td><td>Desempenho</td></tr><tr><td>RNF02</td><td>Escalabilité: expansão para novos@módulos sem refatorações estruturais.</td><td>Arquitetura</td></tr><tr><td>RNF03</td><td>Manutenibilidade: boas praticas (Clean Code); backend modular (camadas Controller-Service-Repository / Spring MVC para REST).</td><td>Qualidade</td></tr><tr><td>RNF04</td><td>Usabilidade: UI responsiva e acessível; feedback visual nas ações.</td><td>UX/UI</td></tr><tr><td>RNF05</td><td>Segança: HTTPS, senhas com hash (BCrypt), controle de;aço por permissões (JWT).</td><td>Segança</td></tr><tr><td>RNF06</td><td>Interoperatividade: endpoints RESTful documentados (Swagger/OpenAPI);consumo desacoplado pelo frontend.</td><td>Integrazione</td></tr></table>

# 5.3.3 Rastreabilidade (RF → Módulos/Artefatos)

A rastreabilidade tem como objetivo manter o vínculo entre os requisitos especificados e os componentes efetivamente implementados. A Tabela 5.3 apresenta um resumo relacionando cada RF aos pacotes e principais artefatos do projeto. 


Tabela 5.3 – Matriz de Rastreabilidade (resumo RF artefatos)


<table><tr><td>RF</td><td>Pacotes</td><td>Principais artefatos</td></tr><tr><td>RF01</td><td>config; service</td><td>JwtAuthFilter, JwtTokenService, SecurityConfig, AuthenticationService</td></tr><tr><td>RF02</td><td>controllers; service; repository; mappers</td><td>UserController, UserService, UserRepository, User-Mapper</td></tr><tr><td>RF03</td><td>controllers; service; repository; mappers; events</td><td>SelectiveProcessController/Service/Repository, enti-dades Note/Stage/Notice; eventos de notificationsão</td></tr><tr><td>RF04</td><td>controllers; service; repository</td><td>ProjectsController/Service/Repository, ProjectGoals-Repository, ProjectMembersRepository, ProjectRiskI-temRepository</td></tr><tr><td>RF05</td><td>controllers; service</td><td>DashboardController/Service; integração com metas BJ</td></tr><tr><td>RF06</td><td>controllers; service; repository; mappers</td><td>ActivitiesController/Service/Repository, BoardColumnController/Service/Repository, CardsRepository</td></tr></table>

# 5.4 Padrões de Navegação e Comportamento do Sistema

Antes de detalhar cada módulo, é importante registrar três convenções adotadas na implementação do Prisma: navegação padronizada por sidebar, remoções lógicas (soft delete) e listagens paginadas. Essas diretrizes uniformizam a experiência de uso e simplificam a manutenção. 

# 5.5 Detalhamento do Sistema e Módulos Implementados

Esta seção descreve os módulos implementados no Prisma, destacando suas funcionalidades principais, objetivos e relação com os requisitos apresentados na Seção 5.3. Cada módulo é acompanhado por capturas de tela da interface e uma breve explicação de seu comportamento, evidenciando como as decisões arquiteturais e tecnológicas foram aplicadas na prática. 

# 5.5.1 Navegação por sidebar com ações consistentes

A navegação principal é realizada por uma sidebar fixa à esquerda, onde cada item agrupa as ações mais frequentes do respectivo módulo. Como regra, as entradas apresentam os subitens Cadastrar e Listar. Há duas exceções: (i) em Projetos há ainda o subitem Dashboard; (ii) o Board é um atalho para o quadro de itens e, por isso, não possui subitens. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/e8ca205c12db50461c02c0ee5361d10c8cf9146bbdedb806d7c2d1cff0f4578b.jpg)



Figura 5.1 – Padrão de navegação na sidebar: subitens Cadastrar/Listar (e Dashboard em Projetos).



Elaborado pelo autor (2025).


# 5.5.2 Soft delete e entidade abstrata de auditoria

Todas as remoções no sistema são lógicas (soft delete): o registro não é excluído fisicamente do banco; em vez disso, é marcado como inativo. Esse comportamento preserva 

a integridade referencial e mantém o histórico para rastreabilidade e auditoria. 

No backend, as entidades de domínio herdam de uma entidade abstrata chamada AbstractEntity que concentra campos de auditoria e status, como: id, createdAt, updatedAt e active, que permitem saber quando um registro foi criado, modificado e se está ativo. As consultas padrão filtram apenas registros com active $=$ true; operações de “excluir” apenas alternam esse campo para false. 

# 5.5.3 Listagens paginadas e desempenho

Todas as telas de listagem implementam paginação no servidor, exibindo botões de navegação (anterior/próximo) e mantendo a consistência de page size. Além de atender aos requisitos de desempenho (RNF01), a paginação reduz carga na rede e no banco de dados, e prepara o sistema para bases maiores. 

# 5.5.4 Módulo de Usuários e Autenticação

O módulo de Usuários materializa os requisitos RF01 (autenticação com JWT e renovação automática) e RF02 (cadastro interno/externo, papéis e permissões), além de RNF05 (segurança). Ele abrange login, registro externo, cadastro interno administrativo, listagem paginada e operações de edição/remoção (por soft delete). 

# 5.5.4.1 Acesso e autenticação (login)

A tela de acesso apresenta campos de e-mail corporativo e senha, opção “Lembrarme”, link “Esqueceu a senha?” e ações para entrar ou registrar-se. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/951555bc5a06df8b883387d542141b1334b2627817cb3f2c181aa32367669afa.jpg)



Figura 5.2 – Tela de login do Prisma.



Elaborado pelo autor (2025).


Fluxo técnico — O backend valida as credenciais e emite um JWT (Bearer) com expiração curta; próximo ao vencimento, há renovação automática para manter a sessão 

ativa (RF01). As requisições subsequentes enviam o token no cabeçalho Authorization, validado por filtros de segurança (Spring Security). 

# 5.5.4.2 Registro externo (autocadastro)

O registro externo permite criar conta com dados mínimos (nome, e-mail, CPF, celular e senha), acelerando a adoção sem depender do administrador. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/de3c6359b6c189855c034f0479032a4ec6b71d23ba4af1acef29190acd7f634c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/f61a200d081f8d9a5bf20b4e1510db61a120d12b4a90089b76acb74c37fdbc75.jpg)



Figura 5.3 – Registro externo com validações e consentimento. Elaborado pelo autor (2025).


Regras — Validações de formato (e-mail, CPF, celular) e força de senha; aceite de Termos de Uso/Privacidade; perfil inicial com permissões básicas, podendo ser elevado por administradores (RF02/RNF05). 

# 5.5.4.3 Cadastro interno (administradores)

Para uso administrativo, o sistema dispõe de Cadastro interno com nível de acesso e permissões por módulo, aplicando o princípio do menor privilégio. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/bdbbec4663e09bbff231db35e2999d9c622249fbabe9f54d9939d7a44deaf897.jpg)



Figura 5.4 – Cadastro interno: definição de papéis e permissões por módulo. Elaborado pelo autor (2025).


# 5.5.4.4 Listagem paginada e operações

A listagem de usuários é paginada e centraliza ações de editar e excluir (via soft delete). Alterações de papéis/permissões têm efeito imediato na autorização aplicada pelos filtros. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/f3e9dbcd1245b8207ac4967133818714589554f7534c460e69d39cbd7b3af778.jpg)



Figura 5.5 – Listagem administrativa de usuários (paginação e ações rápidas). Elaborado pelo autor (2025).


# 5.5.4.5 Arquitetura e rastreabilidade

O módulo se ancora em Controller–Service–Repository (Spring Boot), com DTOs $^ +$ Mappers e entidade abstrata de auditoria/status (AbstractEntity). Na segurança: Jw-

tAuthFilter, JwtTokenService, BCrypt para senhas e políticas de autorização por papéis/permissões (RF01, RF02, RNF05). No modelo C4 (C2–C3), o Frontend Web (React/TypeScript) consome a Backend API (REST), que persiste dados no PostgreSQL. 

# 5.5.5 Módulo: Processo Seletivo

Este módulo materializa o RF03 ao permitir a criação e o acompanhamento de processos seletivos (trainee) com suas etapas, candidatos, lançamentos de notas e publicação de notícias. Todas as operações seguem as diretrizes gerais do sistema: soft delete (entidades ficam inativas via atributo de status na AbstractEntity), listagens paginadas e controle de acesso por permissões de módulo. 

Visão geral e navegação — A entrada principal é a listagem de processos, de onde partem as ações: Cadastrar (novo candidato diretamente para o processo), Candidatos (gerir participantes), Notas (lançamento e consolidação) e Avisos (comunicações publicadas para o processo). 

# 5.5.5.1 Cadastro de processo

O cadastro define informações macro (título, intervalo de inscrições) e as etapas do processo, cada uma com nome, datas de início/fim e ordem. A UI permite adicionar, remover e reordenar etapas (setas $\uparrow / \downarrow )$ , garantindo a consistência do fluxo. Regras básicas: (i) datas obrigatórias respeitando a cronologia; (ii) ordem numérica única por processo; (iii) ao salvar, o estado inicial é ativo (soft delete apenas arquiva). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/17ec4c234c8794a27392e220bc9daa2192a9ebf4cc7f836993bfedd0835c0a32.jpg)



Figura 5.6 – Cadastro de processo seletivo com definição e ordenação de etapas. Elaborado pelo autor (2025).


# 5.5.5.2 Listagem de processos

A listagem apresenta título e datas principais, com ações rápidas por linha (Cadastrar, Candidatos, Notas, Avisos) e paginação no rodapé. Processos desativados via soft 

delete não aparecem por padrão (podem ser recuperados via banco de dados). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/2ff431ac118653dc4438e3105b81eeedde4335ac4add23cdc1b3eaa0a39483e3.jpg)



Figura 5.7 – Lista de processos seletivos com ações de atalho. Elaborado pelo autor (2025).


# 5.5.5.3 Cadastro de candidatos

Candidatos são vinculados a um processo. O formulário contempla CPF, nome/sobrenome, e-mail, celular e matrícula (opcional). Validações incluem formato de CPF e e-mail, além de unicidade por processo quando aplicável. Ao salvar, o candidato inicia com status ativo (soft delete apenas oculta da lista). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/9d952c3e59cf48aaf869ca6fb9390ed46003394f50bcebfd7458c3714628d308.jpg)



Figura 5.8 – Cadastro de candidato associado a um processo. Elaborado pelo autor (2025).


# 5.5.5.4 Listagem de candidatos

A visão lista os candidatos do processo com colunas de identificação (nome, CPF, e-mail, matrícula), paginação e ação de Editar. Regras de permissão garantem que a edição/remoção seja possível apenas a perfis autorizados no módulo de Processo Seletivo. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/7f4ce8bab36fabb82a5a94755609e4caa7061f269bfedbec97d3e52398814468.jpg)



Figura 5.9 – Candidatos de um processo seletivo (listagem paginada). Elaborado pelo autor (2025).


# 5.5.5.5 Lançamento de notas

A tela de notas organiza candidatos em linhas e etapas em colunas, permitindo o lançamento e o cálculo da média aritmética por candidato. Há uma legenda visual para facilitar triagem: $\geq 7 . 0$ (aprovado), 6,0–6,99 (atenção) $\mathrm { e } < 6 { , } 0$ (reprovado). A persistência pode ser feita individualmente, por meio das opções na linha de cada candidato, ou em lote, na parte superior (Salvar todas as notas). A paginação é mantida para grandes volumes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/22da7256f09690651f35fd2610ce560207ba24058693fe4dffa0cb9b47b787c6.jpg)



Figura 5.10 – Lançamento de notas por etapa e cálculo automático de médias. Elaborado pelo autor (2025).


# 5.5.5.6 Notícias do processo

Comunicações oficiais (ex.: resultados parciais, orientações) são publicadas pela área de notícias do processo. O editor suporta Markdown (negrito, itálico, listas, links), com pré-visualização antes da publicação. Ao cadastrar uma notícia, ocorre o envio auto-

mático de e-mail para todos os candidatos que ainda concorrem no processo seletivo. Notícias ficam versionadas e podem ser desativadas (soft delete) sem perda de histórico. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/4e27a4af10c4cdff59c3cb5216925cd2cd14db12cdcfd2afc5e84310e9698bc6.jpg)



Figura 5.11 – Publicação de notícias do processo seletivo com suporte a Markdown. Elaborado pelo autor (2025).


Resumo do desenho e rastreabilidade O SelectiveProcess agrega Stage (etapas) e Candidate; Note associa candidato $\times$ etapa e sustenta o cálculo de médias. A publica-ção de Notice é vinculada ao processo. O módulo implementa o RF03 e se relaciona às classes e serviços descritos nos diagramas (Seção 5.7) e à matriz de rastreabilidade (Tabela 5.3). 

# 5.5.6 Projetos

O módulo de Projetos consolida o planejamento e o acompanhamento das iniciativas da EJ, atendendo ao RF04 (CRUD de projetos, metas, riscos e membros, além de dashboard). A modelagem segue o padrão em camadas (Controller–Service–Repository), com persistência de soft delete nas entidades e paginação nas listagens. 

Objetivos e escopo. (i) Cadastrar e editar projetos com dados essenciais (título, descri-ção, status, categoria e prazos); (ii) Gerenciar metas do projeto e seus status; (iii) Alocar membros com permissões e funções, registrando entrada/saída e alocação; (iv) Mapear riscos (severidade, probabilidade e prazo); (v) Disponibilizar uma visão executiva com indicadores agregados (dashboard). 

Listagem — A Figura 5.12 mostra a lista de projetos, com colunas de título, status, categoria, datas de início/fim e ações rápidas: Detalhes, Editar e menu de opções. Os badges de status facilitam o acompanhamento do portfólio. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/34727f113091f9ec5866823305bf5750866593ca115c80a345535dcc4affe4fb.jpg)



Figura 5.12 – Listagem de projetos com badges de status, paginação e ações rápidas. Elaborado pelo autor (2025).


Cadastro em passos — O cadastro/edição é realizado em um wizard de quatro etapas (Figura 5.13): (1) dados gerais do projeto; (2) metas; (3) membros; (4) riscos. É possível Salvar ou Salvar e continuar entre etapas, mantendo a consistência dos dados. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/d1bc9db525f9d55689e4cdd9305f5c229b5e8f4fb1a940eeb7c0cd3f4ed2d175.jpg)



Figura 5.13 – Fluxo de cadastro em quatro passos: dados gerais, metas, membros e riscos. Elaborado pelo autor (2025).


Detalhes do projeto — A página de detalhes (Figura 5.14) centraliza o acompanhamento: resumo do projeto (status, categoria e prazos) e seções para Metas, Membros e Riscos, cada uma com suas ações (Nova meta, Novo membro, Novo risco). Essa visão facilita a governança do escopo e da equipe. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/d278b61afe5a53438abd08187bc3870de4cb5650ce0ac23cbd9f017d3a691fbb.jpg)



Figura 5.14 – Detalhes do projeto com seções de Metas, Membros e Riscos. Elaborado pelo autor (2025).


Dashboard de projetos — A opção Dashboard (Figura 5.15) apresenta gráficos agregados, como: distribuição de Projetos por Status, Metas por Status, Riscos por Severidade e Projetos por Categoria, além de uma busca de pessoas alocadas agora. Esses indicadores dão suporte à tomada de decisão e priorização do portfólio. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/e301923086f0a752d59091a8f1a120cb9bc4354343b3ebdf7032c0b4be3e9937.jpg)



Figura 5.15 – Dashboard do módulo de Projetos com indicadores e busca por alocações. Elaborado pelo autor (2025).


# 5.5.7 Indicadores e Metas BJ (Dashboard)

Este módulo consolida indicadores estratégicos a partir de uma integração read-only com o Portal BJ (RF05). A aplicação consulta os dados da empresa no Portal BJ, através de um identificador único existente na plataforma e renderiza um dashboard no frontend. 

Não há operações de escrita no sistema de origem; a sincronização é feita sob demanda quando o usuário acessa o módulo, com cache em memória de curto prazo para reduzir latência (RNF01) e manter a experiência responsiva. Em caso de indisponibilidade do serviço externo, o módulo apresenta o último dado válido e uma mensagem de sincronização pendente. 

O dashboard é organizado em três visões principais (abas no topo do gráfico) e três KPIs de apoio: 

• Faturamento x Meta (Figura 5.16): compara o faturado mensal com a meta esperada, permitindo avaliar rapidamente desvios ao longo do ano. 

• Faturamento colaborativo x Meta (Figura 5.17): destaca somente a parcela colaborativa do faturamento em relação à meta, útil para acompanhar iniciativas conjuntas entre setores/equipes. 

• Composição (Figura 5.18): mostra a decomposição mensal (colaborativo vs. não colaborativo) e suas linhas acumuladas (meta acumulada e faturado acumulado), facilitando a leitura de tendência. 

Abaixo dos gráficos, três indicadores em formato de anel resumem aspectos de pessoas e engajamento (obtidos do mesmo conjunto de dados): diversidade de membros, $\%$ de membros que executaram e $\%$ de membros colaboradores. Esses KPIs permitem relacionar resultados econômicos com dinâmica de equipe. 

Do ponto de vista de implementação, a camada de serviço DashboardService orquestra a integração e entrega ao frontend estruturas já processadas (séries mensais e totais acumulados), mantendo o consumo desacoplado (RNF06). O modelo de domínio associa Company aos objetos GoalsBJ/MonthlyGoalBJ, conforme o diagrama apresentado na Seção 5.7.4, garantindo extensibilidade para novas métricas. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/d476ea218d8c1eac69b703aaada8ef35086383970d4407804055a895fdcfbb4b.jpg)



Figura 5.16 – Receitas e Metas — visão Faturamento x Meta. Elaborado pelo autor (2025).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/3628d854e1c3b10be0eb82255941e1950b1f2e2f62c17f90b8c197643b69b787.jpg)



Figura 5.17 – Receitas e Metas — visão Faturamento colaborativo x Meta. Elaborado pelo autor (2025).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/8a8607036de1b35781f94bf44d1343295a85b0c65d44b8490f2bfeca3e5403cc.jpg)



Figura 5.18 – Receitas e Metas — visão Composição (mensal e acumulados). Elaborado pelo autor (2025).


# 5.5.8 Board (Quadro de Atividades)

O Board implementa um quadro kanban para organizar as atividades do time de um projeto, ou de demandas gerenciais da empresa, atendendo ao RF06. Diferente dos demais módulos, ele não possui subitens na sidebar: o acesso abre diretamente o quadro ativo. 

Colunas configuráveis — As colunas do quadro são customizáveis: é possível criar, editar (título/cor) e remover colunas, além de reordená-las. A criação ocorre via um modal simples com seleção de cor e prévia visual (Fig. 5.19). Cada coluna exibe um badge com a contagem de cartões e ícones de atalho para ações frequentes (adicionar cartão, configurações, etc.). Colunas típicas incluem A Fazer, Fazendo, Finalizadas e Erradas, mas o conjunto é livre para cada equipe. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/127ab2da714c0da2066e55c3811331cc5ea5281e2e301c49c01a9971304df785.jpg)



Figura 5.19 – Board com colunas e modal para criação de nova coluna (título e cor). Elaborado pelo autor (2025).


Cartões (atividades) e fluxo — Cada cartão representa uma atividade e armazena os campos básicos definidos no RF06 (título, descrição, responsável, prazo, status). A movimentação entre colunas é feita por drag-and-drop; o serviço registra o histórico de transições para rastreabilidade. A criação/edição de cartões é feita a partir da própria coluna, mantendo o foco no fluxo de trabalho. 

Padrões transversais. O Board herda os padrões de qualidade do sistema: (i) exclusão lógica (soft delete) para colunas e cartões — a entidade base (AbstractEntity) mantém o campo active, preservando histórico e integridade; (ii) feedback visual nas ações (criar/mover/editar); (iii) segurança por permissões: apenas perfis com acesso ao mó- dulo podem alterar a estrutura do quadro; (iv) desempenho: carregamento preguiçoso de cartões em colunas com grande volume e atualização reativa do contador. 

Com isso, o módulo entrega um kanban enxuto, configurável e totalmente integrado às permissões e padrões de rastreabilidade do Prisma, permitindo às EJs acompanhar o fluxo das atividades de ponta a ponta. 

# 5.5.9 Itens (Inventário)

O módulo de Itens apoia o controle de patrimônio e materiais da EJ. Ele oferece o CRUD básico com foco em simplicidade e rastreabilidade, seguindo os padrões transversais do sistema: sidebar com as ações Cadastrar e Listar, exclusão lógica (soft delete) e listagens paginadas. 

Modelo e regras principais. Cada item é identificado por um título (ex., “Notebook Dell”), possui quantidade (inteiro não negativo) e descrição opcional para observações como estado de conservação ou de uso. Exclusões marcam o registro como inativo no AbstractEntity (active $=$ false), preservando histórico para auditoria e evitando perdas de referência em relatórios. 

Cadastro de itens. A tela de criação concentra os campos essenciais e validações de obrigatoriedade (Título e Quantidade). A ação Cadastrar persiste o item e redireciona para a listagem com feedback visual. A Figura 5.20 mostra o formulário. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/c32962c692458957df4dfd5a73830671ae3d1ad3dfc23278a03f8853622971a9.jpg)



Figura 5.20 – Cadastro de item com título, quantidade e descrição opcional. Elaborado pelo autor (2025).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/a54a26997d13082c7ac2e684b6050c0d7aed8e2b27299f038da121b7763f9231.jpg)



Figura 5.21 – Listagem de itens (paginação, quantidade em destaque e ações de edição/remoção). Elaborado pelo autor (2025).


Aspectos de usabilidade e qualidade — O módulo herda os requisitos não funcionais do sistema: UI responsiva, feedback nas ações (salvar/editar/excluir), paginação para manter respostas rápidas e documentação REST para futuras integrações. Em termos de segurança, as operações respeitam as permissões do usuário autenticado (apenas perfis com acesso ao módulo “Itens” podem criar/alterar/remover). 

Em resumo, o módulo de Itens entrega um inventário enxuto, fácil de manter e alinhado aos padrões do Prisma, com histórico preservado por soft delete e operações consistentes com a navegação global via sidebar. 

# 5.6 Decisões de Projeto e Padrões Utilizados

• Padrão camadas (Controller–Service–Repository) para separação de responsabilidades e testabilidade. 

• DTO + Mapper para isolar o domínio da camada de apresentação/API. 

• Eventos e listeners (ex.: NoticeCreatedEvent, NoticeMailListener) para integração assíncrona e envio de e-mails. 

• Segurança com JWT, SecurityConfig e filtros (JwtAuthFilter); senhas com BCrypt. 

• Documentação de endpoints via OpenAPI/Swagger. 

# 5.7 Diagramas de Classe — Módulos Principais

A seguir, os diagramas de classes específicos por módulo. Eles detalham o diagrama geral apresentado no Cap. 4 ao nível de entidades, serviços e repositórios. 

# 5.7.1 Autenticação e Usuários

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/482793d4b591a5ba5610df9f383ded00fcc669ace1e24947b16c4b065ff78193.jpg)



Figura 5.22 – Modelo de classes para autenticação e usuários Elaborado pelo autor (2025).


Descrição estrutural — User agrega credenciais e permissões (coleções de RoleUser e ModuleName) em relação 1:1 com Person. AuthenticationController delega a AuthenticationService, que integra JwtAuthFilter e JwtTokenService para emissão/validação de tokens. 

# Regras e invariantes —

• E-mail único por usuário; senha armazenada com BCrypt. 

• User.active $=$ false impede autenticação e oculta o registro das listagens padrão. 

• Políticas de autorização por papéis e permissões de módulo. 

# Principais operações (serviço) —

• authenticate(credentials): retorna JWT (curta duração) e refresh opaco. 

• refresh(token): renova o access token próximo do vencimento. 

• assignRoles(userId, roles) / assignModules(userId, modules): atualiza autorização efetiva. 

Persistência e segurança — Entidades mapeadas com JPA/Hibernate; índice único em email; filtro global em active $=$ true. Endpoints protegidos por JWT (Bearer) e @PreAuthorize (RF01, RF02, RNF05). 

Resumo do desenho: AuthenticationController AuthenticationService UserDetailsService/UserRepository; JwtAuthFilter/JwtTokenService provêm geração/validação de tokens; User relaciona-se um-para-um com Person e possui coleções de RoleUser e ModuleName. 

# 5.7.2 Processo Seletivo

Descrição estrutural — SelectiveProcess contém Stage (ordem cronológica), Candidate e Note (associação candidato×etapa). Notice guarda comunicados versionados. 

# Regras e invariantes —

• Stage.order único por processo; datas coerentes (início e fim). 

• Note: uma por (candidato, etapa); média aritmética por candidato. 

• Notas e candidatos seguem soft delete para preservar histórico. 

# Principais operações (serviço) —

• createProcess(data) / addStage(processId, stage) / reorderStages(). 

• registerCandidate(processId, data) / upsertNote(candidateId, stageId, value). 

• publishNotice(processId, mdContent) dispara evento para e-mail. 

Persistência e segurança — Índices em processId, stageId; operações de notas em lote; políticas de acesso ao módulo PS (RF03, RNF01, RNF05). 

Resumo do desenho: SelectiveProcess agrega Candidates, Stage, Note e Notice; publicação de eventos dispara listeners para comunicações (e-mail). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/8f644cffc69a31a61c16a35a8ed37ce978c0311f778187a8538e3d5fb4387098.jpg)



Figura 5.23 – Modelo de classes para processo seletivo (candidatos, notas, estágios e notícias) Elaborado pelo autor (2025).


# 5.7.3 Projetos

Descrição estrutural — Project agrega ProjectGoals (metas com progresso e prazos), ProjectRiskItem (probabilidade/severidade/prazo) e ProjectMembers (papel, função, Regras e invariantes — 

• Status restritos: Planejado, Em andamento, Pausado, Concluído, Cancelado. 

• ProjectGoals: prazos obrigatórios; percentual concluído [0,100]. 

• ProjectMembers: não sobrepor intervalos de entrada/saída para o mesmo usuário. 

• soft delete em metas/risco/membros não apaga histórico do projeto. 

# Principais operações (serviço) —

• createProject(data) / updateProject(id, data). 

• addGoal(projectId, goal) / updateProgress(goalId, %). 

• registerRisk(projectId, risk) / prioritizeRisks(projectId). 

• assignMember(projectId, userId, role, allocation). 

Persistência e segurança — Índices em status, category, startDate; cálculos agregados expostos ao dashboard. Acesso por papéis do módulo Projetos (RF04, RNF01, RNF05). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/53cea4c158a9257f8737608da19a86012f138bca27414f359699d8404dd20fff.jpg)



Figura 5.24 – Modelo de classes para projetos (metas, riscos e membros) Elaborado pelo autor (2025).


Resumo do desenho: Project agrega ProjectGoals, ProjectRiskItem e ProjectMembers; serviços expõem operações de CRUD e cálculo de indicadores para o dashboard do projeto. 

# 5.7.4 Metas BJ e Indicadores

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/2429f42bb01de99ed6228486059c00427807cb5a9aa3a25dc6687aef5f2060c2.jpg)



Figura 5.25 – Modelo de classes para metas/indicadores (integração BJ) Elaborado pelo autor (2025).


Descrição estrutural — Company associa-se a GoalsBJ e suas instâncias MonthlyGoalBJ (mês/ano, valores de meta e faturamentos colaborativo/não colaborativo). 

# Regras e invariantes —

• (companyId, year, month) único em MonthlyGoalBJ. 

• Somatórios consistentes entre valores mensais e acumulados exibidos no dashboard. 

# Principais operações (serviço) —

• syncFromBJ(companyUid): coleta e normaliza dados (read-only). 

• seriesForCharts(companyId): entrega séries mensais e acumulados. 

Persistência e segurança — Cache em memória de curto prazo; fallback ao último dado válido; endpoints REST somente leitura (RF05, RNF01, RNF06). 

Resumo do desenho: GoalsBJ (1:N) MonthlyGoalBJ; associação com Company; serviços consolidam dados para o DashboardService. 

# 5.7.5 Board (colunas e cartões)

O diagrama do Board modela o quadro kanban corporativo (não vinculado a um único projeto). As entidades principais são: 

• BoardColumn: representa uma coluna do quadro (p. ex., A Fazer, Fazendo, Finalizadas). Campos: id, columnTitle, colorTitle, position (ordenação), e a coleção cards. 

• Cards: cartões/atividades da empresa. Campos: id, title, description, position (ordem dentro da coluna), deadline, além das referências boardColumn e responsible (User). 

• User: responsável pelo cartão. 

• AbstractEntity: superclasse com createdAt, updatedAt e active (exclusão ló- gica). 

Relacionamentos e cardinalidades. Uma BoardColumn possui $0 . . *$ Cards; cada Card pertence a exatamente uma BoardColumn. Um Card referencia um User como responsável (opcional na criação, obrigatório para conclusão, conforme regra de negócio). Todas as entidades herdam de AbstractEntity. 

Invariantes e regras. (i) position define a ordenação e é única no escopo da coluna; (ii) movimentações entre colunas preservam o histórico e recalculam position; (iii) cartões active $=$ false não aparecem no quadro, mas permanecem auditáveis. 

Operações usuais. CRUD de colunas e cartões, drag-and-drop com atualização de position, mudança de responsável e ajuste de deadline. Serviços correspondentes: BoardColumn-Controller/Service/Repository e CardsRepository (vide Tabela 5.3). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/85244dbc23be6ef130041df4ed03f4c4e0bd1a659a0a8530c8030b9612e90c85.jpg)



Figura 5.26 – Modelo de classes do Board (colunas e cartões). Elaborado pelo autor (2025).


# 5.7.6 Atividades (itens / controle de estoque)

Este diagrama representa o módulo de Itens (estoque/patrimônio). Diferente do Board, aqui Activities é a entidade de inventário. 

• Activities: item do inventário. Campos: id, title, description, quantity (≥ 

0), e referência user (dono/último responsável). 

• User: indivíduo associado ao item (p. ex., sob custódia). 

• AbstractEntity: createdAt, updatedAt, active. 

Relacionamentos e cardinalidades. Activities User é ManyToOne (muitos itens podem estar associados a um mesmo usuário). Todas as entidades especializam AbstractEntity para auditoria e soft delete. 

Invariantes e regras. (i) quantity inteiro não negativo; (ii) remoções são lógicas (active $=$ false); (iii) alterações registram updatedAt para rastreabilidade. 

Operações usuais. CRUD de itens com validação de campos obrigatórios, paginação na listagem e filtros por título/responsável. Serviços controladores conforme Tabela 5.3. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/3d76d647-b992-4411-8a20-718851c65c69/37bca83859ce91f907e8f9deb5b66a0bf175fa74af831127baead0835520ce6b.jpg)



Figura 5.27 – Modelo de classes de Itens (inventário/estoque). Elaborado pelo autor (2025).


# 5.8 Exemplo de Implementação em Código

Esta seção apresenta um exemplo real retirado do código-fonte do Prisma, aplicado tanto no backend quanto no frontend. Os trechos estão em inglês porque refletem exatamente a estrutura utilizada no projeto, preservando a nomenclatura dos arquivos, serviços, entidades e comentários. A intenção é ilustrar o padrão seguido, não reescrever ou adaptar o código para fins acadêmicos. 

Para fins de demonstração, utiliza-se o módulo Activities, por ser enxuto e representativo da arquitetura geral aplicada aos demais módulos do sistema. 

# 5.8.1 Backend

# 5.8.1.1 Controller: criação com DTO, Swagger e resposta padronizada

O controller utiliza injeção via construtor, documentação com OpenAPI/Swagger e resposta padronizada via ApiResponseDTO. A responsabilidade do método é mínima, delegando a lógica ao serviço. 

1 private final ActivitiesService activitiesService;   
2   
public ActivitiesController(ActivitiesService activitiesService) { thisactivitiesService $=$ activitiesService;   
5   
}   
6   
7 @PostMapping("/create")   
8 @Operation.summary $=$ "Criar atividade",description $=$ "Cadastra uma nova $\twoheadrightarrow$ atividade no Sistema.")   
9 @ApiResponses(value $=$ { @ApiResponse(responseCode $=$ "201",description $=$ "Created:Activity $\twoheadrightarrow$ successfully created.,"), @ApiResponse(responseCode $=$ "400",description $=$ "Bad Request: $\twoheadrightarrow$ Invalid data provided.",content $=$ @Content)   
12 ）   
13 public ResponseEntity<ApiResponseDTO<Activities>> createActivities( @RequestBody ActivitiesDTO activitiesDTO) {   
15   
16 Activities activities $=$ activitiesService.create(activitiesDTO);   
17 return ResponseEntity.status(HttpStatus CREATED).body(new $\twoheadrightarrow$ ApiResponseDTO<> ( true, "Atividade criada com succès.", activities, null   
18 ）；   
23 } 

# 5.8.1.2 Service: construção da entidade, validações e persistência

O serviço concentra regra de negócio, montagem da entidade e integração com o repositório. 

```txt
/* */
* Creates a new activity based on the provided DTO.
* 
* @param activitiesDTO the data transfer object containing 
  → activity data
* @return the created {@link Activities} entity
*/ 
```

# 5.8.1.3 Repository: consultas com native queries

As consultas são padronizadas com native queries para obter melhor desempenho, pensando em um cenário escalável. 

public interface ActivitiesRepository extends $\rightarrow$ JpaRepository<Activities, Long> {   
2 @Query(value $=$ "SELECT \* FROM activities a WHERE a.active $=$ true", 

nativeQuery $=$ true)   
List<Activities>findActivitiesActive();   
@Query(value $=$ "SELECT \* FROM activities a WHERE a.active $=$ true and $\leftrightarrow$ a.id $= ?1"$ nativeQuery $=$ true)   
Activities findActivitiesByld(Long id); 

# 5.8.1.4 Modelo: entidade estendendo AbstractEntity

```java
@Entity
@Table(name = "activities")
public class Activities extends AbstractEntity implements
    <serializable>
        @Id
        @GeneratedValue(strategy = GenerationType.SEQUENCE, generator =
            "SEQ_ACTIVITIES")
        @SequenceGenerator(name = "SEQ_ACTIVITIES",SEQUENCE name = "seq_activities", allocationSize = 1)
        private Long id;
        private String title;
        private String description;
        private Integer quantity;
        @ManyToMany(fetch = FetchType.LAZY)
        @JoinColumn(name = "user_id")
        @JsonIgnore
        private User user;
    }
} 
```

# 5.8.2 Frontend

Os trechos a seguir demonstram o padrão adotado no frontend, utilizando React, TypeScript, React Hook Form e React Query. 

# 5.8.2.1 Formulário React com TypeScript

```typescript
const form = useForm<Omit>Activities, "id" || "user">({  
    defaultValues: {  
        title: "",  
        description: "",  
        quantity: 0,  
    },  
}); 
```

```txt
const onSubmit = (payload: Omit<Activities, "id" || "user">) => {
    setSuccessMessage());
    setErrorMessage());
    activityId ? edit(payload) : register(payload);
}; 
```

# 5.8.2.2 Requisição usando React Query

export const useRegisterItem = (onSuccess: () => void, onError: () => $\rightarrow$ void) $=>$ { const userId = Number(localStorage getItem("UserID")); return useMutation({ mutationFn: async (data: Omit<Activities, "id" | "user">) => { const response = await api.post('/activities/create', { ...data,UserId, }); return response.data; }, onSuccess, onError, }; 

# 5.8.2.3 Interface da entidade no frontend

```typescript
export interface Activities {
  id?: number;
  title: string;
  description: string;
  quantity: number;
  user:
    id: number;
    name: string;
    email: string;
    password: string;
}; 
```

# 5.8.3 Síntese

O exemplo mostrado, retirado diretamente do código do Prisma, demonstra os padrões replicados em todos os módulos: 

• Backend: Controllers enxutos, services com regra de negócio, repositórios com native queries e entidades com auditoria. 

# 5.9. IMPLANTAÇÃO E INTEGRAÇÕES

• Frontend: formulários tipados com React Hook Form, comunicação padronizada com React Query e interfaces alinhadas ao domínio. 

Esses padrões garantem organização, manutenção simplificada e coerência entre os módulos do sistema. 

# 5.9 Implantação e Integrações

O ambiente de execução segue o diagrama C4 de deployment: backend em contêineres, PostgreSQL gerenciado e serviço SMTP externo. O frontend estático consome a API REST com autenticação Bearer JWT. Pipelines de build/teste garantem integridade antes do deploy. 

# 5.10 Síntese do Capítulo

Este capítulo consolidou requisitos, decisões arquiteturais e o desenho das principais áreas do Prisma. A ênfase em diagramas em vez de código amplia a compreensão sem excessos técnicos, mantendo a rastreabilidade entre requisitos (RF/RNF), arquitetura (C4) e modelos de domínio (UML). 

# Capítulo 6

# Estudo de Caso e Resultados

Este capítulo apresenta o plano de avaliação, os cenários de uso e os resultados da validação em campo do Prisma. O objetivo central foi verificar se as funcionalidades priorizadas (Seção 5.5) reduzem o esforço operacional das EJs e aumentam a transparência do andamento dos processos internos. 

O sistema foi colocado em validação na Include Engenharia, empresa júnior dos cursos de Engenharia de Computação, Engenharia Mecatrônica, Ciências e Tecnologia e Tecnologia da Informação. Os módulos definidos como prioritários na Seção 5.3 — Processo Seletivo e Projetos — foram aqueles efetivamente utilizados durante os testes. 

Pelo caráter das funcionalidades em validação, as diretorias de Gestão de Projetos e Desenvolvimento e de Gestão de Pessoas foram as principais envolvidas no processo. Participaram diretamente do estudo os diretores de ambas as diretorias, bem como três gerentes responsáveis pela organização do Processo Seletivo. 

# 6.1 Objetivos de avaliação

A avaliação buscou responder, de forma prática, a três questões: (i) se o sistema reduz o esforço manual nos processos de Processo Seletivo e Projetos; (ii) se a centralização das informações, com histórico consultável, diminui o risco de inconsistências; e (iii) se os usuários conseguem executar as tarefas do dia a dia sem necessidade de treinamento extenso. 

# 6.2 Contexto e linha de base (antes do Prisma)

Antes da implantação, o Processo Seletivo (PS) era gerenciado essencialmente com planilhas e documentos. Os candidatos eram cadastrados em arquivos distintos, as notas eram lançadas manualmente em planilhas separadas, a comunicação era feita por $e$ -mails redigidos caso a caso e o desenho das etapas permanecia espalhado em documentos, sem visão consolidada. Como consequência, consultar processos anteriores para coletar dados e tomar decisões específicas tornava-se uma tarefa trabalhosa. 

No acompanhamento de Projetos, a realidade era semelhante. As informações de equipe e cronograma ficavam registradas principalmente no GitLab e no Drive; não havia definição formal de metas, tampouco um risk log estruturado ou um padrão de status. A 

falta de uma visão geral do andamento dos projetos comprometia a definição de objetivos e a identificação de atrasos e necessidades de realocação, pois exigia que cada responsável reportasse individualmente o progresso, gerando gargalos para detectar problemas pontuais. 

Essa linha de base serviu como referência objetiva para comparar esforço, tempo e visibilidade após a introdução do Prisma. 

# 6.3 Desenho do estudo

Para o período de validação, que ocorreu de setembro a outubro de 2025, o frontend foi publicado no Netlify e o backend no Railway, ambos com integração contínua a partir do repositório principal. O banco de dados PostgreSQL permaneceu gerenciado no ambiente do Railway. Essa configuração permitiu deploys rápidos e observação de comportamento em produção. 

A coleta combinou duas frentes: observação do uso durante as rotinas diárias e entrevistas curtas com os participantes (diretores e gerentes). Para o Processo Seletivo, os cenários executados contemplaram todo o ciclo de cadastro de etapas, notas e avisos. Em Projetos, acompanhou-se o ciclo de cadastro com definição de metas, registro de riscos, associação de membros e atualização de status. 

As métricas observadas incluíram tempo de execução de tarefas recorrentes (por exemplo, cadastro de candidatos, lançamento de notas e comunicação de resultados), qualidade da informação com redução de fontes paralelas, presença de histórico e indicadores de adoção/percepção dos usuários. 

# 6.4 Resultados por módulo

# 6.4.1 Processo Seletivo

Com o Prisma, o lançamento de notas passou a ocorrer em um formulário organizado por candidato e por etapa, reduzindo cliques e evitando duplicidades. A comunicação de avisos/notícias diretamente pelo sistema foi um ponto de destaque, substituindo $e$ -mails manuais e planilhas auxiliares, trazendo padronização, rastreabilidade e, principalmente, redução de atividades repetitivas. Todo o ciclo do PS (candidatos, etapas, notas, avisos) ficou registrado em um único lugar, facilitando consultas futuras a edições passadas. Em relação à linha de base, os usuários relataram ganho de velocidade e queda perceptível de retrabalho; comentários recorrentes destacaram que “lançar notas ficou mais rápido” e que “o status de cada candidato ficou evidente sem precisar procurar em várias planilhas”, além de mencionar maior clareza na leitura geral das notas. 

# 6.4.2 Projetos

No módulo de Projetos, a padronização de status (Planejado, Em andamento, Pausado, Concluído, Cancelado) trouxe mais transparência ao andamento. A definição de 

metas por projeto, com prazos e percentual concluído, facilitou a leitura executiva e a priorização, possibilitando uma tomada de decisão mais eficaz. O controle de prazos ficou explícito a partir de campos de início/fim e deadlines claros, e a gestão de riscos passou a existir de forma estruturada, com severidade e probabilidade registradas para acompanhamento, permitindo antecipar problemas potenciais. Comparado ao cenário anterior, com informações dispersas em planilhas e baixa visibilidade, o Prisma ofereceu ficha única do projeto, histórico e trilhas de auditoria, além de visões para acompanhamento no dashboard. 

# 6.5 Indicadores observados

Os indicadores aqui apresentados foram obtidos por meio de um processo combinado de coleta: (i) formulários de feedback enviados aos diretores e gerentes envolvidos; (ii) conversas estruturadas com os responsáveis por cada etapa; e (iii) estimativas de tempo fornecidas pelos próprios usuários com base na rotina anterior ao Prisma. As medições consideraram atividades executadas antes e depois da implantação, permitindo comparar o esforço operacional de forma direta. 

No Processo Seletivo, o principal indicador analisado foi o tempo gasto na consolidação das notas. Antes do Prisma, os avaliadores precisavam abrir planilhas distintas, localizar manualmente a nota do candidato e transferi-la para a planilha final do PS. Esse procedimento levava, em média, entre 50 segundos e 1 minuto por candidato. Considerando o ciclo avaliado, que envolveu 63 candidatos, o tempo total para consolidação atingia facilmente dezenas de minutos, tornando o processo repetitivo e sujeito a erros. 

Após a adoção do Prisma, as notas passaram a ser registradas diretamente no sistema, com visualização por etapa e por candidato. A eliminação das buscas manuais e da transferência para planilhas reduziu o tempo estimado por candidato em aproximadamente $50 \%$ , segundo relatos dos responsáveis. 

Além disso, o envio de avisos deixou de ser realizado por e-mail individual e passou a ocorrer diretamente pelo sistema. Esse ponto, mencionado de forma recorrente nos formulários, gerou uma redução estimada de $70 \%$ no esforço de comunicação comparandose o tempo antes do Prisma, levando apenas 2 minutos, especialmente pela padronização das mensagens e pela eliminação de retrabalho ao notificar grupos distintos de candidatos. 

No módulo de Projetos, a implantação resultou em maior previsibilidade: nove projetos ativos registraram metas formais dentro do período e cinco riscos foram cadastrados e priorizados, permitindo acompanhamento contínuo e visão consolidada do portfólio. 

# 6.6 Discussão

Os resultados obtidos indicam que o Prisma atingiu seu objetivo de reduzir o esforço manual e ampliar a transparência nos processos internos da EJ. Essa conclusão é fundamentada nos dados apresentados na Seção 6.5, na qual foram quantificados os indicadores de tempo e esforço observados antes e depois da implantação do sistema. A comparação 

sistemática — baseada em formulários de feedback, conversas com os responsáveis e medições aproximadas das tarefas realizadas — demonstra de forma concreta a redução de trabalho repetitivo, especialmente no Processo Seletivo. 

No módulo de Processo Seletivo, os ganhos ficaram mais evidentes: o tempo de consolidação das notas, que antes exigia localizar manualmente as avaliações em diferentes planilhas, foi reduzido de forma significativa, conforme discutido na Seção 6.5, assim como o esforço de comunicação diminuiu fortemente com o envio de avisos padronizados diretamente pelo sistema, eliminando a necessidade de compor e-mails individualmente para cada etapa. 

No módulo de Projetos, a introdução de metas e riscos padronizados fortaleceu a previsibilidade e melhorou a clareza sobre o andamento das iniciativas, ainda que o impacto percebido tenha sido menos imediato do que no PS, devido à natureza contínua das atividades de gestão de projetos. 

A avaliação realizada com os usuários — diretores e gerentes — reforça esses pontos. Os relatos indicam uma maior percepção de organização, menor retrabalho e melhor visibilidade das informações. Assim, o conjunto de observações consolidadas nos indicadores apresentados na seção anterior fornece a base que sustenta a afirmação de que o Prisma contribuiu efetivamente para reduzir o esforço operacional e aumentar a transparência na EJ. 

# 6.7 Ameaças à validade

A interpretação dos achados deve considerar algumas limitações: a validação ocorreu em um contexto único (uma EJ e um bimestre específico), o que pode não capturar toda a diversidade de processos; há uma curva de aprendizado em andamento, de modo que ganhos adicionais podem ficar evidentes apenas com o uso prolongado; e a sazonalidade do PS e do portfólio de projetos afeta o volume de dados e a comparabilidade ao longo do tempo. 

Existe também a barreira de adoção de novas ferramentas: apesar dos benefícios constatados do Prisma, é necessário mais tempo de utilização para que a solução se torne amplamente difundida na EJ. 

# 6.8 Síntese

Em síntese, a validação em campo com os diretores e gerentes da Include Engenharia mostrou benefícios concretos: no Processo Seletivo, praticidade no lançamento de notas, visibilidade clara do status e histórico unificado; em Projetos, transparência do andamento, definição visual de metas, controle de prazos e gestão de riscos. A centralização da informação e a padronização dos registros reduziram retrabalho e aumentaram a confiabilidade dos dados usados na gestão cotidiana. 

# Capítulo 7

# Conclusão

Este trabalho apresentou o Prisma, uma plataforma web para apoiar a gestão de Empresas Juniores (EJs) com foco em dois fluxos críticos do dia a dia: Processo Seletivo e Projetos. Do ponto de vista de engenharia, propusemos e implementamos uma arquitetura em camadas (Controller–Service–Repository), com autenticação via JWT, documentação de API, rastreabilidade entre requisitos e artefatos e um frontend responsivo orientado a listas paginadas e ações padronizadas. Do ponto de vista organizacional, buscou-se reduzir esforço manual, centralizar informações e elevar a transparência operacional. 

# 7.1 Síntese das contribuições

Ao longo do desenvolvimento, o Prisma proporcionou uma experiência única como modelo de informação para Processo Seletivo (PS) e Projetos. Anteriormente, as informações que estavam espalhadas em planilhas e documentos, passaram a estar registradas em cadastros consistentes, com histórico e trilhas de auditoria. Isso permitiu automatizar tarefas repetitivas, principalmente o lançamento de notas por etapa e o envio de avisos no PS, reduzindo retrabalho e evitando divergências. 

Nos Projetos, a adoção de padrões de acompanhamento (status, metas, prazos, riscos e membros) possibilitou uma visão mais clara da situação dos projetos, facilitando a tomada de decisões. 

# 7.2 Validação e principais resultados

A validação em campo, realizada de setembro a outubro de 2025, na Include Engenharia, confirmou ganhos nos dois módulos priorizados (Cap. 6). 

No PS, o tempo de consolidação de notas caiu cerca de $50 \%$ e o esforço de comunica-ção, em especial, teve uma redução ainda mais significativa, em torno de $70 \%$ , removendo o esforço necessário de mapear cada candidato que deveria receber aviso específico. Todo o ciclo (candidatos, etapas, notas e avisos) passou a ficar centralizado no sistema, trazendo mais transparência de status para os gerentes do PS. 

Em Projetos, houve um acompanhamento padronizado de 9 projetos ativos, com metas definidas, 5 riscos foram registrados e priorizados e as telas de progresso e prazos facilitaram a tomada de decisão. 

Houve $100 \%$ de centralização dos dados do PS no Prisma, evitando a necessidade de fontes paralelas e diminuindo inconsistências. Foram coletados depoimentos do Diretor de Gestão de Pessoas e de sua equipe responsável pela gestão do PS, onde destacaram menos retrabalho, maior velocidade no dia a dia. 

# 7.3 Implicações práticas

Os resultados indicam que o Prisma ajuda a reduzir a carga de trabalho em períodos do semestre mais conturbados, como conciliar provas e o andamento do PS, liberando tempo da equipe para outras atividades mais importantes, promovendo uma tomada de decisão mais rápida e confiável. Em Projetos, a padronização de status, metas e riscos fortalece a governança e reduz gargalos nas decisões a serem tomadas, como redefinição do cronograma do projeto, mensuração de novos riscos e manutenção de membros. 

# 7.4 Limitações

Os achados refletem um contexto específico: uma EJ, em um bimestre de validação. Processos e cultura podem variar, principalmente em um contexto financeiro e organizacional amplamente diferentes entre EJs, atrelados a uma curva de aprendizado que ainda está em andamento, é razoável esperar ganhos adicionais com o uso contínuo. Além disso, como os ciclos de PS e de projetos têm sazonalidade, comparações temporais podem gerar resultados divergentes. 

# 7.5 Trabalhos futuros

Os próximos passos caminham em três frentes. A primeira é ampliar a automação e comunicação, com templates por etapa do PS e disparos condicionados. A segunda é evoluir relatórios executivos exportáveis (PDF/planilha) para PS e Projetos, com indicadores e séries históricas. A terceira frente seriam integrações (SSO institucional e repositórios de documentos como Drive/Git), para acompanhar impacto ao longo de um ano. 

# 7.6 Considerações finais

O Prisma mostrou-se efetivo em seu propósito de reduzir esforço manual e aumentar a transparência nos processos críticos das EJs, especialmente em Processo Seletivo e Projetos. A combinação de design centrado no fluxo real de trabalho, arquitetura modular e decisões de produto orientadas a valor permitiu ganhos imediatos e ofereceu uma base sólida para evolução. 

Com a continuidade da adoção, o aprofundamento das integrações e a ampliação do período de medição, a expectativa é consolidar o Prisma como uma plataforma de gestão para Empresas Juniores, promovendo melhores práticas, comparabilidade entre ciclos e 

decisões mais rápidas e fundamentadas. Em suma, o sistema cumpre o que se propôs: organizar, padronizar e tornar visível o que antes estava fragmentado em planilhas e e-mails, abrindo espaço para que as equipes foquem no que mais importa: executar e aprender. 

# Referências Bibliográficas



ATLASSIAN. Trello: capture, organize, and tackle your to-dos from anywhere. 2025. Acesso em: 9 out. 2025. Disponível em: <https://trello.com/home?wvideo=uy8s1pjm2i# video>. 





BECK, K.; FOWLER, M. e. a. Manifesto for Agile Software Development. 2001. Acesso em: 5 out. 2025. Disponível em: <https://agilemanifesto.org/>. 





BOOCH, G.; RUMBAUGH, J.; JACOBSON, I. The Unified Modeling Language User Guide. Boston: Addison-Wesley, 2005. 2. ed. 





BRASIL. Lei $n ^ { o } I 3 . 2 6 7 _ { \mathrm { \Omega } }$ , de 6 de abril de 2016: disciplina a criação e a organização das associações denominadas empresas juniores. 2016. Acesso em: 10 out. 2025. Disponível em: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/lei/L13267.htm>. 





BROWN, S. Software Architecture for Developers: Volume 2 – Visualise, document and explore your software architecture. [S.l.]: Leanpub, 2018. 2. ed. 





BROWN, S. The C4 Model for Visualising Software Architecture. s.d. Acesso em: 9 out. 2025. Disponível em: <https://c4model.com/>. 





COMMUNITY, R. Redmine: Flexible Project Management. 2024. Acesso em: 8 out. 2025. Disponível em: <https://www.redmine.org>. 





CORPORATION, M. TypeScript Documentation. 2023. Acesso em: 5 out. 2025. Disponível em: <https://www.typescriptlang.org/>. 





DB-ENGINES. DB-Engines Ranking. 2024. Acesso em: 5 out. 2025. Disponível em: <https://db-engines.com/en/ranking>. 





GMBH, O. OpenProject: Open Source Project Management Software. 2024. Acesso em: 8 out. 2025. Disponível em: <https://www.openproject.org>. 





GROUP, T. P. G. D. PostgreSQL Documentation. 2024. Acesso em: 5 out. 2025. Disponível em: <https://www.postgresql.org/docs/>. 





HAMMER, M.; CHAMPY, J. Reengenharia: Revolucionando a Empresa em Função dos Clientes, da Concorrência e das Grandes Mudanças da Gerência Moderna. Rio de Janeiro: Campus, 1993. 





JETBRAINS. The State of Developer Ecosystem 2023. 2023. Acesso em: 5 out. 2025. Disponível em: <https://www.jetbrains.com/lp/devecosystem-2023/>. 





JS, S. O. State of JavaScript 2023 Survey. 2023. Acesso em: 5 out. 2025. Disponível em: <https://2023.stateofjs.com/>. 





JÚNIOR, B. Relatório Anual 2023. 2023. Acesso em: 5 out. 2025. Disponível em: <https://brasiljunior.org.br>. 





LABS, T. Tailwind CSS Documentation. 2024. Acesso em: 5 out. 2025. Disponível em: <https://tailwindcss.com/>. 





LAUDON KENNETH C.; LAUDON, J. P. Sistemas de Informação Gerenciais. São Paulo: Pearson, 2019. 14. ed. 





OLIVEIRA, D. P. R. Sistemas, Organização e Métodos. São Paulo: Atlas, 2019. 23. ed. 





OVERFLOW, S. Developer Survey 2023. 2023. Acesso em: 5 out. 2025. Disponível em: <https://survey.stackoverflow.co/2023/>. 





PARANÁ, U. F. D. Empresa Júnior. s.d. Acesso em: 10 out. 2025. Disponível em: <https://exatas.ufpr.br/empresa-junior/>. 





PLATFORMS, I. M. React Documentation. 2023. Acesso em: 5 out. 2025. Disponível em: <https://react.dev/>. 





PRESSMAN ROGER S.; MAXIM, B. R. Engenharia de Software: Uma Abordagem Profissional. Porto Alegre: AMGH, 2016. 8. ed. 





RUMMLER GEARY A.; BRACHE, A. P. Melhorando os Processos da Empresa. Rio de Janeiro: Qualitymark, 2010. 





SCHWABER KEN; SUTHERLAND, J. The Scrum Guide. 2020. Acesso em: 5 out. 2025. Disponível em: <https://scrumguides.org/>. 





SILVA M. R.; PEREIRA, D. L. Sistema web de gestão de projetos acadêmicos utilizando django framework. Revista Brasileira de Computação Aplicada, v. 13, n. 2, p. 45–56, 2021. 





SOMMERVILLE, I. Engenharia de Software. São Paulo: Pearson, 2011. 9. ed. 





SOUZA T. A.; CARVALHO, L. F. Automação de processos acadêmicos com spring boot e angular. Anais do Congresso de Engenharia de Software, p. 122–133, 2020. 





STONEBRAKER, M. The design of the postgres storage system. Proceedings of the 13th International Conference on Very Large Data Bases, 1986. 





TECHNOLOGIES, C. ClickUp: All-in-One Productivity Platform. 2023. Acesso em: 8 out. 2025. Disponível em: <https://clickup.com>. 





WALLS, C. Spring Boot in Action. Shelter Island, NY: Manning, 2016. 

