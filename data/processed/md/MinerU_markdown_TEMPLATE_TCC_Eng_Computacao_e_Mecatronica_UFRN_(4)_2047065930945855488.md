# Desenvolvimento de um Agente Cognitivo Integrado ao WhatsApp com Busca Semântica em Grafos de Conhecimento

Lucas Felipe Galvão Silva 

Orientador: Prof. Dr. Ivanovitch Medeiros Dantas da Silva 

Natal, RN, 2025 

# Desenvolvimento de um Agente Cognitivo Integrado ao WhatsApp com Busca Semântica em Grafos de Conhecimento

# Lucas Felipe Galvão Silva

Orientador: Prof. Dr. Ivanovitch Medeiros Dantas da Silva 

Trabalho de Conclusão de Curso de Graduação na modalidade Monografia, submetido como parte dos requisitos necessários para conclusão do curso de Engenharia de Computação pela Universidade Federal do Rio Grande do Norte (UFRN/CT). 

Natal, RN, 2025 

# Universidade Federal do Rio Grande do Norte - UFRN

# Sistema de Bibliotecas - SISBI

# Catalogação de Publicação na Fonte. UFRN - Biblioteca Central Zila Mamede

Silva, Lucas Felipe Galvão. 

Desenvolvimento de um agente cognitivo integrado ao WhatsApp com busca semântica em grafos de conhecimento / Lucas Felipe Galvão Silva. - 2025. 

53f.: il. 

Monografia (Graduação) - Universidade Federal do Rio Grande do Norte, Departamento de Engenharia de Computação e Automação, Engenharia de Computação, Natal, 2025. 

Orientação: Prof. Dr. Ivanovitch Medeiros Dantas da Silva. 

1. Agente cognitivo - Monografia. 2. Busca semântica - Monografia. 3. Grafos de conhecimento - Monografia. 4. Inteligência artificial - Monografia. 5. Modelos de Linguagem de Grande Escala - Monografia. I. Silva, Ivanovitch Medeiros Dantas da. II. Título. 

RN/UF/BCZM 

CDU 004 

# Desenvolvimento de um Agente Cognitivo Integrado ao WhatsApp com Busca Semântica em Grafos de Conhecimento

Lucas Felipe Galvão Silva 

Monografia aprovada em 28 de Novembro de 2025, pela banca examinadora composta pelos seguintes membros: 

Prof. Dr. Ivanovitch Medeiros Dantas da Silva (orientador) . . . . . . DCA/UFRN 

Prof. Dr. Carlos Manuel Dias Viegas . . DCA/UFRN 

Thaís de Araújo de Medeiros 

# Agradecimentos

A Deus, por ter me proporcionado saúde, discernimento e paciência na jornada acadê- mica. 

À minha família, em especial meu pai Francisco Paulo, por sempre ter me incentivado a estudar e proporcionar os meios para isso. 

Aos meus colegas de faculdade, que me ajudaram nos trabalhos e partilharam o conhecimento para enriquecer a trajetória. 

Aos bons amigos que fiz na UERN e UFRN, que tornaram a vida menos penosa e mais feliz. 

Ao meu orientador Prof. Dr. Ivanovitch Medeiros, que prontamente aceitou ser meu guia na reta final do curso. 

À minha companheira Carolyne Náthaly por estar ao meu lado dando conselhos e ordens. 

# Resumo

A evolução da Inteligência Artificial (IA) e o Processamento de Linguagem Natural (PLN) transformaram a interação entre humanos e sistemas, permitindo interfaces mais fluidas. Contudo, no domínio jurídico, a recuperação de informações enfrenta barreiras devido à extensão, densidade e complexidade da linguagem legislativa. A busca tradicional por palavras-chave mostra-se muitas vezes ineficaz para capturar nuances semânticas e relações entre conceitos dispersos nas normas. Visando solucionar esse problema, este trabalho desenvolve um agente cognitivo integrado ao WhatsApp capaz de realizar buscas semânticas em um grafo de conhecimento (KG) jurídico, utilizando o Código Civil como base. A metodologia consistiu na extração e estruturação hierárquica do texto legislativo (capítulos, artigos, parágrafos) via expressões regulares para construção de um Grafo de Conhecimento no banco Neo4j. O sistema utiliza embeddings para calcular a similaridade semântica entre a consulta do usuário e os nós do grafo. A orquestração do fluxo conversacional foi implementada na plataforma N8n, integrando uma interface de programação de aplicações (API) do WhatsApp (via Twilio) a uma API de consulta vetorial. Os resultados validaram a eficácia do agente em retornar trechos legislativos coerentes para consultas em linguagem natural, preservando a estrutura lógica da lei. Conclui-se que a união de grafos de conhecimento e interfaces de mensageria reduz a fricção no estudo de textos complexos, provendo uma ferramenta de consulta rápida, contextualizada e acessível. 

Palavras-chave: Agente cognitivo; Busca semântica; Grafos de conhecimento; Inteligência artificial; Modelos de Linguagem de Grande Escala 

# Abstract

The evolution of Artificial Intelligence (AI) and Natural Language Processing (NLP) has transformed the interaction between humans and systems, enabling more fluid interfaces. However, in the legal domain, information retrieval faces barriers due to the length, density, and complexity of legislative language. Traditional keyword search often proves ineffective in capturing semantic nuances and relationships between concepts dispersed across norms. Aiming to solve this problem, this work develops a cognitive agent integrated into WhatsApp capable of performing semantic searches within a legal knowledge graph (KG), using the Civil Code as a basis. The methodology consisted of extracting and hierarchically structuring the legislative text (chapters, articles, paragraphs) via regular expressions to build a Knowledge Graph in the Neo4j database. The system uses embeddings to calculate semantic similarity between the user query and the graph nodes. The conversational flow orchestration was implemented on the platform N8n, integrating the WhatsApp Application Programming Interface (API) (via Twilio) with a vector search API. The results validated the agent’s effectiveness in returning coherent legislative excerpts for natural language queries, preserving the law’s logical structure. It is concluded that combining knowledge graphs and messaging interfaces reduces friction in studying complex texts, providing a fast, contextualized, and accessible consultation tool. 

Keywords: Artificial intelligence; Cognitive agent; Large Language Models; Semantic search; Knowledge graphs 

# Sumário

# Sumário i

# Lista de Figuras iii

# Lista de Tabelas v

# Lista de abreviaturas e siglas vii

# 1 Introdução 1

1.1 Contextualização 1 

1.2 Motivação . . 2 

1.3 Objetivos 3 

1.4 Trabalhos Relacionados . . 3 

1.5 Organização do texto 5 

# 2 Fundamentação Teórica 7

2.1 Agentes . . 7 

2.2 Modelos de Linguagem de Grande Escala . . . 8 

2.3 Chatbots . 8 

2.4 Embeddings . . . 9 

2.5 Grafos de Conhecimento 9 

2.6 Geração Aumentada por Recuperação 10 

# 3 Metodologia 13

3.1 Desenvolvimento da Base Gráfica 14 

3.1.1 Obtenção dos Dados 14 

3.1.2 Limpeza e Normalização dos Dados . . . 15 

3.1.3 Pré-processamento e Vetorização 15 

3.1.4 Desenvolvimento do Grafo de Conhecimento 16 

3.2 Desenvolvimento do Fluxo de Comunicação . . 16 

3.2.1 Integração com WhatsApp via Twilio . . 16 

3.2.2 API de Comunicação (Backend) . . . 16 

3.2.3 Orquestração de Fluxo no N8n . . . . 17 

3.3 Protocolo de Validação 17 

# 4 Resultados 19

4.1 Geração do Grafo de Conhecimento 19 

4.1.1 Limpeza e Normalização dos Dados . . . . . 19 

4.1.2 Divisão de Chunks 21 

4.1.3 Conversão em Documentos Estruturados 21 

4.1.4 Geração de Embeddings . . . . 22 

4.1.5 Modelagem e Visualização do Grafo . . . . . 22 

4.2 Fluxo de Comunicação com o Usuário . . . 23 

4.2.1 API de Comunicação . . 23 

4.2.2 Resultados da Integração no N8n 24 

4.3 Análise da Interação e Recuperação Semântica 26 

# 5 Conclusão 31

5.1 Trabalhos Futuros . . 31 

# Referências bibliográficas 33

# Lista de Figuras

2.1 Exemplo de grafo de conhecimento. . . . 10 

3.1 Fluxo completo da comunicação com o usuário. . . 14 

4.1 Visualização da hierarquia do grafo no Neo4j. . . 23 

4.2 Fluxo de integração no N8n. 24 

4.3 Recebimento no Webhook. 25 

4.4 Tratamento dos dados. 25 

4.5 Resposta da API. 26 

4.6 Envio para Twilio. . 26 

4.7 Respostas obtidas no WhatsApp. . . 27 

4.8 Limitação na busca por referência numérica. . . 29 

# Lista de Tabelas

4.1 Exemplo da limpeza do corpus . . 20 

4.2 Exemplos de Chunks gerados . . 21 

4.3 Amostra dos embeddings gerados 22 

