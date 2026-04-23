![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/b8488e6b9dd9706ceacc60b751461e4c493e94e70b623b06d5c9c2af2be3ad08.jpg)


# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE

# CENTRO DE TECNOLOGIA

# CURSO DE ENGENHARIA DE COMPUTAÇÃO

# Desenvolvimento de um Sistema Administrativo Dinâmico e Acessível para o Site do LAPPS

Alex Pereira Barros 

Natal-RN, Brasil 

2025 

# Alex Pereira Barros

# Desenvolvimento de um Sistema Administrativo Dinâmico e Acessível para o Site do LAPPS

Trabalho de Conclusão de Curso apresentado ao Departamento de Engenharia de Computação da Universidade Federal do Rio Grande do Norte como requisito parcial para a obtenção do título de Graduando em Engenharia de Computação. 

Orientador: Prof.º Dr. Tiago Tavares Leite Barros 

Natal-RN, Brasil 

2025 

Universidade Federal do Rio Grande do Norte - UFRN 

Sistema de Bibliotecas - SISBI 

Catalogacäo de Publicacäo na Fonte. UFRN - Biblioteca Central Zila Mamede 

Barros, Alex Pereira. 

Desenvolvimento de um sistema administrativo dinamico e acessivel para o site do LAPPS / Alex Pereira Barros. - 2025. 71 f.: i1. 

Trabalho de Conclusao de Curso - TCC (graduacao) 

Universidade Federal do Rio Grande do Norte, Centro de 

Tecnologia， Curso de Engenharia de Computacao， Natal， RN, 2025. 

Orientacäo: Prof. Dr. Tiago Tavares Leite Barros. 

1. Sistema Administrativo - TCC. 2. Gestao de Conteido - TCC. 3. Acessibilidade Digital - TCC. 4. WCAG 2.1 - TCC.5. Laborat0rio de Pesquisa - TCC. 6. PHP - TCC. I. Barros, Tiago Tavares Leite. II. Titulo. 

RN/UF/BCZM 

CDU 004.4 

# Alex Pereira Barros

# Desenvolvimento de um Sistema Administrativo Dinâmico e Acessível para o Site do LAPPS

Trabalho de Conclusão de Curso apresentado ao Departamento de Engenharia de Computação da Universidade Federal do Rio Grande do Norte como requisito parcial para a obtenção do título de Graduando em Engenharia de Computação. 

Trabalho aprovado. Natal-RN, Brasil, 03 de dezembro de 2025: 

Prof.º Dr. Tiago Tavares Leite Barros Orientador 

Prof.º Dr. Carlos Manuel Dias Viegas Examinador 

Prof.º Dr. Eduardo de Lucena Falcão Examinador 

Natal-RN, Brasil 2025 

Dedico este trabalho aos usuários que fazem parte do LAPPS e aos usuários que necessitam e fazem uso de sistemas acessíveis. 

# Agradecimentos

Meus agradecimentos a UFRN e a todos os professores que fizeram parte dessa trajetória acadêmica desde a ECT até a finalização deste curso no DCA. Esses anos todos foram uma grande jornada de aprendizado, adquirindo conhecimentos e amadurecendo na vida profissional e pessoal. Meus agradecimentos também aos amigos e colegas de curso, que apesar de muitos terem ficado pelo caminho, me deram muita força pra continuar essa trajetória. Principalmente grupinhos das mesas do RU, onde fazíamos nossa terapia diária. E também à minha família por ter me acompanhado até aqui. 

E também não poderia deixar de agradecer ao professor Tiago Tavares, que com toda paciência e dedicação, me acompanhou e orientou no desenvolvimento não só deste trabalho, mas também do meu estágio. Sua experiência e sugestões no trabalho foram muito importantes. 

# Resumo

O Laboratório de Arquiteturas Paralelas para Processamento de Sinais (LAPPS), da UFRN, mantinha seu site institucional de forma predominantemente estática, com conteúdo inserido diretamente no código-fonte. Esse modelo gerava forte dependência de desenvolvedores para atualizações simples, favorecendo erros e desatualização, além de não atender plenamente às diretrizes de acessibilidade digital, em especial à WCAG e às orientações legais brasileiras. Este trabalho teve como objetivo desenvolver um Sistema Administrativo Acadêmico Dinâmico e acessível para o site do LAPPS, permitindo a gestão autônoma de publicações, pessoas, projetos, aplicações de pesquisa e notícias. 

A solução foi implementada em PHP com PDO e MySQL, adotando uma arquitetura modular baseada no padrão Page Controller, com módulos CRUD, autenticação com controle de sessões e boas práticas de segurança (consultas parametrizadas, validação e sanitização de dados e hashes seguros para senhas). As diretrizes da WCAG 2.1 nível AA foram incorporadas por meio de HTML5 semântico, navegação por teclado, foco visível e ajustes de contraste. A avaliação, realizada com testes funcionais, ferramentas como Google Lighthouse e WAVE, e inspeções com leitores de tela, demonstrou atendimento aos requisitos definidos, com pontuações de acessibilidade $\qquad \geq ~ 9 0$ nas principais telas. O sistema reduziu significativamente o esforço de atualização do site, descentralizando a gestão e tornando o portal mais acessível e alinhado às práticas de inclusão digital, configurando-se como solução potencialmente replicável para outros grupos de pesquisa. 

Palavras-chave: Sistema administrativo. Gestão de conteúdo. Acessibilidade digital. WCAG 2.1. Laboratório de Pesquisa. PHP. MySQL. 

# Abstract

The Laboratory of Parallel Architectures for Signal Processing (LAPPS), at UFRN, previously maintained its institutional website in a predominantly static way, with content hardcoded into the source code. This approach created a strong dependency on developers for simple updates, leading to errors, outdated information and limited compliance with digital accessibility guidelines, especially WCAG 2.1 and Brazilian regulations. This work aimed to develop a dynamic and accessible Academic Administrative System for the LAPPS website, enabling autonomous management of publications, people, projects, research applications and news. 

The solution was implemented in PHP with PDO and MySQL, using a modular architecture based on the Page Controller pattern, with CRUD modules, authentication with session control, and security best practices (parameterized queries, data validation and sanitization and secure password hashes). WCAG 2.1 level AA guidelines were incorporated through semantic HTML5, keyboard navigation, visible focus and adequate color contrast. Evaluation with functional tests, tools such as Google Lighthouse and WAVE, and manual inspection with screen readers showed that the defined requirements were met, with accessibility scores $\geq 9 0$ on main screens. The system significantly reduced the effort required to update the website, decentralized content management and made the portal more accessible and aligned with digital inclusion practices, representing a solution that can be replicated by other research groups. 

Keywords: Administrative system. Content management. Web accessibility. WCAG 2.1. LAPPS. PHP. MySQL. 

# Lista de ilustrações

Figura 1 - Avaliação automática da página Inicial do LAPPS. 

Figura 2 - Pontos da página inicial que ferem algumas diretrizes da WCAG. 

Figura 3 - Pontos da página /people que ferem algumas diretrizes da WCAG. 

Figura 4 - Pontos da Figura 3 com mais detalhes. 

Figura 5 - Arquitetura do Administrative System 

Figura 6 - Estrutura de diretórios do Administrative System 

Figura 7 - Tela do dashboard. 

Figura 8 - Tela de login. 

Figura 9 - Tela de Gerenciar Publicação. 

Figura 10 - Tela de Publicações no LAPPS. 

Figura 11 - Tela de Gerenciar Pessoas. 

Figura 12 - Tela de Pessoas no LAPPS. 

Figura 13 - Tela de Gerenciar Projetos. 

Figura 14 - Tela de Projetos no LAPPS. 

Figura 15 - Tela de Gerenciar Pesquisas. 

Figura 16 - Tela de Pesquisas no LAPPS. 

Figura 17 - Tela de Gerenciar Notícias. 

Figura 18 - Tela Inicial no LAPPS. 

Figura 19 - Tabelas dos módulos. 

Figura 20 - Avaliação automática da tela de dashboard. 

Figura 21 - Resultado da avaliação automática da tela de dashboard. 

Figura 22 - INSERT com Prepared Statement 

Figura 23 - SELECT com Prepared Statement 

Figura 24 - Sanitização de saída 

Figura 25 - Trecho do código da autenticação 

Figura 26 - Trecho do código para upload de arquivo 

Figura 27 - Tela de autenticação 

Figura 28 - Pontuação de desempenho da tela de login 

Figura 29 - Pontuação de desempenho da tela de dashboard 

Figura 30 - Pontuação de desempenho da tela de Publicações 

Figura 31 - Pontuação de acessibilidade da tela de autenticação 

Figura 32 - Pontuação de acessibilidade da tela de Publicações 

# Lista de abreviaturas e siglas

ARIA Accessible Rich Internet Applications 

CDN Content Delivery Network 

CMS Content Management System 

eMAG Modelo de Acessibilidade em Governo Eletrônico 

LAIS Laboratório de Inovação Tecnológica em Saúde 

LAPPS Laboratório de Arquiteturas Paralelas para Processamento de Sinais 

UFRN Universidade Federal do Rio Grande do Norte 

WCAG Web Content Accessibility Guidelines 

W3C World Wide Web Consortium 

# Sumário

# 1 INTRODUÇÃO 14

1.1 Contexto 14 

1.2 Problema 15 

1.3 Objetivo geral 15 

1.4 Objetivo específico 16 

1.5 Escopo do Projeto 17 

1.6 Justificativa 17 

# 2 FUNDAMENTAÇÃO TEÓRICA 19

2.1 Acessibilidade digital e WCAG 19 

2.2 Sistemas administrativos acadêmicos 20 

2.3 Avaliação de acessibilidade e ferramentas automatizadas 21 

2.4 Segurança e boas práticas 22 

# 3 TRABALHOS RELACIONADOS 24

# 4 METODOLOGIA 26

4.1 Requisitos funcionais 31 

4.2 Requisitos não-funcionais 33 

4.3 Modelagem das entidades 33 

4.4 Tecnologia e ferramentas propostas 34 

# 5 PROJETO E IMPLEMENTAÇÃO DO SISTEMA 36

5.1 Arquitetura do Sistema 36 

5.1.1 Estrutura de diretório 37 

5.1.2 Painel administrativo 39 

5.1.3 Justificativa da arquitetura adotada 41 

5.2 Módulos Implementados 41 

5.3 Banco de Dados 49 

5.4 Interface e Usabilidade 49 

5.5 Segurança 52 

5.5.1 Prevenção de SQL Injection 52 

5.5.2 Prevenção de Cross-Site Scripting (XSS) 54 

5.5.3 Autenticação e Gerenciamento de Sessões 55 

5.5.4 Upload Seguro de Arquivos 56 

5.6 Integração com o Site Público 58 

# 6 RESULTADOS E AVALIAÇÃO DE QUALIDADE 59

6.1 Resultados Obtidos 59 

6.2 Avaliação de Qualidade 60 

6.2.1 Segurança 61 

6.2.2 Performance 61 

6.2.3 Acessibilidade 64 

6.2.4 Usabilidade e Manutenção 65 

6.3 Impactos 66 

# 7 CONSIDERAÇÕES FINAIS 67

# REFERÊNCIAS 69

# 1 Introdução

# 1.1 Contexto

O Laboratório de Arquiteturas Paralelas para Processamento de Sinais (LAPPS) é um centro ativo de pesquisa vinculado à Universidade Federal do Rio Grande do Norte, dedicado ao desenvolvimento de soluções em processamento de sinais, computação paralela e aplicações científicas de alto desempenho. Ao longo dos anos, o laboratório consolidou uma produção acadêmica relevante, com artigos, projetos de pesquisa, orientações e parcerias científicas. 

Apesar desse dinamismo interno, o site institucional do LAPPS não acompanha a mesma agilidade. Atualmente, o conteúdo é predominantemente estático ou “hardcoded”, ou seja, inserido diretamente no código‑fonte das páginas. Na prática, qualquer atualização — cadastro de uma nova publicação, inclusão de um membro do grupo, modificação em um projeto ou adição de uma notícia — exige a intervenção de um desenvolvedor para alterar arquivos PHP/HTML manualmente. 

