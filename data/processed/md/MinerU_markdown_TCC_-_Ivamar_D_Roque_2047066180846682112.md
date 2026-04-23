# Desenvolvimento de um Sistema Web de Controle Financeiro para a Secretaria de Carnaúba dos Dantas com Aplicação de Boas Práticas de Engenharia de Software e Acessibilidade Digital

Ivamar Dantas Roque 

Orientador: Prof. Dr. Rummenigge Rudson Dantas 

# Desenvolvimento de um Sistema Web de Controle Financeiro para a Secretaria de Carnaúba dos Dantas com Aplicação de Boas Práticas de Engenharia de Software e Acessibilidade Digital

Ivamar Dantas Roque 

Orientador: Prof. Dr. Rummenigge Rudson Dantas 

Trabalho de Conclusão de Curso de Graduação na modalidade Monografia, submetido como parte dos requisitos necessários para conclusão do curso de Engenharia de Computação pela Universidade Federal do Rio Grande do Norte (UFRN/CT). 

# Universidade Federal do Rio Grande do Norte - UFRN

# Sistema de Bibliotecas - SISBI

# Catalogação de Publicação na Fonte. UFRN - Biblioteca Central Zila Mamede

Roque, Ivamar Dantas. 

Desenvolvimento de um sistema web de controle financeiro para a secretaria de carnaúba dos dantas com aplicação de boas práticas de engenharia de software e acessibilidade digital / Ivamar Dantas Roque. - 2025. 

61 f.: il. 

Monografia (graduação) - Universidade Federal do Rio Grande do Norte, Centro de Tecnologia, Curso de Engenharia da Computação, Natal, RN, 2025. 

Orientação: Prof. Dr. Rummenigge Rudson Dantas. 

1. Engenharia de software - Monografia. 2. Acessibilidade digital - Monografia. 3. WCAG - Monografia. 4. Sistema web - Monografia. 5. Controle financeiro - Monografia. I. Dantas, Rummenigge Rudson. II. Título. 

RN/UF/BCZM 

CDU 004 

# Desenvolvimento de um Sistema Web de Controle Financeiro para a Secretaria de Carnaúba dos Dantas com Aplicação de Boas Práticas de Engenharia de Software e Acessibilidade Digital

Ivamar Dantas Roque 

Monografia aprovada em 8 de dezembro de 2025, pela banca examinadora composta pelos seguintes membros: 

Prof. Dr. Rummenigge Rudson Dantas (orientador) . . . . . ECT/UFRN 

Prof. Dr. Bruno Marques Ferreira da Silva . . . ECT/UFFN 

Prof. Dr Aquiles Medeiros Filgueira Burlamaqui . . . ECT/UFRN 

Aos meus pais...... 

# Agradecimentos

Agradeço primeiramente a Deus e à minha família, em especial aos meus pais e meus avós, que sempre me apoiaram para que eu chegasse até aqui. Sou extremamente grato por toda a compreensão e pelo apoio em minhas decisões, que me possibilitaram cursar uma faculdade em outra cidade. 

Ao meu orientador, professor Rummenigge, e aos professores da monitoria, por terem me acompanhado durante anos sempre desejando o meu melhor. 

À Emilly Gabrielly, minha namorada, que sempre me deu todo o amor, suporte, paciência e apoio incondicionale. 

Aos meus amigos, tanto os de infância quanto os feitos na faculdade, que tornaram meu dia a dia nesta jornada mais leve. 

# Resumo