4.4 Resultados da busca semântica, texto “fale sobre homicídio” 28 

4.5 Resultados da busca semântica, texto “fale sobre dívida” 28 

# Lista de abreviaturas e siglas

AKN: Akoma Ntoso 

API: Application Programming Interface — Interface de Programação de Aplicações 

BDI: Beliefs, Desires, Intentions — Crenças, Desejos e Intenções 

GPT: Generative Pre-trained Transformer — Transformador Generativo Pré-treinado 

HTTP: Hypertext Transfer Protocol — Protocolo de Transferência de Hipertexto 

HTTPS: Hypertext Transfer Protocol Secure — Protocolo de Transferência de Hipertexto Seguro 

IA: Inteligência Artificial 

JSON: JavaScript Object Notation — Notação de Objetos do JavaScript 

KG: Knowledge Graph — Grafo de Conhecimento 

LGPD: Lei Geral de Proteção de Dados 

LLaMA: Large Language Model Meta AI — Modelo de Linguagem de Grande Escala da Meta AI 

LLM: Large Language Model — Modelo de Linguagem de Grande Escala 

LSA: Latent Semantic Analysis — Análise Semântica Latente 

NER: Named Entity Recognition - Reconhecimento de Entidade Nomeada 

NLG: Natural Language Generation — Geração de Linguagem Natural 

NLP: Natural Language Processing — Processamento de Linguagem Natural 

NLU: Natural Language Understanding — Entendimento de Linguagem Natural 

PaLM: Pathways Language Model — Modelo de Linguagem Pathways 

PDF: Portable Document Format — Formato de Documento Portátil 

RAG: Retrieval-Augmented Generation — Geração Aumentada por Recuperação 

RDF: Resource Description Framework — Estrutura de Descrição de Recursos 

REST: Representational State Transfer — Transferência de Estado Representacional 

URL: Uniform Resource Locator — Localizador Uniforme de Recursos 

UX: User Experience — Experiência de Usuário 

XML: Extensible Markup Language — Linguagem de Marcação Extensível 

# Capítulo 1 Introdução

Neste capítulo introdutório é apresentado, em um primeiro plano, o contexto atual da evolução da Inteligência Artificial, com destaque para o surgimento dos agentes cognitivos e a popularização dos Modelos de Linguagem de Grande Escala (LLMs) como ferramentas de interação. Nesse cenário, discute-se a necessidade de aplicar essas tecnologias em domínios especializados, bem como os desafios de precisão e confiabilidade que ainda limitam seu uso, especialmente no contexto jurídico. Outro ponto tratado é a proposta de integração entre a busca semântica em Grafos de Conhecimento e interfaces de mensagens populares, visando mitigar problemas como a alucinação de dados e democratizar o acesso à informação técnica. Ao final deste capítulo, serão apresentadas a motivação do trabalho, bem como os objetivos traçados, as contribuições do estudo e a organização estrutural dos conteúdos subsequentes. 

# 1.1 Contextualização

A evolução dos sistemas de interação humano-máquina tem migrado de interfaces baseadas em comandos rígidos para agentes conversacionais capazes de processar linguagem natural. Historicamente, os primeiros chatbots operavam mediante regras pré- definidas e reconhecimento de padrões simples, o que limitava sua capacidade de manter diálogos coerentes fora de domínios específicos (SHAWAR; ATWELL, 2007). No entanto, a demanda por sistemas que não apenas automatizem respostas, mas que compreendam o contexto do usuário, impulsionou o desenvolvimento de novas arquiteturas baseadas em Inteligência Artificial (ADAMOPOULOU; MOUSSIADES, 2020). 

Recentemente, a consolidação dos Modelos de Linguagem de Grande Escala transformou esse cenário ao permitir a geração de textos com fluidez comparável à humana. Apesar desse avanço, a literatura aponta limitações críticas no uso isolado desses modelos em ambientes corporativos ou técnicos. Conforme destacado por Huang e Huang (2024), modelos generativos são suscetíveis a "alucinações", fenômeno no qual o sistema produz informações plausíveis, porém factualmente incorretas, devido à natureza probabilística de sua arquitetura e à falta de acesso a dados atualizados em tempo real. 

Para mitigar tais problemas em domínios que exigem alta precisão, como a engenharia e o direito, surge a necessidade de integrar a capacidade linguística dos LLMs com bases de conhecimento estruturadas. A utilização de Grafos de Conhecimento permite 

representar informações complexas e suas inter-relações de forma explícita, oferecendo uma fonte de verdade verificável para o agente cognitivo (JI et al., 2020). A sinergia entre LLMs e Grafos de Conhecimento possibilita a construção de sistemas de tutoria e suporte inteligentes, onde a resposta gerada é fundamentada em dados recuperados semanticamente, e não apenas em predições estatísticas (WANG; ZHAN; QIN, 2025; NEGRO et al., 2025). 

Nesse contexto, a aplicação dessas tecnologias exige interfaces que sejam onipresentes no cotidiano dos usuários para garantir a acessibilidade da informação. A integração de agentes cognitivos avançados em plataformas de mensageria instantânea apresenta-se como uma solução viável para democratizar o acesso a conhecimentos técnicos, como legislações e normas, sem exigir que o usuário domine ferramentas de busca complexas. Especificamente no âmbito legislativo, a modelagem de sistemas em grafos de propriedade tem demonstrado eficácia na detecção de padrões e na recuperação precisa de informações, conforme proposto por Colombo, Bernasconi e Ceri (2024), fundamentando a abordagem adotada nesta pesquisa. 

# 1.2 Motivação

A motivação primária para este trabalho decorre da necessidade de otimizar a recuperação de informações em grandes bases de dados não estruturadas. Em contextos profissionais e técnicos, a busca por palavras-chave mostra-se frequentemente ineficiente, pois falha em capturar a semântica e as relações lógicas entre os documentos. Embora os LLMs tenham demonstrado capacidade de processar texto natural, eles enfrentam uma limitação arquitetural crítica conhecida como "conhecimento paramétrico estático". Segundo Lewis et al. (2020), esses modelos não possuem a capacidade nativa de acessar ou atualizar informações externas após o seu treinamento, o que compromete sua aplicabilidade em cenários que exigem precisão factual e dados atualizados, como na consulta a legislações ou manuais técnicos. 

Para mitigar a obsolescência e a alucinação de dados, torna-se imperativo o desenvolvimento de arquiteturas que desacoplem o raciocínio linguístico do armazenamento de conhecimento. A integração de LLMs com Grafos de Conhecimento surge como uma solução de engenharia robusta. Diferentemente de bancos de dados vetoriais simples, os KGs preservam a estrutura explícita das relações entre entidades. Essa abordagem estrutural permite que o sistema não apenas recupere fragmentos de texto, mas construa respostas baseadas em conexões verificáveis, transformando dados brutos em informação acionável com maior rastreabilidade. 

Outro vetor de motivação é a barreira de usabilidade imposta por sistemas corporativos tradicionais. A eficácia de uma ferramenta de software não reside apenas em sua precisão técnica, mas também na sua acessibilidade. A escolha de integrar o agente cognitivo ao WhatsApp justifica-se pela onipresença da plataforma e pela redução da curva de aprendizado para o usuário final. Lantarón et al. (2022) destacam que o uso de interfaces móveis familiares favorece a adoção de tecnologias e o engajamento contínuo, permitindo que a consulta técnica seja realizada de forma ágil e integrada ao fluxo de trabalho existente, sem a necessidade de novos logins ou treinamentos complexos. 

Por fim, a pesquisa é motivada pelos desafios de avaliar a qualidade de sistemas conversacionais orientados a tarefas em domínios específicos. Deriu et al. (2021) ressaltam que a avaliação de sistemas de diálogo modernos exige métricas que vão além da fluidez textual, focando no sucesso da tarefa e na satisfação do usuário. Dessa forma, este trabalho contribui tecnicamente ao propor e validar uma arquitetura de integração que une a busca semântica estruturada à interfaces de mensageria, preenchendo uma lacuna de implementação prática que visa garantir a integridade da informação recuperada e a usabilidade em dispositivos móveis. 

# 1.3 Objetivos

O presente trabalho tem como objetivo principal desenvolver um agente cognitivo integrado ao WhatsApp capaz de realizar buscas semânticas em um grafo de conhecimento. A proposta busca unir técnicas de inteligência artificial, processamento de linguagem natural e representação de conhecimento em grafos, de modo a construir um sistema conversacional, permitindo respostas contextuais e relevantes ao usuário. 

De forma mais específica, neste trabalho proponho a: 

1. Implementar um agente cognitivo funcional que opere por meio do aplicativo de mensagens WhatsApp, utilizando sua API para comunicação entre o usuário e o sistema; 

2. Modelar e construir um grafo de conhecimento que armazene informações de domínio específico, possibilitando consultas semânticas e relações entre conceitos; 

3. Aplicar técnicas de embeddings semânticos para viabilizar a busca por similaridade entre nós do grafo, permitindo que o agente compreenda o significado das consultas do usuário mesmo quando formuladas de maneiras diferentes; 