Esse modelo de atualização apresenta diversas limitações. Em primeiro lugar, torna o processo de manutenção lento e burocrático, uma vez que pequenas correções dependem de conhecimento técnico em programação. Em segundo lugar, aumenta a probabilidade de erros, como quebras de layout, links inconsistentes, duplicidade de informações e problemas de navegação. Em um contexto acadêmico, em que a atualidade das informações é um fator importante para visibilidade e transparência, tais problemas afetam diretamente a eficiência da comunicação científica do laboratório. 

Além disso, vivemos um cenário em que a inclusão digital é reconhecida como parte fundamental da inclusão social. Websites institucionais de universidades e laboratórios de pesquisa devem atender às diretrizes de acessibilidade, como as Web Content Accessibility Guidelines (WCAG) (W3C, 2018), garantindo que pessoas com deficiência possam acessar informações e interagir com os conteúdos. No Brasil, esse compromisso com a acessibilidade também se encontra refletido em marcos legais e normativos (BRASIL, 2018), que orientam a adequação de sites públicos e educacionais. 

Diante disso, se torna necessário modernizar a forma como o LAPPS gerencia e publica seus conteúdos, ao mesmo tempo em que se assegura a conformidade com padrões técnicos, legais e éticos de acessibilidade na web. 

# 1.2 Problema

A forma estática como o site do LAPPS está implementado hoje gera uma série de problemas práticos de gestão de conteúdo. Não há uma interface administrativa dedicada, de modo que pesquisadores, secretarias ou demais colaboradores não conseguem, por conta própria, inserir ou alterar informações. Cada mudança exige o envolvimento de um desenvolvedor familiarizado com o código‑fonte, o que cria um gargalo operacional e uma dependência contínua da equipe técnica. 

Essa limitação impacta diretamente a capacidade do laboratório de manter um site atualizado e alinhado à sua produção acadêmica. Publicações recentes podem demorar a aparecer, alunos e pesquisadores egressos podem permanecer listados indevidamente, projetos finalizados podem continuar sendo exibidos como ativos e notícias importantes podem simplesmente deixar de ser divulgadas. Em suma, o site deixa de funcionar como um canal vivo de comunicação científica e passa a ser apenas um repositório estático de informações eventualmente desatualizadas. 

Junto a esse cenário as falhas de acessibilidade. Sem um projeto voltado para atender às recomendações das WCAG e às diretrizes nacionais, o site atual apresenta barreiras de uso para pessoas com deficiência visual ou até motora. Entre essas barreiras, encontram-se contraste inadequado, áreas de toque não têm tamanho ou espaçamento suficiente e falta de estrutura semântica adequada para ajudar na navegação completa por teclado. Assim, o site não cumpre plenamente o seu papel social de democratizar o acesso à informação científica, deixando de atender a requisitos éticos e legais de inclusão digital (BRASIL, 2018). 

Portanto, o problema a ser enfrentado é a ausência de uma solução de gerenciamento de conteúdo dinâmica, que permita autonomia e eficiência na atualização do site, junto a recursos de acessibilidade que garantam a possibilidade de qualquer pessoa usá-lo. 

# 1.3 Objetivo Geral

Este trabalho propõe uma solução para esse gargalo por meio do desenvolvimento de um Sistema Administrativo Acadêmico Dinâmico para o site do LAPPS. O objetivo geral é projetar e implementar uma plataforma modular, segura e acessível, que permita gerenciar de forma centralizada e estruturada os principais conteúdos do laboratório. 

A proposta é que pesquisadores, professores e administradores possam cadastrar, 

editar e remover, por meio de uma interface web amigável, informações como publicações, perfis de membros, projetos de pesquisa, aplicações de pesquisa e notícias institucionais, sem a necessidade de editar diretamente o código‑fonte. Desde seu planejamento, o sistema incorpora as diretrizes de acessibilidade da WCAG, buscando oferecer um ambiente inclusivo também na área administrativa, além de garantir que o conteúdo publicado no site público seja acessível a todos. 

# 1.4 Objetivos Específicos

Para transformar o objetivo geral em realidade, o trabalho foi dividido nas seguintes etapas: 

I. Projetar uma arquitetura de sistema robusta, baseada na separação de responsabilidades (como o padrão Page Controller com organização modular ou modelos inspirados em MVC), que favoreça a manutenção e a evolução futura do sistema. 

II. Implementar módulos de gerenciamento (operações de Create, Read, Update e Delete — CRUD) para os seguintes tipos de conteúdo: publicações, pessoas, projetos, aplicações de pesquisa e notícias. 

III. Integrar um sistema de controle de acesso com autenticação de usuários e gerenciamento de sessões, protegendo as rotas e funcionalidades administrativas contra acessos não autorizados. 

IV. Aplicar boas práticas de segurança em todo o sistema, com uso de consultas parametrizadas (prepared statements), validação e sanitização de dados, políticas para upload de arquivos e proteção contra ataques comuns, como SQL Injection e XSS. 

V. Incorporar, desde o design da interface até a implementação final, os requisitos de acessibilidade baseados nas diretrizes WCAG, tanto para as telas administrativas quanto para as páginas públicas alimentadas pelo sistema. 

VI. Validar o sistema por meio de testes funcionais, avaliações automatizadas de qualidade (incluindo métricas de performance e acessibilidade) e inspeções manuais, utilizando leitores de tela e navegação por teclado. 

VII. Documentar todo o processo de desenvolvimento, incluindo modelo de dados, arquitetura, instruções de instalação, scripts de banco de dados, manual de uso para administradores e o relatório técnico final deste Trabalho de Conclusão de Curso. 

# 1.5 Escopo do Projeto

O escopo deste projeto concentra-se no desenvolvimento de um painel administrativo integrado ao site institucional do LAPPS. Esse painel será responsável por gerenciar o conteúdo que hoje é mantido de forma estática, permitindo que o site público passe a ser alimentado dinamicamente a partir do banco de dados do sistema. 

As principais funcionalidades desejadas pelos membros do LAPPS é que o sistema tenha a capacidade de realizar cadastro, edição, listagem e exclusão de publicações, pessoas, projetos, aplicações de pesquisa e notícias, esses são os elementos principais do site público. Para poder ter acesso e realizar essas atividades é preciso ter um mecanismo de autenticação e controle de acesso ao sistema administrativo. Em alguns cadastros é necessário ter a possibilidade de fazer upload controlado de arquivos (imagens e .bib). E por fim, qualquer alteração nesse sistema deve ser refletida no site público do LAPPS, pois ele deve consumir o conteúdo dinamicamente dele. 

A implantação será direcionada ao ambiente já utilizado pelo LAPPS, baseado em XAMPP com PHP e MySQL, de modo a garantir compatibilidade com a infraestrutura existente e facilitar a adoção do sistema pela equipe técnica atual. 

# 1.6 Justificativa

A relevância deste projeto pode ser analisada sob duas perspectivas principais: eficiência operacional e inclusão digital. 

Do ponto de vista da eficiência, a adoção de um sistema administrativo dinâmico reduz significativamente o esforço necessário para manter o site atualizado. A eliminação da dependência constante de desenvolvedores para tarefas simples de atualização de textos, imagens e registros de pesquisa permite que os próprios pesquisadores e colaboradores administrativos assumam o papel de editores de conteúdo. Isso se traduz em menor tempo entre a produção de um resultado científico e a sua divulgação pública, ampliando a visibilidade do laboratório e contribuindo para sua inserção na comunidade acadêmica. 

Do ponto de vista da inclusão, o projeto está alinhado às diretrizes nacionais e internacionais de acessibilidade digital. Ao incorporar as recomendações da WCAG desde o início do desenvolvimento, o sistema busca garantir que pessoas com deficiência tenham condições equivalentes de acessar, compreender e interagir com os conteúdos 

disponibilizados. Trata-se, portanto, não apenas de cumprir obrigações legais, mas de adotar uma postura ética de respeito à diversidade de usuários, reforçando a imagem institucional do LAPPS. 

Além disso, o sistema proposto tem potencial de reaplicação em outros grupos de pesquisa e unidades acadêmicas que enfrentam desafios semelhantes, o que amplia o impacto deste trabalho para além do contexto específico do LAPPS. 

# 2 Fundamentação Teórica

Este capítulo apresenta os principais conceitos e referências teóricas que sustentam o desenvolvimento do Sistema Administrativo Acadêmico Dinâmico para o LAPPS (LAPPS Administrative System). São discutidos os fundamentos de acessibilidade digital e as diretrizes WCAG, as características de sistemas administrativos acadêmicos, as abordagens de avaliação de acessibilidade, bem como boas práticas de segurança para aplicações web. Esses elementos servirão de base para as decisões de projeto e implementação descritas nos capítulos seguintes. (Albuquerque et al., 2024), (Revista Brasileira de Biblioteconomia e Documentação, 2024). 

# 2.1 Acessibilidade digital e WCAG

A acessibilidade digital refere‑se à capacidade de pessoas, independentemente de suas condições físicas, sensoriais, cognitivas ou tecnológicas, de perceber, compreender, navegar e interagir com conteúdos e serviços disponibilizados na web. Um site acessível não beneficia apenas pessoas com deficiência; ele também melhora a experiência de uso em diferentes contextos, como conexões lentas, dispositivos móveis ou ambientes com restrições de áudio e vídeo (WAKE, 2024). 

As Web Content Accessibility Guidelines (WCAG) constituem o principal conjunto de diretrizes internacionais para avaliação e implementação de práticas de acessibilidade na web (W3C, 2018). Atualmente na versão 2.2, essas diretrizes são organizadas em torno de quatro princípios fundamentais, conhecidos pelo acrônimo POUR: 

Perceptível (Perceivable): as informações e componentes da interface devem ser apresentados de forma que possam ser percebidos pelos usuários, por meio de diferentes sentidos e tecnologias assistivas (por exemplo, uso de textos alternativos em imagens, legendas em vídeos e contraste adequado de cores). 

● Operável (Operable): os componentes de interface e a navegação devem ser utilizáveis por diferentes dispositivos e modos de interação, incluindo teclado, leitores de tela e tecnologias alternativas, garantindo tempos adequados e evitando interações que causem desconforto ou crises (como conteúdo que pisca excessivamente). 

● Compreensível (Understandable): tanto a interface quanto as mensagens e conteúdos 

devem ser claros e previsíveis, com linguagem adequada ao público‑alvo, feedback consistente e auxílio à correção de erros em formulários. 

● Robusto (Robust): o conteúdo deve ser suficientemente robusto para poder ser interpretado de forma confiável por uma ampla variedade de agentes de usuário, incluindo tecnologias assistivas presentes e futuras, o que implica uso de HTML semântico, ARIA de forma adequada e aderência a padrões. 

As WCAG definem três níveis de conformidade: A, AA e AAA, sendo A a cobertura mínima de conformidade; o nível AA o mais recomendado como referência mínima em sites institucionais e governamentais; e o nível AAA conformidade total com todos os critérios. Este trabalho adota a WCAG 2.1 (compatível com a ferramenta Lighthouse) como referência principal, buscando a conformidade de nível AA em fluxos principais da área administrativa (LEITE, 2020). 

# 2.2 Sistemas administrativos acadêmicos

Sistemas administrativos em contextos acadêmicos têm como finalidade apoiar a gestão de informações relacionadas a pessoas, cursos, disciplinas, publicações, projetos de pesquisa, eventos e outros elementos característicos da vida universitária. Esses sistemas podem atuar em diferentes camadas: desde a gestão interna de processos (como matrículas e registros acadêmicos) até a publicação de informações em portais públicos. 

No caso específico de laboratórios de pesquisa, sistemas administrativos frequentemente incluem módulos para gestão de publicações científicas, com registro de metadados (título, autores, conferência/periódico, ano, DOI, entre outros) e arquivos associados. Cadastro de membros da equipe (pesquisadores, alunos, colaboradores), com perfis, fotos, áreas de atuação e contatos. Gerenciamento de projetos de pesquisa, incluindo informações como status, financiadores, períodos de vigência e resultados. Divulgação de notícias, eventos e chamadas públicas. E controle de acesso baseado em papéis, permitindo que diferentes usuários tenham permissões específicas para editar, aprovar ou apenas visualizar conteúdos. 

Estudos na área de Engenharia de Software e Sistemas de Informação apontam a modularidade e a separação de camadas como características essenciais para a qualidade desses sistemas (ALMEIDA, 2024; OLIVEIRA, 2017). A modularidade permite que componentes específicos (por exemplo, módulo de publicações ou de pessoas) sejam 