O gerenciamento eficiente de custos é um pilar central na administração pública, mas muitas organizações ainda dependem de métodos tradicionais, como registros manuais ou planilhas, que são propensos a erros e dificultam a análise gerencial. Diante deste cená- rio, este trabalho propôs o Desenvolvimento de um Sistema Web de Controle Financeiro para a Secretaria de Carnaúba dos Dantas. O objetivo geral foi criar uma solução robusta (ConSec), articulando boas práticas de Engenharia de Software com os princípios de Acessibilidade Digital (WCAG), garantindo a usabilidade e a inclusão de todos os perfis de servidores. A metodologia empregada adotou o modelo arquitetural Cliente-Servidor, com o Backend implementado como uma API RESTful em .NET Core (C#), responsá- vel pela lógica de negócio e persistência de dados via Entity Framework Core (ORM), e o Frontend como uma Single Page Application (SPA) em Angular (TypeScript), focada na interação do usuário. A acessibilidade foi tratada como um Requisito Não-Funcional (RNF) primário, aplicando os quatro princípios WCAG (Perceptível, Operável, Compreensível e Robusto - POUR) desde o design da interface. Os resultados demonstram o desenvolvimento de uma aplicação web funcional e acessível, composta por módulos operacionais (cadastro e auditoria de custos) e um Dashboard Gerencial que transforma dados brutos em insights visuais para a tomada de decisão. O sistema passou por auditorias de acessibilidade usando ferramentas como Lighthouse e testes manuais (navegação via teclado e NVDA), confirmando a conformidade com o padrão WCAG. Por fim, o ConSec foi validado ao processar e analisar integralmente os dados financeiros reais da Secretaria referentes ao exercício de 2024, abrangendo 18 centros de custo (ex: Frota, Infraestrutura, Alimentação Escolar), confirmando sua eficácia em prover capacidade inédita de auditoria e controle financeiro para o planejamento estratégico 

Palavras-chave: Engenharia de Software; Acessibilidade Digital; WCAG; Sistema Web; Controle Financeiro; .NET; Angular. 

# Abstract

Efficient cost management is a central pillar in public administration, yet many organizations still rely on traditional methods, such as manual records or spreadsheets, which are error-prone and hinder managerial analysis. Against this backdrop, this work proposed the Development of a Web Financial Control System for the Secretariat of Carnaúba dos Dantas. The general objective was to create a robust solution (ConSec) by articulating good Software Engineering practices with Digital Accessibility (WCAG) principles, ensuring usability and inclusion for all employee profiles. The methodology adopted the Client-Server architectural model, with the Backend implemented as a RESTful API in .NET Core (C#), responsible for business logic and data persistence via Entity Framework Core (ORM), and the Frontend as an Angular (TypeScript) Single Page Application (SPA), focused on user interaction. Accessibility was treated as a primary Non-Functional Requirement (NFR), applying the four WCAG principles (Perceivable, Operable, Understandable, and Robust - POUR) from the interface design phase. The results show the development of a functional and accessible web application, featuring operational modules (cost registration and auditing) and a Managerial Dashboard that transforms raw data into visual insights for decision-making. The system successfully passed accessibility audits using tools like Lighthouse and manual tests (keyboard navigation and NVDA), confirming adherence to the WCAG standard. Finally, ConSec was validated by fully processing and analyzing the Secretariat’s real financial data for the 2024 fiscal year, covering 18 cost centers (e.g., Fleet, Infrastructure, School Meals), confirming its effectiveness in providing an unprecedented capacity for auditing and financial control for strategic planning 

Keywords: Software Engineering; Digital Accessibility; WCAG; Web System; Financial Control; .NET; Angular. 

# Sumário

# Sumário i

# Lista de Figuras iii

# Lista de Tabelas iv

# 1 Introdução 1

1.1 Justificativa 1 

1.2 Objetivos 2 

# 2 Revisão Bibliográfica e Fundamentação Teórica 3

2.1 Engenharia de Software . . 3 

2.1.1 Arquitetura de Sistemas Web Modernos . . . . 3 

2.2 Banco de Dados . . 5 

2.2.1 Modelo Relacional 6 

2.2.2 Mapeamento Objeto-Relacional (ORM) . . . . . . . . . 6 

2.3 Acessibilidade Digital . 7 

2.3.1 As Diretrizes WCAG . . 8 

2.3.2 WAI-ARIA 9 

# 3 Metodologia 10

3.1 Levantamento e Modelagem de Requisitos . . 10 

3.2 Design da Solução e Arquitetura . . . 11 

3.2.1 Arquitetura do Sistema . . 12 

3.2.2 Modelagem e Persistência de Dados . . 14 

3.2.3 Implementação da Interface e Acessibilidade . . . . . . . . 16 

3.3 Desenvolvimento e Implementação . . . 17 

3.3.1 Implementação do Backend (.NET) 17 

3.3.2 Implementação do Frontend (Angular) . . . . 17 

3.4 Testes e Validação do Sistema 18 

3.4.1 Testes Funcionais . 18 

3.4.2 Auditoria de Acessibilidade 18 

# 4 Resultados e Discussões 19

4.1 Apresentação do Sistema Desenvolvido 19 

4.1.1 Dashboard Gerencial . . . . 19 

4.1.2 Módulo Operacional: Custos . . . . . . 20 

4.1.3 Módulos Administrativos . . . . . 22 

4.2 Validação de Acessibilidade 24 

4.2.1 Performance e Boas Práticas (Lighthouse) . . . . . . . . . . 24 

4.2.2 Conformidade Semântica (WAVE) . . . . 24 

4.3 Estudo de Caso: Análise Financeira 2024 25 

4.3.1 Análise de Frota Própria . . . . 25 

4.3.2 Logística de Transporte Terceirizado . . . . . 28 

4.3.3 Infraestrutura . . 30 

4.3.4 Consumo e Insumos 32 

4.3.5 Auditoria de Utilitários (Concessionárias) . . . . . . . . . 35 

4.3.6 Alimentação Escolar . . . . 38 

4.3.7 Investimentos e Serviços Diversos . . . 40 

4.4 Conclusão 47 

5 Conclusão 48 

Referências bibliográficas 49 

# Lista de Figuras

2.1 Exemplo de Arquitetura Cliente-Servidor . . . . . . 5 

2.2 Diagrama Entidade-Relacionamento (DER) 6 

2.3 Camada de Mapeamento Objeto-Relacional (ORM) . . 7 

2.4 Os quatro princípios da Acessibilidade (POUR) . . . 9 

3.1 Transformação de dados brutos em insights visuais no Dashboard. . . . . 12 

3.2 Arquitetura Cliente-Servidor do sistema ConSec . . . 13 

3.3 Diagrama Entidade-Relacionamento (DER) do ConSec . . 15 

3.4 Camada de Mapeamento Objeto-Relacional (ORM) . . 16 

4.1 Tela de Dashboard: Visão geral dos custos em tempo real. 20 

4.2 Tela de Adicionar Custo: Formulário acessível e responsivo. . . . . 21 

4.3 Tela de Visualizar Custos: Listagem tabular com opções de filtro e edição. 21 

4.4 Tela de Gerenciar Funcionários: Controle de acesso e perfis de usuário. . 22 

4.5 Tela de Gerenciar Temas: Personalização das categorias de despesa. . . . 23 

4.6 Tela de Gerenciar Saldo: Registro de aportes e orçamentos. . 23 

4.7 Pontuação de Acessibilidade e Boas Práticas (Lighthouse). . . . . . . . . 24 

4.8 Relatório de Conformidade Semântica (WAVE). . . . 25 

4.9 Gráfico: Carros . 26 

4.10 Gráfico: Ônibus Escolares 27 

4.11 Gráfico: Transporte Escolar . . 29 

4.12 Gráfico: Auxílio Transporte . . 30 

4.13 Gráfico: Infraestrutura 31 

4.14 Gráfico: Água Potável 33 

4.15 Gráfico: Gás de Cozinha 34 

4.16 Gráfico: Material de Limpeza . . . 35 

4.17 Gráfico: Energia Elétrica 36 

4.18 Gráfico: Água (CAERN) . 37 

4.19 Gráfico: Alimentos Atacado 39 

4.20 Gráfico: Agricultura Familiar . . 40 

4.21 Gráfico: Material de Expediente 41 

4.22 Gráfico: Esporte Educacional . 42 

4.23 Gráfico: Viagens Licitadas 43 

4.24 Gráfico: Projetos Pedagógicos 44 

4.25 Gráfico: Sistemas e Assessoria 45 

4.26 Gráfico: Estágio Remunerado . . 47 

# Lista de Tabelas

4.1 Carros (Combustível/Manutenção) . 26 

4.2 Ônibus Escolares 27 

4.3 Transporte Terceirizado . . 28 

4.4 Auxílio Transporte 30 

4.5 Infraestrutura e Obras . . 31 

4.6 Água Potável 32 

4.7 Gás de Cozinha 34 

4.8 Material de Limpeza 35 

4.9 Energia Elétrica (COSERN) 36 

4.10 Água (CAERN) . . . 37 

4.11 Alimentos Atacado 38 

4.12 Agricultura Familiar 40 

4.13 Material de Expediente . . 41 

4.14 Esporte Educacional 42 

4.15 Viagens Licitadas 43 

4.16 Projetos Pedagógicos . . 44 

4.17 Sistemas e Assessoria . . 45 

4.18 Estágio Remunerado 46 

# Capítulo 1 Introdução

# 1.1 Justificativa

Na administração moderna, a otimização da distribuição de recursos assume protagonismo, sendo vital tanto na esfera pública quanto na privada. Em instituições como secretarias municipais, o gerenciamento dos custos operacionais torna-se indispensável para maximizar o retorno dos investimentos e garantir a saúde financeira da organização (Martins 2003). Contudo, diversas entidades ainda dependem de métodos de controle tradicionais, como registros manuais ou o uso de planilhas (Panko 2000). Tais abordagens são propensas a erros humanos, consomem um tempo significativo, não garantem a integridade dos registros e criam barreiras para a consolidação de dados voltada à análise gerencial. 

A substituição dessas práticas convencionais por um sistema web dedicado representa um salto qualitativo em eficiência e organização. A solução proposta, um Sistema Web de Controle de Custos, centraliza essa modernização. Com base nas informações fornecidas pelos colaboradores (tais como despesas operacionais e pagamentos a fornecedores, entre outros), a aplicação sistematiza e converte esses dados, empregando-os como fundamento para a elaboração de relatórios analíticos e painéis visuais (Pressman & Maxim 2021). 

Esses painéis constituem instrumentos indispensáveis ao suporte decisório, permitindo ao gestor identificar gargalos, analisar tendências de gastos e, consequentemente, otimizar o orçamento (Few 2006). Todavia, a adoção real e o uso efetivo de uma ferramenta de controle interno não dependem apenas de sua funcionalidade técnica; o sistema precisa ser intuitivo e acessível, assegurando que qualquer funcionário consiga operá- lo. Nesse contexto, surge o desafio da Acessibilidade Digital. As Diretrizes de Acessibilidade para Conteúdo Web (WCAG, do inglês Web Content Accessibility Guidelines) (World Wide Web Consortium (W3C) 2023) representam a norma técnica global para tratar desse tema, estabelecendo os princípios para que as aplicações web sejam Perceptíveis, Operáveis, Compreensíveis e Robustas (POUR). 

No cenário de softwares corporativos, muitas soluções focam exclusivamente nos aspectos tradicionais da engenharia de software: assegurar a persistência das informações e estruturar regras de negócio complexas, geralmente apoiadas em bancos de dados relacionais e um backend sólido (Sommerville 2011). Tal estratégia, embora funcional, muitas vezes origina sistemas pouco amigáveis ao usuário final. Essas plataformas costumam 

ser marcadas por interfaces de difícil compreensão, curvas de aprendizado lentas e pela inaptidão em acolher servidores com variados graus de letramento digital ou que possuam deficiências (sejam elas visuais, motoras, entre outras). 

A engenharia de software clássica, ainda que vital para a operação do sistema (como mencionado anteriormente), mostra-se insuficiente para suprir as necessidades atuais de interfaces que unem eficiência e inclusão. Essa demanda exige uma estratégia integrada, tecnicamente viável, graças à maturidade das tecnologias de frontend e backend (como Angular e .NET). Diante desse cenário, este trabalho projeta a criação de uma solução que integra, desde o início, três eixos fundamentais: a aplicação de boas práticas de Engenharia de Software, uma modelagem de Banco de Dados consistente e os preceitos de Acessibilidade Digital, com foco na usabilidade plena para o gestor interno. 

# 1.2 Objetivos

Objetivo Geral: Identificar as principais dificuldades relacionadas ao controle financeiro da Secretaria Municipal de Educação e desenvolver um sistema web que otimize a organização, o monitoramento e a gestão dos recursos financeiros, promovendo maior transparência, precisão e eficiência nos processos administrativos. 

Para alcançar o objetivo geral, este trabalho se propõe a: 

• Modelar os requisitos do sistema: Levantar as necessidades funcionais (regras de negócio) e não-funcionais (acessibilidade) da Secretaria e traduzi-las em artefatos de engenharia de software, incluindo a modelagem de dados (MER) e o desenho da arquitetura (Frontend Angular e Backend .NET). 

• Projetar a interface com foco em acessibilidade: Aplicar os princípios das WCAG (Web Content Accessibility Guidelines) desde a fase de design da interface (UI/UX), garantindo que os protótipos do sistema atendam aos critérios de Perceptibilidade, Operabilidade e Compreensibilidade (HTML semântico, WAI-ARIA e navegação por teclado). 

• Desenvolver e implementar o sistema "ConSec": Codificar e integrar a plataforma web, articulando o backend (.NET) para persistência e lógica de negócio com o frontend (Angular) para interação do usuário, entregando as funcionalidades de cadastro de custos, gerenciamento de saldos e visualização de dashboards. 

• Validar a conformidade e funcionalidade do sistema: Realizar testes funcionais para verificar o atendimento aos requisitos de negócio e executar auditorias de acessibilidade, utilizando ferramentas (como Lighthouse e WAVE) e testes manuais (como navegação por teclado), para comprovar a conformidade com os padrões WCAG. 

# Capítulo 2

# Revisão Bibliográfica e Fundamentação Teórica

Este capítulo apresenta os conceitos teóricos que fundamentam o desenvolvimento do sistema ConSec. A revisão abrange os fundamentos de Engenharia de Software, com foco nos processos e na arquitetura de sistemas; os princípios de Banco de Dados, que estruturam a persistência e a modelagem da informação; os critérios de Acessibilidade Digital (WCAG), que norteiam o design inclusivo da interface; e os conceitos de Visualização de Dados, aplicados no desenvolvimento do dashboard gerencial. 

# 2.1 Engenharia de Software

A Engenharia de Software consolida-se como um ramo tecnológico focado na constru-ção sistemática de soluções computacionais, visando garantir que os sistemas sejam não apenas funcionais e robustos, mas também economicamente viáveis e entregues dentro dos cronogramas estipulados. Essa área engloba a aplicação de uma abordagem disciplinada e quantificável ao desenvolvimento, operação e manutenção de software (Pressman & Maxim 2021). 

Além disso, a disciplina abarca um vasto conjunto de metodologias, ferramentas de apoio e processos técnicos desenhados para gerenciar a complexidade intrínseca à fabricação de produtos de software em escala industrial (Sommerville 2011). 

O contexto histórico que impulsionou o surgimento dessa área remonta à chamada "crise do software", identificada entre as décadas de 1960 e 1970. Nesse período, a indústria percebeu que a habilidade de codificação isolada era insuficiente para sustentar a demanda por sistemas complexos. Projetos dessa época eram frequentemente marcados por orçamentos estourados, não cumprimento de prazos e baixa confiabilidade, evidenciando a necessidade de uma abordagem de engenharia profissionalizada para a gestão do ciclo de vida do software (Pressman & Maxim 2021). 

# 2.1.1 Arquitetura de Sistemas Web Modernos

Diferentemente do paradigma monolítico clássico, as aplicações web atuais, como o sistema ConSec proposto, estruturam-se predominantemente sobre a segregação de fun-

ções entre o ambiente do cliente (frontend) e o do servidor (backend). Um modelo de como a arquitetura opera pode ser visualizado na Figura 2.1, 

O componente do servidor (backend) é implementado sob a forma de uma API (Application Programming Interface), alicerçada no padrão arquitetural REST (Representational State Transfer). Esse modelo estabelece diretrizes que fomentam o desacoplamento e a padronização das trocas de mensagens entre cliente e servidor (Fielding 2000). Nesse contexto, a abstração fundamental é o recurso, definido teoricamente como qualquer informação que possa ser nomeada e identificada individualmente (Fielding 2000). A API disponibiliza o acesso a esses recursos (que, neste projeto, materializam-se em entidades como Custos ou Usuários) através de endpoints (URLs específicas), que são manipulados pelo cliente mediante os métodos do protocolo HTTP (GET, POST, PUT, DELETE). 

Por sua vez, a interface do cliente (frontend) é construída como uma Single Page Application (SPA). Nessa abordagem, a estrutura base da aplicação (HTML, CSS e JavaScript) é transferida ao navegador em uma carga inicial única. As interações subsequentes dispensam o recarregamento total da página; a interface solicita dados à API sob demanda e atualiza o conteúdo visual dinamicamente, o que minimiza o tráfego de dados e o tempo de resposta percebido pelo usuário (latency). 


Figura 2.1: Exemplo de Arquitetura Cliente-Servidor


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/5b82d4d8ea841d3faf2784383c4bf9ac54c477b6644ba0c82768efc0f5b96153.jpg)



Fonte: Elaborado pelo próprio autor (2025).


# 2.2 Banco de Dados

Os Sistemas de Gerenciamento de Banco de Dados (SGBD) consistem em softwares especializados na custódia, administração e recuperação eficiente de grandes volumes de informações de maneira segura (Elmasri & Navathe 2011). No contexto de uma ferramenta de controle financeiro como o ConSec, a utilização de um SGBD é vital. Ela assegura pilares como a integridade (precisão e validade dos registros), o controle de concorrência (acesso simultâneo por diversos servidores) e a perenidade dos dados fiscais, superando as vulnerabilidades típicas do uso descentralizado de planilhas eletrônicas (Panko 2000). 

# 2.2.1 Modelo Relacional

A arquitetura relacional estrutura as informações do banco de dados através de "rela-ções", popularmente visualizadas como tabelas. Nesse paradigma, cada tabela é constitu-ída por tuplas (linhas) que representam os registros, e atributos (colunas) que definem as propriedades desses dados. O grande diferencial desse modelo reside na sua capacidade de conectar informações de tabelas distintas por meio de chaves estrangeiras (Foreign Keys), o que assegura a consistência e a integridade referencial de todo o sistema (Elmasri & Navathe 2011). No ConSec, essa lógica impede, por exemplo, que uma despesa seja lançada sem estar devidamente vinculada a um usuário existente e a uma categoria de custo válida. É possível visualizar um exemplo de como isso é feito na Figura 2.2 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/e6cad2c88f94271571912ffe0cc6b0a3737acdcf71750310d6bd731409cddbb1.jpg)



Figura 2.2: Diagrama Entidade-Relacionamento (DER) .



Fonte: Elaborado pelo próprio autor (2025).