4. Integrar o agente ao grafo de conhecimento, estabelecendo um fluxo completo de interação, da entrada em linguagem natural até a recuperação e formatação da resposta; 

5. Avaliar o desempenho e a eficiência do sistema, considerando métricas de similaridade semântica, relevância das respostas e usabilidade no contexto conversacional. 

# 1.4 Trabalhos Relacionados

A literatura consultada para este trabalho abrange três eixos fundamentais: a estruturação de documentos legislativos em Grafos de Conhecimento, o desenvolvimento de agentes conversacionais integrados a bases estruturadas e a aplicação de busca semântica para recuperação de informação. A seguir, são analisadas as abordagens existentes, destacando suas contribuições e as diferenças metodológicas em relação à proposta deste trabalho. 

A representação de normas jurídicas em formatos computáveis é o primeiro passo para habilitar sistemas inteligentes. Nesse contexto, Colombo, Bernasconi e Ceri (2024) propõem uma alternativa aos modelos tradicionais baseados em Resource Description 

Framework (RDF). Aplicado à legislação italiana, o estudo desenvolve um pipeline de extração de entidades e relacionamentos a partir de textos normativos, convertendo-os para o formato Akoma Ntoso (AKN) e, posteriormente, para um grafo de propriedade no Neo4j. Embora o trabalho de Colombo et al. demonstre a eficácia do grafo para consultas complexas, ele se limita à etapa de modelagem e consulta direta via banco de dados, sem integrar uma camada de interação em linguagem natural ou um agente cognitivo. 

No cenário nacional, Oliveira et al. (2025) realizam uma investigação análoga focada na legislação brasileira, especificamente nos dados da Assembleia Legislativa do Rio Grande do Norte. Os autores utilizam Processamento de Linguagem Natural e LLMs para analisar a legibilidade do corpus e construir um grafo de conhecimento, validando a viabilidade técnica nesse domínio. A relação com o presente trabalho é direta, visto que ambos operam sobre contextos legislativos similares. Contudo, as abordagens são complementares: enquanto Oliveira et al. concentram-se na análise exploratória dos dados e na metodologia de construção do grafo, este trabalho avança para a operacionalização dessa base, desenvolvendo um agente cognitivo funcional "de ponta a ponta"que consome esses dados. 

A integração entre grafos e interfaces de conversação é explorada por Meloni et al. (2023) através do sistema AIDA-Bot. O trabalho apresenta um agente para o domínio científico capaz de responder perguntas sobre Scientific Knowledge Graphs. A arquitetura proposta utiliza componentes de compreensão de linguagem natural para gerar consultas SPARQL, integrando-se a assistentes como Alexa e Telegram. Diferentemente do AIDA-Bot, que depende de mapeamento rígido para SPARQL (uma linguagem de consulta estruturada), a presente proposta adota uma abordagem híbrida utilizando busca vetorial e embeddings semânticos. Isso permite uma recuperação de informações mais flexível e contextual, alinhada aos conceitos defendidos por Clarke, Hughes e Banerjee (2025), que postulam a busca semântica e os embeddings como paradigmas centrais para a descoberta de conhecimento em domínios complexos. 

Uma proposta mais próxima ao escopo deste trabalho é a de Ostrovskyy (2025), que descreve um guia para agentes conversacionais jurídicos integrados ao Neo4j. O autor demonstra a orquestração entre LLMs e grafos utilizando o framework LangChain. Embora similar nos objetivos, as implementações divergem significativamente na arquitetura de software: Ostrovskyy baseia-se fortemente nas abstrações fornecidas pelo LangChain para gerenciar o fluxo, enquanto este trabalho propõe uma arquitetura de integração independente e customizada, visando maior controle sobre a latência e o tratamento de dados na interface do WhatsApp. 

A análise dos trabalhos relacionados revela avanços significativos em áreas isoladas: Colombo, Bernasconi e Ceri (2024) e Oliveira et al. (2025) resolvem o problema da estruturação dos dados legais, mas não oferecem interfaces de interação final para o usuário leigo. Por outro lado, Meloni et al. (2023) e Ostrovskyy (2025) apresentam agentes conversacionais, mas focam em domínios científicos ou dependem de frameworks de orquestração "caixa-preta". 

Nota-se, portanto, a ausência de uma solução que integre, simultaneamente: a especificidade da legislação brasileira modelada em grafos; a flexibilidade da busca semântica vetorial (superando a rigidez do SPARQL); e a acessibilidade de uma interface de mensa-

geria popular (WhatsApp) sem dependência excessiva de bibliotecas de orquestração de terceiros. Este trabalho busca preencher essa lacuna ao propor uma arquitetura que une a robustez estrutural dos Grafos de Conhecimento com a fluidez dos LLMs, aplicada e validada em um canal de comunicação de ampla adoção. 

# 1.5 Organização do texto

Este trabalho está estruturado em quatro capítulos principais. O Capítulo 2 apresenta a fundamentação teórica, abordando os conceitos de agentes cognitivos, processamento de linguagem natural, embeddings e bancos de dados orientados a grafos, que servem de base para a proposta desenvolvida. O Capítulo 3 descreve a metodologia de implementa-ção, detalhando as etapas de construção da base de conhecimento, extração de entidades, geração de embeddings e integração do sistema. O Capítulo 4 apresenta os resultados e a análise das validações realizadas, discutindo o desempenho do agente cognitivo em diferentes cenários de consulta. Por fim, o Capítulo 5 traz as conclusões, destacando as contribuições alcançadas, as limitações observadas e as perspectivas para trabalhos futuros. 

# Capítulo 2

# Fundamentação Teórica

Este capítulo estabelece a fundamentação teórica necessária para o desenvolvimento do sistema proposto. Visto que o objetivo do trabalho é criar um Agente Cognitivo com Busca Semântica em Grafos de Conhecimento via WhatsApp, esta revisão foi estruturada para detalhar os componentes centrais que formam a arquitetura da solução. Inicialmente, apresenta-se a definição de Agentes, estabelecendo o paradigma de sistemas autônomos. Em seguida, abordam-se os LLMs, que atuam como o componente cognitivo do agente. Na sequência, discute-se o conceito de Chatbots como camada de interação. Para fundamentar a busca semântica, detalha-se a técnica de Embeddings, crucial para a representa-ção vetorial do significado. Posteriormente, introduzem-se os Grafos de Conhecimento, estrutura selecionada para o armazenamento de informações. Por fim, apresenta-se a Geração Aumentada por Recuperação (RAG), padrão arquitetural que integra os componentes anteriores. 

# 2.1 Agentes

De acordo com Russell e Norvig (2021), um agente racional é aquele que busca maximizar o desempenho esperado com base nas percepções recebidas e no conhecimento prévio que possui sobre o ambiente. Esse conceito estabelece o fundamento para o desenvolvimento dos agentes inteligentes: sistemas capazes de perceber o ambiente, processar informações e agir de maneira autônoma para atingir objetivos específicos. Tais agentes não apenas reagem a estímulos, mas também utilizam representações internas e estraté- gias de decisão para otimizar seus resultados. 

A partir desse paradigma, os agentes cognitivos surgem como uma extensão, incorporando mecanismos de raciocínio simbólico, aprendizado e memória para representar o conhecimento. Conforme Wooldridge (2002), um agente cognitivo caracteriza-se por possuir crenças, desejos e intenções (Beliefs, Desires, Intentions — BDI), estrutura que lhe confere a capacidade de planejar e justificar ações de forma análoga ao raciocínio humano. 

Com o avanço da Inteligência Artificial Generativa, observa-se uma nova geração de agentes. Esses sistemas utilizam LLMs como núcleo de processamento, sendo capazes de interpretar linguagem natural, acessar conhecimento externo e coordenar ações em fluxos complexos. Estudos recentes destacam a integração desses modelos a mecanismos 

de memória de longo prazo, bases de conhecimento estruturadas e ferramentas externas, formando sistemas híbridos que combinam a flexibilidade do aprendizado estatístico com a precisão da cognição simbólica (PARK et al., 2023; LangChain, 2024). 

Nesse contexto, os agentes cognitivos modernos têm sido empregados em domínios como atendimento automatizado e pesquisa científica. Sua principal característica reside na capacidade de contextualizar interações e raciocinar sobre informações, diferenciandose de chatbots puramente reativos. 

# 2.2 Modelos de Linguagem de Grande Escala

Os Modelos de Linguagem de Grande Escala são redes neurais treinadas em vastos volumes de texto, capazes de identificar padrões complexos e gerar conteúdo coerente. Esses modelos beneficiam-se de técnicas de transfer learning, que permitem aproveitar o conhecimento adquirido em grandes corpora gerais e adaptá-lo a tarefas específicas. Uma aplicação prática é o ajuste fino (fine-tuning), no qual o modelo pré-treinado é refinado com dados de um domínio particular. Outra abordagem é o aprendizado em contexto (incontext learning), em que exemplos fornecidos na entrada guiam a resposta do modelo (BROWN et al., 2020; RUDER et al., 2019). 