desenvolvidos, testados e evoluídos de forma relativamente independente, reduzindo o acoplamento entre partes do sistema e facilitando correções e melhorias futuras (Gabrieli, Cortimiglia e Ribeiro, 2007). 

A separação entre as camadas de apresentação, lógica de negócio e acesso a dados contribui para uma melhor organização do código, maior reutilização de componentes e diminuição do impacto de mudanças. Por exemplo, alterações no layout da interface podem ser realizadas sem afetar diretamente a lógica de negócio, e modificações no banco de dados podem ser encapsuladas em camadas de acesso a dados, mitigando efeitos colaterais. 

Outra característica importante em sistemas administrativos acadêmicos é o foco em interfaces intuitivas e acessíveis para usuários não técnicos. Painéis administrativos mal projetados podem se tornar tão complexos quanto a edição manual de código, desmotivando seu uso. Ao privilegiar clareza, feedback adequado e fluxos de interação simples, a organização reduz sua dependência da equipe de desenvolvimento para tarefas rotineiras de atualização de conteúdo, liberando recursos tecnológicos para demandas mais estratégicas (ALMEIDA, 2024). 

# 2.3 Avaliação de acessibilidade e ferramentas automatizadas

A avaliação da acessibilidade de um sistema web é um processo que combina métodos automatizados e inspeções manuais. Ferramentas automatizadas, como Google Lighthouse e WAVE, desempenham um papel importante ao identificar rapidamente violações técnicas, ausência de atributos obrigatórios, problemas de contraste e outros aspectos que podem ser verificados de forma programática. 

Essas ferramentas geram relatórios objetivos, com pontuações e listas de recomendações, que auxiliam desenvolvedores a corrigir problemas e monitorar a evolução da qualidade ao longo do ciclo de desenvolvimento. No entanto, avaliações automatizadas apresentam limitações significativas. Muitos problemas de acessibilidade estão relacionados à forma como o conteúdo é organizado e compreendido por pessoas reais, ou à experiência de navegação com leitores de tela e outros dispositivos assistivos. Por exemplo, sentido lógico da ordem de foco ao navegar por teclado, clareza e concisão dos textos de links e botões, interpretação correta de mensagens de erro e instruções em formulários, são aspectos que só podem ser avaliados de maneira confiável por meio de testes manuais e, preferencialmente, com a participação de usuários reais, incluindo pessoas com diferentes tipos de deficiência. 

A utilização de leitores de tela como NVDA (no Windows) e VoiceOver (em sistemas da Apple) permite simular experiências de navegação e identificar barreiras que passam despercebidas em avaliações automatizadas. Portanto, uma estratégia eficaz de avaliação de acessibilidade é combinar auditoria automatizada para cobertura ampla e identificação rápida de falhas técnicas e inspeção manual criada por especialistas ou desenvolvedores familiarizados com as diretrizes WCAG, com usuários representativos, garantindo que o sistema atenda às necessidades de diferentes públicos. 

# 2.4 Segurança e boas práticas web

Sistemas administrativos que lidam com informações institucionais e dados pessoais precisam adotar boas práticas de segurança da informação, para garantir a confidencialidade, a integridade e a disponibilidade dos dados. Em aplicações web, algumas das principais ameaças de segurança são a Injeção SQL (ou SQL Injection), em que entradas maliciosas são utilizadas para manipular consultas ao banco de dados; Cross‑Site Scripting (XSS) que permite a injeção de scripts maliciosos em páginas visualizadas por outros usuários; Cross‑Site Request Forgery (CSRF), em que ações indesejadas são realizadas em nome de um usuário autenticado; e Sequestro de sessão por meio da captura ou predição de identificadores de sessão (session IDs). 

Uma das técnicas fundamentais para mitigar ataques de injeção SQL é o uso de consultas parametrizadas (prepared statements), como as disponibilizadas pela extensão PDO em PHP. Nesse modelo, a estrutura da consulta é separada dos dados fornecidos pelo usuário, impedindo que entradas maliciosas sejam interpretadas como parte da lógica da consulta (OWASP FOUNDATION, 2025). Junto a isso, a validação e sanitização de dados deve ser aplicada tanto no lado do cliente, no front‑end, quanto no lado do servidor, no back‑end. A validação no cliente melhora a experiência de uso, fornecendo feedback imediato, enquanto a validação no servidor é essencial para a segurança, pois não pode ser burlada por manipulação de scripts ou de requisições HTTP (BRASIL, 2024). 

A gestão adequada de sessões e senhas também é muito importante para a segurança. As Senhas devem ser armazenadas utilizando algoritmos de hash seguros, como por exemplo o bcrypt ou Argon2, nunca em texto puro. E as sessões precisam ser gerenciadas com atenção à geração de IDs aleatórios, expiração de sessões inativas e uso de cookies com atributos de segurança (HttpOnly, Secure, SameSite). 

Por fim, se o sistema contiver muitos conteúdos e informações valiosas e for muito visado por pessoas que desejam ter essas informações, recomenda-se o uso de bibliotecas e frameworks consolidados mais robustos, que incorporam correções de segurança e são continuamente aprimorados pela comunidade. Essas práticas fazem parte das diretrizes de segurança da informação são essenciais para minimizar riscos e garantir a confiabilidade de sistemas institucionais (OWASP FOUNDATION, 2025). No caso para o sistema do LAPPS essa situação não se aplica, então uma implementação básica de segurança já seria suficiente. 

# 3 Trabalhos relacionados

A literatura sobre acessibilidade digital, sistemas administrativos e gestão de conteúdo fornece bases conceituais importantes para o desenvolvimento de soluções que, como o sistema proposto para o LAPPS, buscam integrar boas práticas de engenharia de software, acessibilidade e usabilidade. Os estudos encontrados oferecem perspectivas complementares, abrangendo desde análises de conformidade com diretrizes de acessibilidade até abordagens arquiteturais voltadas à organização e manutenção de sistemas web. 

Um dos trabalhos mais relevantes no contexto brasileiro é o de Lemos (2023), que realizou uma avaliação sistemática dos portais da Justiça Federal sob a ótica da acessibilidade digital. Os resultados evidenciaram a recorrência de problemas como contraste insuficiente, ausência de textos alternativos, falhas de navegação por teclado e inconsistências estruturais. O autor destaca que, apesar de avanços institucionais, muitos portais públicos ainda tratam acessibilidade como etapa final de revisão, e não como característica integrada ao ciclo de desenvolvimento. Essa constatação reforça a necessidade de incorporar desde o início práticas de design inclusivo e conformidade às WCAG—abordagem que norteou a construção do sistema administrativo do LAPPS. 

No campo da gestão de conteúdo, o estudo de Couto (2011) analisa princípios fundamentais de sistemas de gerenciamento de conteúdo (CMS), como modularidade, organização editorial e automação de fluxos de publicação. O autor argumenta que CMS bem-estruturados reduzem a dependência de equipes técnicas e ampliam a autonomia dos usuários responsáveis pela atualização de informações. Embora o sistema do LAPPS não utilize um Content Management System (CMS) completo, ele incorpora os mesmos princípios: gerenciamento modular de dados, padronização de formulários e separação clara entre área pública e administrativa. 

A literatura técnica relacionada a arquiteturas de software também contribui significativamente. Almeida (2024) destaca que abordagens modulares e a separação de responsabilidades entre camadas favorecem a escalabilidade e a manutenção ao longo do ciclo de vida de sistemas institucionais. A autora argumenta que essas características são especialmente importantes quando se busca garantir acessibilidade, já que componentes isolados facilitam testes específicos e evitam que problemas introduzidos em um módulo 

comprometam toda a aplicação. Essa visão fundamenta a adoção de uma arquitetura baseada em Page Controller com organização modular no projeto do LAPPS. 

Complementando essa perspectiva, Oliveira (2017) discute detalhadamente os benefícios da modularidade em sistemas web, destacando como essa abordagem reduz complexidade, aumenta a reutilização de componentes e diminui o acoplamento entre funcionalidades. Embora o trabalho não trate diretamente de acessibilidade, suas conclusões sustentam a decisão de estruturar o sistema administrativo do LAPPS em módulos independentes para publicações, pessoas, projetos, aplicações de pesquisa e notícias. 

No cenário internacional, as diretrizes da Web Content Accessibility Guidelines (WCAG) (W3C, 2018) constituem a principal referência para avaliações e implementações de acessibilidade digital. Estudos relacionados demonstram que a adoção contínua e sistematizada de seus critérios reduz barreiras enfrentadas por pessoas com diferentes tipos de deficiência, aumentando a robustez e a usabilidade de aplicações web. Pesquisas recentes enfatizam que a conformidade não deve ser encarada como tarefa isolada, mas como parte do processo de desenvolvimento e manutenção de software — uma diretriz seguida durante o projeto deste sistema. 

Por fim, observa-se que, embora existam estudos robustos sobre acessibilidade, modularidade e gestão de conteúdo, ainda há uma lacuna na literatura quando se trata de integrar essas áreas no contexto de sistemas administrativos acadêmicos, especialmente considerando a necessidade de alinhamento com metodologias ágeis e ferramentas de avaliação automatizada (como Lighthouse e WAVE). Este trabalho busca atuar justamente nesse ponto de convergência, propondo uma solução prática que combina acessibilidade digital, arquitetura modular, segurança e gestão estruturada de conteúdo para um ambiente acadêmico real. 

# 4 Metodologia

O desenvolvimento do Sistema Administrativo LAPPS seguiu uma abordagem incremental, organizada em etapas que vão desde o entendimento do cenário atual até a validação final das funcionalidades implementadas. A opção por esse caminho permitiu ajustar decisões de projeto ao longo do processo, em vez de tentar definir tudo de forma rígida logo no início. 

As principais fases foram: análise do cenário atual, levantamento e priorização de requisitos, modelagem de dados e arquitetura, implementação incremental dos módulos, realização de testes funcionais, de acessibilidade e segurança, e, por fim, documentação e preparação para implantação. Ao estruturar o trabalho dessa forma, buscou-se equilibrar organização metodológica e flexibilidade prática, algo relevante em projetos que precisam conciliar prazos acadêmicos e demandas reais de um laboratório de pesquisa em funcionamento. 

O levantamento de requisitos combinou diferentes estratégias. Em primeiro lugar, foi feita uma inspeção detalhada do site atual do LAPPS e do código existente, com análise de diretórios, arquivos PHP e CSS. Em seguida, foram realizadas conversas com professores e pesquisadores que atuam no laboratório, a fim de compreender quais tipos de conteúdo são mais críticos, com que frequência são atualizados e quais dificuldades enfrentam no modelo estático atual. Também foram estudados painéis administrativos acadêmicos e sistemas de gerenciamento de conteúdo (CMS), como o LAIS (https://lais.huol.ufrn.br) e UNI-RN (https://unirn.edu.br) já utilizados em outros contextos, o que ajudou a identificar funcionalidades consideradas básicas em soluções desse tipo. 

Além dos requisitos funcionais, houve uma preocupação desde o início em explicitar requisitos de acessibilidade com base nas diretrizes da WCAG 2.1, com foco no nível AA. Isso inclui tanto o uso de elementos semânticos e boas práticas de front-end quanto a definição de metas mensuráveis de acessibilidade que pudessem ser verificadas por ferramentas automáticas e testes manuais. 

Durante a inspeção técnica, arquivos específicos, como o style.css, localizado em sitelapps\css\style.css, foram avaliados em conjunto com páginas do site, utilizando a extensão Lighthouse no navegador. As Figuras 1 a 4 ilustram alguns dos pontos críticos 

encontrados, como problemas de contraste, foco visível insuficiente, hierarquia inadequada de títulos e falta de estrutura semântica adequada. Esses achados serviram como linha de base para a definição das melhorias que o sistema administrativo proposto deveria promover. 


Figura 1 - Avaliação automática da página Inicial do LAPPS.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/cd9473865385bdd94092c5a71c8458e8bd6c3d679b6256de975fb8abdb8d52e4.jpg)



Laboratory of Parallel Architectures for Sianal Processing


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/d1004b638dc5600ee4d27276586f96fb5165921f405d0d12becaabf662211cc2.jpg)


Fonte: Próprio autor (2025). 