# 2.2.2 Mapeamento Objeto-Relacional (ORM)

Existe uma discrepância natural entre a linguagem de programação do backend (C#), que opera sob o paradigma orientado a objetos, e o banco de dados, que segue o modelo relacional. Esse fenômeno é tecnicamente denominado "descasamento de impedância"(impedance mismatch) (Fowler et al. 2002). Para solucionar esse conflito, adota-se o Mapeamento Objeto-Relacional (ORM), como pode ser visto um modelo na Figura 2.3. Essa técnica funciona como uma camada intermediária que traduz os objetos do código 

(como uma instância da classe Custo) para registros relacionais no banco, e vice-versa, abstraindo a complexidade das consultas SQL diretas (Fowler et al. 2002). No desenvolvimento deste projeto, a ferramenta escolhida para realizar essa ponte foi o Entity Framework Core (EF Core), otimizando a produtividade ao permitir que o foco se mantivesse nas regras de negócio. 


Figura 2.3: Camada de Mapeamento Objeto-Relacional (ORM).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/84940f59cab2091197d6016b99cb54acb8d1925c4269faa4408b4e3bb8bd0bed.jpg)



Fonte: Elaborado pelo próprio autor (2025).


# 2.3 Acessibilidade Digital

A acessibilidade digital é a prática de projetar e desenvolver sistemas e conteúdos web de forma que possam ser utilizados por todas as pessoas, independentemente de suas habilidades físicas, motoras, visuais, auditivas ou cognitivas. É fundamental distinguir 

este conceito da Usabilidade. Enquanto a Usabilidade foca na eficiência e na satisfação do usuário-alvo durante a interação (Nielsen 1993), a Acessibilidade concentra-se em eliminar as barreiras que impedem o acesso e a operação do sistema por pessoas com deficiência (World Wide Web Consortium (W3C) 2023). 

No contexto de um sistema de controle interno como o ConSec, a aplicação dos princípios de acessibilidade garante que todos os servidores da secretaria, inclusive os com deficiência, possam operar a ferramenta e desempenhar suas funções. Esta abordagem é essencial para promover a inclusão digital e a autonomia produtiva no ambiente de trabalho. 

# 2.3.1 As Diretrizes WCAG

A referência global para a acessibilidade digital é estabelecida pelo World Wide Web Consortium (W3C), consolidada nas Diretrizes de Acessibilidade para Conteúdo Web (WCAG). Tais orientações organizam-se alicerçadas em quatro pilares essenciais, frequentemente referenciados pela sigla POUR: 

• Perceptível (Perceivable): É imperativo que os elementos da interface e as informações sejam dispostos de forma que os usuários consigam assimilá-los através dos sentidos. Na prática, isso demanda a inclusão de descrições textuais alternativas para mídias visuais e a aplicação de taxas de contraste cromático apropriadas para garantir a legibilidade. 

• Operável (Operable): A navegação e os mecanismos interativos da interface necessitam ser plenamente utilizáveis por qualquer indivíduo. O sistema requer compatibilidade total com comandos via teclado (sem depender exclusivamente do mouse), além de conceder ao usuário o tempo necessário para a leitura e interação com o conteúdo sem pressa. 

• Compreensível (Understandable): Tanto o conteúdo informativo quanto a opera-ção da interface devem ser de fácil entendimento cognitivo. Isso implica a utilização de textos claros e legíveis, bem como a construção de fluxos de navegação e funcionalidades que se comportem de forma previsível e consistente, evitando surpresas ao usuário. 

• Robusto (Robust): A estrutura do código deve possuir solidez suficiente para ser interpretada corretamente por uma vasta gama de agentes de usuário, o que inclui as tecnologias assistivas, como os leitores de tela. Tal característica é obtida, sobretudo, através da utilização rigorosa de HTML semântico e da conformidade com os padrões web vigentes, garantindo a compatibilidade futura. 

Na Figura 2.4 é possível visualizar de forma mais simples os quatrro princípios da acessibilidade 

Figura 2.4: Os quatro princípios da Acessibilidade (POUR) (World Wide Web Consortium (W3C) 2023). 

# Os Quatro Principios da Acessibilidade (POUR)

# Perceptivel

A informacäo deve ser apresentavel aos usuarios de formas que eles possam perceber (ex: alternativas em texto para imagens, legendas para videos, bom contraste). 

# Operävel

Os componentes da interface e a navegacäo devem ser operaveis (ex: funcionalidade completa via teclado, sem "armadilhas de teclado", tempo suficiente para leitura). 

# Compreensivel

A informacäo e a operacäo da interface devem ser compreensiveis (ex: texto legivel, operacäo previsivel, ajuda na correcäo de erros). 

# Robusto

O conteudo deve ser robusto o suficiente para ser interpretado por uma ampla variedade de tecnologias assistivas (ex: uso correto de HTML semäntico, WAI-ARIA). 

Fonte: Elaborado pelo próprio autor (2025). 

# 2.3.2 WAI-ARIA

Em aplicações ricas e dinâmicas, como as SPAs (desenvolvidas em Angular), o HTML semântico, embora fundamental, é frequentemente insuficiente para descrever componentes de interface complexos, como menus. A iniciativa Web Accessibility Initiative – Accessible Rich Internet Applications (WAI-ARIA) (W3C Web Accessibility Initiative 2018) preenche essa lacuna. Ela fornece um conjunto de atributos (como ‘role‘, ‘aria-label‘, ‘aria-required‘) que podem ser adicionados ao HTML para melhorar a semântica de componentes dinâmicos, tornando-os compreensíveis para tecnologias assistivas. 

# Capítulo 3

# Metodologia

A metodologia empregada neste trabalho adota um processo estruturado de engenharia de software para a concepção e desenvolvimento do sistema ConSec. A abordagem articula, desde a concepção, os três pilares teóricos centrais deste projeto: a arquitetura web moderna (separação Frontend/Backend), os princípios de design de banco de dados relacional e os critérios de acessibilidade digital (WCAG). Notavelmente, a acessibilidade foi tratada não como um adendo, mas como um requisito não-funcional fundamental, influenciando o design desde a fase inicial. 

A execução do projeto foi decomposta em etapas sequenciais e bem definidas, refletindo um fluxo de desenvolvimento lógico. Este percurso metodológico inicia-se na concepção abstrata do problema e na captura rigorosa dos requisitos (Funcionais e Não-Funcionais); transita pelo design da solução e pela arquitetura; segue para a implementa-ção técnica; e culmina na fase de Verificação e Validação (V&V). A adoção deste processo sequencial foi crucial para assegurar que os dois objetivos centrais do projeto, atender às demandas funcionais da Secretaria e garantir a conformidade com os requisitos de acessibilidade, fossem alcançados de forma integrada. 

Para tal, o projeto foi dividido nos seguintes componentes, que estruturam este capítulo: Levantamento e Modelagem de Requisitos; Design da Solução e Arquitetura do Sistema; Desenvolvimento e Implementação; e, por fim, Testes e Validação de Conformidade. 

# 3.1 Levantamento e Modelagem de Requisitos

A etapa inicial e mais crítica do projeto consistiu no levantamento de requisitos. Este processo foi conduzido por meio de entrevistas semiestruturadas com a gestão da Secretaria de Educação. O objetivo foi compreender o domínio do problema, identificando as deficiências e os gargalos do processo vigente. 

Identificou-se que o desafio central residia na dificuldade de organizar e rastrear os custos operacionais. Esse processo, anteriormente manual e descentralizado, gerava retrabalho e comprometia a tomada de decisão. Com base nesse diagnóstico, definiram-se os requisitos funcionais (RFs) do sistema. Estes requisitos foram então categorizados segundo os dois perfis de usuário (atores) identificados, detalhando suas respectivas permissões: 

# • Ator: Gestora (Admin)

RF01 Visualizar custos de forma agregada por meio de um dashboard gerencial. 

RF02 Visualizar, editar e excluir custos individuais lançados por qualquer funcioná- rio. 

RF03 Criar, editar e excluir "Temas"de custo (ex.: "Transporte", "Alimentação"). 

RF04 Criar, editar e desativar contas de "Funcionários", definindo seus perfis de acesso. 

RF05 Associar "Funcionários"a "Temas"específicos (relação N:M), definindo quais temas cada funcionário pode utilizar ao lançar um custo. 

# • Ator: Funcionário (Usuário Padrão)

RF06 Adicionar novos custos, associando-os a um tema previamente atribuído pela gestão (ver RF05). 

RF07 Informar os dados essenciais do custo: data, valor e descrição. 

RF08 Anexar, opcionalmente, um comprovante (imagem/PDF) ao registro do custo. 

RF09 Visualizar (apenas leitura) o histórico dos custos lançados pelo próprio usuá- rio. 

# Requisito Não-Funcional (RNF) Primário: Acessibilidade

Além dos requisitos funcionais (RFs), que definem o que o sistema deve fazer, foi estabelecido um requisito não-funcional (RNF) primário que define como o sistema deve operar: a aderência aos princípios de Acessibilidade Digital. Esta decisão foi crucial, pois tratou a acessibilidade não como um detalhe final ou um "adendo", mas como um pilar central do projeto, alinhado ao padrão internacional WCAG. 

Isso significa que o sistema foi projetado para ser utilizado por todos os servidores, independentemente de suas habilidades físicas, motoras, visuais ou cognitivas, aplicando na prática os conceitos fundamentados no Referencial Teórico. 

# 3.2 Design da Solução e Arquitetura

Com os requisitos e o planejamento de UI/UX definidos, a fase de design da solução focou em traduzir essas necessidades em uma arquitetura de software robusta, escalável e acessível, utilizando tecnologias web modernas. 

# Design da Experiência do Usuário (UI/UX) e Acessibilidade

Com os requisitos funcionais e os perfis de usuário definidos, iniciou-se a fase de design da interface (UI) e da experiência do usuário (UX). Esta etapa foi fundamental para traduzir os requisitos em protótipos de tela que fossem, simultaneamente, eficientes e acessíveis. O design de UX focou em fluxos de usuário distintos: 

• Fluxo do Funcionário: A prioridade foi a eficiência. Sendo o lançamento de custos ([RF06], [RF07], [RF08]) uma tarefa repetitiva, ele deveria ser o mais rápido 

e simples possível. Isso levou ao design de uma tela limpa, com um formulário objetivo e validação imediata. 

• Fluxo da Gestora: A prioridade foi a visualização de dados e o controle. A gestora analisa dados ([RF01]) e gerencia o sistema ([RF02], [RF03], [RF04], [RF05]). Isso levou ao design de um dashboard com gráficos para insights rápidos e tabelas densas, mas com capacidade de filtragem e busca, para o gerenciamento detalhado. 

Para o dashboard, em vez de apresentar apenas tabelas, o sistema foi desenhado para transformar dados brutos em visualizações gráficas (como gráficos de pizza ou barras), permitindo uma tomada de decisão fundamentada, conforme ilustrado na Figura 3.1. 


Figura 3.1: Transformação de dados brutos em insights visuais no Dashboard.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/3d363775c14c99f128c752c367ab75868dd9041142730a2ce8be36a7495f97ce.jpg)



Fonte: Elaborado pelo próprio autor (2025).


Este planejamento de UI/UX produziu protótipos de baixa fidelidade (wireframes) que definiram a estrutura de navegação, o layout das telas e a disposição dos componentes. Foi nesta fase que o RNF de acessibilidade começou a ser implementado no design, levantando questões como: "Como um usuário de leitor de tela navegará por este formulário?"ou "Este contraste de cores é suficiente?". 