As principais famílias de LLMs incluem arquiteturas como o GPT, desenvolvido pela OpenAI, e o LLaMA, da Meta, entre outros. Embora apresentem diferenças arquiteturais, esses modelos compartilham limitações inerentes aos dados de treinamento, como a presença de vieses e a propensão a gerar informações incorretas, fenômeno conhecido como alucinação (hallucination) (CHOWDHERY et al., 2022). 

Apesar da capacidade de geração fluente, os LLMs isolados apresentam dificuldades em recuperar fatos específicos fora de seu corte temporal ou em responder a consultas que exigem relações estruturadas explícitas. Essa lacuna motiva o uso de estratégias como a integração com bases de conhecimento externas (LEWIS et al., 2020). 

# 2.3 Chatbots

Os chatbots são aplicações que permitem interações com usuários por meio de linguagem natural (SHAWAR; ATWELL, 2007). O campo evoluiu de sistemas baseados em regras rígidas e reconhecimento de padrões para agentes modernos alimentados por modelos neurais (ADAMOPOULOU; MOUSSIADES, 2020). Revisões da literatura abordam aspectos como a compreensão de linguagem natural (NLU), gerenciamento de diálogo e geração de resposta (NLG), além de métricas de avaliação focadas na satisfação do usuário e na precisão da tarefa (DERIU et al., 2021). 

A emergência dos LLMs reavivou a pesquisa na área, introduzindo a necessidade de técnicas de controle, como verificação de fontes (grounding) e filtros de segurança, essenciais para a aplicação dessas interfaces em domínios sensíveis (WU et al., 2024). 

# 2.4 Embeddings

Embeddings são representações densas e contínuas de unidades textuais (palavras, sentenças ou documentos) em espaços vetoriais. O conceito fundamenta-se na hipótese distribucional, segundo a qual itens linguísticos com contextos semelhantes tendem a ocupar posições próximas no espaço vetorial, permitindo mensurar a similaridade semântica por meio de operações algébricas, como o cosseno (MIKOLOV et al., 2013; ALMEIDA; XEXéO, 2019). 

A introdução de contexto semântico representou um avanço no Processamento de Linguagem Natural. Ao superar a dependência de correspondências literais de palavraschave, os sistemas passaram a compreender relações de significado, recuperando informações relevantes mesmo na ausência de vocabulário exato. Essa abordagem aprimora a precisão em tarefas de busca e classificação textual. 

Historicamente, métodos preditivos como Word2Vec e GloVe popularizaram o uso de vetores densos para palavras (PENNINGTON; SOCHER; MANNING, 2014). Mais recentemente, arquiteturas baseadas em Transformadores, como o BERT, permitiram a geração de embeddings de sentenças completas, capturando nuances contextuais complexas e viabilizando a busca semântica em documentos extensos com maior eficiência computacional (REIMERS; GUREVYCH, 2019). 

# 2.5 Grafos de Conhecimento

Os Grafos de Conhecimento consolidam-se como uma abordagem central para a representação formal de informações, estruturando dados provenientes de fontes heterogê- neas. Um grafo é composto essencialmente por três elementos: nós (entidades), arestas (relacionamentos) e propriedades. Os nós representam abstrações de objetos ou conceitos do mundo real; as propriedades descrevem características dessas entidades; e os relacionamentos explicitam as conexões semânticas entre elas. Essa estrutura privilegia a conexão lógica dos dados, refletindo a organização do conhecimento humano (JI et al., 2020). 

A Figura 2.1 ilustra a estrutura básica de um grafo de conhecimento, destacando a interconexão entre entidades. 


Figura 2.1: Exemplo de grafo de conhecimento.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/a7f7b0cd-f89c-4bc9-91f5-ff11f87c76ae/cd699fb56a06ef2a297797a8f7e245f65fb59232854f1f7d47fa8269652bcaba.jpg)



Fonte: Adaptado de Negro et al. (2025).


# 2.6 Geração Aumentada por Recuperação

O treinamento de modelos de Inteligência Artificial baseia-se em conjuntos de dados estáticos, o que impõe uma limitação temporal intrínseca ao conhecimento do modelo. Uma vez finalizado o treinamento, o conhecimento paramétrico da IA torna-se fixo, restringindo-se às informações disponíveis até a data de corte. Consequentemente, o modelo torna-se incapaz de responder corretamente a questões sobre eventos recentes ou sobre domínios específicos que não constavam no corpus original, tendendo a gerar respostas obsoletas ou alucinadas. Conforme Huang e Huang (2024), modelos dependentes apenas de dados estáticos enfrentam barreiras severas de cobertura de conhecimento e atualização. 

Para mitigar essa obsolescência, adota-se a técnica de Geração Aumentada por Recuperação. Essa arquitetura desacopla a capacidade de raciocínio linguístico (do LLM) da capacidade de armazenamento de informações. O sistema integra fontes externas de dados atualizados, que são recuperadas em tempo de execução e fornecidas como contexto ao modelo gerativo. 

Dessa forma, a resposta é construída a partir da tríade: a instrução do usuário; o conhecimento paramétrico do modelo; e o contexto recuperado dinamicamente. Essa abordagem permite a integração de APIs, bases vetoriais ou raspagem de dados web, garantindo que a geração de texto esteja fundamentada em fatos recentes e verificáveis (GU, 2025). Os conceitos aqui apresentados fundamentam a arquitetura do sistema proposto, 

# 2.6. GERAÇÃO AUMENTADA POR RECUPERAÇÃO

que combina o paradigma RAG com a estrutura relacional dos Grafos de Conhecimento. 

# Capítulo 3

# Metodologia

Este capítulo apresenta a metodologia adotada para o desenvolvimento do agente cognitivo, detalhando as etapas de engenharia de dados, construção da base de conhecimento e implementação da arquitetura de comunicação. O método proposto divide-se em dois macroprocessos principais: o desenvolvimento da base gráfica, que compreende a preparação do corpus, a modelagem vetorial e a estruturação no banco de dados Neo4j e o desenvolvimento do fluxo de comunicação, que orquestra a interação entre o usuário final via WhatsApp e o núcleo semântico do sistema. 

Para facilitar a compreensão da arquitetura proposta, a Figura 3.1 ilustra a visão geral do sistema, evidenciando a interconexão entre os módulos de coleta, processamento, armazenamento e interface. 


Figura 3.1: Fluxo completo da comunicação com o usuário.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/a7f7b0cd-f89c-4bc9-91f5-ff11f87c76ae/b489bc33fdfb343ce2a77723be16ea9537ba01db4160a8c80cb81866c3fbbff1.jpg)



Fonte: Elaborada pelo autor (2025).


# 3.1 Desenvolvimento da Base Gráfica

Esta seção descreve o processo de engenharia de conhecimento aplicado para transformar o conteúdo jurídico bruto em uma estrutura consultável. O procedimento envolve a curadoria do corpus, a segmentação semântica, a vetorização e a modelagem estrutural no banco de dados. 

# 3.1.1 Obtenção dos Dados

A estratégia de coleta de dados priorizou a conformidade com a Lei Geral de Proteção de Dados (LGPD) e a estabilidade do acesso à informação. Embora a raspagem de dados (web scraping) automatizada permita a extração em larga escala, tal prática enfrenta barreiras técnicas e legais em portais governamentais (CARDOSO, 2021). Diante disso, 

optou-se pela aquisição manual dos textos legislativos oficiais a partir do portal do Planalto, constituindo um corpus local em formato Portable Document Format (PDF). Essa abordagem garante a integridade dos documentos originais e mitiga riscos de bloqueio ou violação de termos de uso durante a fase de desenvolvimento. 

# 3.1.2 Limpeza e Normalização dos Dados

A etapa de pré-processamento visou maximizar a densidade semântica do corpus, removendo elementos ruidosos que poderiam degradar a performance dos modelos de linguagem. O processo foi implementado em Python, utilizando expressões regulares para higienização textual. 

O protocolo de limpeza aplicou filtros para remoção de: metadados administrativos irrelevantes (datas de publicação, códigos de controle); referências externas (URLs e links); numerações isoladas que quebram a fluidez da leitura; e caracteres especiais não-textuais. Adicionalmente, aplicou-se a normalização Unicode para padronização de acentos e a conversão para caixa baixa, reduzindo a dimensionalidade do vocabulário. Em subconjuntos específicos, realizou-se a remoção de stopwords (palavras de parada sem valor semântico), utilizando a biblioteca do nltk que possui um dicionário de stop words da língua portuguesa, e a lematização, processos que reduzem as palavras às suas raízes canônicas, otimizando a futura etapa de vetorização. 

# 3.1.3 Pré-processamento e Vetorização

Após a higienização, o texto foi submetido à segmentação e vetorização, preparandoo para a ingestão no banco de dados. O fluxo consistiu em quatro procedimentos técnicos sequenciais. 