Figura 2 - Pontos da página inicial que ferem algumas diretrizes da WCAG.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/3d6e520a971eb60c5b88f4ad10a2a0cd1ba29e6c16f1eed3434f37cef1ae461d.jpg)



Fonte: Próprio autor (2025).



Figura 3 - Pontos da página /people que ferem algumas diretrizes da WCAG.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/f7f290626a29f5e75788e80bbd0ee176fc9798f87c3466f4ae5e5201d0c4ef8e.jpg)



Fonte: Próprio autor (2025).



Figura 4 - Pontos da Figura 3 com mais detalhes.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/cc1615100cf425ce9a7c965938861b6f265179282ff254de2778ee8124d44a69.jpg)



Fonte: Próprio autor (2025).


# 4.1 Requisitos funcionais

Os requisitos funcionais (RF) descrevem o que o sistema precisa oferecer em termos de comportamento e serviços para os membros do LAPPS, ou seja, descrevem o que o sistema faz e seus respectivos critérios de aceitação (CA) para ser validado. A partir do levantamento realizado, foram definidos quinze requisitos funcionais, dos quais oito foram considerados obrigatórios (RF1 a RF8) e seis opcionais (RF9 a RF14), pensados como extensões desejáveis para serem implementados conforme o avanço do desenvolvimento do sistema e a disponibilidade de tempo para desenvolvê los. São eles: 

RF1 — Autenticação e autorização por papéis (admin) 

CA1 — O sistema deve permitir o login de usuários autorizados e restringir o acesso ao painel administrativo apenas a esses usuários. Inicialmente, foi previsto o papel “administrador”, responsável pela gestão dos conteúdos. 

RF2 — CRUD para publicações 

CA2 — O sistema deve permitir criar, visualizar, editar e excluir registros de publicações científicas, incluindo metadados (título, autores, ano, tipo, link/DOI) e upload de arquivos relacionados (como PDFs). 

RF3 — CRUD para pessoas 

CA3 — O sistema deve disponibilizar um módulo para gerenciamento de pessoas vinculadas ao laboratório (docentes, discentes e colaboradores), com campos de perfil, foto, área de atuação, currículo e contatos. 

RF4 — CRUD para projetos 

CA4 — O sistema deve possibilitar o cadastro e gestão de projetos de pesquisa, incluindo título, descrição, período de vigência, coordenador, equipe e status (em andamento, concluído etc.). 

RF5 — CRUD para aplicações de pesquisa 

CA5 — O sistema deve permitir o gerenciamento de aplicações de pesquisa desenvolvidas pelo laboratório, com descrição, tecnologias utilizadas, objetivos e links de demonstração ou repositórios. 

RF6 — CRUD para notícias 

CA6 — O sistema deve oferecer um módulo para criação e gerenciamento de notícias 

institucionais, com título, texto, data de publicação e opcionalmente imagens ilustrativas. 

RF7 — Upload de arquivos de imagens 

CA7 — O sistema deve permitir o upload de imagens JPEG, JPG e GIF 

RF8 — Publicação dinâmica de conteúdo no site público 

CA8 — O sistema deve fornecer dados para o site público do LAPPS de forma dinâmica, substituindo conteúdos estáticos por informações provenientes do banco de dados, garantindo consistência entre o painel administrativo e as páginas públicas. 

Os requisitos opcionais, por sua vez, foram definidos como recursos que agregam valor, mas não são essenciais para o funcionamento inicial do painel. Entre eles estão: 

RF9 — Recuperação de senha por email. 

CA9 — O sistema deve permitir que usuários recuperem acesso à conta através de um processo seguro de redefinição de senha via email. 

RF10 — Timestamps automáticos para auditoria 

CA10 — O sistema deve registrar automaticamente as datas de criação e última modificação de todos os registros para fins de auditoria básica. 

RF11 — Sistema de status de publicação para as notícias. 

CA11 — O sistema deve permitir controlar a visibilidade de notícias através de status de publicação (rascunho/publicado). 

RF12 — Parser automático de BibTeX 

CA12 —O sistema deve extrair automaticamente metadados de publicações a partir de código BibTeX para facilitar o cadastro. 

RF13 — Dashboard com estatísticas gerais 

CA13 — O sistema deve apresentar um painel central com visão geral de estatísticas e acesso rápido aos módulos. 

RF14 — Validação de uploads de arquivos 

CA14 — O sistema deve validar o tipo, tamanho e segurança de arquivos enviados para prevenir vulnerabilidades. 

Essa divisão entre requisitos obrigatórios e opcionais permite gerenciar melhor o 

escopo do projeto e o tempo de desenvolvimento. Pois, garantiu a entrega de um núcleo funcional mínimo viável com as principais funcionalidades desejadas sendo atendidas, sem impedir que o sistema evolua futuramente para funcionalidades mais avançadas, de acordo com as necessidades do laboratório.. 

# 4.2 Requisitos não‑funcionais

Além de definir o que o sistema faz, foi necessário estabelecer como ele deveria se comportar em termos de qualidade, segurança, desempenho, usabilidade, acessibilidade e manutenção. Esses aspectos foram formalizados como requisitos não funcionais (RNF), que orientaram as decisões técnicas ao longo do desenvolvimento do sistema. São eles: 

RNF1 – Acessibilidade: O sistema deve ser utilizado por pessoas com diferentes perfis, incluindo usuários com deficiências visuais, motoras ou cognitivas, seguindo padrões internacionais de acessibilidade web com base nas diretrizes WCAG. 

RNF2 – Segurança: O sistema deve proteger dados sensíveis e mitigar ataques comuns, como SQL Injection e XSS, além de garantir que apenas usuários autorizados acessem funcionalidades administrativas. 

RNF3 – Usabilidade: O sistema tem que ser amigável ao ponto que os usuários sem formação técnica possam conseguir utilizar o sistema de forma intuitiva. 

RNF4 – Manutenção: Documentação para futuros desenvolvedores entender e realizar manutenção no código sem grandes dificuldades. 

RNF5 – Performance e boas práticas: O sistema deve responder de forma adequada às interações cotidianas do usuário. 

RNF6 — Responsividade: O sistema deve ser funcional e visualmente adequado em diferentes resoluções de tela, sem perda de funcionalidades ou conteúdo cortado. 

RNF7 — Validação de Dados: O sistema deve validar todos os dados de entrada tanto no cliente quanto no servidor para garantir integridade e prevenir erros. E nenhum dado inválido deve ser inserido no banco de dados; mensagens de erro claras devem orientar o usuário sobre correções necessárias. 

# 4.3 Modelagem das entidades

A modelagem das entidades teve como objetivo traduzir os requisitos funcionais em 

uma estrutura de dados coerente, que representasse bem as principais entidades e elementos do site do laboratório. Foram identificadas entidades centrais, como Publicação, Pessoa, Projeto, Aplicação de Pesquisa e Notícia, além de tabelas auxiliares para suporte a funcionalidades adicionais, como a tabela users para autenticação e controle de acesso . 

Para cada entidade, foram definidos atributos que refletem em como essas entidades serão mostradas no site público: 

users: representa os usuários do painel administrativo, com campos para identificação, credenciais (login, senha com hash); 

publications: armazena informações sobre publicações científicas, como título, autores, ano, veículo de publicação, link e caminhos para arquivos anexos; 

people: registra dados das pessoas vinculadas ao laboratório, incluindo nome completo, tipo de vínculo (professor, aluno, colaborador), área de atuação, mini‑bio, foto e informações de contato; 

projects: contém dados dos projetos de pesquisa do LAPPS, com título, descrição, coordenador, período de execução, status e possíveis relações com pessoas e publicações; 

research_applications: descreve aplicações de pesquisa desenvolvidas pelo laboratório, tecnologias envolvidas, objetivos e links para demonstrações, repositórios de código ou páginas de apresentação; 

news: registra notícias institucionais, com título, conteúdo, data de publicação e, opcionalmente, imagens de destaque. 

# 4.4 Tecnologias e ferramentas propostas

A seleção das tecnologias e ferramentas utilizadas no desenvolvimento deste projeto levou em consideração três fatores principais: compatibilidade com o ambiente de desenvolvimento do site público do LAPPS, minha experiência técnica com projetos de desenvolvimento e adequação às diretrizes de acessibilidade previstas no WCAG. Dessa forma, busquei um conjunto de tecnologias maduras e consolidadas no mercado, com facilidade para encontrar documentação e ajuda na internet. Foram elas: PHP, MySQL, HTML5, CSS3, JavaScript e bibliotecas auxiliares, com execução em ambiente XAMPP 

O backend foi desenvolvido em PHP $7 . 2 +$ , uma versão estável e já muito utilizada, o 

site público foi desenvolvido nesta versão, e por questões de compatibilidade e integração entre os sistemas, optei por desenvolver o sistema administrador nesta versão também. Por causa da compatibilidade com a infraestrutura já existente no laboratório, para acessar o banco MySQL escolhi o PHP com PDO (PHP Data Objects) pela possibilidade de implementar de forma direta o uso de consultas parametrizadas. O uso de sessões PHP para autenticação e controle de acesso também se alinha a esse contexto, permitindo que a implementação seja simples, mas eficaz, de login, logout e verificação de identidade dos usuários administrativos. 

No banco de dados, MySQL foi mantido como SGBD (Sistema de Gerenciamento de Banco de Dados) padrão, tanto por já estar presente no ambiente do laboratório quanto por ser bem documentado e com muito suporte. Assim, foram criadas as tabelas específicas para cada uma das entidades modeladas anteriormente. 

Na camada de apresentação, ou seja, no frontend, foi implementado combinando HTML5 semântico e CSS3 com o framework Bootstrap, para oferecer um layout responsivo e consistente entre diferentes resoluções de tela. O JavaScript foi utilizado de forma pontual, em especial para melhorar a experiência em formulários e de acessibilidade para quem navega com teclado ou tecnologia assistiva, como os leitores de tela, pois com ele foi implementado recursos adicionais como validação em tempo real com anúncios via ARIA, gerenciamento automático de foco e pré-visualização de uploads melhoram significativamente a usabilidade para todos os usuários. 

Outras ferramentas de apoio também foram utilizadas ao longo do desenvolvimento, como o Lighthouse e o Eye Dropper. O Lighthouse foi o principal, serviu como instrumento para avaliar métricas de desempenho e acessibilidade, enquanto Eye Dropper permitiu inspecionar contraste e cores dos elementos do site. Editores de código como o VSCode, sistemas de controle de versão gitlab e outros utilitários complementares contribuíram para manter o código organizado e facilitar ajustes incrementais no decorrer do desenvolvimento. 

# 5 Projeto e Implementação do Sistema

Este capítulo detalha as principais decisões de projeto e os aspectos de implementação do sistema administrativo desenvolvido para o LAPPS. Serão apresentadas a arquitetura adotada, os módulos implementados, o modelo de banco de dados, a interface do usuário e os mecanismos de segurança e integração com o site público. 

# 5.1 Arquitetura do Sistema

O sistema foi desenvolvido em PHP, adotando uma arquitetura modular baseada no padrão Page Controller, com separação e organização entre arquivos de apresentação (views), scripts de lógica de negócio e componentes de acesso a dados. Embora não implemente um padrão MVC completo com camadas totalmente desacopladas, a solução busca um equilíbrio entre simplicidade e organização, adequado ao porte do projeto e ao ambiente de implantação, o XAMPP já usado pelo laboratório. 

A arquitetura do sistema foi construída para atender a três objetivos principais: manter a integração com o site público já existente do LAPPS, oferecer um painel administrativo funcional e de fácil manutenção e organizar o código de forma simples, compatível com o ambiente XAMPP e com PHP nativo, sem uso de frameworks complexas. Conforme ilustrado na Figura 5, o sistema está organizado em quatro camadas lógicas que interagem de forma sequencial para processar as requisições do usuário. 


Figura 5 - Fluxo e arquitetura do Administrative System


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/1395454b06f19b65a2c98ce2376f3d30d8ca94e78785d592bf312215cfd653e3.jpg)



Fonte: Próprio autor (2025).