O resultado dessa etapa de modelagem foi a consolidação dos artefatos de design: a arquitetura do sistema (Figura 3.2) e o Diagrama Entidade-Relacionamento (Figura 3.3), que define a estrutura do banco de dados. 

# 3.2.1 Arquitetura do Sistema

Conforme ilustrado na Figura 3.2, o sistema ConSec foi projetado no modelo arquitetural Cliente-Servidor. Esta abordagem contemporânea opõe-se ao design monolítico tradicional e fundamenta-se no princípio da separação de responsabilidades. 


Figura 3.2: Arquitetura Cliente-Servidor do sistema ConSec.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/6249ad9a883bdfb9b4c9271142e90cbe283bf65ab0f9b7f0cad0732e33fc932c.jpg)



Fonte: Elaborado pelo próprio autor (2025).


Na prática, o sistema é decomposto em duas aplicações distintas e desacopladas que se comunicam via rede: 

• Backend (Servidor): Construído sobre a plataforma .NET Core (C#) seguindo o padrão RESTful. Este componente centraliza o processamento das regras de ne-

gócio (incluindo os requisitos [RF01] a [RF09]) e gerencia a segurança através de autenticação JWT (JSON Web Token)e controle de permissões por perfil. A manipulação e persistência dos dados ficam a cargo do ORM Entity Framework Core, que dialoga com o banco de dados. A comunicação externa é realizada via protocolo HTTPS, disponibilizando endpoints que permitem ao cliente operar os recursos do sistema de maneira segura e padronizada. 

• Frontend (Cliente): Implementado como uma Single Page Application (SPA) utilizando o framework Angular (TypeScript). Nessa arquitetura, o navegador carrega a estrutura base da aplicação em uma única requisição inicial. A partir desse momento, a navegação torna-se fluida: a interface não recarrega a página inteira a cada ação, mas sim consome dados JSON da API do backend e atualiza dinamicamente apenas os elementos necessários da tela, garantindo uma experiência de usuário ágil e responsiva. 

Esta separação de responsabilidades é um pilar da engenharia de software moderna. Ela é fundamental, pois permite que as camadas de lógica de negócios (backend) e de apresentação (frontend) sejam desenvolvidas, testadas, atualizadas e escaladas de forma independente. 

# 3.2.2 Modelagem e Persistência de Dados

A persistência dos dados fundamentou-se no modelo relacional. O Diagrama Entidade-Relacionamento (DER), apresentado na Figura 3.3, demonstra como as informações são estruturadas. 


Figura 3.3: Diagrama Entidade-Relacionamento (DER) do ConSec.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/e765d28a4ee4797425971df7b94c80367a1de0f8115d90857075dc42a71e8e22.jpg)



Fonte: Elaborado pelo próprio autor (2025).


No esquema relacional do ConSec, a integridade referencial é uma prioridade. Por exemplo, a tabela ‘Custo‘ possui chaves estrangeiras que apontam para a tabela ‘Usuario‘ e para a tabela ‘TemaCusto‘, assegurando que um custo não pode ser registrado sem estar vinculado a um usuário e a um tema válidos. 

Para mediar a comunicação entre o backend orientado a objetos (C#) e este banco de dados relacional, foi utilizado o framework de Mapeamento Objeto-Relacional (ORM) Entity Framework Core (EF Core). 


Figura 3.4: Camada de Mapeamento Objeto-Relacional (ORM) no ConSec.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/c74713c9b295060894983055be2ec3a7a94511e78753b3392fc90461b285e187.jpg)



Fonte: Elaborado pelo próprio autor (2025).


O EF Core atua como uma camada de abstração (ver Figura 3.4) que resolve o "descasamento de impedância objeto-relacional". Isso permitiu que o desenvolvimento focasse na lógica de negócios, manipulando classes C# puras POCOs (Plain OLD CLR Object), como Custo.cs, Usuario.cs, Tema.cs e a tabela de junção FuncionarioTema.cs, enquanto o ORM se encarrega de traduzir essas operações em consultas SQL otimizadas. 

# 3.2.3 Implementação da Interface e Acessibilidade

O design das interfaces (UI/UX), planejado na etapa anterior, foi tecnicamente implementado nesta fase. A escolha pelo Angular não foi acidental; o framework é baseado em componentes, o que significa que a tela é construída em "blocos"modulares (como ../login/ ou ../cadastrar-custos/). Essa arquitetura facilita a aplicação dos prin-

cípios de acessibilidade de forma controlada e modular. 

O design seguiu os quatro princípios POUR (Perceptível, Operável, Compreensível e Robusto). Na prática, a implementação envolveu: 

• Perceptível e Robusto: Para garantir que o sistema fosse Robusto e funcionasse com tecnologias assistivas, a base do código foi o HTML semântico (uso correto de tags como <nav>, <main>, <button>). Isso garante que os leitores de tela entendam a estrutura da página, tornando o conteúdo Perceptível. 

• Operável: Foi assegurado que todas as interações do sistema (navegar por menus, preencher formulários, fechar janelas) pudessem ser realizadas $100 \%$ via teclado (usando ’Tab’, ’Shift+Tab’ e ’Enter’), essencial para usuários com deficiências motoras. 

• Compreensível: Para tornar o sistema Compreensível, foram utilizados atributos WAI-ARIA (ex.: role $: =$ "alert", aria-label) para fornecer contexto adicional a leitores de tela sobre componentes dinâmicos do Angular. 

# 3.3 Desenvolvimento e Implementação

A fase de desenvolvimento consistiu na codificação da arquitetura e dos requisitos definidos, materializando o design. O repositório do projeto foi estruturado para refletir a separação entre Frontend e Backend. 

# 3.3.1 Implementação do Backend (.NET)

No Backend (.NET), a lógica foi centralizada nos Controllers, que atuam como a camada de entrada da API, recebendo requisições HTTP, validando os dados encapsulados em DTOs (Data Transfer Objects), objetos destinados ao transporte de dados entre processos, e orquestrando a lógica de negócio. 

• Controllers/AuthController.cs: Gerencia a autenticação (endpoint de login e geração de JWT) e registro de usuários. 

• Controllers/UsuarioController.cs: Implementa endpoints para a Gestora gerenciar os funcionários. 

• Controllers/TemaCustoController.cs: Implementa o CRUD para as categorias de custo. 

• Controllers/CustoController.cs: Expõe endpoints para listagem e CRUD de custos. Aplica a lógica de permissão (RF02 vs RF08) verificando o perfil do usuá- rio. 

• Controllers/DashboardController.cs: Responsável por processar e agregar os dados de custos para o dashboard da Gestora. 

# 3.3.2 Implementação do Frontend (Angular)

No Frontend (Angular), a SPA foi modularizada em componentes: 

• ../login/: Componente de autenticação. 

• ../cadastrar-custos/: Formulário de cadastro de custos (RF05). 

• ../visualizar-custos/: Tabela de gerenciamento de custos para a Gestora. 

• ../gerenciar-funcionarios/ e ../gerenciar-temas/: Telas de administra-ção (CRUD). 

• ../dashboard/: Componente que renderiza os gráficos consumindo o DashboardController. 

• ../services/: Camada de abstração de chamadas HTTP (HttpClient). 

• ../guards/auth.guard.ts: Proteção de rotas para usuários não autenticados. 

# 3.4 Testes e Validação do Sistema

A etapa final da metodologia foi a de Verificação e Validação (V&V), destinada a verificar se o sistema ConSec atende aos requisitos funcionais e não funcionais. 

# 3.4.1 Testes Funcionais

Foram realizados testes funcionais manuais com base nos cenários de uso (requisitos). 

• Fluxo do Funcionário: Validação de login, criação de custos e restrições de acesso. 

• Fluxo da Gestora: Validação de login, visualização do dashboard, e gerenciamento completo (CRUD) de temas, usuários e custos. 

# 3.4.2 Auditoria de Acessibilidade

Para validar o RNF de Acessibilidade Digital, foi realizada uma auditoria híbrida: 

• Ferramentas Automáticas: Utilização de Lighthouse e WAVE para identificar problemas de baixo nível (contraste, alt text). 

• Testes Manuais: Verificação da navegabilidade via teclado e testes de legibilidade com leitores de tela, como o NVDA (NonVisual Desktop Access) para validar a semântica e os atributos WAI-ARIA. 

Os resultados dessas validações são discutidos no Capítulo 4. 

# Capítulo 4

# Resultados e Discussões

Este capítulo apresenta os resultados obtidos com a realização deste trabalho, divididos em duas perspectivas principais: a técnica, que demonstra as interfaces do sistema ConSec desenvolvido e sua conformidade com os requisitos de acessibilidade; e a prá- tica, que apresenta a consolidação integral e a análise crítica dos dados financeiros da Secretaria de Carnaúba dos Dantas referentes ao exercício de 2024. 

Todos os dados apresentados na segunda parte deste capítulo foram processados, armazenados e auditados pelo sistema desenvolvido, o que valida sua capacidade de atuar como uma ferramenta de Inteligência de Negócios (Business Intelligence) em ambiente de produção real. 

# 4.1 Apresentação do Sistema Desenvolvido

O desenvolvimento resultou em uma aplicação web funcional, responsiva e acessível. A interface final reflete os princípios de design focados na experiência do usuário e na clareza da visualização de dados, atendendo aos requisitos funcionais levantados. A seguir, são detalhadas as principais telas que compõem a solução. 

# 4.1.1 Dashboard Gerencial

A tela principal do sistema, acessível ao perfil de gestora, é o Dashboard (Figura 4.1). Esta interface cumpre o objetivo de transformar registros individuais em inteligência de negócio, exibindo totalizadores de saldo, despesas por categoria e gráficos que facilitam a compreensão imediata da execução orçamentária. 


Figura 4.1: Tela de Dashboard: Visão geral dos custos em tempo real.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/6b5d3f3a77567b56f8ac938b90dd13818ebaa703b00978be3361f710e07e50d1.jpg)



Fonte: Elaborado pelo autor (2025).


# 4.1.2 Módulo Operacional: Custos

O núcleo do sistema reside no lançamento e controle das despesas. Para isso, foram desenvolvidas interfaces distintas para a inserção (focada na agilidade) e para a auditoria (focada no detalhamento). 

# Lançamento de Custos

Para o perfil de funcionário, a interface de cadastro (Adicionar Custo), vista na Figura 4.2, priorizou a simplicidade. O formulário utiliza máscaras de entrada para valores monetários e seletores intuitivos para os temas, além de ser totalmente responsivo. 


Figura 4.2: Tela de Adicionar Custo: Formulário acessível e responsivo.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/06f9f2657ead38d972e7c26d174b7c87ca838da6120ca2a68aca2b9d3bad5660.jpg)



Fonte: Elaborado pelo autor (2025).


# Visualização e Auditoria

A tela de Visualizar Custos (Figura 4.3) apresenta os dados em formato tabular, permitindo à gestora filtrar despesas por período, tema ou funcionário. É nesta tela que ocorrem as ações de auditoria, garantindo a integridade dos dados financeiros. 


Figura 4.3: Tela de Visualizar Custos: Listagem tabular com opções de filtro e edição.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/c2d3270034194bc01f5b9dac0f8c08be11c30bee0ddf2beed709e38b66ee2d54.jpg)



Fonte: Elaborado pelo autor (2025).


# 4.1.3 Módulos Administrativos