Inicialmente, o texto contínuo foi submetido ao processo de segmentação (chunking), sendo dividido em unidades menores conforme a estrutura hierárquica da legislação, abrangendo artigos, parágrafos e incisos. Essa estratégia de corte visou preservar o contexto local de cada norma, granularidade considerada fundamental para assegurar que a unidade recuperada durante a busca contenha uma informação completa, conforme preconizado por Colombo, Bernasconi e Ceri (2024). Na sequência, cada segmento gerado foi encapsulado em um objeto do tipo Document, garantindo a preservação de metadados essenciais para a rastreabilidade da informação, tais como a fonte original e a página de extração. 

Posteriormente, procedeu-se à geração das representações vetoriais (embeddings) para cada segmento textual, utilizando modelos de linguagem pré-treinados, especificamente o text-embedding-ada-002 da OpenAI e o paraphrase-multilingual-MiniLM-L12-v2. Tais vetores numéricos capturam a semântica do texto, viabilizando o cálculo matemático de similaridade entre termos e conceitos. Por fim, os chunks e seus respectivos vetores foram inseridos no banco de dados Neo4j, onde foi criado um índice vetorial dedicado a habilitar a busca eficiente por similaridade de cosseno. 

# 3.1.4 Desenvolvimento do Grafo de Conhecimento

A construção do grafo no Neo4j seguiu uma modelagem centrada na estrutura documental hierárquica. Diferentemente de bancos relacionais tradicionais, o uso de grafos permitiu representar explicitamente a relação de pertencimento entre os fragmentos e seus documentos de origem. 

Os nós foram tipificados em duas categorias principais: Document (representando o arquivo legal completo) e Chunk (representando o trecho da lei vetorizado). Estes nós foram conectados pela relação hierárquica PART_OF (parte de), estabelecendo que um determinado Chunk pertence a um Document específico. 

Os vetores de embedding gerados na etapa anterior foram armazenados como propriedades dos nós do tipo Chunk. Utilizando a funcionalidade nativa de índices vetoriais do Neo4j, criou-se uma estrutura de busca que permite recuperar os nós com base na proximidade semântica. O resultado é uma base de dados que combina a organização lógica dos documentos legais com a capacidade de recuperação (retrieval) baseada no significado da consulta do usuário, e não apenas em palavras-chave exatas. 

# 3.2 Desenvolvimento do Fluxo de Comunicação

Esta seção detalha a arquitetura de software responsável por expor a inteligência do grafo aos usuários finais através de uma interface de mensageria. 

# 3.2.1 Integração com WhatsApp via Twilio

A interface de usuário foi implementada sobre o aplicativo WhatsApp, utilizando a plataforma Twilio como gateway de comunicação. O Twilio atua como intermediário, convertendo as mensagens recebidas no aplicativo em requisições HTTP (Webhooks) para o sistema backend. Um Webhook é um mecanismo de callback HTTP que permite que uma aplicação envie dados em tempo real para outra assim que um evento ocorre. 

A escolha desta plataforma deve-se à sua conformidade com a API oficial do WhatsApp Business e à facilidade de prototipagem em ambiente de sandbox. A autenticação das requisições é realizada via Basic Auth, um esquema de autenticação padrão do protocolo HTTP no qual o cliente envia o nome de usuário e a senha codificados em Base64 no cabeçalho da requisição. 

# 3.2.2 API de Comunicação (Backend)

Para processar as consultas, desenvolveu-se uma API RESTful utilizando o framework FastAPI em Python, a qual atua como o controlador lógico do sistema. O fluxo de execução inicia-se com a etapa de recepção, na qual o endpoint /processar recebe a mensagem do usuário via método HTTP POST. Na sequência, ocorre a vetorização, onde a consulta do usuário é convertida em um vetor de embedding utilizando o mesmo modelo aplicado na construção da base de dados. Posteriormente, o sistema realiza a recupera-ção executando a função db.index.vector.queryNodes no Neo4j; neste momento, o 

vetor da pergunta é comparado com os vetores dos chunks armazenados, recuperandose os nós com maior pontuação de similaridade. Para o cálculo de similaridade entre a pergunta do usuário e os chunks, utilizou-se a Similaridade de Cosseno (Cosine Similarity). Essa métrica foi escolhida por ser agnóstica à magnitude dos vetores, focando na orientação no espaço vetorial, o que é padrão para embeddings gerados por modelos Sentence-BERT/OpenAI. Por fim, na etapa de resposta, o conteúdo textual dos nós recuperados é formatado e retornado ao solicitante como um objeto JSON. 

Vale ressaltar que, durante a fase de desenvolvimento, utilizou-se a ferramenta ngrok para expor a API local à internet através de um túnel seguro, viabilizando a comunicação bidirecional com os serviços em nuvem do Twilio e do N8n. 

# 3.2.3 Orquestração de Fluxo no N8n

A orquestração entre a recepção da mensagem, a consulta à inteligência e o envio da resposta foi implementada na plataforma low-code N8n. O fluxo automatizado, conforme ilustrado anteriormente na Figura 3.1, coordena a troca de mensagens em uma sequência lógica de cinco etapas. 

O processo inicia-se com o Webhook de Entrada, um nó gatilho configurado para receber a requisição POST do Twilio contendo a mensagem do usuário. Em seguida, executa-se um script de Tratamento em JavaScript, responsável por normalizar os dados, extraindo o corpo da mensagem e o número do remetente. O fluxo prossegue para a Consulta à API, onde um nó de requisição HTTP envia os dados tratados para o backend em Python (FastAPI). Após o recebimento dos dados processados, um novo script realiza a Formatação de Saída, ajustando os trechos recuperados para respeitar os limites de caracteres impostos pelo WhatsApp. A etapa final consiste no Envio de Resposta, utilizando a API do Twilio para encaminhar a mensagem formatada de volta ao usuário. 

# 3.3 Protocolo de Validação

O protocolo de validação estabelecido para este trabalho consistiu em uma análise funcional do sistema completo (end-to-end), verificando a capacidade do agente cognitivo de processar consultas em linguagem natural e recuperar informações jurídicas pertinentes. Dado o caráter de prova de conceito da aplicação, a avaliação concentrou-se na eficácia da recuperação da informação (information retrieval) diretamente na interface do usuário final. 

A validação foi realizada por meio de interações reais no aplicativo WhatsApp, simulando o comportamento de um usuário em busca de informações sobre a legislação. Durante os testes, submeteram-se perguntas variadas ao agente, abrangendo diferentes níveis de complexidade semântica. A análise dos resultados foi qualitativa, observandose se os trechos recuperados pelo sistema (os chunks) correspondiam semanticamente à intenção da pergunta realizada. 

Dessa forma, a integridade da base de dados e a conectividade do grafo foram validadas de maneira implícita: o sucesso na entrega de uma resposta coerente demonstra que as 

etapas anteriores de limpeza do corpus, vetorização e indexação no Neo4j foram executadas corretamente, permitindo que o fluxo automatizado operasse conforme o esperado. 

# Capítulo 4

# Resultados

Este capítulo apresenta os resultados práticos obtidos a partir da metodologia descrita anteriormente, evidenciando o desempenho e a eficácia do agente cognitivo desenvolvido. A análise é organizada conforme as principais etapas do sistema, com foco nos produtos gerados e na interpretação das evidências experimentais. Inicialmente, detalham-se os resultados da geração do grafo de conhecimento, incluindo a limpeza textual, segmentação em chunks e vetorização semântica. Em seguida, demonstram-se as saídas gráficas e as consultas realizadas no Neo4j, comprovando a coerência da estrutura hierárquica obtida. Na sequência, apresentam-se os dados referentes ao fluxo de comunicação, detalhando a integração entre a API, o N8n e o WhatsApp. Por fim, a seção de validação reúne os testes de conversação realizados, analisando a precisão e as limitações observadas no comportamento do sistema. 

# 4.1 Geração do Grafo de Conhecimento

Esta seção detalha os artefatos resultantes da construção da base de conhecimento. São apresentados comparativos da etapa de limpeza, amostras da segmentação textual, exemplos dos vetores gerados e a visualização final da estrutura no banco de grafos. 

# 4.1.1 Limpeza e Normalização dos Dados

A etapa de limpeza e normalização foi aplicada aos textos extraídos dos arquivos PDF com o objetivo de remover ruídos e padronizar a estrutura documental. Buscou-se manter apenas o conteúdo textual relevante, reduzindo interferências que pudessem degradar a qualidade dos embeddings. 

Para mensurar a eficiência dessa etapa, desenvolveu-se um algoritmo em Python que processa o texto bruto extraído via biblioteca PyPDFLoader. O script aplica expressões regulares para identificar e remover padrões recorrentes de ruído, como por exemplo: as referências a URLs e rodapés de impressão e linhas contendo apenas numeração ou carimbos de data/hora. Além disso, o algoritmo normaliza espaços múltiplos e quebras de linha excessivas. 

A Tabela 4.1 apresenta um comparativo visual entre o texto original extraído e o resultado após o processamento. 


Tabela 4.1: Exemplo da limpeza do corpus