O fluxo de interação se inicia na Camada de Apresentação, responsável pela interface com o usuário (HTML/Bootstrap), que captura as ações e envia requisições HTTP para a Camada de Controle. Nesta etapa, scripts PHP individuais (os Page Controllers, localizados em /admin) processam a lógica de negócio e validam as entradas. A integridade das informações é assegurada pela Camada de Acesso a Dados, que utiliza a classe Database (Singleton) e PDO com consultas parametrizadas para intermediar a comunicação segura com a Camada de Persistência (banco de dados MySQL). Essa estratificação permite que o código seja mantido de forma organizada, sem a necessidade de frameworks complexos que poderiam elevar a curva de aprendizado para futuros mantenedores. 

# 5.1.1 Estrutura de diretório

A estrutura de diretórios foi organizada para separar claramente o que é parte do site público, o que pertence ao painel administrativo e o que diz respeito à infraestrutura e recursos estáticos. Na raiz do projeto permanecem as páginas públicas (index.php, people.php, projects.php, research_publications.php, research_applications.php e news_details.php), responsáveis por exibir informações do laboratório, que agora, são carregadas dinamicamente a partir do banco de dados. Além dos arquivos da raiz, há diretórios específicos incluem admin/, que concentra o painel administrativo; auth/, que reúne 

o código de autenticação e controle de sessões; config/, que guarda arquivos de configuração compartilhados, como parâmetros de banco de dados; includes/, que contém componentes de layout reutilizáveis, como cabeçalho e rodapé; e pastas como css/, js/, images/ e assets/, armazenam recursos estáticos, como folhas de estilo, scripts, imagens e ícones. Essa organização facilita tanto o desenvolvimento quanto a futura manutenção, porque delimita responsabilidades e evita misturar lógica de negócio com código de apresentação. A Figura 6 ilustra visualmente essa estrutura geral de diretórios. 


Figura 6 - Estrutura de diretórios do Administrative System


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/5f6026d35a11e84486d93ba320f87bfd73c54adb88d49539e473c3329c0dc092.jpg)



Fonte: Próprio autor (2025).


# 5.1.2 Painel administrativo

No diretório admin/ é onde se localizam os arquivos do sistema administrativo. 

Optou-se por não criar subpastas por módulo e manter um único nível de arquivos, o que simplifica a navegação pelo código e é suficiente para o porte atual do sistema. Entre os arquivos principais está dashboard.php, página inicial do painel, que apresenta uma visão geral com contagens de publicações, pessoas, projetos, aplicações de pesquisa e notícias cadastrados no sistema e métricas de quantidade de conteúdo público também. Aqui nessa tela também é possível encontrar os botões para as páginas de listagem de cada módulo e para a criação de cada módulo também. Além de um botão que leva direto para o site público do LAPPS. 

Clicando em um dos botões para adicionar um item em qualquer um dos módulos, exibe um formulário vazio corresponde, podendo ser add_publication.php, add_people.php, add_project.php, add_research_application.php ou add_news.php. Esse formulário permite ao usuário cadastrar novos itens precheendo os campos obrigatorios. Clicando no botão Save ocorre o processamento dos dados enviados via POST, realizando inserções das informações no banco, por meio de PDO com consultas parametrizadas. 

O formulário de edição segue um padrão semelhante. Ao clicar no botão Edit de um item cadastrado em um dos módulos, irá acessar arquivos como edit_publication.php ou edit_people.php, eles carregam um registro específico a partir de seu identificador, preenchem o formulário com dados existentes e, ao receber o envio após clicar no botão Save, atualizam o registro no banco de dados. Essa padronização de fluxo facilita a compreensão do código e reduz o risco de inconsistências entre módulos. 


Figura 7 - Tela do dashboard.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/51cf55d6b87e3296a863923d76325fa717f8a71ccbcadb47c107957add15a19f.jpg)



Fonte: Próprio autor (2025).


Cada uma dessas páginas funciona como um Page Controller, seguindo uma estrutura comum: 

1. Controle de acesso: inclusão da lógica de autenticação e chamada a requireLogin() para garantir que apenas usuários autenticados acessem o conteúdo administrativo. 

2. Conexão com o banco de dados: inclusão da classe Database para obter a instância PDO. 

3. Processamento da requisição: verificação do método HTTP (GET ou POST), validação de entradas, execução de consultas SQL parametrizadas. 

4. Renderização da interface: inclusão de trechos de layout (header/menu) e saída do HTML com os dados vindos do banco. 

# 5.1.3 Justificativa da arquitetura adotada

A arquitetura adotada prioriza a simplicidade e baixo acoplamento tecnológico. O uso de PHP nativo, sem frameworks pesados, facilita a implantação em ambientes já conhecidos como o XAMPP, e a baixa curva de aprendizado para novos desenvolvedores que venham a manter o sistema. 

A organização mesmo sem subpastas por módulo dentro de admin/, há uma separação clara entre site público (raiz), painel administrativo (admin/), autenticação (auth/), configurações (config/), layout (includes/) e recursos estáticos (css/, js/, images/, assets/). Embora não implemente um padrão mais robusto como o MVC, o padrão de arquitetura Page Controller é adequado ao escopo do projeto e ao contexto institucional, oferecendo um bom equilíbrio entre organização, facilidade de manutenção e curva de aprendizado. 

# 5.2 Módulos Implementados

Os cinco módulos principais do sistema foram pensados para refletir os principais tipos de informação que o LAPPS precisa gerenciar no dia a dia. Cada módulo segue o padrão CRUD, com páginas de listagem, criação, edição e remoção, e compartilha elementos comuns, como validação de dados, mensagens de feedback e navegação consistente pelo menu administrativo. Além desses, também foi implementado o módulo de autenticação, e vamos abordar cada um deles nessa sessão. 

O módulo de autenticação é responsável pelo controle de acesso ao sistema. A página de login valida credenciais informadas pelo usuário consultando a tabela de usuários no banco 

de dados e utilizando password_verify para comparar a senha digitada com o hash armazenado. Em caso de sucesso, é criada uma sessão e o usuário é redirecionado ao dashboard; em caso de falha, mensagens de erro claras orientam o próximo passo. A Figura 8 ilustra a tela de autenticação. O arquivo auth_check.php é incluído no início de cada página administrativa para verificar se existe sessão válida. Em caso negativo, o usuário é redirecionado para a tela de login. 


Figura 8 - Tela de login.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/1c8583abb84cfcd471597a002cb7280d5da9042a27e906273019208c3f76a5c6.jpg)



Fonte: Próprio autor (2025).


O módulo de publicações permite registrar e gerenciar a produção científica do laboratório, incluindo título, autores, ano, tipo de publicação, veículo, link, além de arquivos de imagem. A listagem apresenta filtros básicos e ordenação, e as telas de cadastro e edição seguem o padrão de formulários semânticos, com validação de campos obrigatórios. As Figuras 9 e 10 exemplificam o fluxo de gerenciamento e exibição de publicações. As publicações cadastradas são exibidas automaticamente na página pública de publicações, consumindo dados diretamente da tabela publications. 


Figura 9 - Tela de Gerenciar Publicação.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/2145701cebc6a8779fa69b531bcefd5279be25ba5bc595cf5da720519ac40190.jpg)


Administrative System 

Welcome.admin! 

Logout 

Dashboard 

People 

Projects 

Applications 

News 

Manage Publications 

+ New Publication 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/1685a38066921664704f78f4469bca4adf8a35391330300983b2e952be6ffffe.jpg)


Fonte: Próprio autor (2025). 


Figura 10 - Tela de Publicações no LAPPS.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/17ef627f23ba5e3ce5b13be5db061553c44f3abae4ff98338864b2298527e8e6.jpg)


People 

Research 

Education 

Projects v 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/fd3f0b567e490640c43205808ab95a5f0b57059cb836dfb33a4455dd27224e66.jpg)


# Publications

Home/Research/Publications 

# 2024

AParity-BasedDual Modular RedundancyApproachfortheReliabilityofData Transmisson in Nanosatelite's Onboard Processing 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/8039f374b91876deca4f5fb59f21aca02cf9722efebd159172bb97357f25e341.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/233a29254c297f7503c513cee806ad6c73ddcc8f55eb90f8a64c38f605dfc2b4.jpg)


Evaluating the Effects of Reducing Voltage Margins for Energy-Efficient Operation of MPSoCs 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/1080606460bbd3332b57d8709908d09a397c7d1651c21a323573b8fa6f4c1bbe.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/3e37433ace40d8977460aaf77c689a009f25af46a5159f621616df7f260b3225.jpg)


PATSMA: Parameter Auto-tuning for Shared Memory Algorithms 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/e8d15ca786eea31df63d0cbf88cd6c8cd3449b538270bd2564b4d3fe9c2e3a3b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/51d1fb704991964bf4521640688f12e16a27f59bf429fdc13010d18055bbc901.jpg)


Fonte: Próprio autor (2025). 

O módulo de Pessoas reúne informações sobre os docentes, discentes e colabores. nele é possível cadastrar nome, tipo de vínculo, área de atuação, mini-biografia, foto e um link para sua página de contato. Esse módulo abastece a página pública de membros, permitindo que o laboratório mantenha uma visão atualizada de sua composição. As Figuras 11 e 12 mostram as telas de gerenciamento e visualização dessas informações. 


Figura 11 - Tela de Gerenciar Pessoas.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/52c3ceab705a4e0bc01177b63a414cbd75faf553828e4248daec1eb223cf9e2a.jpg)


Administrative System 

Welcome, admin! 

Logout 

Dashboard 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/72dbf558fcccc3c990527328bd6fe93f41b6755a285c3cfa3c66d46e8919b68c.jpg)


ications ！ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/653576e9314ce0af7dcdc18d04a3426330a8f7a00267bb2f5766ccc6508b4c4d.jpg)


Projects 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/07810b53d2e1242c6eae92cb0fb71d5a6f67747c650e7857255ce9297764761f.jpg)


olications 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/ecd53c6f425ac7e1ad086311a57964e36c37214af591f71b43fbd569d0c69171.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/5c26780f08201efbc80c10876e4819383b262e90078fbdc7f3f35ded6b72d478.jpg)


Manage People 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/6a186520927b51f32883398e48861dcf0c28af191a23da9a327e4ab8d0d36df0.jpg)


Name 

Position 

Biography 

Actions 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/c320789f9dfc4306b57159b6a3dede3ae8f1d480971909cbeb7281798d84b4a0.jpg)


Alex Barros 

Pesquisador 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/fb353c33d9e21ea99f9826f7d8e8d369825f066d3e6f831232f8136f5b9b5f6f.jpg)


Master's student at Universidade Federal do.. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/8a8a2f58ef05c1a99162c5983255d2212bbac84ef59df0076298663836ef86c3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/1a9e46bedab2c4d81af97eb97f390937f02edf6704496c053ff4d1ea5659ab7f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/df990fa087580d7cb3248d174fcbd2961e90a4499a265ee3599576c41f9a158d.jpg)


Luiz F. Q. Silveira 

Associate Professor 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/d809a7b8566ad66aac52e12c23ff332fd5681bb547eee2f9150edec12a0d9a7d.jpg)


Luiz F. Q. Silveira received his Bachelor Deg... 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/7bcff04bd99c61b69879628bf3025512b7a2cef0cf6cb22a923bb02218d5b818.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/3a8b895ee8334bb91a35a60ea2fd2376449b2cca96341b2e9cbbc2b8c8e307f9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/d185c032a38f90d0344b2fdd0b1ef26719eede8be7f9a01b0c832e85179c7895.jpg)


Samuel Xavier-de-Souza 

Associate Professor 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/1c63f41fde58106507d352c12fb2a7061bb5a186b4d3ca3b4ff63f28e12b6453.jpg)


Holds a Computer Engineer degree by Unive... 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/4d6c44b13e02b1afa43d96d922534ffde159e31e7086ae634c8dc7df22d05873.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/2c7d5b767bc35305f25557151a7e743b677e534352f93d2fca1a0e50a4792a40.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/567ed7142f0a98ae5305534f4af1289127972be89f5ae26a80a0969cb5b54b76.jpg)


Tiago Barros 

Adjunct Professor 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/00319537dd2596eb7a0e493d8065767f244dcf252d819e2003f2bf131200a2bf.jpg)


Holds a Ph.D.degree in Electrical Engineerin.. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/d2b0ce2028ecb094397868a700f6698a5ca23dc5d2428d00d66a071ac4be3526.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/2cbbb5137951b895092903835f25222802e88e859c21fdaf6ec51f72e31dd183.jpg)