Para garantir que o sistema seja flexível e não dependa de intervenção técnica para mudanças simples no dia a dia da Secretaria, foram implementadas telas de gerenciamento administrativo. 

# Gerenciamento de Funcionários

O controle de acesso é centralizado na interface da Figura 4.4, onde a gestora possui autonomia para cadastrar servidores, sendo possível criar, editar e excluir o servidor. 


Figura 4.4: Tela de Gerenciar Funcionários: Controle de acesso e perfis de usuário.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/d3112ca21d194761f8dd5b44e76035fb3b179fba768d88e75f45613f6acebcf7.jpg)



Fonte: Elaborado pelo autor (2025).


# Gerenciamento de Temas

O sistema permite a criação dinâmica de categorias de custo (Temas). Conforme a Figura 4.5, a gestora pode criar, editar ou excluir categorias, associando cores e ícones específicos. 


Figura 4.5: Tela de Gerenciar Temas: Personalização das categorias de despesa.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/fbee08956bd3b6febed0177a39adbb8aa9af690165fdbb8c47fc699ba14e21d9.jpg)



Fonte: Elaborado pelo autor (2025).


# Controle de Saldos

Para que o Dashboard exiba o saldo real, o módulo de Gerenciar Saldo (Figura 4.6) registra os aportes financeiros e orçamentos. 


Figura 4.6: Tela de Gerenciar Saldo: Registro de aportes e orçamentos.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/5235e9a3d85ade4de6b714735bfb8d21b2666b061c2b7af83a3d4bb3457fe37b.jpg)



Fonte: Elaborado pelo autor (2025).


# 4.2 Validação de Acessibilidade

A garantia da qualidade técnica do sistema foi realizada através de uma auditoria cruzada, utilizando ferramentas de referência no mercado para validação de conformidade com as diretrizes WCAG. 

# 4.2.1 Performance e Boas Práticas (Lighthouse)

Inicialmente, o sistema foi submetido à auditoria do Google Lighthouse (Figura 4.7), focando em métricas de desempenho e experiência do usuário. A análise destacou a eficiência no carregamento e a adesão às melhores práticas de desenvolvimento web. 


Figura 4.7: Pontuação de Acessibilidade e Boas Práticas (Lighthouse).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/48e40997e129679b2d97cc3694dfab798d15b8f5df34721167010e8ef6828bf0.jpg)



Fonte: Auditoria realizada via Google Chrome DevTools (2025).


# 4.2.2 Conformidade Semântica (WAVE)

Para uma validação mais profunda da estrutura semântica, utilizou-se a ferramenta WAVE (Web Accessibility Evaluation Tool). Conforme demonstrado na Figura 4.8, o sistema obteve resultado de excelência, registrando zero erros de acessibilidade e zero erros de contraste. 


Figura 4.8: Relatório de Conformidade Semântica (WAVE).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/1c235e933ecb9b0db3f183af9493b052303867aee8629f26f02cda2d4663ecf8.jpg)



Fonte: Auditoria realizada via extensão WAVE (2025).


Este resultado confirma a eficácia da implementação do HTML semântico e dos atributos WAI-ARIA, assegurando que a árvore de acessibilidade esteja limpa e correta para a interpretação por tecnologias assistivas, como leitores de tela. 

# 4.3 Estudo de Caso: Análise Financeira 2024

Uma vez validada a ferramenta técnica, o sistema ConSec foi utilizado para auditar e categorizar os dados reais da Secretaria. A apresentação a seguir segue uma estrutura analítica integrada: para cada centro de custo, apresentam-se os dados tabulares e gráficos, seguidos da discussão sobre os padrões identificados. 

# 4.3.1 Análise de Frota Própria

# Manutenção de Carros (Frota Leve)

Os custos operacionais da frota de carros de passeio estão sumarizados na Tabela 4.1 e na Figura 4.9. O sistema permitiu a decomposição detalhada das despesas, revelando que os picos orçamentários do segundo semestre não derivaram de um aumento no consumo de combustível, mas sim da incidência de manutenções corretivas. 

A análise dos dados de setembro $( \mathbf { R } \$ 6.370, 8 3 )$ indica que mais de $60 \%$ do custo mensal foi destinado a peças $( \mathbf { R \$ 2 . 4 6 1 , 7 1 } )$ ) e serviços de manutenção $( \mathbb { R } \mathbb { S } 1 . 3 9 9 , 2 0 )$ ). O padrão se repetiu em outubro, onde o gasto exclusivo com peças $( \mathbb { R } \$ 3.30 8 ,00 )$ ) superou o valor do abastecimento $( \mathbf { R \$ 2 . 6 4 3, 5 5 } )$ ), evidenciando o desgaste mecânico da frota no período. 

Em contrapartida, meses como janeiro e abril, compostos quase integralmente por custos de abastecimento, serviram para estabelecer a linha base de consumo operacional. O sistema também registrou a ausência de lançamentos em junho, um alerta automático que sugere a necessidade de auditoria sobre o fluxo de notas fiscais neste mês. 


Tabela 4.1: Carros (Combustível/Manutenção)


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Janeiro</td><td>995,44</td></tr><tr><td>Fevereiro</td><td>3.272,95</td></tr><tr><td>Março</td><td>1.784,41</td></tr><tr><td>Abril</td><td>2.144,98</td></tr><tr><td>Maio</td><td>3.521,91</td></tr><tr><td>Junho</td><td>0,00</td></tr><tr><td>Julho</td><td>3.564,38</td></tr><tr><td>Agosto</td><td>3.407,51</td></tr><tr><td>Setembro</td><td>6.370,83</td></tr><tr><td>Outubro</td><td>5.951,55</td></tr><tr><td>Novembro</td><td>5.266,78</td></tr><tr><td>Dezembro</td><td>1.679,09</td></tr><tr><td>Total</td><td>37.959,83</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/96d3e7d8e77e31aaedbf4ce975970eccd668e1d6e019d57259ecb23ffb0f9f81.jpg)



Figura 4.9: Gráfico: Carros



Fonte: Elaborado pelo autor.


# Manutenção de Ônibus (Frota Pesada)

Os dados referentes à frota de transporte escolar estão detalhados na Tabela 4.2 e na Figura 4.10. O custo total acumulado foi de $\mathtt { R } \$ \mathtt { S }$ 107.958,91, valor aproximadamente três vezes superior ao da frota de carros. 

O detalhamento permitido pelo sistema possibilitou identificar a natureza dos custos nos meses de maior despesa. Em março (R$ 21.079,91), verificou-se que a maior parte do valor foi destinada à aquisição de peças $( \mathrm { R } \$ 16.40 8,9 2 )$ , enquanto o abastecimento se manteve na média. Já em outubro $( \mathrm { R } \$ 20 .115,40 )$ , o aumento foi impulsionado pela contratação de serviços de manutenção $( \mathrm { R } \$ 10.389,00 )$ ) somada à compra de peças. Essas informações permitem distinguir gastos rotineiros de intervenções corretivas pontuais. 


Tabela 4.2: Ônibus Escolares


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Janeiro</td><td>3.531,51</td></tr><tr><td>Fevereiro</td><td>8.421,74</td></tr><tr><td>Março</td><td>21.079,91</td></tr><tr><td>Abril</td><td>11.397,11</td></tr><tr><td>Maio</td><td>6.971,52</td></tr><tr><td>Junho</td><td>4.040,78</td></tr><tr><td>Julho</td><td>5.099,62</td></tr><tr><td>Agosto</td><td>11.814,32</td></tr><tr><td>Setembro</td><td>5.171,80</td></tr><tr><td>Outubro</td><td>20.115,40</td></tr><tr><td>Novembro</td><td>5.722,24</td></tr><tr><td>Dezembro</td><td>4.592,96</td></tr><tr><td>Total</td><td>107.958,91</td></tr></table>


Figura 4.10: Gráfico: Ônibus Escolares


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/ae4e9628af97f57cb5f4848ab315e1dd2dec662adc21c3a4f014b320ec148b40.jpg)



Fonte: Elaborado pelo autor.


# 4.3.2 Logística de Transporte Terceirizado

# Transporte Escolar (Rotas)

O pagamento das rotas terceirizadas segue rigorosamente o calendário letivo, conforme evidenciado na Tabela $4 . 3 \mathrm { e }$ na Figura 4.11. O sistema não apenas validou a redução de custos nos meses de férias (Janeiro zerado) e recesso (redução em Julho/Dezembro), mas também permitiu auditar a distribuição dos pagamentos por prestador de serviço. 

A análise identificou uma reestruturação logística no início do segundo semestre. O sistema registrou que o prestador José Franceilton, ativo com pagamentos regulares até junho, cessou suas atividades no sistema a partir de julho. Correlacionado a isso, os dados evidenciaram um aumento expressivo nos repasses ao prestador Plínio a partir de agosto (saltando da casa de $\mathtt { R } \$ \Phi$ 14 mil para aproximadamente $\mathrm { R } \$ 20\mathrm { \ m i l }$ ), indicando a absorção das rotas vacantes e validando a capacidade da ferramenta de rastrear alterações contratuais dinâmicas. 


Tabela 4.3: Transporte Terceirizado


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Janeiro</td><td>0,00</td></tr><tr><td>Fevereiro</td><td>16.767,22</td></tr><tr><td>Março</td><td>29.662,20</td></tr><tr><td>Abril</td><td>38.849,30</td></tr><tr><td>Maio</td><td>37.159,80</td></tr><tr><td>Junho</td><td>30.181,24</td></tr><tr><td>Julho</td><td>20.873,64</td></tr><tr><td>Agosto</td><td>35.324,96</td></tr><tr><td>Setembro</td><td>37.286,08</td></tr><tr><td>Outubro</td><td>30.658,48</td></tr><tr><td>Novembro</td><td>33.119,44</td></tr><tr><td>Dezembro</td><td>19.203,36</td></tr><tr><td>Total</td><td>555.986,80</td></tr></table>


Figura 4.11: Gráfico: Transporte Escolar


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/4606cbd75bf0cfd5d0cc8a41107f624dc2ec6bf6999a30e3b27d971b5bc78723.jpg)



Fonte: Elaborado pelo autor.


# Auxílio Transporte Universitário

A execução financeira do subsídio universitário está detalhada na Tabela 4.4 e na Figura 4.12. Diferentemente dos gastos com oficinas, que variam muito, esta despesa caracteriza-se pela estabilidade. O sistema permitiu monitorar o fluxo de caixa de março a dezembro, validando a integridade dos 10 repasses mensais realizados, que totalizaram $\mathrm { R } \$ 229.965,00$ . 

A ferramenta de análise demonstrou uma consistência orçamentária robusta, com uma variação inferior a $5 \%$ entre o maior valor (R$ 23.195,00 em março/junho) e o menor $( \mathrm { R } \$ 22.1 45 , 00 e m$ novembro/dezembro). Os dados evidenciaram uma leve tendência de queda nos valores a partir de agosto, refletindo a atualização dinâmica do cadastro de beneficiários devido à saída natural de alunos concluintes ou desistentes ao longo do ano letivo. 