<table><tr><td>Texto Original</td><td>Texto(after limpeza</td></tr><tr><td>CAPÍTULO II Dos Direitos da Personalidade ? Art. 11. Com excedo dos casos previstos em lei, os ... ? Art. 12. Pode-se exigir que cesse a ameaça, ou a lesão, ... Parágrafo谁能. Em se tratando de morto, tera legitimação ... ? Art. 13. Salvo por exigência médica, é defeso o ato de ... &lt;https://www.planalto.gov.br/ccivil_03/Leis /2002/L10406.htm&gt; 2/197 14/05/2025, 18:16 L10406 Parágrafo谁能. O ato previsto;neste artigo sera admitido ... ? Art. 14. É valida, com objetivocientífico, ou altruístico...</td><td>CAPÍTULO II Dos Direitos da Personalidade Art. 11. Com excedo dos casos previstos em lei, os ... Art. 12. Pode-se exigir que cesse a ameaça, ou a lesão, ... Parágrafo谁能. Em se tratando de morto, tera legitimação ... Art. 13. Salvo por exigência médica, é defeso o ato de... Parágrafo谁能. O ato previsto;neste artigo sera admitido ... Art. 14. É valida, com objetivocientífico, ou altruístico...</td></tr></table>

Observa-se na Tabela 4.1 que ruídos como ícones de formatação incorreta, URLs e metadados de página foram removidos, preservando-se a estrutura dos artigos. 

Em relação à remoção de stopwords (palavras de ligação como "de", "para", "com"), optou-se por não aplicar esse filtro na versão final do grafo. Essa decisão baseou-se na premissa de que, na linguagem jurídica, preposições e conectivos desempenham papel fundamental na definição de causalidade e escopo das normas. A remoção indiscriminada desses termos poderia comprometer a semântica vetorial dos embeddings, resultando na perda de nuances interpretativas essenciais. 


Listing 4.1: Exemplo de limpeza com Remoção de Stop Words e Normalização


<table><tr><td>text: &quot;art 675 mandante obrigar satisfazer todo obrigacoes contraida mandatario conformidade mandato conferer adiantar importancia despesa necessario execucao mandatario lho pedir art 676 obrigar mandante pagar mandatario remuneracao ajustar despesa execucao mandato ainda negocio nao surto esperar efeito salvo ter mandatario culpa art 677 SOMA adiantar mandatario execucao mandato vencer juro desde data.desembolso [...] &quot;</td></tr></table>

Para quantificar o impacto da limpeza estrutural, o algoritmo comparou o volume de caracteres antes e depois do processamento. Os resultados obtidos foram: 


Listing 4.2: Quantificação da limpeza


<table><tr><td>Tamanho original: 711.990 characteres
Tamanho après limpeza: 696.507 characteres
Texto limpo: 2,17% do conteudo FOi Removedo</td></tr></table>

A redução de aproximadamente $2 , 1 7 \%$ indica que a limpeza foi mínima, eliminando apenas elementos periféricos sem comprometer a integridade do conteúdo legislativo. 

# 4.1.2 Divisão de Chunks

Para a segmentação do texto jurídico em unidades coerentes, utilizou-se um padrão de expressões regulares desenhado para respeitar a hierarquia da lei. O padrão emprega o recurso de lookahead $\left( ? = \right)$ , permitindo identificar pontos de corte (início de Artigos, Parágrafos ou Incisos) sem descartar os marcadores textuais. 

A Tabela 4.2 apresenta uma amostra dos segmentos gerados. 


Tabela 4.2: Exemplos de Chunks gerados


<table><tr><td>ChunkID</td><td>Texto (prévia)</td><td>Tamanho</td></tr><tr><td>f4c1ad16-59cb...</td><td>Presidência da Répubrica, Casa Civil...</td><td>504</td></tr><tr><td>40419a74-e516...</td><td>Art. 1° Toda pessoa é capaz de direitos...</td><td>67</td></tr><tr><td>94ab6e52-1a63...</td><td>Art. 2° A personalidade civil da和个人...</td><td>138</td></tr><tr><td>16d43993-1165...</td><td>Art. 3° São absolutamente inca-pazes de...</td><td>83</td></tr><tr><td>e52a2124-6bf6...</td><td>I - os que, por infermidade ou deficiência...</td><td>117</td></tr><tr><td>f9412af5-b114...</td><td>Art. 5° A maioridade cessa aos dezoito...</td><td>187</td></tr></table>

Nota-se que cada chunk corresponde a um núcleo semântico autônomo. Essa granularidade favorece a recuperação precisa, pois evita que conceitos distintos (presentes em artigos diferentes) sejam misturados no mesmo vetor. 

# 4.1.3 Conversão em Documentos Estruturados

Após a segmentação, os trechos foram encapsulados em objetos do tipo Document, preservando metadados contextuais. A estrutura de dados adotada incluiu informações sobre a hierarquia normativa de origem, conforme o exemplo a seguir: 

metadata $=$ { "livro":current_livro, "titulo":current_titulo, "capitulo":current_capitulo, "artigo":f"Art.{artigo_num}", 

```txt
"chunk_id": chunk_id, "source": "codigo_civil.pdf" } 
```

Essa estruturação permitiu reconstruir a “árvore” da legislação dentro do grafo, garantindo que um parágrafo isolado pudesse ser rastreado de volta ao seu Capítulo e Título de origem. 

# 4.1.4 Geração de Embeddings

A representação vetorial foi realizada utilizando o modelo paraphrase-multilingual-MiniLM-L12-v2, executado localmente. Este modelo converteu cada chunk em um vetor denso de 384 dimensões. A Tabela 4.3 exibe uma amostra dos valores vetoriais gerados. 


Tabela 4.3: Amostra dos embeddings gerados


<table><tr><td>Pré-visualização do Texto</td><td>Embedding (10 primeiros valore)</td><td>Dim.</td></tr><tr><td>Presidência da República...</td><td>[-0.031, 0.093, -0.008, -0.044, 0.250, 0.147, -0.089, 0.179, 0.118, 0.322]</td><td>384</td></tr><tr><td>Art. 1° Toda pessoa é...</td><td>[-0.164, 0.272, -0.244, 0.053, -0.092, 0.118, 0.217, 0.011, 0.170, 0.244]</td><td>384</td></tr><tr><td>Art. 2° A personalidade...</td><td>[-0.091, 0.352, -0.314, 0.260, 0.130, 0.298, 0.007, 0.206, -0.022, 0.449]</td><td>384</td></tr></table>

Esses vetores foram armazenados como a propriedade textEmbedding nos nós do grafo, habilitando o cálculo de similaridade de cosseno durante as consultas. 

# 4.1.5 Modelagem e Visualização do Grafo

A inserção no Neo4j utilizou consultas Cypher com a cláusula MERGE, assegurando a unicidade e a hierarquia dos nós $( P a r t e  L i \nu r o  T i t u l o  C a p i t u l o  S e \varsigma \tilde { a } o  A r t i g o$ Parágrafo Incisos). 

A Figura 4.1 apresenta uma visualização parcial do grafo gerado. 


Figura 4.1: Visualização da hierarquia do grafo no Neo4j.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/a7f7b0cd-f89c-4bc9-91f5-ff11f87c76ae/bcda2640d1b133e25d27a427e3f9a5bc8492238576dcdd151e4ccc6db7fe9e40.jpg)



Fonte: Elaborada pelo autor (2025).


Na visualização, observa-se a estrutura arborescente da legislação. hierarquia se inicia com os nós de Parte (em verde pastel), que se conectam aos Livros (azul clara). Estes, por sua vez, se ligam aos Títulos (ciano), que estão conectados aos Capítulos (rosa). Seguindo a estrutura legal, os Capítulos agrupam as Seções (lilás), que contêm os nós de Artigo (verde). No final, na camada mais granular, visível na periferia do grafo, os Artigos se conectam tanto aos Parágrafos (rosa mais suave) quanto aos Incisos (rosa mais forte). 

# 4.2 Fluxo de Comunicação com o Usuário

Esta seção detalha os resultados da integração entre os componentes de software. Descreve-se o funcionamento da API de backend e a orquestração do fluxo de mensagens. 

# 4.2.1 API de Comunicação

O Algoritmo 1 resume a lógica implementada na API para processar as requisições. 


Algoritmo 1: Lógica simplificada da API de Consulta


Entrada: m: mensagem do usuario
Saía: resposta:texts concatenados
1 vetor \(\leftarrow\) model_encode(m);
2 session \(\leftarrow\) driver.session(   );
3 result \(\leftarrow\) session.run("CALLdb.index.query('index',\\(veter)...");
4 chunks \(\leftarrow \left\lbrack  \right\rbrack  ;\)   
5 para cada record em result_faÇA
6 texto \(\leftarrow\) record["node".textto;
7 Adicional texto em chunks;
8 fim
9 resposta \(\leftarrow\) jintar(chunks,----");
10 returna resposta; 

A API demonstrou capacidade de receber a consulta, vetorizá-la em tempo real e recuperar os nós mais relevantes, utilizando o índice vetorial do Neo4j. 

# 4.2.2 Resultados da Integração no N8n

A Figura 4.2 ilustra o fluxo completo configurado na plataforma N8n. 


Figura 4.2: Fluxo de integração no N8n.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/a7f7b0cd-f89c-4bc9-91f5-ff11f87c76ae/bbd876cf5cf78230edd8a81b7bf0c37302454b9e1184d5f85bc936972b285bfd.jpg)



Fonte: Elaborada pelo autor (2025).


A validação do fluxo ocorreu através da inspeção dos dados em cada nó de processamento: 

• Webhook (Figura 4.3): Recebimento correto do corpo da mensagem via Twilio. 

• Processamento (Figura 4.4): Extração bem-sucedida do texto e do número do remetente via JavaScript. 

• Consulta à API (Figura 4.5): Retorno do JSON contendo os trechos da legislação recuperados. 

• Envio (Figura 4.6): Confirmação do disparo da resposta de volta ao WhatsApp. 


Figura 4.3: Recebimento no Webhook.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/a7f7b0cd-f89c-4bc9-91f5-ff11f87c76ae/4aa55e4f8987d562c0769f6b0ac4924b6abcbaf83473a83b3977cafebc3b84f1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/a7f7b0cd-f89c-4bc9-91f5-ff11f87c76ae/48b78d88abd8410ae800f17a8785fe6fe9b93736d0bc44e4803aeddb7b80aad8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/a7f7b0cd-f89c-4bc9-91f5-ff11f87c76ae/1d3c575f25e422eaf29a84d91e560d5e8aa72f570553e43bcfe45e99f434877f.jpg)



Fonte: Elaborada pelo autor (2025).



Figura 4.4: Tratamento dos dados.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/a7f7b0cd-f89c-4bc9-91f5-ff11f87c76ae/c0fa17490642427bc771b4265c2cc98a6e30613dd368d15f146cd4daee147e91.jpg)