Fonte: Próprio autor (2025). 


Figura 12 - Tela de Pessoas no LAPPS.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/2286862d865f6419b029565b8b7b4ae2766fba5fdd2a8c25103a583d96e054e1.jpg)


# Faculty Members

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/cd62973b41c865d8a9cf3c0108a820f44c9b13b36173f12ae1f2109c11058839.jpg)



Luiz F. Q. Silveira



Associate Professor


Luiz E. O. Silveira received his Bachelor Degree in Electrical Engineering from Universidade Federal da Paraiba (UFPB),.. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/e2bead96f79dc3a96f480e26bcdb124abbb518d4177234f1f2fc8d03440ea1c0.jpg)



Samuel Xavier-de-Souza



Associate Professor


Holds a Computer Engineer degree by Universidade Federal do Rio Grande do Norte-UFRN, Brazil, 20OO,and a Ph.D. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/61adb6900afdf9a191ba847fbcdf857f44458ff83583529565f1fcb36c4b03b8.jpg)


Tiago Barros 

Adjunct Professor 

Holds a Ph.D, degree in Electrical Engineering from the University of Campinas - Unicamp, Brazil (2018). His 


Fonte: Próprio autor (2025).


Os módulos de projetos e de aplicações de pesquisa seguem lógica similares, eles registram título, descrição, período de execução, status, tecnologias utilizadas e links relevantes. Dessa forma, o painel administrativo passa a concentrar os dados que antes eram mantidos de forma dispersa ou manual no código do site. As Figuras 13 a 16 apresentam exemplos dessas telas em funcionamento. 


Figura 13 - Tela de Gerenciar Projetos.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/6b75b2fdef220569906fa63073fcacc2509f2f0b58b79a115cc4d24fa1f38989.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/4e5a2bc183afc0f6fd9c74e5fa71a7da86d78c561f61731b3db824f3330d3954.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/e945295e8204470314c7a0e9f7be42e1a223ffe6f2ea10f3bb71bec5ab1b96b0.jpg)


Fonte: Próprio autor (2025). 


Figura 14 - Tela de Projetos no LAPPS.


People 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/7801a873dc5dfd0651014a0c71e672da89d6cc9848b60b02d71d039a2bd6c233.jpg)


Home/Projects /Academia 

# Simulation and Analysis of Algorithms for the Multi-Core Era

Original title (Portuguese): Simulacäo e analise de algoritmos para a era multicore 

Period: 2010-11 to 2012-10 

Fundingagency: Conselho Nacional de Desenvolvimento Cientifico e Tecnologico 

# Energy Efficient Channel Coding Applied to Wireless Sensor Networks

Fonte: Próprio autor (2025). 


Figura 15 - Tela de Gerenciar Pesquisas.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/e6d49e1757adcd2ca1572ebed0b7efcf28e47d8d0c242a1964b2804aa6b4c938.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/60a5f9143613b95033073b3a7e547e50ffb7fb40b532b328a0deb1b3d1f2c218.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/9a05b1235548d055b01029bbaa0e01b62eb3a043791af6b711f8e15a27112703.jpg)


Fonte: Próprio autor (2025). 


Figura 16 - Tela de Pesquisas no LAPPS.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/6e1e1f9810d4e3b353a9ffbf045754f5edf1d67dd4203f7f11d573ce1e4debae.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/c0528731c347b6a60f0bfa2d6a089d5c496436ae87e7c246e04b955834dabe9a.jpg)


Home/Research/Applications 

# Parallel Energy-Efficient GNSS Receiver

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus risus erat, tempus quis portitora aliquet a dolor. Duis eficitur purus a varius molls. Mauris nunc nibh, volutpat ac tristigue a, hendrerit at velit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam quam metus euismod a tincidunt quis, aliquet vestibulum leo. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/d99e65b028a699db8f0a12f2a88fee903e668352c17a012bc867a0388292ebf5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/7f8dd162f74fe59db99455fdc82df8a2ed9ecc69798eacbe31802422a4fa4118.jpg)


# CEVERO - Chip multi-procEssor for Very Energy-efficient aeRospace missiOns

The CEVERO Project aims at developing Chip multi-procEssors forVery Energyefficient aeRospace missiOns. Given the nature of their operation, aerospace and mission-critical system processors are customarily required to be fault tolerant and energy-efficient. Fault tolerance is required to deal with the higher probability of radiation strikes when operating far from the Earth's surface, which causes failure due to “single event upsets"(SEUs) and “single event latchups"(SELs). Nowadays, these processors are even more susceptible to such 

Fonte: Próprio autor (2025). 

Por fim, o módulo de notícias permite a criação, edição e remoção de comunicados institucionais, eventos e atualizações, com título, texto, data de publicação e imagem de 

destaque. As notícias cadastradas alimentam a página inicial do site público, próximo ao rodapé, contribuindo para que o portal reflita melhor as atividades recentes do LAPPS. As Figuras 17 e 18 ilustram essa integração. 


Figura 17 - Tela de Gerenciar Notícias.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/c39eb58f5f5250a4c1baf7f8f057ed362e03ea220271e275224f8b54d4f9f124.jpg)



Fonte: Próprio autor (2025).



Figura 18 - Tela Inicial no LAPPS.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/5ca23917eaceada10396cc380647da665bb4dd0f5eef93103326f7a13dfc1396.jpg)



Fonte: Próprio autor (2025).


# 5.3 Banco de Dados

O banco de dados foi modelado de forma normalizada, buscando um equilíbrio entre redução de redundâncias e simplicidade de consultas. 

As principais tabelas são: 


Figura 19 - Tabelas dos módulos.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/bc8ad3bda787d3f0fb09797fea221d8435076d4780c3d9dbd433e4f392448293.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/38232e87c7cbd599959a778e3e4ad025a61564d7795c0ed29109f32890ac926c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/8ebfa50902c342856b45db57cc078269395fddb1c9e7afb412fd65ea4e410f54.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/6ef0ac3df1e67b8c8e5cc0e2f5ed74045f91bdc0db5e453caec558b2ef33081b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/98da826e73da9cb6a16aa25705b77ba4c14c03ebe6b6fcacac0360c851942696.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/a6da97515989379c58079e4ae164f76f6ea4bbaaa815c263fe1edbd8565142cf.jpg)



Fonte: Próprio autor (2025).


Todos os campos de identificação utilizam chave primária do tipo inteiro auto incrementada, e timestamps created_at e updated_at que permitem identificar alterações nos módulos principais ao longo do tempo. O diagrama e o script SQL de criação de tabelas foram todos documentados e entregues como artefatos do projeto. 

# 5.4 Interface e Usabilidade

A interface do sistema foi planejada para ser clara e intuitiva para os usuários, a organização do menu, a padronização visual entre as telas e o uso de elementos conhecidos, como tabelas, botões de ação e mensagens de feedback, buscam reduzir a curva de aprendizado e tornar o sistema amigável e acessível. As páginas utilizam um layout responsivo baseado em Bootstrap, o que permite que o sistema seja acessado de diferentes tamanhos de tela sem perda de funcionalidade. Formulários seguem um padrão consistente: campos obrigatórios são destacados, mensagens de erro aparecem próximas aos campos com 

problema e, sempre que possível, textos de ajuda orientam o preenchimento correto dos campos. 

Além da usabilidade, houve preocupação com aspectos de acessibilidade, como contraste adequado, navegação por teclado e identificação clara de estados de foco. Combinando isso com o HTML5 semântico e atributos ARIA, abre a possibilidade para o uso de mais ferramentas assistivas, como leitores de tela. Essas características são importantes tanto para atender aos requisitos não funcionais quanto para garantir que o sistema possa ser utilizado por uma variedade maior de perfis de usuário. 

O sistema administrativo utiliza um layout típico de sistemas de gestão, com barra de navegação superior (header) com identificação do sistema, nome do usuário logado e opção de logout. No menu de navegação ficam os links para o Dashboard e os módulos principais Publicações, Pessoas, Projetos, Aplicações de Pesquisa, Notícias. esse ponto é comum em todas as telas do sistema administrativo, o que vai diferenciar é o conteúdo do corpo da página, onde podem ser exibidos, um painel do dashboard, listas de itens de cada módulo ou formulários para cadastro de um novo item. Os elementos de layout utilizam landmarks semânticos comuns em páginas web, como <header>, <nav>, <main>, <footer>, o que facilita a navegação por leitores de tela. Os títulos de página são organizados hierarquicamente, podendo ir da tag $\mathrm { \Phi } \mathrm { < h l > }$ até $\operatorname { c h } 6 >$ . A ${ \mathrm { < h l > ~ } } \dot { \mathrm { \Omega } }$ usado para o título principal e ${ \tt - h 2 > }$ para seções internas a $\mathrm { \Phi } \mathrm { < h l > }$ , $\mathrm { < h } 3 \mathrm { > }$ para seções internas a $\mathrm { \ c h { 2 } > }$ e assim sucessivamente. 

Sobre os formulários, eles apresentam, labels explícitos associados a seus respectivos campos <label fo $\kappa { = } ^ { 1 }$ "nome_campo">, evitando o uso de placeholders como única forma de identificação, possuindo também indicação clara de campos obrigatórios e quando não cumpridos, apresentando mensagens de erro, quando possível, marcadas com atributos ARIA adequados para serem anunciadas por leitores de tela, os botões de ação possuem textos descritivos, evitando rótulos ambíguos. 

Do ponto de vista de acessibilidade visual, foram ajustadas cores e contrastes para atender aos níveis mínimos da WCAG, especialmente em textos, botões e ícones. O foco de teclado é visível e destacado, permitindo que usuários identifiquem em qual elemento estão navegando e interagindo. A ordem de tabulação foi testada e corrigida, evitando “saltos” inesperados na navegação com o uso do Bootstrap, as páginas do painel são responsivas, adaptando‑se a diferentes tamanhos de tela. Isso permite que o administrador acesse e gerencie conteúdos também em dispositivos móveis, sem perda significativa de 

funcionalidade. E por último, foram utilizados os ícones do Font Awesome, sempre acompanhados de texto visível ou atributos aria-label/title quando necessário, para não depender exclusivamente de ícones visuais. 


Figura 20 - Avaliação automática da tela de dashboard.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/2126f7b3779a8e4452205443203388c302b3203878d6eb64a96714f575926682.jpg)



Fonte: Próprio autor (2025).



Figura 21 - Resultado da avaliação automática da tela de dashboard.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/a1f92414ef0b4066c4352128916bec422c5f470f703be2ae0c41b53450ce184d.jpg)



Fonte: Próprio autor (2025).


# 5.5 Segurança

A segurança foi um pilar fundamental no projeto e implementação do Sistema Administrativo do LAPPS, visando proteger a confidencialidade, integridade e disponibilidade dos dados institucionais. Foram adotadas algumas práticas e mecanismos de defesa contra as vulnerabilidades web mais comuns, conforme as diretrizes da OWASP Top Ten (Open Web Application Security Project) (OWASP, 2021). 

# 5.5.1 Prevenção de SQL Injection

A injeção SQL, é uma das vulnerabilidades mais críticas, ocorre quando entradas maliciosas são inseridas em campos de formulário e interpretadas como parte de uma consulta SQL, permitindo a manipulação indevida do banco de dados. Para mitigar essa ameaça, todas 

as operações de acesso ao banco de dados no sistema utilizam Prepared Statements (consultas parametrizadas) via PDO (Choi et al., 2025). Essa abordagem garante que a estrutura da consulta SQL seja separada dos dados fornecidos pelo usuário. Os dados são enviados ao banco de dados como parâmetros, e não como parte do comando SQL, impedindo que caracteres especiais alterem a lógica da consulta. Nas Figuras 22 e 23 são mostrados trechos de código como exemplo de aplicação. 

Figura 22 - INSERT com Prepared Statement 

```php
<?php
// Arquivos: admin/add_publication.php
// Inserção segura de nova(publicação
try {
// Prepared statement com placeholders (?)
${stmt = $conn->prepare(
INSERT INTO publications (year, title, reference, bibtex, link, type)
VALUES (?, ?, ?, ?, ?, ?
));
}
// Execuição com array de parâmetros
${stmt->execute([${year}, $title, $reference, $bibtex, $link, $type]);
${success_message = "Publication added successfully!";
} catch (PDOException $e) {
${error_message = "Error: ". $e->getMessage();
}
} 
```