Tabela 4.4: Auxílio Transporte


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Março</td><td>23.195,00</td></tr><tr><td>Abril</td><td>22.995,00</td></tr><tr><td>Maio</td><td>22.945,00</td></tr><tr><td>Junho</td><td>23.195,00</td></tr><tr><td>Julho</td><td>23.125,00</td></tr><tr><td>Agosto</td><td>22.645,00</td></tr><tr><td>Setembro</td><td>22.170,00</td></tr><tr><td>Outubro</td><td>22.170,00</td></tr><tr><td>Novembro</td><td>22.145,00</td></tr><tr><td>Dezembro</td><td>22.145,00</td></tr><tr><td>Total</td><td>229.965,00</td></tr></table>


Figura 4.12: Gráfico: Auxílio Transporte


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/ffef37a498a4f068491e435b7b1833d39ba6430de72c319634a6167448a80504.jpg)



Fonte: Elaborado pelo autor.


# 4.3.3 Infraestrutura

O centro de custo de Infraestrutura representou o maior volume financeiro do ano $( \mathbb { R } \$ 2, 6$ milhões) e, simultaneamente, a maior volatilidade, conforme evidenciado na Tabela 4.5 e na Figura 4.13. O sistema ConSec foi fundamental para entender essa instabilidade, permitindo o rastreamento dos pagamentos vinculados a medições de obras de engenharia. 

A auditoria dos dados de março (pico de R$ 463.250,31) revelou que o montante resultou da coincidência de pagamentos a dois grandes prestadores de serviço: a BBC Construtora $( \mathrm { R } \$ 300 .546,26 )$ referente a obras no ensino fundamental, e a empresa Judson G. da Silva $( \mathbf { R } \$ 162. 7 7 4, 0 0 )$ $\mathrm { R } \$ 1$ para obras no ensino infantil. Da mesma forma, o pico de 

maio $( \mathrm { R } \$ 38 8 .58 4,25 )$ refletiu novas medições simultâneas destes mesmos contratos $( \mathtt { R } \$ $ 180 mil e $\mathtt { R } \$ \mathtt { S }$ 207 mil, respectivamente). 

Por outro lado, o sistema registrou corretamente o valor zerado em julho, validando a ausência de medições faturadas neste período. Essa visibilidade detalhada, distinguindo custos fixos operacionais de grandes desembolsos contratuais, é crucial para a gestão do fluxo de caixa municipal, permitindo prever que meses de "silêncio financeiro"geralmente precedem meses de grandes liquidações. 


Tabela 4.5: Infraestrutura e Obras


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Janeiro</td><td>81.108,64</td></tr><tr><td>Fevereiro</td><td>139.025,61</td></tr><tr><td>Março</td><td>463.250,31</td></tr><tr><td>Abril</td><td>91.572,45</td></tr><tr><td>Maio</td><td>388.584,25</td></tr><tr><td>Junho</td><td>304.133,59</td></tr><tr><td>Julho</td><td>0,00</td></tr><tr><td>Agosto</td><td>175.141,54</td></tr><tr><td>Setembro</td><td>200.084,76</td></tr><tr><td>Outubro</td><td>180.094,98</td></tr><tr><td>Novembro</td><td>399.826,34</td></tr><tr><td>Dezembro</td><td>210.200,00</td></tr><tr><td>Total</td><td>2.633.022,47</td></tr></table>


Figura 4.13: Gráfico: Infraestrutura


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/c3b86c18f8add9f56bc85cf5ae5b2d66f74c6bc5832b12d7ae2dfc1a694f7558.jpg)



Fonte: Elaborado pelo autor.


# 4.3.4 Consumo e Insumos

# Água Potável

O monitoramento do fornecimento de água mineral e potável é apresentado na Tabela 4.6 e na Figura 4.14. A granularidade dos dados processados pelo sistema permitiu uma auditoria setorial, distinguindo o consumo das unidades de ensino do consumo administrativo. 

Essa distinção foi crucial para validar o comportamento da despesa nos meses de recesso. Em janeiro, o sistema registrou consumo apenas na Secretaria $\left( \mathrm { R } \$ 43,20 \right)$ , confirmando que não houve desperdício nas escolas fechadas. Da mesma forma, a queda global observada em julho foi impulsionada exclusivamente pelas reduções no Ensino Fundamental (queda de $40 \%$ ) e Infantil (queda de $45 \%$ ), enquanto os setores administrativos (Secretaria) e de suporte (AEE) mantiveram seus padrões de consumo, refletindo a continuidade do expediente interno durante as férias escolares. 


Tabela 4.6: Água Potável


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Janeiro</td><td>43,20</td></tr><tr><td>Fevereiro</td><td>3.272,40</td></tr><tr><td>Março</td><td>3.530,20</td></tr><tr><td>Abril</td><td>4.060,20</td></tr><tr><td>Maio</td><td>3.897,40</td></tr><tr><td>Junho</td><td>3.422,80</td></tr><tr><td>Julho</td><td>2.107,60</td></tr><tr><td>Agosto</td><td>4.253,60</td></tr><tr><td>Setembro</td><td>4.274,40</td></tr><tr><td>Outuro</td><td>3.348,80</td></tr><tr><td>Novembro</td><td>3.474,00</td></tr><tr><td>Total</td><td>35.684,60</td></tr></table>


Figura 4.14: Gráfico: Água Potável


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/3101057f3dd1180bd21178d8f7d95b3424ade2d727b576d8e8c20ccd35ffb237.jpg)



Fonte: Elaborado pelo autor.


# Gás de Cozinha

A evolução dos custos com gás de cozinha está apresentada na Tabela 4.7 e na Figura 4.15. A granularidade dos dados no sistema permitiu decompor a despesa final em suas duas variáveis fundamentais: oscilação de preço unitário e volume de demanda setorial. 

A auditoria dos dados explicou o pico de custos observado em outubro $( \mathbf { R \$ 2 . 0 8 2 , 0 0 } )$ . O sistema detectou um reajuste no preço do insumo (que variou de $\mathtt { R } \$ \mathtt { S }$ 112,00 no primeiro semestre para $\mathtt { R } \$ \mathtt { S }$ 118,00 neste período) concomitante a um aumento abrupto de consumo nas unidades de ensino. Em outubro, apenas o Ensino Fundamental $( \mathbf { R } \$ 1 .03 8 , 0 0 )$ e o Infantil $( \mathbf { R } \$ 926,00 )$ consumiram o dobro do registrado no mês anterior, correlacionado provavelemente a eventos do calendário escolar (Dia das Crianças). Já a análise do mês de abril revela um padrão de consumo similar, indicando a sazonalidade da demanda. 


Tabela 4.7: Gás de Cozinha


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Fevereiro</td><td>816,00</td></tr><tr><td>Março</td><td>448,00</td></tr><tr><td>Abril</td><td>1.680,00</td></tr><tr><td>Maio</td><td>1.456,00</td></tr><tr><td>Junho</td><td>1.232,00</td></tr><tr><td>Julho</td><td>1.120,00</td></tr><tr><td>Agosto</td><td>1.239,00</td></tr><tr><td>Setembro</td><td>1.017,00</td></tr><tr><td>Outuro</td><td>2.082,00</td></tr><tr><td>Novembro</td><td>2.006,00</td></tr><tr><td>Total</td><td>13.096,00</td></tr></table>


Figura 4.15: Gráfico: Gás de Cozinha


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/029806b492492d38c697b97df5620687875b00605b3fd7bccde5e9407eb1e70e.jpg)



Fonte: Elaborado pelo autor.


# Material de Limpeza

A execução financeira desta rubrica, apresentada na Tabela 4.8 e na Figura 4.16, difere das despesas de consumo contínuo. O sistema validou a estratégia de "gestão de estoque"da Secretaria, caracterizada por grandes aquisições pontuais (concentradas em abril, junho, outubro e novembro) intercaladas por períodos de ausência de movimenta-ção financeira. 

Adicionalmente, a auditoria setorial permitiu rastrear o destino final dos insumos. Os dados evidenciara mque os recursos foram integralmente alocados nas unidades de ensino (Ensino Infantil e Fundamental). A ausência de registros de custo para os setores administrativos (Secretaria e AEE) nesta categoria indica uma priorização dos recursos 

para a atividade-fim (as escolas) ou um modelo de distribuição centralizada que desonera o centro administrativo. 


Tabela 4.8: Material de Limpeza


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Abril</td><td>9.092,70</td></tr><tr><td>Junho</td><td>7.499,33</td></tr><tr><td>Outubro</td><td>4.648,14</td></tr><tr><td>Novembro</td><td>4.997,08</td></tr><tr><td>Total</td><td>26.237,25</td></tr></table>


Figura 4.16: Gráfico: Material de Limpeza


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/b928652daea201b123c445bfee5e0d39e996ab904c73910aeac13b6fec9eba27.jpg)



Fonte: Elaborado pelo autor.


# 4.3.5 Auditoria de Utilitários (Concessionárias)

# Energia Elétrica (COSERN)

A análise da eficiência energética, detalhada na Tabela 4.9 e na Figura 4.17, demonstra a capacidade do sistema de correlacionar o consumo financeiro com a atividade operacional. A ferramenta permitiu segregar os custos por unidade consumidora, identificando o Ensino Fundamental como o centro de custo de maior impacto, responsável por cerca de $70 \%$ do valor total nos meses letivos. 

O sistema validou matematicamente o impacto do calendário escolar nas contas pú- blicas. Comparando-se o pico de atividade em maio ( $\mathrm { R } \$ 1$ 10.232,54 com o mês de férias em janeiro $( \mathbf { R \$ 4 . 5 3 4, 3 2 } )$ , observa-se uma redução de mais de $50 \%$ . O detalhamento setorial mostra que essa economia advém quase exclusivamente das escolas: o consumo do Ensino Fundamental caiu de $\mathrm { R } \$ 7 . 101 ,35$ (maio) para $\mathrm { R \$ 3.5 35,14 }$ (janeiro). 

Em contrapartida, o sistema registrou que o consumo administrativo (Secretaria) mantevese estável e operante mesmo nos meses de recesso escolar (média de $\mathtt { R } \$ \mathtt { S }$ 300,00 a $\mathtt { R } \$ \mathtt { S }$ 400,00), evidenciando a continuidade dos serviços de gestão. 


Tabela 4.9: Energia Elétrica (COSERN)


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Janeiro</td><td>4.534,32</td></tr><tr><td>Fevereiro</td><td>9.634,12</td></tr><tr><td>Março</td><td>5.257,22</td></tr><tr><td>Abril</td><td>7.357,09</td></tr><tr><td>Maio</td><td>10.232,54</td></tr><tr><td>Junho</td><td>8.252,29</td></tr><tr><td>Julho</td><td>4.416,82</td></tr><tr><td>Agosto</td><td>4.356,41</td></tr><tr><td>Setembro</td><td>7.419,88</td></tr><tr><td>Outuro</td><td>3.150,00</td></tr><tr><td>Novembro</td><td>4.245,12</td></tr><tr><td>Total</td><td>68.855,81</td></tr></table>


Figura 4.17: Gráfico: Energia Elétrica


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/a7a5e83c46a66316124c32e2734f5897f9c922ff2179a1a074bca05efd6fcfbf.jpg)



Fonte: Elaborado pelo autor.


# Água e Esgoto (CAERN)

O monitoramento do consumo de água e esgoto está detalhado na Tabela 4.10 e na Figura 4.18. A auditoria setorial realizada pelo sistema identificou o Ensino Fundamental como o centro de custo predominante, respondendo individualmente por cerca de $70 \%$ da fatura nos meses de maior atividade. 