Fonte: Elaborada pelo autor (2025).



Figura 4.5: Resposta da API.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/a7f7b0cd-f89c-4bc9-91f5-ff11f87c76ae/8678d1ead4758366fce142e41383d40fc0d761dee4dc27e8d17d5af3d8642f07.jpg)



Fonte: Elaborada pelo autor (2025).



Figura 4.6: Envio para Twilio.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/a7f7b0cd-f89c-4bc9-91f5-ff11f87c76ae/83662d1b49b5349b1d3ab872f1fb058f1ef0cc20d9a96a18c80b1a3895da27a9.jpg)



Fonte: Elaborada pelo autor (2025).


# 4.3 Análise da Interação e Recuperação Semântica

Os testes de interação via WhatsApp demonstraram a capacidade funcional do sistema em ambiente real. A Figura 4.7 exibe exemplos de respostas geradas, onde o agente foi capaz de interpretar a intenção do usuário e formular retornos baseados no contexto jurídico. 


Figura 4.7: Respostas obtidas no WhatsApp.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/a7f7b0cd-f89c-4bc9-91f5-ff11f87c76ae/8c02e93dd78d2e873efe936569f1d0a47eeb511d725d777ac7e7ec46068da68b.jpg)



Fonte: Elaborada pelo autor (2025).


Para compreender a granularidade da recuperação de informações que suporta essas interações, analisaram-se os logs de similaridade em dois cenários distintos: busca conceitual e busca literal. 

A Tabela 4.4 apresenta os resultados para a consulta “fale sobre homicídio”. É importante notar que, embora a palavra “homicídio” não apareça explicitamente nos trechos recuperados, o modelo demonstrou capacidade de generalização semântica ao retornar artigos que tratam de “morte”, “tentativa de morte” e “óbitos”. 


Tabela 4.4: Resultados da busca semântica, texto “fale sobre homicídio”


<table><tr><td>Rank</td><td>Trecho Recuperado (Chunk)</td><td>Score</td></tr><tr><td>1°</td><td>Art. 1.722. Extingue-se, igualmente, o bem de família com a morte de outros os confjuges e a maioridade dos filhos, desde que não sujeitos a curatela. DA UNIÃO ESTÁVEL</td><td>0.7472</td></tr><tr><td>2°</td><td>Art. 1.573. Podem caracterizar a impossibilitadade da comunção de vida a correência de algoim seguintes motivos: I - adultério; II - tentativa de morte; III - sevência ou injúria grave; IV - abandono voluntário do lar conjugal [...] O juiz poderá considerar以及其他 fatos que tornem evidente a impossibilitadade da vida em comum.</td><td>0.7429</td></tr><tr><td>3°</td><td>Art. 9° Serais registrados em registrar-publico: I - os nascimento, casamentos e óbitos; II - a emancipação por outorga dos pais ou por sentença do juiz; III - a interdição por incapacidade absoluta ou relativa; IV - a sentença declaratória de ausência e de morte presumida.</td><td>0.7183</td></tr></table>

Os scores de similaridade variando entre 0.71 e 0.74 indicam uma correlação positiva forte, mas não absoluta. Isso ocorre porque o corpus utilizado (Código Civil) trata das consequências cíveis da morte, e não da tipificação penal do homicídio. Assim, o sistema corretamente identificou que, na ausência do termo exato, os trechos sobre o fim da vida e suas implicações legais (extinção de bem de família, registro de óbito) eram os mais pertinentes semanticamente. 

Em contraste, a Tabela 4.5 exibe os resultados para a consulta “fale sobre dívida”. Neste caso, observa-se uma similaridade de cosseno significativamente mais alta, com valores próximos a 0.88. 


Tabela 4.5: Resultados da busca semântica, texto “fale sobre dívida”


<table><tr><td>Rank</td><td>Trecho Recuperado (Chunk)</td><td>Score</td></tr><tr><td>1°</td><td>Art. 382. A confusão pode verificar-se a respeito de toda aDSLDA, ou só de parte dela.</td><td>0.8784</td></tr><tr><td>2°</td><td>Art. 285. Se aDSLDA solidária interessar exclusivamente a um dos devedores, responderá este por toda ela para com aquele que pagar. Da Transmissão das Obrigações Da Cessão de Crédito</td><td>0.8767</td></tr><tr><td>3°</td><td>Art. 345. Se aDSLDA se vencer,PENDendo litígio entrecretores que se pretendem mutually excludir, poderá qualquer deles re-querer a consignação. Do Pagamento com Sub-Rogação</td><td>0.8710</td></tr></table>

Essa pontuação elevada deve-se ao alinhamento direto entre a terminologia da consulta e o conteúdo do corpus. Como os artigos recuperados contêm explicitamente o termo “dívida” e tratam centralmente do tema, a distância vetorial entre a query e os documentos é menor, resultando em um grau de confiança superior. 

Contudo, identificou-se uma limitação em consultas de referência específica. Conforme demonstra a Figura 4.8, ao solicitar um dispositivo pelo seu identificador numérico 

(“artigo 88”), o sistema falhou em realizar a correspondência exata, retornando trechos semanticamente próximos ao tema de “artigos de lei”, mas distantes do alvo numérico. 


Figura 4.8: Limitação na busca por referência numérica.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/a7f7b0cd-f89c-4bc9-91f5-ff11f87c76ae/623240119092ea80e14b39ff52702f19af11304baf4f10207ab5fb3a4a9a437b.jpg)



Fonte: Elaborada pelo autor (2025).


A análise técnica do pipeline de recuperação revelou que tal falha decorre diretamente da estratégia de vetorização adotada. Os embeddings foram gerados exclusivamente a partir da propriedade texto (conteúdo da lei), excluindo a propriedade nome, onde reside o identificador numérico (ex: “Artigo 88”). Como o número do artigo não faz parte do corpo do texto vetorizado, essa informação não foi projetada no espaço latente. Consequentemente, o mecanismo de busca priorizou a similaridade semântica no conteúdo legislativo disponível, ignorando a referência numérica que existia apenas nos metadados não indexados vetorialmente. 

# Capítulo 5

# Conclusão

O desenvolvimento realizado comprovou a viabilidade de um agente cognitivo capaz de realizar buscas semânticas em um grafo de conhecimento, integrado ao aplicativo WhatsApp. A proposta combinou técnicas de processamento de linguagem natural, gera-ção de embeddings, representação de conhecimento e integração de sistemas, resultando em um modelo funcional de comunicação automatizada com base em grafos. 

Os experimentos realizados evidenciaram que o sistema é capaz de interpretar consultas em linguagem natural, identificar similaridades semânticas no banco de dados Neo4j e retornar respostas coerentes e contextualizadas. A integração entre o WhatsApp, a API cognitiva e o fluxo automatizado no N8n mostrou-se estável e eficiente, permitindo a interação de ponta a ponta entre o usuário e a base de conhecimento. 

Esses resultados validam o uso combinado de bancos de dados vetoriais e grafos de conhecimento em aplicações conversacionais, demonstrando o potencial dessa arquitetura para consultas complexas e domínios especializados. O protótipo desenvolvido consolida uma base sólida para futuras extensões, como o aprimoramento do modelo semântico, a expansão do corpus jurídico. 

A partir desta base funcional, algumas possibilidades de aprimoramento e expansão do modelo são possíveis, as quais são discutidas na seção a seguir. 

# 5.1 Trabalhos Futuros