Fonte: Próprio autor (2025). 

Figura 23 - SELECT com Prepared Statement 

```php
<?php
// Arquivo: admin/edit_people.php
// Busca segura por ID
// Type casting para garantir tipo inteiro
$id = (int)$GET['id'];
try {
    // Prepared statement para SELECT
        $stmt = $conn->prepare("SELECT * FROM people WHERE id=?");
        $stmt->execute($id));
        $person = $stmt->fetch(PDO::FETCH_ASSOC);
    }
    if (!$person) {
        header("Location: people.php");
        exit();
    }
} catch (PDOException $e) {
    $error_message = "Error loading person: ". $e->getMessage();
} 
```


Fonte: Próprio autor (2025).


# 5.5.2 Prevenção de Cross-Site Scripting (XSS)

O Cross-Site Scripting (XSS) permite que atacantes injetem scripts maliciosos em páginas web, que são executados no navegador de outros usuários. Para prevenir ataques XSS, foi implementado no sistema a sanitização de todas as saídas de dados antes de serem renderizadas no HTML. A função htmlspecialchars() é bastante utilizada para converter caracteres especiais, como $( < , > , \ : \& , " , " )$ , em suas entidades HTML correspondentes, garantindo que qualquer código injetado seja exibido como texto simples e não executado pelo navegador. Na Figura $2 4 \textup { \texteuro }$ mostrado um trecho de código aplicando a sanitização de saída. Essa prática foi aplicada nas saídas de dados provenientes do banco de dados ou de entradas do usuário, protegendo o sistema contra ataques XSS refletidos e armazenados. 

Figura 24 - Sanitização de saída 

```php
<?php
// Arquivo: admin/publications.php
// Sanitização de dados antes de exibir no HTML
<td><strong></?php echo www.htmlspecialchars($pub['year']);
?></strong></td>
<td><strong></?php echo www.htmlspecialchars($pub['title']);
?></strong>
?php if ($pub['reference']):
?>
<br><small class="text-muted">
?php echo www.htmlspecialchars(substr($pub['reference'], 0, 100)). '...' ; ?
</small>
?phpendif; ?
</td>
<td><?php if ($pub['link']):
?a href="/?php echo www.htmlspecialchars($pub['link']);
?">
target="_blank" class="btn btn-sm">
<i class="fa fa-external-link"></i> View </a>
?phpendif; ?
</td> 
```


Fonte: Próprio autor (2025).


# 5.5.3 Autenticação e Gerenciamento de Sessões

A segurança da autenticação e das sessões é crucial para proteger o acesso ao sistema administrativo para que só os usuários autorizados tenham acesso a ele. Para isso, foram implementados algumas medidas, como o armazenamento seguro de senhas: As senhas dos usuários são armazenadas no banco de dados utilizando a função password_hash() do PHP, que emprega o algoritmo bcrypt. Este algoritmo gera hashes criptográficos robustos e únicos para cada senha, dificultando ataques de força bruta e dicionário. A verificação é feita com password_verify(). Com o gerenciamento de sessões PHP o estado de autenticação do usuário é mantido através de sessões PHP após um login bem-sucedido, um ID de sessão é gerado e associado ao usuário. Proteção de rotas: A classe Auth centraliza o controle de acesso, utilizando o método requireLogin() para verificar a existência de uma sessão ativa em todas as páginas administrativas. Usuários não autenticados são redirecionados para a página de login. 


Figura 25 - Trecho do código da autenticação com bcrypt


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/943ead51aaa3346be6e843552cfbd3bb0b4c1dbd9a7b29b02bafd4ac950fbf4a.jpg)



Fonte: Próprio autor (2025).


# 5.5.4 Upload Seguro de Arquivos

O sistema permite o upload de alguns tipos de arquivos para imagens e bibtex, o que pode representar um potencial de ataque se não for devidamente controlado. As seguintes validações e medidas de segurança foram aplicadas: Validação de tipo de arquivo: O tipo do arquivo é verificado para garantir que apenas formatos permitidos apenas extensões .jpg, .jpeg, .png, .gif e .bib são aceitas; Limitação de tamanho: Um tamanho máximo de arquivo é imposto para evitar ataques de negação de serviço, chamado de DoS, e sobrecarga do servidor. Renomeação de arquivos: Os arquivos enviados são renomeados com um identificador único e um timestamp, prevenindo colisões de nomes e dificultando a execução de scripts maliciosos com nomes previsíveis. Armazenamento em diretórios específicos: Os arquivos são armazenados em diretórios dedicados (images/profiles/, images/news/, etc.), separados do código-fonte da aplicação. 

Figura 26 - trecho do código para upload de arquivo 

```php
<?php
// Arquivos: admin/edit_people.php
// Uploaduveo de fotode perfil
if (asset(\$_FILES['photo']) && \$FILES['photo']['error'] == UPGoad_ERR_OK) {
\upload_dir = '.images/profiles';
// Criar diretorio se não existir
if (!file_exists(\$upload_dir)) {
mkdir(\$upload_dir, 0755, true);
}
// 1. Validacao de extensions
\$file_extension = strtolower(pathinfo(\$_FILES['photo']['name'], PATHINFO Extensions);
\$allowed Extensions = ['jpg', 'jpeg', 'png', 'gif'];
if (in_array(\$file_extension, \$allowed Extensions)) {
// 2. Validacao de tamanho (5MB maximo)
if (\$_FILES['photo']['size'] <= 5 * 1024 * 1024) {
// 3. Renomeacao com ID unique
\$newphotofilename =uniqid().‘.’.\$file_extension;
\$upload_path = \$upload_dir . \$newphotofilename;
// 4. Mover arquivos para diretorio seguro
if (move_upload文件(\$_FILES['photo'])['tmp_name'], \$upload_path) {
// 5. Remove fotogantiga se existir
if (\$person['photo'] && file_exists(\$upload_dir . \$person['photo'])) {
unlink(\$upload_dir . \$person['photo']);
}
\$photofilename = \$newphotofilename;
} else {
\$error_message = "Error uploading new photo."; }
} else {
\$error_message = "Photo must be maximum 5MB."; }
} else {
\$error_message = "Invalid file format. Use only JPG, PNG or GIF."; }
}
```

Fonte: Próprio autor (2025). 

# 5.6 Integração com o Site Público

A integração com o site público do LAPPS foi projetada para ser o mais transparente e simples possível para os usuários. As páginas já existentes, como people.php e projects.php, foram adaptadas e passaram a buscar dados diretamente no banco de dados alimentado pelo sistema administrativo. Em vez de manter listas estáticas no código-fonte, chamado de hardcoded, o conteúdo é montado dinamicamente a cada requisição, o que assegura que qualquer alteração feita no sistema seja refletida imediatamente no site. Essa integração transforma o portal do LAPPS em um canal mais vivo de divulgação científica e institucional, reduzindo o esforço de manutenção e diminuindo o risco de desatualização de informações. 

# 6 Resultados e Avaliação de Qualidade

Este capítulo apresenta os resultados obtidos com a implementação do Administrative System para o LAPPS, detalhando as funcionalidades entregues e a avaliação de sua qualidade. A análise é feita com base nos critérios de aceitação e métricas definidos na metodologia, abrangendo aspectos funcionais, de segurança, performance e acessibilidade. 

# 6.1 Resultados Obtidos

O desenvolvimento do sistema resultou na entrega de uma plataforma web funcional, que atendeu integralmente aos requisitos funcionais estabelecidos na Seção 4.1. Foram implementados com sucesso os cinco módulos principais de gerenciamento de conteúdo, cada um com as operações completas de criação, leitura, atualização e exclusão, mais o módulo de autenticação de usuário: 

O Módulo de Autenticação permite o login e logout de usuários administradores, com controle de sessão e proteção contra acesso não autorizado às áreas restritas do painel. O módulo de Publicações oferece uma interface para cadastrar, listar, editar e remover publicações científicas, incluindo metadados detalhados e a opção de upload de arquivos PDF. O módulo de Pessoas gerencia os perfis dos membros do laboratório (professores, alunos, colaboradores), com campos para informações pessoais, área de atuação e upload de fotos. O módulo de Projetos permite o registro e a gestão de projetos de pesquisa, com dados como título, descrição, período de execução e status. O módulo de Aplicações de Pesquisa facilita o cadastro de aplicações e ferramentas desenvolvidas pelo LAPPS, com descrições e links relevantes. E o módulo de Notícias: Habilita a criação, edição e publicação de notícias institucionais, com controle de data e status de visibilidade. Todos esses módulos operam no ambiente XAMPP, garantindo compatibilidade com a infraestrutura existente do LAPPS. 

O sistema de autenticação e controle de acesso foi implementado conforme o RF1, garantindo que apenas usuários com credenciais válidas possam acessar o painel administrativo. As senhas são armazenadas de forma segura (com hash), e as sessões são gerenciadas para proteger contra acessos indevidos. Isso assegura a integridade e a confidencialidade das informações administrativas (Figura 27). 


Figura 27 - Tela de autenticação


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/27143e4c86f3ce2b935ffdc0b56829eb2b4949095456d6bacdfe38d8989fcbe0.jpg)



Fonte: Próprio autor (2025).


A interface do usuário foi projetada com foco na usabilidade para usuários não técnicos, conforme o RNF3. As telas são intuitivas, com navegação clara e feedback visual para as ações realizadas (mensagens de sucesso ou erro). A padronização dos formulários e a consistência do layout contribuem para uma curva de aprendizado reduzida, permitindo que os administradores do LAPPS utilizem o sistema com autonomia. 

A integração com o site público do LAPPS foi um resultado crucial (RF8). As páginas estáticas existentes foram convertidas para consumir dados dinamicamente do banco de dados do sistema administrativo. Isso significa que qualquer atualização realizada no painel (uma nova publicação, um projeto atualizado, uma notícia) é refletida instantaneamente no site público, eliminando a necessidade de intervenção manual no código-fonte. 

# 6.2 Avaliação de Qualidade

A avaliação da qualidade do sistema foi realizada com base nos requisitos não‑funcionais (RNFs) e nos critérios de aceitação (CAs) definidos na Seção 4.2 e 4.3, utilizando uma ferramenta de auditoria e avaliação automatizada Lighthouse . 

# 6.2.1 Segurança

A segurança foi um dos pilares fundamentais do desenvolvimento, conforme foi especificado na RNF2. Para cumprir com esse requisito, estabeleceu-se o uso de PDO com consultas parametrizadas nas operações de banco de dados, sanitização sistemática de saídas com funções como htmlspecialchars, validação de todas as entradas vindas do usuário no servidor e armazenamento de senhas exclusivamente na forma de hashes seguros por meio de password_hash (bcrypt) e password_verify. A gestão de sessões foi centralizada em uma classe de autenticação, usada obrigatoriamente em todas as rotas administrativas, e uploads de arquivos passaram a ser validados quanto a tipo, extensão e tamanho. 

# 6.2.2 Performance

A performance do sistema requisitada na RNF5 foi avaliada com foco na experiência do usuário. para isso foi adotada como referência uma pontuação mínima de 90 na métrica “Desempenho” do Lighthouse, além de cuidados com otimização de consultas SQL, uso de índices em colunas frequentemente consultadas e aproveitamento de Content Delivery Network (CDN) para bibliotecas externas, quando necessário. Também se buscou manter o código organizado de forma modular para facilitar a manutenção e futuras melhorias. Esses resultados garantem uma experiência de navegação fluida e eficiente para os usuários. É possível ver as notas de desempenho nas Figuras 28 a 30 das principais páginas, como os módulos possuem características semelhantes, as notas de desempenho também foram, por isso, não se torna necessário mostrar todas elas. 


Figura 28 - Pontuação de desempenho da tela de login


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/cb4df02b71a94058168000d1e9c0dc6e018c708614859445cdfd8e02124fe54e.jpg)


Fonte: Próprio autor (2025). 


Figura 29 - Pontuação de desempenho da tela de dashboard


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/8a0db9df91ac5440438d9c79bcb7cb782b29bb16b0b0fc2de6dbd506964a79db.jpg)



Fonte: Próprio autor (2025).