A análise temporal validou a correlação direta entre a despesa e o calendário escolar. O pico de consumo registrado em maio $\mathrm { R } \$ 1$ 1.121,50) foi impulsionado pelo pleno funcionamento das unidades de ensino, com o Fundamental consumindo R$ 783,22. Em contraste, o sistema explicou a queda abrupta em julho $( \mathrm { R } \$ 271,56)$ $\mathrm { R } \$ 1$ : com o recesso escolar, o consumo do Ensino Fundamental despencou para R$ 157,83 e o do Infantil para $\mathtt { R } \$ \mathtt { S }$ 51,16, comprovando que a variação do custo é operacional e não decorrente de desperdí- cios estruturais. 


Tabela 4.10: Água (CAERN)


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Janeiro</td><td>520,81</td></tr><tr><td>Fevereiro</td><td>616,59</td></tr><tr><td>Março</td><td>476,40</td></tr><tr><td>Abril</td><td>797,40</td></tr><tr><td>Maio</td><td>1.121,50</td></tr><tr><td>Junho</td><td>667,00</td></tr><tr><td>Julho</td><td>271,56</td></tr><tr><td>Agosto</td><td>905,16</td></tr><tr><td>Setembro</td><td>1.069,50</td></tr><tr><td>Outubro</td><td>651,81</td></tr><tr><td>Novembro</td><td>724,26</td></tr><tr><td>Total</td><td>7.821,99</td></tr></table>


Figura 4.18: Gráfico: Água (CAERN)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/e41be476f34b7a35aa932d2b37f2a8b8641b983f112af58476516598bfe52fa5.jpg)



Fonte: Elaborado pelo autor.


# 4.3.6 Alimentação Escolar

# Alimentos (Atacado)

A gestão da merenda escolar, detalhada na Tabela 4.11 e na Figura 4.19, representa um dos maiores volumes financeiros da Secretaria. A granularidade do sistema permitiu a análise das despesas por nível de ensino, identificando o Ensino Fundamental como o maior centro de custo, absorvendo consistentemente cerca de $60 \%$ do orçamento mensal desta rubrica (oscilando entre $\mathtt { R } \$ \mathtt { S }$ 16 mil e $\mathtt { R } \$ \Phi$ 20 mil nos meses letivos). 

A auditoria dos dados permitiu interpretar as oscilações atípicas. A queda observada em julho (R$ 19.584,87) refletiu o recesso escolar, com uma redução acentuada no consumo da Pré-escola (queda de $50 \%$ em relação a junho). Já a retração em outubro $( \mathbb { R } \mathbb { S }$ 16.766,27), o menor valor do ano letivo, não indicou falta de insumos, mas sim uma estratégia de gestão de estoque: os altos volumes de compra registrados em agosto $( \mathbb { R } \$ \mathbb { S }$ 33.491,50) e setembro $( \mathrm { R } \$ 30.227,0 1 )$ ) garantiram o abastecimento das unidades, reduzindo a necessidade de aquisições no mês seguinte. 


Tabela 4.11: Alimentos Atacado


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Fevereiro</td><td>27.481,97</td></tr><tr><td>Março</td><td>31.760,10</td></tr><tr><td>Abril</td><td>23.901,79</td></tr><tr><td>Maio</td><td>29.235,67</td></tr><tr><td>Junho</td><td>28.219,87</td></tr><tr><td>Julho</td><td>19.584,87</td></tr><tr><td>Agosto</td><td>33.491,50</td></tr><tr><td>Setembro</td><td>30.227,01</td></tr><tr><td>Outuro</td><td>16.766,27</td></tr><tr><td>Novembro</td><td>32.830,03</td></tr><tr><td>Total</td><td>273.499,08</td></tr></table>


Figura 4.19: Gráfico: Alimentos Atacado


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/c0aa3926b42db6886943d5945387606b9491952190afe8bde6821829985feb27.jpg)



Fonte: Elaborado pelo autor.


# Agricultura Familiar

O monitoramento das aquisições da Agricultura Familiar, apresentado na Tabela 4.12 e na Figura 4.20, destaca-se pela tendência de crescimento sustentado no segundo semestre. O sistema permitiu uma auditoria cruzada com os dados de "Alimentos Atacado", revelando um comportamento divergente e estratégico. 

Enquanto as compras de supermercado caíram em julho devido ao recesso, os repasses à agricultura familiar mais que dobraram em relação a junho (saltando de ${ \mathrm { R } } \$ 3.139,9 9$ para $\mathtt { R } \$ \mathtt { S }$ 6.673,59). O detalhamento setorial mostra que esse aumento foi impulsionado pelo Ensino Fundamental (que quadruplicou suas compras para $\mathrm { R } \$ 4.027,94$ ) e pela Creche. Esse dado valida a eficácia do sistema em monitorar o cumprimento das cotas obrigatórias do PNAE (Programa Nacional de Alimentação Escolar), garantindo a continuidade do apoio ao produtor local mesmo em períodos de baixa atividade escolar. 

O pico anual registrado em agosto $( \mathrm { R } \$ 14.776,18 )$ também foi auditado pelo sistema, que identificou a primeira ocorrência de compras para o setor AEE (Atendimento Educacional Especializado) neste mês $( \mathbb { R } \mathbb { S } \ 6 2 2 , 0 2 )$ $\mathrm { R } \$ 1$ , sinalizando a expansão da política de alimentação saudável para todas as modalidades de ensino. 


Tabela 4.12: Agricultura Familiar


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Fevereiro</td><td>2.132,79</td></tr><tr><td>Março</td><td>3.585,81</td></tr><tr><td>Abril</td><td>4.275,42</td></tr><tr><td>Maio</td><td>4.006,33</td></tr><tr><td>Junho</td><td>3.139,99</td></tr><tr><td>Julho</td><td>6.673,59</td></tr><tr><td>Agosto</td><td>14.776,18</td></tr><tr><td>Setembro</td><td>6.373,49</td></tr><tr><td>Outubro</td><td>8.208,17</td></tr><tr><td>Novembro</td><td>9.917,33</td></tr><tr><td>Total</td><td>63.089,10</td></tr></table>


Figura 4.20: Gráfico: Agricultura Familiar


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/b2a5c05e7330c9cbd93652e9755160354dff58e8cec9126fcf78ce324de30613.jpg)



Fonte: Elaborado pelo autor.


# 4.3.7 Investimentos e Serviços Diversos

# Material de Expediente e Mobiliário

A análise financeira desse gasto, apresentada na Tabela 4.13 e na Figura 4.21, exige uma distinção clara entre custeio e investimento. O sistema ConSec permitiu segregar essas naturezas de despesa através da auditoria de credores, revelando que os picos de execução não se referem a material de consumo. 

A auditoria dos dados de outubro $( \mathrm { R } \$ 18 6 .05 7,00 )$ e dezembro $( \mathbf { R } \$ 710.8 7 4,20 )$ identificou que os pagamentos foram destinados à empresa APFORM MOBILIÁRIO, caracterizando aquisição de patrimônio permanente (mobiliário escolar) e não despesa corrente. 

Mais do que isso, o sistema rastreou a alocação estratégica do recurso: o aporte massivo de dezembro foi destinado integralmente ao Ensino Infantil, evidenciando uma política de modernização focada nas creches, enquanto os meses com valores baixos (como maio, R$ 296,15) representam o consumo rotineiro de itens de escritório. 


Tabela 4.13: Material de Expediente


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Abril</td><td>1.751,85</td></tr><tr><td>Maio</td><td>296,15</td></tr><tr><td>Junho</td><td>8.986,00</td></tr><tr><td>Julho</td><td>5.919,20</td></tr><tr><td>Setembro</td><td>4.337,10</td></tr><tr><td>Outubro</td><td>186.057,00</td></tr><tr><td>Novembro</td><td>20.104,15</td></tr><tr><td>Dezembro</td><td>710.874,20</td></tr><tr><td>Total</td><td>938.325,65</td></tr></table>


Figura 4.21: Gráfico: Material de Expediente


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/e74ff54d7d7736bad20750978e3c0906b24fa7c653737cbe3b98c9c187838aef.jpg)



Fonte: Elaborado pelo autor.


# Esporte Educacional

A execução financeira desta rubrica, apresentada na Tabela 4.14 e na Figura 4.22, caracteriza-se pela pontualidade dos gastos. O sistema ConSec permitiu distinguir claramente entre investimentos estruturantes e custos de participação em eventos, validando a alocação dos recursos conforme o calendário esportivo. 

A auditoria do pico de março $( \mathbf { R } \mathbb { S } 4 5 . 0 2 2 , 1 2 )$ identificou que se tratou de uma aquisição única anual de material esportivo para as escolas. O detalhamento do sistema permitiu, inclusive, rastrear a composição do custeio: parte proveniente do VAAT (Valor 

Aluno Ano Total - $\mathrm { R } \$ 27 .264,12 )$ e parte de Recursos Próprios (R$ 17.758,00). Já o gasto registrado em novembro $( \mathrm { R \$ 3 . 8 2 5 , 0 0 } )$ foi corretamente classificado pelo sistema como despesa de evento, referente especificamente às inscrições e compra de medalhas/troféus para o "Seridosão", demonstrando a capacidade da ferramenta de registrar o destino final do recurso. 


Tabela 4.14: Esporte Educacional


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Março</td><td>45.022,12</td></tr><tr><td>Novembro</td><td>3.825,00</td></tr><tr><td>Total</td><td>48.847,12</td></tr></table>


Figura 4.22: Gráfico: Esporte Educacional


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/e424c433329a21312cbb1a73ef8652889b85f886d9a15c22137628d15a2f6a2f.jpg)



Fonte: Elaborado pelo autor.


# Viagens Licitadas

O monitoramento das despesas com deslocamentos, detalhado na Tabela 4.15 e na Figura 4.23, apresenta uma tendência de alta no encerramento do exercício. A capacidade de auditoria do sistema ConSec permitiu identificar a centralização da execução dos serviços em um prestador principal (GEIZA), responsável por mais de $98 \%$ do volume financeiro processado a partir de abril. 

A ferramenta foi crucial para entender a composição dos picos de novembro $( \mathbb { R } \$ \mathbb { S }$ 10.176,67) e dezembro $( \mathrm { R } \$ 11 . 70 8,32 )$ . Ao contrário do primeiro semestre, marcado por eventos pontuais (como os deslocamentos isolados para Natal e Mossoró), o sistema registrou uma intensificação da frequência de viagens no final do ano, com três pagamentos distintos processados em cada um dos últimos dois meses. Essa granularidade de dados afasta a hipótese de superfaturamento unitário, justificando o aumento do custo total pelo maior volume de demandas administrativas típicas do fechamento de ano fiscal. 


Tabela 4.15: Viagens Licitadas


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Março</td><td>676,75</td></tr><tr><td>Abril</td><td>2.500,00</td></tr><tr><td>Maio</td><td>3.700,00</td></tr><tr><td>Junho</td><td>2.730,00</td></tr><tr><td>Julho</td><td>6.445,00</td></tr><tr><td>Agosto</td><td>4.030,00</td></tr><tr><td>Setembro</td><td>6.490,00</td></tr><tr><td>Outubro</td><td>3.980,00</td></tr><tr><td>Novembro</td><td>10.176,67</td></tr><tr><td>Dezembro</td><td>11.708,32</td></tr><tr><td>Total</td><td>52.436,74</td></tr></table>


Figura 4.23: Gráfico: Viagens Licitadas


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/d3dfb2385f9c7a6e20dd9aa72aa7d5acb888466da5516dbcd7d029de1d792a6a.jpg)