Trabalhos futuros podem se concentrar no refinamento do pipeline de pré-processamento de Linguagem Natural, integrando técnicas que foram exploradas incialmente, mas não incorporadas à versão final. Sugere-se a reavaliação de métodos como a remoção de stop words, a lematização e a normalização de termos jurídicos, por exemplo, a abreviação padronizada de ’Artigo’ para ’Art.’ e outros termos jurídicos passíveis de abreviação, visando a redução de ruído e a otimização do consumo de tokens. Paralelamente, há espaço para aprimorar as expressões regulares utilizadas na segmentação dos textos, garantindo uma granulação mais fiel à estrutura hierárquica das leis. Por fim, destaca-se o potencial da incorporação de modelos baseados em BERT, finamente ajustados ao domínio jurídico, para tarefas de Reconhecimento de Entidades Nomeadas (NER). Essa abordagem permitiria enriquecer o Grafo de Conhecimento com nós de entidades específicas, aprimorando a precisão da busca semântica em consultas que exigem alta especificidade factual. 

Outra direção promissora consiste em substituir o N8n por frameworks específicos para construção de agentes cognitivos, como o LangChain, em Python. Essa alternativa gratuita oferece recursos avançados, incluindo a interpretação e geração de texto diretamente sobre a base de conhecimento, o uso de prompts especializados e a integração nativa com o Neo4j. Tais funcionalidades podem tornar o fluxo de consultas mais flexí- vel, robusto e adaptável a diferentes contextos de uso, além de fornecer interação mais humanizada. 

Além disso, a incorporação de múltiplos documentos jurídicos, ou até mesmo de textos provenientes de outros domínios, pode ampliar a abrangência e a profundidade semântica do grafo de conhecimento, favorecendo consultas mais ricas e contextualizadas. 

# Referências Bibliográficas



ADAMOPOULOU, E.; MOUSSIADES, L. An overview of chatbot technology. In: Artificial Intelligence Applications and Innovations (AIAI 2020). Cham: Springer, 2020. p. 373–383. Disponível em: <https://doi.org/10.1007/978-3-030-49186-4_31>. Acesso em: 30 out. 2025. 





ALMEIDA, F.; XEXéO, G. Word embeddings: A survey. arXiv preprint ar-Xiv:1901.09069, 2019. Disponível em: <https://arxiv.org/abs/1901.09069>. Acesso em: 01 dez. 2025. 





BROWN, T. B. et al. Language models are few-shot learners. In: Advances in Neural Information Processing Systems 33. New York: Curran Associates, Inc., 2020. p. 1877–1901. Disponível em: <https://arxiv.org/abs/2005.14165>. Acesso em: 30 out. 2025. 





CARDOSO, O. V. O web scraping viola a proteção de dados pessoais? Jusbrasil, São Paulo, 2021. Disponível em: <https://www.jusbrasil.com.br/artigos/o-web-scraping-vio la-a-protecao-de-dados-pessoais/1152362639>. Acesso em: 23 out. 2025. 





CHOWDHERY, A. et al. Palm: Scaling language modeling with pathways. arXiv preprint arXiv:2204.02311, 2022. Disponível em: <https://arxiv.org/abs/2204.02311>. Acesso em: 30 out. 2025. 





CLARKE, A.; HUGHES, N.; BANERJEE, P. Semantic search and its role in knowledge discovery. Innovative Research Journal, 2025. Acesso em: 05 nov. 2025. Disponível em: <https://www.researchgate.net/publication/392014461_Semantic_Search_and_Its_Role_ in_Knowledge_Discovery>. 





COLOMBO, A.; BERNASCONI, A.; CERI, S. Modelling Legislative Systems into Property Graphs to Enable Advanced Pattern Detection. 2024. Disponível em: <https://arxiv.org/abs/2406.14935>. Acesso em: 10 maio 2025. 





DERIU, J. et al. Survey on evaluation methods for dialogue systems. Artificial Intelligence Review, New York, v. 54, n. 1, p. 755–810, 2021. Disponível em: <https://doi.org/10.1007/s10462-020-09866-x>. 





GU, J. A research of challenges and solutions in retrieval augmented generation (RAG) systems. Highlights in Science, Engineering and Technology, Dr. Press, v. 124, 2025. Disponível em: <https://drpress.org/ojs/index.php/HSET/article/view/28756>. Acesso em: 01 dez. 2025. 





HUANG, Y.; HUANG, J. X. A survey on retrieval-augmented text generation for large language models. arXiv preprint arXiv:2404.10981, 2024. V2, submitted 17 Apr 2024. Disponível em: <https://arxiv.org/abs/2404.10981>. 





JI, S. et al. A survey on knowledge graphs: Representation, acquisition and applications. arXiv preprint arXiv:2002.00388, mar 2020. Disponível em: <https: //arxiv.org/pdf/2002.00388.pdf>. 





LangChain. Building cognitive agents with LangChain and LangGraph. 2024. Disponível em: <https://python.langchain.com/docs/langgraph>. Acesso em: 22 out. 2025. 





LANTARóN, B. S. et al. The educational use of whatsapp. Sustainability, MDPI, Basel, Suíça, v. 14, n. 17, p. 10510, 2022. ISSN 2071-1050. Disponível em: <https://www.mdpi.com/2071-1050/14/17/10510>. Acesso em: 30 nov. 2025. 





LEWIS, P. et al. Retrieval-augmented generation for knowledge-intensive NLP Tasks. In: LAROCHELLE, H. et al. (Ed.). Advances in Neural Information Processing Systems. New York: Curran Associates, Inc., 2020. v. 33, p. 9459–9474. Disponível em: <https://proceedings.neurips.cc/paper_files/paper/2020/file/6b493230205f780e1bc269 45df7481e5-Paper.pdf>. 





MELONI, A. et al. Integrating conversational agents and knowledge graphs within the scholarly domain. IEEE Access, IEEE, v. 11, p. 22468–22489, 2023. Disponível em: <https://doi.org/10.1109/ACCESS.2023.3253388>. 





MIKOLOV, T. et al. Efficient estimation of word representations in vector space. arXiv preprint arXiv:1301.3781, 2013. Disponível em: <https://arxiv.org/abs/1301.3781>. Acesso em: 01 dez. 2025. 





NEGRO, A. et al. Knowledge Graphs and LLMs in Action. 10. ed. Shelter Island, NY: Manning Publications, 2025. 





OLIVEIRA, N. R. et al. Generation of knowledge graphs from legislative texts: An exploratory analysis of data from the legislative assembly of rio grande do norte. Data, MDPI, Basel, Suíça, v. 10, n. 7, 2025. ISSN 2306-5729. Disponível em: <https://www.mdpi.com/2306-5729/10/7/106>. Acesso em: 15 jul. 2025. 





OSTROVSKYY, A. Production LLM: Legal Chatbot with Knowledge Graphs and LangGraph. Alex Ostrovskyy Blog, 2025. Disponível em: <https://alexostrovskyy.com /production-llm-legal-chatbot-with-knowledge-graphs-and-langgraph/>. Acesso em: 22 out. 2025. 





PARK, J. S. et al. Generative agents: interactive simulacra of human behavior. In: Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST). San Francisco: ACM, 2023. Disponível em: <https: //arxiv.org/abs/2304.03442>. Acesso em: 30 out. 2025. 





PENNINGTON, J.; SOCHER, R.; MANNING, C. GloVe: Global vectors for word representation. In: Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP). Doha, Qatar: Association for Computational Linguistics, 2014. p. 1532–1543. Disponível em: <https://aclanthology.org/D14-1162/>. Acesso em: 01 dez. 2025. 





REIMERS, N.; GUREVYCH, I. Sentence-BERT: Sentence embeddings using siamese BERT-networks. In: Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP). Hong Kong, China: Association for Computational Linguistics, 2019. p. 3982–3992. Disponível em: <https: //aclanthology.org/D19-1410/>. Acesso em: 01 dez. 2025. 





RUDER, S. et al. Transfer learning in natural language processing. In: Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Tutorials. Minneapolis, Minnesota: Association for Computational Linguistics, 2019. p. 15–18. Disponível em: <https://aclanthology.org/N19-5004/>. Acesso em: 01 dez. 2025. 





RUSSELL, S.; NORVIG, P. Artificial Intelligence: A Modern Approach. 4. ed. Boston: Pearson, 2021. 





SHAWAR, B.; ATWELL, E. Chatbots: Are they really useful? LDV Forum, Berlin, v. 22, p. 29–49, 07 2007. 





WANG, G.; ZHAN, Z.; QIN, S. Synergizing knowledge graphs and LLMs: An intelligent tutoring model for self-directed learning. Education Sciences, Basel, Suíça, v. 15, n. 9, p. 1102, 2025. Disponível em: <https://doi.org/10.3390/educsci15091102>. Acesso em: 18 out. 2025. 





WOOLDRIDGE, M. An Introduction to MultiAgent Systems. Chichester: John Wiley & Sons, 2002. 





WU, K. et al. How well do LLMs cite relevant medical references? An evaluation framework and analyses. arXiv preprint arXiv:2402.02008, 2024. Disponível em: <https://arxiv.org/abs/2402.02008>. Acesso em: 01 dez. 2025. 