Figura 30 - Pontuação de desempenho da tela de Publicações


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/c39b4db1297c400affb389041b7899f262629bb045b85872b1b45bda70b472e4.jpg)



Fonte: Próprio autor (2025).


# 6.2.3 Acessibilidade

A acessibilidade também foi um dos focos centrais do projeto que necessitou de bastante atenção. Para conseguir entregar o que foi requisitado na RNF1. Essa exigência se traduziu em práticas concretas, como o uso de HTML5 semântico, landmarks (header, nav, main, footer), cabeçalhos hierárquicos coerentes, labels adequadas em formulários, atributos alt descritivos em imagens, foco visível, ordem lógica de tabulação e suporte à navegação por teclado. Adicionalmente, foi definida como meta uma pontuação mínima de 90 na métrica “Acessibilidade” (Figura 31 e 32) nas auditorias realizadas pela ferramenta Lighthouse e compatibilidade com leitores de tela, como o NVDA. A navegação por teclado foi testada e validada em todos os fluxos principais de cadastro, edição e exclusão, permitindo que usuários que não utilizam mouse possam interagir plenamente com o sistema. O foco visível é claro e a ordem de tabulação é lógica. Testes manuais com leitor de tela NVDA em fluxos primários login, cadastro de publicação confirmaram a compatibilidade e a correta leitura dos elementos da interface, incluindo labels de formulários e mensagens de feedback. A implementação e combinação de todas essas tecnologias contribuiu para uma estrutura de conteúdo robusta e interpretável por tecnologias assistivas. 


Figura 31 - Pontuação de acessibilidade da tela de autenticação


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/f7dca5c34e782ffb5e48d92fb0a6d22daa2549d61e945cf70e5a885bfac85bdd.jpg)



Fonte: Próprio autor (2025).



Figura 32 - Pontuação de acessibilidade da tela de Publicações


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/e74dcb2c-9e43-4e76-9caa-855a260d283a/24e9ce2092739255837b58142df942a6741960e0cdd9f09d16b4442c13a6fe72.jpg)



Fonte: Próprio autor (2025).


# 6.2.4 Usabilidade e Manutenção

Embora os testes de usabilidade com mais usuários, incluindo usuários com deficiência, não tenham sido possível ser feito, a interface foi projetada para ser intuitiva. A taxa de sucesso em tarefas chave, como criar uma publicação ou editar um perfil, foi alta, indicando que o sistema é fácil de usar para usuários não técnicos. Para isso, a interface foi organizada com base em componentes visuais consistentes utilizando Bootstrap, as mensagens de erro e sucesso foram pensadas para serem objetivas e claras para o usuário, cumprindo assim com a RNF3. Tudo isso foi produzido e organizado na documentação técnica com junto com descrição da arquitetura, scripts de banco de dados e padrões de desenvolvimento utilizados no projeto para auxiliar na manutenção. 

# 6.3 Impactos

A implementação do sistema administrativo resultou em impactos positivos para a gestão do site do LAPPS. O benefício mais significativo é a redução da dependência técnica, beneficiando a eficiência operacional. O tempo de uma atualização de conteúdo foi drasticamente reduzido de 15–30 minutos, quando feito por um desenvolvedor, para uma média de 3–5 minutos, podendo ser feito por qualquer membro autorizado, caracterizando uma melhoria de aproximadamente $90 \%$ no lead time para a publicação. Este ganho de eficiência confere autonomia aos membros do laboratório para realizar a manutenção do site, promovendo uma gestão de conteúdo eficiente e descentralizada. A maior agilidade na atualização permite que publicações, projetos e notícias sejam divulgados em tempo sem atrasos, aumentando a visibilidade da produção científica do LAPPS. 

Além disso, o sistema assegura a conformidade com as diretrizes de acessibilidade WCAG, ampliando o acesso do sistema a usuários com deficiência e fortalecendo a imagem institucional. Por fim, o sistema impõe uma padronização na forma de inserção e exibição das informações, garantindo a consistência do conteúdo. Em síntese, o projeto transformou o site do LAPPS de um repositório estático em uma plataforma dinâmica, eficiente e em parte, inclusiva. 

# 7 Considerações Finais

O desenvolvimento do Sistema Administrativo Acadêmico Dinâmico para o site do LAPPS surgiu da necessidade de resolver um problema simples, mas que trazia impactos importantes para o laboratório: a dificuldade de atualizar o conteúdo do site, que até então possuía uma estrutura estática e dependia totalmente de alguém com conhecimento técnico. Essa limitação tornava o processo lento, pouco flexível e, muitas vezes, inviável no dia a dia. Com a construção do novo sistema, foi possível transformar esse cenário. O projeto integrou aspectos ligados à arquitetura de software, segurança, usabilidade e acessibilidade, resultando em uma ferramenta mais moderna e prática para quem precisa gerenciar informações. O painel administrativo desenvolvido permite que pesquisadores, bolsistas ou gestores atualizem o conteúdo do portal sem precisar recorrer a um desenvolvedor, tornando o fluxo de manutenção mais ágil e independente. 

Outro ponto importante do trabalho foi a preocupação com acessibilidade. Seguindo recomendações baseadas na WCAG, buscou-se tornar o site mais inclusivo e coerente com as diretrizes atuais sobre acesso igualitário à informação. Isso não apenas melhora a experiência de diferentes perfis de usuários, como também reforça o compromisso institucional com práticas acessíveis e alinhadas ao uso responsável da tecnologia. O projeto, como um todo, mostrou que é possível aplicar conhecimentos teóricos adquiridos ao longo da formação acadêmica em um problema real, enfrentando desafios técnicos, estruturais e de tomada de decisão. Esse processo trouxe aprendizados tanto sobre desenvolvimento web quanto sobre organização de requisitos, comunicação com usuários e adaptação da solução ao contexto do laboratório. 

Os resultados obtidos indicam que o sistema contribui de forma direta para o funcionamento do LAPPS, ao facilitar a atualização de informações e tornar o portal mais acessível e alinhado às necessidades do laboratório. Além disso, o código estruturado e a arquitetura adotada deixam espaço para futuras melhorias, como integração com outros serviços, ampliação das funcionalidades, como implementar um editor de texto mais robusto (CKEditor ou WYSIWYG) e com mais funcionalidades de personalizar os textos do sistema administrativo ou novas soluções voltadas à automação. Assim, o trabalho cumpre não apenas seu papel acadêmico, mas também oferece um produto útil e aplicável ao laboratório LAPPS, 

servindo como base para evoluções e pesquisas futuras. 

# Referências



ALBUQUERQUE, Danyllo; PONCIANO, Gustavo; PEDRO, João; SANTOS, Arlan; SILVA, Fabrício; OLIVEIRA, Caíque; VASCONCELOS, Felipe; HONORATO, Thiago. Análise da Conformidade com Acessibilidade Digital: Um Estudo no Contexto dos Websites das Universidades Federais Brasileiras. In: LATIN AMERICAN SYMPOSIUM ON DIGITAL GOVERNMENT (LASDIGOV), 12., 2024, Brasília/DF. Anais [...]. Porto Alegre: Sociedade Brasileira de Computação, 2024. p. 133-144. DOI: https://doi.org/10.5753/wcge.2024.2891. Acesso em: 26 out. 2025. 





ANÁLISE da acessibilidade em sites de bibliotecas de universidades públicas. Revista Brasileira de Biblioteconomia e Documentação, São Paulo, v. 20, p. 1-15, 2024. Disponível em: https://rbbd.febab.org.br/rbbd/article/view/2048. Acesso em: 26 out. 2025. 





BRASIL. Decreto $\mathrm { n } ^ { \circ } 9 . 2 9 6 $ , de 01 de março de 2018. Institui o Modelo de Acessibilidade em Governo Eletrônico (eMAG). Acesso em: 28 out. 2025. 





W3C. Web Content Accessibility Guidelines (WCAG) 2.1. World Wide Web Consortium, 2018. Acesso em: 28 out. 2025. 





ALMEIDA, Rodrigo Monteiro Guedes de. Impactos da arquitetura de microsserviços na manutenção de sistemas corporativos. Revista LEV, São José dos Pinhais, v. XIV, n. XXXII, p. 83-101, 2024. Disponível em: https://periodicos.newsciencepubl.com/LEV/article/view/5211/7361. Acesso em: 3 nov. 2025. 





OLIVEIRA, Lanna Mayra Silva. Caracterização do conceito de modularidade no desenvolvimento de linguagens de programação. 2017. 58 f. Monografia (Graduação em Sistemas de Informação) – Instituto de Ciências Exatas e Aplicadas, Universidade Federal de Ouro Preto, João Monlevade, 2017. Disponível em: https://www.monografias.ufop.br/bitstream/35400000/367/1/MONOGRAFIA_Caracteriza%C 3%A7%C3%A3oConceitoModularidade.pdf. Acesso em: 03 nov. 2025. 





BRASIL. Laboratório Nacional de Computação Científica. Os quatro pilares da segurança da informação – Confidencialidade, Disponibilidade, Integridade e Autenticidade. 2024. Disponível em: https://www.gov.br/lncc/pt-br/centrais-de-conteudo/campanhas-de-conscientizacao/gestao-de-





seguranca-da-informacao/os-quatro-pilares-da-seguranca-da-informacao-2013-confidencialid ade-disponibilidade-integridade-e-autenticidade. Acesso em: 3 nov. 2025. 





LEMOS, Samuel Afonso da Câmara. Uma Avaliação da Acessibilidade dos Portais Web da Justiça Federal na $5 ^ { \mathrm { a } }$ Região. Natal-RN: Universidade Federal do Rio Grande do Norte, Instituto Metrópole Digital, Programa de Residência em Tecnologia da Informação, 2023. Acesso em: 03 nov. 2025. 





COUTO RAMON, J. do. Sistema de Gerenciamento de Conteúdo na Web. TCC (Especialização) – UFMG, 2011. Acesso em: 08 nov. 2025. 





EXPERIÊNCIA do Usuário: Uma abordagem das 10 heurísticas de Nielsen no problema da acessibilidade Web no Brasil. Revista Semiárido De Visu, v. 12, n. 2, 2024. DOI: 10.31416/rsdv.v12i2.598. Disponível em: 





https://semiaridodevisu.ifsertao-pe.edu.br/index.php/rsdv/article/view/598. Acesso em: 08 nov. 2025. 





GABRIELI, Leandro; CORTIMIGLIA, Marcelo; RIBEIRO, José Luis. Modelagem e avaliação de um sistema modular para gerenciamento de informação na Web. Ciência da Informação, Brasília, v. 36, n. 1, p. 35-53, jan./abr. 2007. DOI: 10.1590/S0100-19652007000100003. Disponível em: 





https://www.scielo.br/j/ci/a/SQ3xyHqZ4GpyThPFKmBSh6C/. Acesso em: 08 nov. 2025. 





Choi, J.; Jung, Y.-A.; Ko, H. Comparative Analysis of SQL Injection Defense Mechanisms Based on Three Approaches: PDO, PVT, and ART. Applied Sciences, v. 15, n. 23, artigo 12351, 2025. Disponível em: https://www.mdpi.com/2076-3417/15/23/12351. Acesso em: 15 nov. 2025. 





SINGH, A. Designing Inclusive Web Applications with Accessibility in Mind. International Journal for Multidisciplinary Research (IJFMR), v. 6, n. 5, artigo 29091, 2024. Disponível em: https://www.ijfmr.com/papers/2024/5/29091.pdf. Acesso em: 15 nov. 2025. 





OWASP FOUNDATION. Introduction – OWASP Top 10:2025 RC1. 2025. Disponível em: https://owasp.org/Top10/2025/0x00_2025-Introduction/. Acesso em: 20 nov. 2025. 





WAKE. A importância da inclusão digital e acessibilidade na tecnologia. Disponível em: https://wake.tech/blog/acessibilidade-na-tecnologia/. Acesso em: 20 nov. 2025. 





LEITE, Manoel Victor Rodrigues. Um estudo sobre o conhecimento em acessibilidade digital entre desenvolvedores de aplicações móveis no Brasil. 2020. Dissertação (Mestrado) – 



Universidade de São Paulo, São Paulo, 2020. Disponível em: https://www.teses.usp.br/teses/disponiveis/100/100131/tde-27032020-082040/publico/versaoc orrigida.pdf. Acesso em: 20 nov. 2025. 