Fonte: Elaborado pelo autor.


# Projetos Pedagógicos

A categoria de Projetos Pedagógicos, detalhada na Tabela 4.16 e na Figura 4.24, apresentou o segundo maior volume financeiro do ano. A capacidade de auditoria analítica do sistema foi fundamental para entender a natureza dessas despesas, que variaram de contratações artísticas a grandes aportes de capital. 

O sistema permitiu qualificar os picos de investimento. Em março $( \mathrm { R } \$ 38 7 . 93 8 ,00 )$ , identificou-se a aplicação de recursos em tecnologia educacional (Projeto Cinema 3D) e materiais para o AEE. Em agosto, o sistema rastreou o financiamento de atividades cívico-culturais (fanfarras e coreógrafos) preparatórias para o 7 de setembro. 

Contudo, a maior contribuição da ferramenta foi a transparência dada ao pico de dezembro $( \mathrm { R } \$ 1.195.180,10 )$ $\mathrm { R } \$ 1$ . O sistema desagregou este montante expressivo em quatro investimentos estruturantes distintos: aquisição de mobiliário escolar $( \mathbf { R \Phi } 7 1 0 . 8 7 4 , 2 0 )$ , compra de material didático $( \mathrm { R \$ 156.000 ,00 } )$ ), confecção de atlas municipais $( \mathsf { R S 8 9 . 5 0 0 } , 0 0 )$ 0 e execução do Projeto Rever $( \mathrm { R } \$ 23 8 . 805,90 )$ ). Essa rastreabilidade comprova que os recursos foram convertidos em ativos tangíveis e intangíveis para a rede de ensino. 


Tabela 4.16: Projetos Pedagógicos


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Fevereiro</td><td>7.000,00</td></tr><tr><td>Março</td><td>387.938,00</td></tr><tr><td>Abril</td><td>206.850,50</td></tr><tr><td>Julho</td><td>15.370,00</td></tr><tr><td>Agosto</td><td>15.521,13</td></tr><tr><td>Setembro</td><td>12.505,00</td></tr><tr><td>Outubro</td><td>186.057,20</td></tr><tr><td>Novembro</td><td>15.255,00</td></tr><tr><td>Dezembro</td><td>1.195.180,10</td></tr><tr><td>Total</td><td>1.826.849,50</td></tr></table>


Figura 4.24: Gráfico: Projetos Pedagógicos


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/4b4bb61594bbdc4a50c0e18d64f574aca10371729b16062d66b6a10a16b8fc23.jpg)



Fonte: Elaborado pelo autor.


# Sistemas e Assessoria (SIGEDUC)

A execução financeira dos serviços de tecnologia e suporte administrativo, apresentada na Tabela 4.17 e na Figura 4.25, caracteriza-se pela alta previsibilidade. A granularidade dos dados no sistema permitiu decompor o custo mensal fixo $( \mathbf { R \$ 4 . 29 4, 9 0 } )$ ) em 

suas três vertentes contratuais: licenciamento de software (SIGEDUC - $\mathtt { R } \$ \mathtt { S }$ 1.717,00), prestação de serviços de assessoria (R$ 2.500,00) e despesas de telefonia corporativa $( \mathbb { R } \mathbb { S }$ 77,90). 

Essa capacidade de rastreamento detalhado foi essencial para auditar as variações ocorridas no encerramento do exercício. O sistema identificou que o leve aumento registrado em novembro $( \mathbf { R \$ 4 . 3 6 1 } , 9 0 )$ decorreu especificamente de um reajuste no contrato do SIGEDUC, que passou para R$ 1.784,00. Já a queda abrupta em dezembro $( \mathbb { R } \mathbb { S }$ 1.794,90) foi sinalizada pelo sistema como a ausência do pagamento da assessoria técnica, validando o encerramento ou suspensão temporária deste contrato específico. 


Tabela 4.17: Sistemas e Assessoria


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Janeiro</td><td>4.294,90</td></tr><tr><td>Fevereiro</td><td>4.294,90</td></tr><tr><td>Março</td><td>4.294,90</td></tr><tr><td>Abril</td><td>4.294,89</td></tr><tr><td>Maio</td><td>4.294,90</td></tr><tr><td>Junho</td><td>4.294,90</td></tr><tr><td>Julho</td><td>4.294,90</td></tr><tr><td>Agosto</td><td>4.294,90</td></tr><tr><td>Setembro</td><td>4.294,90</td></tr><tr><td>Outubro</td><td>4.294,90</td></tr><tr><td>Novembro</td><td>4.361,90</td></tr><tr><td>Dezembro</td><td>1.794,90</td></tr><tr><td>Total</td><td>49.010,79</td></tr></table>


Figura 4.25: Gráfico: Sistemas e Assessoria


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/7336ca2569705e946e6bb6d25aa60d5221049b928f528b6097e2f3752a020a49.jpg)



Fonte: Elaborado pelo autor.


# Estágio Remunerado

A folha de pagamento de estagiários, detalhada na Tabela 4.18 e na Figura 4.26, apresentou comportamento estável ao longo do exercício. A capacidade de segmentação do sistema ConSec permitiu analisar a distribuição da força de trabalho auxiliar, identificando o Ensino Fundamental como o setor com maior demanda, absorvendo consistentemente cerca de $50 \%$ dos recursos mensais (média de $\mathtt { R } \$ \mathtt { S }$ 12 mil), seguido pela Creche e Pré-escola. 

A ferramenta foi essencial para auditar a variação registrada em julho $( \mathrm { R } \$ 21 . 800,00 )$ , o menor valor do período letivo. O sistema demonstrou que essa redução de $1 3 { , } 5 \%$ em relação a junho não foi aleatória, mas reflexo de ajustes contratuais no período de férias escolares que impactaram todos os níveis: o custo do Fundamental caiu de $\ R \$ 13.200,00$ para R$ 11.000,00, e o da Creche de $\mathrm { R } \$ 7 . 200,00$ para $\mathrm { R } \$ 6.600,00$ . Essa sensibilidade do sistema valida a correlação entre o pagamento e a efetiva atividade escolar. 


Tabela 4.18: Estágio Remunerado


<table><tr><td>Mês</td><td>Valor (R$)</td></tr><tr><td>Fevereiro</td><td>25.200,00</td></tr><tr><td>Março</td><td>25.800,00</td></tr><tr><td>Abril</td><td>25.800,00</td></tr><tr><td>Maio</td><td>25.200,00</td></tr><tr><td>Junho</td><td>25.200,00</td></tr><tr><td>Julho</td><td>21.800,00</td></tr><tr><td>Agosto</td><td>22.800,00</td></tr><tr><td>Setembro</td><td>23.400,00</td></tr><tr><td>Outuro</td><td>22.800,00</td></tr><tr><td>Novembro</td><td>22.800,00</td></tr><tr><td>Dezembro</td><td>22.800,00</td></tr><tr><td>Total</td><td>263.600,00</td></tr></table>


Figura 4.26: Gráfico: Estágio Remunerado


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/8a9bda6b-c862-454f-9f2c-2f5664b413af/137eee0f68f068de8fac5311dac1eae23f97ea780a1aa90035ef8632265d7b82.jpg)



Fonte: Elaborado pelo autor.


# 4.4 Conclusão

A análise granular dos 18 centros de custo monitorados pelo ConSec confirma que o sistema não apenas atendeu aos requisitos funcionais de registro, mas também proveu à Secretaria de Carnaúba dos Dantas uma capacidade inédita de auditoria e de controle financeiro. A visibilidade, mês a mês, de cada rubrica permite, pela primeira vez, o planejamento estratégico baseado em dados históricos precisos, com uma interface amigável e validada nos critérios de acessibilidade. 

# Capítulo 5

# Conclusão

O desenvolvimento do sistema ConSec cumpriu o objetivo central deste trabalho: modernizar o controle financeiro da Secretaria de Carnaúba dos Dantas. O projeto substituiu processos manuais e frágeis por uma solução de software robusta, segura e, acima de tudo, inclusiva. 

Tecnicamente, a escolha pela arquitetura Cliente-Servidor (com frontend em Angular e backend em .NET) mostrou-se acertada. Essa estrutura não apenas garantiu a performance necessária para lidar com o volume de dados financeiros, mas também entregou uma interface moderna e responsiva. Além disso, a modelagem de dados relacional resolveu o problema histórico de integridade, eliminando as inconsistências comuns ao uso de planilhas descentralizadas. 

No entanto, a maior contribuição deste trabalho vai além da funcionalidade técnica. Ao tratar a Acessibilidade Digital como um requisito primário desde o início, o projeto provou que é viável desenvolver sistemas corporativos "nativamente acessíveis". A aplicação das diretrizes WCAG e dos princípios POUR validou a premissa de que a inclusão não é uma etapa corretiva final, mas um alicerce do design. O resultado é uma ferramenta que não apenas gerencia custos, mas democratiza o acesso ao trabalho dentro da Secretaria. 

A validação prática, feita com dados reais do exercício de 2024, confirmou o potencial do ConSec como ferramenta de inteligência. Mais do que apenas registrar despesas, o sistema permitiu visualizar padrões de gastos e identificar anomalias (como variações em custos de frota e infraestrutura), oferecendo à gestão dados concretos para um planejamento estratégico mais eficiente do dinheiro público. 

Conclui-se, portanto, que o ConSec resolve o problema imediato da gestão financeira e serve como referência para a administração pública local, demonstrando que a eficiência técnica pode, e deve, caminhar junto com a responsabilidade social e a inclusão digital. 

# Referências Bibliográficas



Elmasri, Ramez & Shamkant B. Navathe (2011), Sistemas de Banco de Dados, $6 ^ { \mathsf { a } }$ edição, Pearson Addison Wesley, São Paulo. 





Few, Stephen (2006), Information Dashboard Design: The effective visual communication of data, $1 ^ { \mathsf { a a } }$ edição, O’Reilly Media, Inc. 





Fielding, Roy Thomas (2000), Architectural Styles and the Design of Network-based Software Architectures, Dissertação de doutorado, University of California, Irvine. 





Fowler, Martin, David Rice, Matthew Foemmel, Edward Hieatt, Robert Mee & Randy Stafford (2002), Patterns of Enterprise Application Architecture, Addison-Wesley. 





Martins, Eliseu (2003), Contabilidade de Custos, $9 ^ { \mathrm { a a } }$ edição, Atlas. 





Nielsen, Jakob (1993), Usability Engineering, Academic Press, Inc. (AP Professional). 





Panko, Raymond R. (2000), Spreadsheet errors: What we know. what we think we can do., em ‘Proceedings of the Spreadsheet Risk Symposium European Spreadsheet Risks Interest Group (EuSpRIG)’, Greenwich, England. 





Pressman, Roger S. & Bruce R. Maxim (2021), Engenharia de Software: Uma Abordagem Profissional, $9 ^ { \mathrm { a a } }$ edição, AMGH. 





Sommerville, Ian (2011), Engenharia de Software, $9 ^ { \mathsf { a a } }$ edição, Pearson Prentice Hall. 





W3C Web Accessibility Initiative (2018), ‘Wai-aria overview’. W3C Working Group Note. 





URL: https://www.w3.org/WAI/standards-guidelines/aria/ 





World Wide Web Consortium (W3C) (2023), ‘Web content accessibility guidelines (wcag) 2.2’. W3C Recommendation 05 October 2023. 





URL: https://www.w3.org/TR/WCAG22/ 

