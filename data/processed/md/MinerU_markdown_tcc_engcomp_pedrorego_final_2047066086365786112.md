# Representação Matemática e Agrupamento de Assovios de Golfinhos a partir de Contornos Tempo–Frequência

Natal – RN 

Dezembro de 2025 

# Representação Matemática e Agrupamento de Assovios de Golfinhos a partir de Contornos Tempo–Frequência

Trabalho de Conclusão de Curso de Engenharia de Computação da Universidade Federal do Rio Grande do Norte, apresentado como requisito parcial para a obtenção do grau de Bacharel em Engenharia de Computação 

Orientador: Prof. Dr. Luiz Affonso Henderson Guedes de Oliveira 

Coorientador: Dr. Ignacio Sánchez Gendriz 

Universidade Federal do Rio Grande do Norte – UFRN 

Departamento de Engenharia de Computação e Automação – DCA 

Curso de Engenharia de Computação 

Natal – RN 

Dezembro de 2025 

# Universidade Federal do Rio Grande do Norte - UFRN

# Sistema de Bibliotecas - SISBI

# Catalogação de Publicação na Fonte. UFRN - Biblioteca Central Zila Mamede

Vilar Neto, Pedro Rêgo. 

Representação matemática e agrupamento de assovios de golfinhos a partir de contornos tempo-frequência / Pedro Rêgo Vilar Neto. - 2025. 

71 f.: il. 

Trabalho de Conclusão de Curso - TCC (graduação) - Universidade Federal do Rio Grande do Norte, Centro de Tecnologia, Curso de Engenharia de Computação, Natal, RN, 2025. 

Orientação: Prof. Dr. Luiz Affonso Henderson Guedes de Oliveira. 

Coorientação: Prof. Dr. Ignacio Sánchez Gendriz. 

1. Bioacústica - TCC. 2. Clusterização - TCC. 3. UMAP - TCC. 4. HDBSCAN - TCC. 5. Golfinhos - TCC. 6. Análise de sinais - TCC. I. Oliveira, Luiz Affonso Henderson Guedes de. II. Gendriz, Ignacio Sánchez. III. Título. 

RN/UF/BCZM 

CDU 004:591 

Pedro Rêgo Vilar Neto 

# Representação Matemática e Agrupamento de Assovios de Golfinhos a partir de Contornos Tempo–Frequência

Trabalho de Conclusão de Curso de Engenharia de Computação da Universidade Federal do Rio Grande do Norte, apresentado como requisito parcial para a obtenção do grau de Bacharel em Engenharia de Computação 

Orientador: Prof. Dr. Luiz Affonso Henderson Guedes de Oliveira Coorientador: Dr. Ignacio Sánchez Gendriz 

Trabalho aprovado. Natal – RN, 8 de Dezembro de 2025: 

Prof. Dr. Luiz Affonso Henderson Guedes de Oliveira — Orientador UFRN 

Dr. Ignacio Sánchez Gendriz — Coorientador UFRN 

Prof. Dr. Tiago Tavares Leite Barros — Membro da banca UFRN 

Dra. Luane Maria Stamatto Ferreira — Membro da banca UFRN 

Natal – RN 

Dezembro de 2025 

Dedico este trabalho à minha mãe, ao meu pai e ao meu irmão, pelo amor incondicional, pela força nos momentos difíceis e por acreditarem em mim muito antes que eu próprio acreditasse. 

# AGRADECIMENTOS

Agradeço primeiramente à minha mãe, por sempre me ouvir nos momentos de dúvida e incerteza, oferecendo acolhimento, força e todos os incentivos possíveis para que eu continuasse seguindo em frente. Ao meu pai, por acreditar em mim, me encorajar a enfrentar meus medos e me lembrar constantemente do meu próprio potencial. Ao meu irmão, por estar ao meu lado em todas as etapas e por me apoiar de forma incondicional. A toda a minha família, que acreditou em mim, torceu por este momento e celebrou cada pequena conquista ao longo deste caminho. 

Aos meus orientadores, Prof. Dr. Luiz Affonso Henderson Guedes de Oliveira e Dr. Ignacio Sánchez Gendriz, deixo meu sincero agradecimento pela orientação competente, pela paciência, pelas discussões enriquecedoras e pela confiança depositada durante o desenvolvimento deste trabalho. Agradeço também ao EarHub, especialmente à Profa. Dra. Renata Santoro de Sousa-Lima e a todos os integrantes do laboratório, pelo suporte contínuo, pelo acesso aos dados e pelas contribuições fundamentais da perspectiva biológica. 

Registro ainda meu agradecimento especial aos colegas que colaboraram diretamente na etapa de marcação manual dos assovios - Camila, Gabryella, Júlia, Lara, Luísa, Matheus e Sávio — cuja dedicação e cuidado foram essenciais para a construção do dataset utilizado nesta pesquisa. 

Aos amigos que me acompanharam nessa jornada, agradeço pelas conversas, pelo incentivo e pelos momentos de leveza que tornaram o processo mais humano e suportável. Mesmo sem citar nomes individualmente, cada um deles teve papel importante nesta trajetória. 

A todos os professores e servidores que contribuíram para minha formação na UFRN, sou grato pelos ensinamentos, pelo ambiente acadêmico e pelas oportunidades que moldaram meu percurso. Por fim, agradeço à Universidade Federal do Rio Grande do Norte e ao curso de Engenharia de Computação pela estrutura e pelo espaço que permitiram a realização deste trabalho. 

# RESUMO

Este trabalho apresenta um pipeline computacional para a caracterização automática de assovios de golfinhos a partir de espectrogramas obtidos com gravador autônomo subaquático. As vocalizações foram inicialmente segmentadas e anotadas manualmente, permitindo a geração de máscaras tempo–frequência que foram convertidas em contornos tonais. Cada contorno passou por suavização e foi posteriormente ajustado por polinômios de Chebyshev de grau 9, resultando em um conjunto de atributos compactos que descrevem sua modulação de frequência. A partir dessas representações, aplicou-se redução de dimensionalidade utilizando UMAP e agrupamento por densidade via HDBSCAN, possibilitando a identificação de 22 clusters principais de assovios. A análise das curvas médias revelou padrões tonais distintos, incluindo perfis ascendentes, descendentes, convexos e côncavos, refletindo tendências estruturais observadas nos espectrogramas reais. Embora alguns clusters apresentem correspondência direta com rótulos manuais tradicionais, outros exibiram maior heterogeneidade interna, indicando zonas de transição entre diferentes formas de modulação. Os resultados demonstram a eficácia da abordagem proposta na organização estrutural dos assovios e na identificação de padrões acústicos emergentes, além de oferecer uma base quantitativa promissora para estudos futuros de classificação automática e análise comportamental em bioacústica. 

Palavras-chaves: Bioacústica; Golfinhos; Contorno Tonal; Análise de Sinais; Clusterização; UMAP; HDBSCAN. 

# ABSTRACT

This work presents a computational pipeline for the automatic characterization of dolphin whistles from spectrograms collected using autonomous underwater acoustic recorder. The vocalizations were manually segmented and annotated to generate time–frequency masks, which were then converted into tonal contours. Each contour was smoothed and fitted using degree-9 Chebyshev polynomials, producing a compact set of features that describe its frequency modulation. Based on these representations, dimensionality reduction was performed using UMAP, followed by density-based clustering with HDBSCAN, resulting in 22 main whistle groups. Analysis of the mean curves revealed distinct tonal patterns, including ascending, descending, convex, and concave profiles, consistent with structural tendencies observed in real spectrograms. While some clusters showed strong correspondence with traditional manual labels, others displayed greater internal heterogeneity, indicating transitional regions between different modulation shapes. The results demonstrate the effectiveness of the proposed approach in organizing whistle structures and identifying emerging acoustic patterns, providing a promising quantitative basis for future research in automatic classification and behavioral analysis in bioacoustics. 

Keywords: Bioacoustics; Dolphins; Tonal Contour; Signal Analysis; Clustering; UMAP; HDBSCAN. 

# LISTA DE ILUSTRAÇÕES

Figura 1 – Espectogramas dos seis tipos de assovios: (A) ascendente, (B) descendente, (C) constante, (D) convexo, (E) côncavo, (F) múltiplo. . . . . . 26 

Figura 2 – Ilustração do fluxo computacional do processamento digital de sinais aplicado à análise bioacústica de cetáceos, desde a captação do som até a geração do espectrograma. 28 

Figura 3 – Exemplo de assovios de um odontoceto (golfinho) no espectograma. . . 29 

Figura 4 – Exemplo de uma redução com PCA, onde o dataset original possuia 7 dimensões. . 34 

Figura 5 – Exemplo de aplicações UMAP com diferentes parâmetros. 35 

Figura 6 – Exemplo de agrupamento com K-Means 36 

Figura 7 – Árvore de clusters (em vermelho) induzida pela função de densidade (em azul). . 3 8 

Figura 8 – Ilustração do arranjo de gravação DASBR. . 44 

Figura 9 – Exemplo de um espectograma produzido para anotação manual. . . . . 45 

Figura 10 – Exemplo de uma assovio com marcação manual no LabelMe. . . . . . . 46 

Figura 11 – Exemplo de uma máscara binária. . 47 

Figura 12 – Exemplo de uma máscara com sua curva representativa . 4 9 

Figura 13 – Exemplos reais $^ +$ curva suavizada. 54 

Figura 14 – Exemplos reais $^ +$ polinômio ajustado. 55 

Figura 15 – Fluxograma ilustrativo do processo de criação e estruturação do dataset de assovios bioacústicos. 56 

Figura 16 – Resultado do processo de redução de dimensionalidade com o PCA. . . 57 

Figura 17 – Resultado do processo de redução de dimensionalidade com o t-SNE. . 58 

Figura 18 – Resultado do processo de redução de dimensionalidade com o UMAP. . 58 

Figura 19 – Resultado do processo de agrupamento com HDBSCAN e com dimensão reduzida por UMAP. 59 

Figura 20 – Resultado do processo de agrupamento com HDBSCAN e com dimensão reduzida por UMAP, sem o cluster de ruído. 59 

Figura 21 – Comparação de 5 curvas dos clusters 17 e 5. . 61 

Figura 22 – Curvas médias e desvios padrão dos contornos de assovios agrupados pelo HDBSCAN, reconstruídos via polinômios de Chebyshev em domínio temporal real. 63 

Figura 23 – Exemplos de espectrogramas representativos dos 22 clusters identificados pelo HDBSCAN. 65 

# LISTA DE TABELAS

Tabela 1 – Coeficientes do polinômio de Chebyshev de grau 9 para os seis exemplos ilustrados na Figura 14. 54 

Tabela 2 – Distribuição das classes manuais em cada grupo identificado pelo HDBS-CAN, com total de assovios e porcentagem relativa. . 62 

# LISTA DE ABREVIATURAS E SIGLAS

A Ascendente (classe manual de assovios) 

AD Côncavo (classe manual de assovios) 

C Constante (classe manual de assovios) 

DA Convexo (classe manual de assovios) 

D Descendente (classe manual de assovios) 

CLARA Clustering Large Applications — Agrupamento para Grandes Aplicações 

CNN Convolutional Neural Network — Rede Neural Convolucional 

DASBR Drifting Acoustic Spar Buoy Recorder — Gravador Acústico Derivante do Tipo Spar Buoy 

DBSCAN Density-Based Spatial Clustering of Applications with Noise — Agrupamento Espacial Baseado em Densidade com Tratamento de Ruído 

DFT Discrete Fourier Transform — Transformada Discreta de Fourier 

dB Decibéis 

EDA Exploratory Data Analysis — Análise Exploratória de Dados 

FFT Fast Fourier Transform — Transformada Rápida de Fourier 

HDBSCAN Hierarchical Density-Based Spatial Clustering of Applications with Noise — Agrupamento Espacial Hierárquico Baseado em Densidade com Tratamento de Ruído 

IT Iniciação Tecnológica 

JSON JavaScript Object Notation — Notação de Objetos JavaScript 

JSONL JSON Lines — Formato JSON em Linhas 

kHz Quilohertz 

LPAM Long-term Passive Acoustic Monitoring — Monitoramento Acústico Passivo de Longa Duração 

M Múltiplo (classe manual de assovios) 

MST Minimum Spanning Tree — Árvore Geradora Mínima 

PAM Passive Acoustic Monitoring — Monitoramento Acústico Passivo 

PCA Principal Component Analysis — Análise de Componentes Principais 

PDS Processamento Digital de Sinais 

RMS Root Mean Square — Valor Quadrático Médio 

STFT Short-Time Fourier Transform — Transformada de Fourier de Tempo Curto 

TF Transformada de Fourier 

t-SNE $t$ -Distributed Stochastic Neighbor Embedding — Embelezamento Estocástico de Vizinhos Distribuído-t 

UMAP Uniform Manifold Approximation and Projection — Aproximação e Projeção Uniforme de Variedades 

# LISTA DE SÍMBOLOS

$t$ Tempo (s) 

$f$ Frequência (Hz ou kHz) 

$f _ { s }$ Frequência de amostragem 

$\mu$ Média 

$\sigma$ Desvio padrão 

$p ( t )$ Polinômio de Chebyshev ajustado ao contorno 

$c _ { i }$ Coeficientes do polinômio de Chebyshev 

Tn(x) Polinômio de Chebyshev de grau $n$ 

$w ( t )$ Contorno tempo–frequência do assovio 

v Vetor de características (features) de um assovio 

z Representação reduzida no espaço UMAP 

$d$ Duração temporal do assovio 

fmin Frequência mínima 

fmax Frequência máxima 

∆f Largura de banda 

N Número total de assovios analisados 

K Número de clusters identificados pelo HDBSCAN 

# SUMÁRIO

1 INTRODUÇÃO 17 

1.1 Contexto e Relevância da Bioacústica de Cetáceos 17 

1.2 Problema e Lacuna da Literatura 18 

1.2.1 Desafios na análise dos assovios 18 

1.2.2 Limitações dos Parâmetros Acústicos Tradicionais 19 

1.3 Motivação 20 

1.4 Objetivos 20 

1.4.1 Objetivo Geral 20 

1.4.2 Objetivos Específicos 21 

1.5 Estrutura do Trabalho 21 

2 CAPÍTULO 2 . . 22 

2.1 Bioacústica e Comunicação de Golfinhos 22 

2.1.1 Assovios e Função Comunicativa 22 

2.1.2 Características Acústicas dos Assovios 23 

2.1.3 Classificação dos tipos de assovio 24 

2.1.3.1 Ascendente (ou Upsweep) 24 

2.1.3.2 Descendente (ou Downsweep) 24 

2.1.3.3 Constante (ou Regular) 24 

2.1.3.4 Côncavo (ou Descendente-Ascendente) . 25 

2.1.3.5 Convexo (ou Ascendente-Descendente) 25 

2.1.3.6 Múltiplo (ou Sinusoidal/Senóide) . 25 

2.2 Análise e Representação dos assovios 26 

2.2.1 Fundamentos de Processamento Digital de Sinais (PDS) 26 

2.2.2 Espectrogramas e Transformadas de Fourier . 28 

2.3 Modelagem Matemática de Curvas 29 

2.3.1 Polinômios e Interpolação 30 

2.3.2 Aproximação de Curvas com Polinômios de Chebyshev 31 

2.4 Técnicas de Redução de Dimensionalidade e Agrupamento 32 

2.4.1 Técnicas de Redução de Dimensionalidade 32 

2.4.1.1 Métodos lineares . 33 

2.4.1.2 Métodos não lineares . 33 

2.4.2 Métodos de Agrupamento 35 

2.4.2.1 Limitações de métodos tradicionais . 36 

2.4.2.2 HDBSCAN: fundamentos e vantagens 37 

2.5 Trabalhos Relacionados 39 

2.5.1 Métodos de detecção e extração de contornos . 40 

2.5.2 Representações paramétricas 40 

2.5.3 Caracterização e análise de padrões 41 

2.5.4 Síntese final . 41 

3 CAPÍTULO 3 . . 43 

3.1 Aquisição e Organização dos Dados Acústicos 43 

3.2 Geração das Máscaras Binárias 45 

3.2.1 Vetorização das Máscaras e Conversão para Tempo–Frequência . 47 

3.3 Ajuste e Suavização dos Contornos Acústicos 48 

3.3.1 Construção da Curva Representativa 48 

3.3.2 Normalização e Ajuste por Polinômios de Chebyshev 49 

3.3.3 Extração de Atributos Finais 50 

3.4 Redução de Dimensionalidade e Agrupamento . 51 

3.4.1 Redução de Dimensionalidade 51 

3.4.2 Agrupamento via HDBSCAN 51 

3.4.3 Integração com o Modelo Acústico . 52 

4 CAPÍTULO 4 . . 53 

4.1 Pré-processamento e Construção do Dataset 53 

4.2 Redução de Dimensionalidade 55 

4.3 Agrupamento com HDBSCAN 57 

4.4 Caracterização dos Clusters . 60 

5 CONCLUSÃO 66 

REFERÊNCIAS . . . 68 

# 1 INTRODUÇÃO

O ambiente marinho impõe limitações significativas à visibilidade do animais, levando os cetáceos (que incluem baleias, golfinhos e toninhas) a desenvolver um notável sistema de emissão e recepção acústica. O som é o principal meio de comunicação na água, propagando-se aproximadamente cinco vezes mais rápido do que no ar, alcançando maiores distâncias e não sendo afetado pela turbidez (MORON, 2015). Os cetáceos dividem-se em dois grandes grupos: Misticetos, que incluem as baleias de grande porte e caracterizam-se por possuírem barbatanas filtradoras; e Odontocetos, grupo que engloba golfinhos e botos, distinguindo-se pela presença de dentes e pela capacidade de produzir vocalizações de alta frequência, como cliques e assovios (REEVES et al., 2002). 

# 1.1 Contexto e Relevância da Bioacústica de Cetáceos

O monitoramento acústico passivo (PAM) tem se destacado como uma ferramenta essencial para superar as limitações do monitoramento visual tradicional, incluindo o comportamento subaquático dos animais e os desafios ambientais e logísticos (MORON, 2015). Por meio do uso de hidrofones e gravadores acústicos autônomos, o PAM permite a coleta contínua de sons subaquáticos, inclusive durante a noite, em águas turvas ou sob alto estado de mar — situações em que a observação visual se torna inviável (ANDRIOLO et al., 2018). Nesse contexto, o estudo das vocalizações dos golfinhos é, portanto, de grande relevância para a compreensão de seus comportamentos sociais e padrões de comunicação, além de ser fundamental para o monitoramento e a conservação das espécies (CAMARGO, 2008). A variabilidade no repertório acústico de uma espécie reflete seu estado comportamental, as relações sociais, a estrutura de variação populacional e histório de seleções ambientais (MORON, 2015). 

Os odontocetos produzem três categorias principais de sinais acústicos: assovios, cliques de ecolocalização e sons pulsados explosivos (também denominados grasnidos) (MORON, 2015). Os assovios são vocalizações tonais de banda estreita, moduladas em frequência, tipicamente utilizadas em contextos sociais, como a manutenção da coesão do grupo (CAMARGO, 2008) e a coordenação de atividades. Conforme estudos de Moron (2015), uma das descobertas mais notáveis é a produção de “assovios assinatura”, sinais altamente específicos para o indivíduo, que funcionam como indicadores de identidade (KERSHENBAUM; SAYIGH; JANIK, 2013). Estudos demonstram que a informação de identidade está codificada primariamente no perfil de modulação de frequência do assovio. A complexidade sonora tonal de um assovio pode ser quantificada por meio de variáveis 

discretas, como o número de pontos de inflexão (mudanças na inclinação do contorno) e o número de alças, sendo que o aumento dessa complexidade tende a se correlacionar com a sociabilidade e o tamanho do grupo (MORON, 2015; CAMARGO, 2008). 

O espectrograma é uma representação visual derivada da Transformada de Fourier de Curto Tempo (Short-Time Fourier Transform — STFT), utilizada para descrever como o conteúdo de frequência de um sinal varia ao longo do tempo (SANCHEZ-GENDRIZ, 2021). Essa representação é composta por uma matriz de cores, em que o tempo é disposto no eixo x, a frequência no eixo y, e a amplitude (ou potência) dos bins tempo-frequência é indicada pelo gradiente de cores (SANCHEZ-GENDRIZ, 2021). Segundo Sanchez-Gendriz (2021), na Bioacústica e na Ecoacústica, o uso de espectrogramas constitui uma ferramenta essencial, pois possibilita a análise exploratória de dados acústicos (EDA) em gravações de longo prazo, permitindo aos pesquisadores caracterizar padrões temporais e espectrais de eventos acústicos biológicos. 

# 1.2 Problema e Lacuna da Literatura

# 1.2.1 Desafios na análise dos assovios

A análise quantitativa de vocalizações em estudos de bioacústica enfrenta desafios significativos. Segundo Camargo (2008), a comparação de resultados entre diferentes estudos é frequentemente dificultada por: 

1. Variabilidade Geográfica e Comportamental: Os assovios apresentam variação intraespecífica que reflete fatores como o isolamento geográfico, as condições ecológicas e o comportamento dos grupos. 

2. Inconsistências Metodológicas e Vieses: Diferenças no limite superior de frequência dos equipamentos de gravação, na largura de banda de análise e na interpretação subjetiva dos espectrogramas por diferentes pesquisadores podem levar a resultados inconsistentes, especialmente em parâmetros como duração, frequência mínima e frequência máxima. 

3. Ruído Ambiente Biológico: Em habitats costeiros, o alto ruído de fundo — incluindo sons transientes e de banda larga, como o dos camarões pistola — interfere na visualização dos contornos tonais, comprometendo a clareza dos espectrogramas e a medição precisa dos parâmetros. 

4. Ruído de Embarcações: Em regiões costeiras e estuarinas, o ruído antrópico proveniente de embarcações constitui uma das principais fontes de mascaramento acústico, reduzindo a detectabilidade dos assovios e podendo afetar o comportamento 

vocal dos golfinhos. Além disso, sistemas PAM rebocados devem registrar sinais em faixas acima da banda dominada pelo ruído da própria plataforma. 

5. Ruído de Ondas Quebrando e Condições Oceanográficas: O alto estado do mar e a quebra de ondas aumentam significativamente o ruído de fundo, dificultando a análise visual e degradando a relação sinal-ruído dos assovios. Em ambientes rasos, variações de temperatura, salinidade e turbidez influenciam a propagação do som, podendo atenuar ou distorcer os contornos dos sinais tonais. 

6. Efeitos na Precisão dos Parâmetros Acústicos: A presença de ruído (natural ou antrópico) pode levar à seleção preferencial de assovios com boa relação sinal-ruído, introduzindo vieses na amostragem e dificultando a extração confiável de parâmetros como frequência final, frequência máxima e modulações rápidas. 

Diante desse cenário, torna-se evidente a importância de desenvolver métodos capazes de representar, descrever e comparar de forma objetiva os padrões de modulação de frequência observados nos assovios dos golfinhos. Essa necessidade motiva a busca por ferramentas computacionais que reduzam a subjetividade das análises e possibilitem uma caracterização mais consistente das vocalizações. 

# 1.2.2 Limitações dos Parâmetros Acústicos Tradicionais

A análise bioacústica de cetáceos tem se baseado tradicionalmente na extração de parâmetros acústicos contínuos e discretos de fácil mensuração em espectrogramas, como duração, frequência mínima, frequência máxima, número de inflexões e número de quebras (CAMARGO, 2008; MORON, 2015). Embora amplamente empregados, esses descritores apresentam alta variabilidade intraespecífica e não capturam a geometria não linear do contorno tonal, limitando sua capacidade de representar a estrutura completa dos assovios (MORON, 2015). 

Diversos estudos reportam dificuldades em agrupar assovios de forma consistente a partir desses parâmetros, resultando em baixas métricas de qualidade de agrupamento em análises tradicionais como CLARA (Clustering Large Applications), e em categorias qualitativas que nem sempre possuem significado biológico claro (MORON, 2015). De acordo com Moron (2015), a natureza arbitrária dessas classificações dificulta a generalização das variações observadas entre populações e compromete análises comparativas robustas. 

Apesar dos avanços do long-term passive acoustic monitoring (LPAM) — uma abordagem que utiliza gravadores acústicos autônomos para coletar sons ambientais de forma contínua, frequentemente 24 horas por dia ao longo de vários meses (SANCHEZ-GENDRIZ, 2021) — ainda existe uma lacuna crítica na literatura, tanto nacional quanto internacional, no desenvolvimento de métodos capazes de modelar automaticamente a estrutura temporal 

e espectral dos contornos tonais de forma contínua, quantitativa e comparável (MORON, 2015). Assim, torna-se necessário propor metodologias computacionais que representem essa complexidade de forma principial, reduzindo a subjetividade e ampliando o potencial de classificação e reconhecimento acústico. 

# 1.3 Motivação

A ideia para o desenvolvimento deste trabalho surgiu durante a participação do autor em um projeto de Iniciação Tecnológica (IT) no Laboratório de Bioacústica da Universidade Federal do Rio Grande do Norte (EarHub) (BIOACOUSTICS, 2025), sob a coordenação da professora Dra. Renata Santoro Sousa-Lima. O laboratório realiza pesquisas com gravações acústicas de diferentes animais, resultando em um vasto acervo de dados sonoros. 

No decorrer dessa experiência, foi identificada uma demanda específica do laboratório: a necessidade de caracterizar com maior precisão o formato e o contorno dos assovios produzidos por golfinhos. Diante dessa necessidade concreta, surgiu o interesse em propor uma abordagem computacional que pudesse auxiliar na análise automática desses sinais acústicos. Além de representar um desafio técnico relevante, o tema mostrou-se particularmente significativo por envolver dados reais e contribuir diretamente para as atividades do laboratório, fortalecendo a integração entre pesquisa científica e desenvolvimento tecnológico. 

Assim, este trabalho busca propor uma abordagem de caracterização automática dos assovios de golfinhos a partir de suas representações espectrográficas, empregando técnicas de processamento digital de sinais para ajustar curvas que descrevem o contorno tonal dessas vocalizações. A partir dessas representações, pretende-se extrair parâmetros quantitativos que possam auxiliar em análises comportamentais e comparações entre indivíduos e grupos, contribuindo para o avanço das metodologias de análise bioacústica. Para atender a essa demanda, este trabalho integra a aproximação polinomial dos contornos tonais, a projeção desses descritores em espaços de baixa dimensão e a identificação automática de agrupamentos baseada em densidade, oferecendo uma alternativa quantitativa às classificações tradicionais. 

# 1.4 Objetivos

# 1.4.1 Objetivo Geral

Desenvolver uma metodologia de caracterização automática dos assovios de golfinhos, com base na extração e no ajuste do contorno tonal, uma curva que descreve a variação 

da frequência dominante de um assovio ao longo do tempo, a partir de espectrogramas, visando quantificar e descrever seus padrões de modulação de frequência. 

# 1.4.2 Objetivos Específicos

• Implementar técnicas de processamento digital de sinais para a geração e análise de espectrogramas das vocalizações. 

• Aplicar métodos de ajuste de curvas, como interpolação e aproximação polinomial, para representar o contorno tonal dos assovios. 

• Aplicar técnicas de redução de dimensionalidade para representar vetores de características em espaços de menor dimensão preservando sua estrutura local. 

• Empregar métodos de agrupamento baseados em densidade para identificar padrões acústicos emergentes. 

• Propor métricas quantitativas para descrever propriedades dos assovios. 

• Avaliar a aplicabilidade da metodologia em dados reais de gravações do Laboratório de Bioacústica (EarHub/UFRN). 

# 1.5 Estrutura do Trabalho

Este trabalho inicia com uma contextualização sobre a comunicação acústica dos golfinhos, apresentando a motivação, a justificativa e os objetivos gerais da pesquisa. Em seguida, o Capítulo 2 reúne os fundamentos teóricos necessários, abrangendo aspectos de bioacústica, processamento digital de sinais, técnicas de extração e modelagem de contornos tonais, além de métodos de agrupamento e redução de dimensionalidade. O Capítulo 3, por sua vez, detalha a metodologia adotada para a geração dos espectrogramas, construção das máscaras binárias, extração dos contornos e ajuste dos polinômios de Chebyshev utilizados como representação compacta dos assovios. No Capítulo 4, são discutidos os resultados obtidos, explorando a caracterização dos clusters, as tendências observadas e a interpretação acústica dos grupos formados. Por fim, o Capítulo 5 traz as conclusões, limitações do trabalho e possíveis direções para pesquisas futuras. 

# 2 REFERENCIAL TEÓRICO

Este capítulo apresenta o referencial teórico que fundamenta o desenvolvimento deste trabalho, abordando os principais conceitos, métodos e técnicas relacionados à análise de sinais acústicos de odontocetos. Inicialmente, discutem asepectos gerais da bioacústica e das características espectrais dos assovios, seguidos pela revisão de métodos matemáticos e computacionais aplicados à representação e caracterização de curvas, como técnicas de interpolação e aproximação polinomial. Além disso, serão apresentadas técnicas modernas de redução de dimensionalidade e agrupamento, com ênfase em métodos como o Uniform Manifold Approximation and Projection (UMAP) e o Hierarchical Density-Based Spatial Clustering of Applications with Noise (HDBSCAN), que oferecem ferramentas essenciais para explorar padrões estruturais e a variabilidade acústica nos assovios analisados. 

# 2.1 Bioacústica e Comunicação de Golfinhos

Os odontocetos desenvolveram um notável sistema de emissão e recepção acústica (MORON, 2015). Conforme Camargo (2008) o mecanismo de produção sonora nos odontocetos é distinto dos mamíferos terrestres, envolvendo tampões musculares associados aos sacos nasais, onde o som é gerado pela passagem de ar dentro desses sacos, sem envolver a laringe. Os sinais acústicos dos odontocetos são geralmente classificados em três categorias: assovios (sinais tonais de frequência variável contínua), cliques de ecolocalização (sons pulsados de curta duração, usados para navegação e forrageamento) e uma variedade de sons pulsados explosivos (burst pulses) usados na comunicação social (MORON, 2015). Entre os sinais acústicos produzidos pelos odontocetos, os assovios se destacam por sua importância na comunicação social e de identidade, sendo objeto de intensos estudos comportamentais e acústicos. 

# 2.1.1 Assovios e Função Comunicativa

Segundo Camargo (2008) função social dos assovios é crucial, desempenhando um papel fundamental na manutenção da coesão social e na organização dos agrupamentos. Em curtas distâncias, a comunicação por assovios é usada em interações sociais que envolvem identificação individual, agressão e manutenção do contato (MORON, 2015). Uma das funções mais estudadas é a do assovio assinatura, que são assovios repetitivos considerados indivíduo-específicos e que funcionam como indicadores individuais (CAMARGO, 2008). Moron (2015) afirma que o assovio assinatura é um sinal aprendido e distintivo que transporta a identidade do emissor através do seu padrão de modulação de frequência. 

Além disso, os assovios são frequentemente usados na comunicação entre fêmeas e filhotes. Também variam a taxa de emissão de assovios de acordo com o horário, como observado em golfinhos-rotadores (Stenella longirostris) no Havaí, onde a taxa é cinco a dez vezes maior no período noturno, possivelmente ligada à necessidade de maior coesão social quando a visibilidade é limitada (CAMARGO, 2008). 

Dada a importância desses sinais, a caracterização qualitativa e quantitativa de suas propriedades acústicas torna-se essencial para compreender os mecanismos de comunicação e diferenciação entre espécies e populações. 

# 2.1.2 Características Acústicas dos Assovios

Os assovios são emissões acústicas de banda estreita com frequência variável ao longo do tempo (MORON, 2015). Sua principal característica é o contorno de frequência, que descreve a variação da frequência instantânea em função do tempo e é comumente analisado a partir de espectrogramas (CAMARGO, 2008). Ainda segundo Camargo (2008), essa abordagem permite extrair parâmetros que descrevem quantitativamente e qualitativamente a forma e o comportamento do sinal. 

As variáveis acústicas são geralmente divididas em dois conjuntos: parâmetros contínuos, relacionados à frequência e à duração, e parâmetros discretos, que descrevem a forma do contorno (CAMARGO, 2008; MORON, 2015). Entre os parâmetros contínuos mais comuns estão a frequência inicial, frequência final, frequência mínima, frequência máxima e a duração (CAMARGO, 2008). Outras medidas, apontadas por Rodrigues (2014), como variação de frequência, frequência dominante e amplitude espectral, também são relevantes para caracterizar o comportamento temporal e espectral do assovio. 

Já entre os parâmetros discretos, destacam-se o número de pontos de inflexão (que indica mudanças de inclinação no contorno), o número de quebras (variações abruptas na frequência) e o número de alças (curvaturas no traçado) (CAMARGO, 2008; RODRIGUES, 2014). 

A variabilidade desses parâmetros reflete aspectos comportamentais, sociais e ambientais (CAMARGO, 2008; MORON, 2015). De modo geral, as frequências inicial e final apresentam baixa variabilidade intrapopulacional, enquanto a duração e o número de inflexões tendem a variar mais entre indivíduos ou contextos (CAMARGO, 2008). Conforme apontado por Moron (2015), essa variabilidade pode estar associada à modulação individual dos sinais e ao processo de aprendizagem vocal observado em diversas espécies de odontocetos. 

Por fim, destaca-se que as medições dos parâmetros acústicos podem, segundo Camargo (2008), variar conforme o sistema de gravação, o método de análise e a interpretação do pesquisador, sendo recomendada cautela na comparação de resultados entre diferentes 

estudos. A categorização dos assovios segundo o formato de seus contornos será detalhada no próximo subtópico. 

# 2.1.3 Classificação dos tipos de assovio

A classificação dos assovios de cetáceos constitui um passo fundamental para a compreensão do comportamento acústico das espécies, uma vez que permite descrever as propriedades estruturais das emissões sonoras e compreender suas possíveis funções comunicativas (ANDRIOLO et al., 2018). 

A metodologia mais utilizada para categorizar assovios baseia-se na análise visual de espectrogramas, a partir da forma do contorno da frequência fundamental ao longo do tempo (ANDRIOLO et al., 2018). Andriolo et al. (2018) aponta que essa abordagem, embora subjetiva, é amplamente empregada em estudos comparativos por permitir a padronização qualitativa do repertório acústico entre espécies e populações. 

Os contornos são classificados de acordo com a inclinação/declive da frequência e pelo número de pontos de inflexão (ANDRIOLO et al., 2018), na figura 1 é possível ver o contorno tonal dos tipos. Tradicionalmente, são reconhecidas seis categorias principais de contornos de assovios: 

# 2.1.3.1 Ascendente (ou Upsweep)

Caracteriza-se por um aumento contínuo da frequência durante a emissão (ANDRI-OLO et al., 2018). É um dos contornos mais comuns observados em populações de botos e golfinhos (RODRIGUES, 2014). Segundo Rodrigues (2014), assim como o tipo constante, o ascendente não apresenta pontos de inflexão. 

# 2.1.3.2 Descendente (ou Downsweep)

O contorno exibe uma diminuição contínua da frequência ao longo do tempo (ANDRIOLO et al., 2018). Também é considerado um contorno simples, sem pontos de inflexão, e geralmente aparece como segundo tipo mais frequente em repertórios naturais, como no caso dos golfinhos-rotadores registrados na quebra da plataforma continental brasileira (RODRIGUES, 2014). 

# 2.1.3.3 Constante (ou Regular)

O assovio apresenta um contorno praticamente reto, com frequência que se mantém estável ao longo do tempo, sem variações significativas (ANDRIOLO et al., 2018). Este tipo de assovio não possui pontos de inflexão e é geralmente raro no repertório de espécies como Stenella longirostris (golfinho-rotador) e Sotalia guianensis (boto-cinza) (RODRIGUES, 2014). 

# 2.1.3.4 Côncavo (ou Descendente-Ascendente)

A frequência inicia em valores mais altos, diminui e depois volta a subir, formando uma curva em formato de “U” (ANDRIOLO et al., 2018). Este tipo apresenta um ponto de inflexão e é descrito formalmente como um contorno descendente-ascendente (ANDRIOLO et al., 2018). 

# 2.1.3.5 Convexo (ou Ascendente-Descendente)

É o oposto do côncavo: a frequência sobe inicialmente e depois decresce, formando uma curva semelhante a um “U” invertido (ANDRIOLO et al., 2018). Assim como o anterior, o contorno possui um ponto de inflexão, sendo também classificado entre os tipos simples com modulação de frequência moderada (ANDRIOLO et al., 2018). 

# 2.1.3.6 Múltiplo (ou Sinusoidal/Senóide)

Representa o tipo de assovio mais complexo, caracterizado por duas ou mais inversões na inclinação da frequência, ou seja, dois ou mais pontos de inflexão (ANDRIOLO et al., 2018). De acordo com Bazúa-Durán (2004) é descrito como um contorno altamente modulado ou ondulatório, e frequentemente denominado sinusoidal. Apesar de sua complexidade, esta categoria tende a ser pouco representativa — em Sotalia guianensis, foi observada em apenas 0,37% das emissões analisadas (RODRIGUES, 2014). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/e1a2081e63e2f416301e43bd945ffed4f0b2cad418e76fdf560bf3a718f9d434.jpg)



Figura 1 – Espectogramas dos seis tipos de assovios: (A) ascendente, (B) descendente, (C) constante, (D) convexo, (E) côncavo, (F) múltiplo.



Fonte: Rodrigues (2014).


# 2.2 Análise e Representação dos assovios

A transformação dos assovios em representações adequadas para análise quantitativa baseia-se em técnicas de processamento digital de sinais e resulta, principalmente, na geração do espectrograma (SANCHEZ-GENDRIZ, 2021). O espectrograma é a representação gráfica da frequência instantânea do assovio em função do tempo (CAMARGO, 2008). Para produzi-lo, o sinal de áudio é processado por meio da Transformada Rápida de Fourier (FFT)(MORON, 2015).Essa representação é considerada essencial, pois, a partir dela, torna-se possível a descrição e a quantificação dos sinais acústicos emitidos pelos cetáceos (ver fluxo de processamento na figura 2) (CAMARGO, 2008). 

# 2.2.1 Fundamentos de Processamento Digital de Sinais (PDS)

O Processamento Digital de Sinais constitui o alicerce técnico que possibilita a análise quantitativa de sons de cetáceos. Esse campo da engenharia transforma sinais físicos e contínuos, como os captados por hidrofones em ambientes subaquáticos, em dados numéricos discretos, permitindo a manipulação, a filtragem e a extração de informações acústicas relevantes (SANCHEZ-GENDRIZ, 2021). 

Em bioacústica, conforme Sanchez-Gendriz (2021) aponta, um sinal é entendido como uma sequência de valores que representam a variação de uma grandeza física ao longo do tempo. As variáveis acústicas na natureza são contínuas, e portanto, os sinais analógicos podem assumir infinitos valores em um intervalo finito de tempo. Para serem processados digitalmente, esses sinais precisam ser convertidos em sinais discretos, o que ocorre por meio dos processos de amostragem e quantização (SANCHEZ-GENDRIZ, 2021). A amostragem (sampling) converte o tempo contínuo em tempo discreto, registrando o valor do sinal em intervalos específicos. A frequência de amostragem (fs) define quantas amostras são coletadas por segundo e deve ser escolhida de modo a preservar as informações de interesse. Já a quantização consiste em converter as amplitudes contínuas em valores numéricos de precisão finita, representando cada amostra por um nível discreto. 

A escolha da taxa de amostragem é particularmente crítica em estudos com odontocetos, pois esses animais produzem sons que podem atingir centenas de quilohertz (RODRIGUES, 2014). Em geral, taxas de 96 kHz ou superiores a 192 kHz são empregadas para assegurar a captura fiel das frequências fundamentais e harmônicos dos assovios (ANDRIOLO et al., 2018; MORON, 2015), que podem se estender à faixa ultrassônica, segundo apontado por Camargo (2008). De acordo com o Teorema de Nyquist-Shannon, para evitar a perda de informação a frequência de amostragem deve ser superior ao dobro da maior frequência presente no sinal ( $f _ { s } > 2 f _ { m a x } .$ ) (SANCHEZ-GENDRIZ, 2021). 

Após a digitalização, a análise quantitativa do sinal requer a conversão do domínio do tempo para o domínio da frequência. Essa abordagem permite observar os contornos tonais e padrões espectrais característicos dos assovios. 

Essa transformação está sujeita ao compromisso entre resolução temporal e espectral, detalhado na subseção seguinte. Assim, a escolha dos parâmetros depende do tipo de sinal analisado: assovios contínuos demandam alta resolução espectral, enquanto sinais pulsados curtos, como burst-pulses, requerem maior resolução temporal (CAMARGO, 2008). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/7b7f1dac47ae934dec91cdc5ba06c2086c359fb9601da87282e4921f05d055c8.jpg)



Figura 2 – Ilustração do fluxo computacional do processamento digital de sinais aplicado à análise bioacústica de cetáceos, desde a captação do som até a geração do espectrograma.



Fonte: Elaborado pelo autor (2025).


# 2.2.2 Espectrogramas e Transformadas de Fourier

A análise bioacústica de sinais, como os assovios de golfinhos, depende fundamentalmente de ferramentas de processamento de sinais que permitam visualizar e quantificar a variação temporal do conteúdo em frequência (SANCHEZ-GENDRIZ, 2021). Conforme mostrado por Sanchez-Gendriz (2021), a Transformada de Fourier (TF) é o princípio matemático central dessa análise, ao possibilitar a decomposição de um sinal em suas componentes senoidais elementares. No domínio do tempo, um sinal é descrito pela variação de sua amplitude ao longo do tempo; no domínio da frequência, a Transformada de Fourier revela a amplitude e frequência dessas componentes, oferecendo uma visão espectral do sinal. Para sinais discretos, utiliza-se a DFT (SANCHEZ-GENDRIZ, 2021), cuja implementação eficiente é realizada por algoritmos de FFT, altamente empregados em linguagens de programação como MATLAB, Python e R. 

Entretanto, a DFT tradicional é adequada apenas para sinais estacionários, cujas características espectrais não variam no tempo. Os assovios de golfinhos, por outro lado, são sinais não estacionários, com modulação de frequência contínua (MORON, 2015). Para analisá-los, utiliza-se a STFT (ver equação 2.1), que divide o sinal em janelas temporais sucessivas, dentro das quais a DFT é calculada (SANCHEZ-GENDRIZ, 2021). 

$$
X (t, \omega) = \sum_ {n = - \infty} ^ {\infty} x [ n ] w [ n - t ] e ^ {- j \omega n} \tag {2.1}
$$

A geração de um espectrograma requer a definição de parâmetros fundamentais, entre eles o tamanho da janela, que determina o equilíbrio entre resolução temporal e resolução espectral. Esse compromisso, conhecido como Princípio da Incerteza, implica que janelas mais longas oferecem melhor resolução em frequência, mas menor precisão temporal — e vice-versa (SANCHEZ-GENDRIZ, 2021). Outros parâmetros importantes incluem o tipo de janela, o percentual de sobreposição entre janelas (segundo Camargo (2008) valores de 50% são comuns na análise de assovios), e a escala de amplitude, frequentemente expressa em decibéis (dB) por meio de transformações logarítmicas (LI et al., 2023). 

Nos espectrogramas de assovios, observa-se um contorno de frequência que reflete a variação tonal ao longo do tempo. Esse contorno constitui a base para a interpretação e quantificação acústica (ver Figura 3). Em complemento, técnicas de interpolação e modelagem matemática de curvas, permitem representar de forma contínua e suave os contornos extraídos dos espectrogramas, mitigando oscilações e possibilitando análises quantitativas refinadas. Este tema será abordado na próxima seção. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/4e41bfdb9d2884a496802d12df7d0dbb7251ce18fae033802281b55253e1b04d.jpg)



Figura 3 – Exemplo de assovios de um odontoceto (golfinho) no espectograma.



Fonte: Adaptado de Camargo (2008).


# 2.3 Modelagem Matemática de Curvas

A modelagem matemática de curvas constitui uma etapa essencial na análise de sinais bioacústicos, sobretudo no estudo dos assovios de odontocetos (MORON, 2015). Embora o contorno do assovio, também chamado de contorno da frequência fundamental 

(CAMARGO, 2008), seja uma forma contínua (ver Figura 3), a análise digital produz dados discretos, obtidos a partir de pontos de frequência medidos em instantes específicos, segundo Moron (2015) aponta. Assim, torna-se necessária uma representação analítica contínua que recupere o comportamento original do sinal. 

A modelagem de curvas possibilita suavizar, analisar e comparar dados experimentais com maior precisão (MORON, 2015). Ao converter dados discretos em curvas matematicamente contínuas, é possível calcular características acústicas relevantes (como duração, frequências extremas e número de pontos de inflexão) de forma objetiva e reprodutível. 

Diversas técnicas podem ser utilizadas para a modelagem de curvas, entre elas métodos baseados em funções polinomiais. Contudo, a interpolação polinomial clássica apresenta limitações importantes, sobretudo quando se utilizam pontos igualmente espaçados, levando ao Fenômeno de Runge, um aumento significativo do erro de oscilação nas bordas do intervalo (RODRIGUES, 2022). Nesse contexto, os polinômios de Chebyshev oferecem uma alternativa particularmente estável: como formam uma base ortogonal no intervalo $[ - 1 , 1 ]$ e utilizam nós distribuídos de maneira não equidistante, esses polinômios reduzem significativamente as oscilações nas extremidades e atenuam os efeitos do mau condicionamento (RIVLIN, 1990). 

# 2.3.1 Polinômios e Interpolação

A interpolação polinomial é um conceito matemático fundamental amplamente utilizado para aproximar funções contínuas a partir de um conjunto discreto de pontos (ATKINSON, 1989). O conceito da interpolação consiste em encontrar uma função $p ( x )$ que pertence a uma determinada classe, de modo que o gráfico de $y = p ( x )$ passe exatamente pelos pontos fornecidos. No caso da interpolação polinomial, conforme apontado por Rodrigues (2022), essa classe é formada por polinômios, que apresentam propriedades analíticas vantajosas, como a facilidade no cálculo de derivadas e integrais, o que os torna convenientes para aplicações computacionais e científicas. 

Dado um conjunto de $n + 1$ pontos distintos $( x _ { 0 } , y _ { 0 } ) , \ldots , ( x _ { n } , y _ { n } )$ , o objetivo é encontrar um polinômio interpolador $p ( x )$ de grau menor ou igual a $n$ que satisfaça $p ( x _ { i } ) = y _ { i }$ para todo $i$ . O Teorema da Interpolação Polinomial garante a existência e unicidade de tal polinômio (ATKINSON, 1989). Sua obtenção pode ser feita por diferentes métodos, entre os quais se destacam o método de Lagrange e o método de Newton por diferenças divididas. No método de Lagrange, conforme demonstrado por Atkinson (1989), o polinômio é construído como uma combinação linear dos valores $y _ { i }$ , ponderados por funções base $l _ { k } ( x )$ que valem 1 em $x _ { k }$ e 0 nos demais pontos (ver equação 2.2). Já o método de Newton representa o polinômio através de uma soma de termos com coeficientes obtidos 

por diferenças divididas, o que o torna mais eficiente quando se deseja adicionar novos pontos ao conjunto (ver equação 2.3) (ATKINSON, 1989). 

$$
P _ {n} (x) = \sum_ {i = 0} ^ {n} y _ {i} l _ {i} (x) \tag {2.2}
$$

$$
P _ {n} (x) = f (x _ {0}) + (x - x _ {0}) (x - x _ {1}) f [ x _ {0}, x _ {1}, x _ {2} ] + \ldots + (x - x _ {0}) \ldots (x - x _ {(n - 1)}) f [ x _ {0}, x _ {1},.., x _ {n} ] (2. 3)
$$

Apesar de sua simplicidade, a interpolação polinomial apresenta limitações quando aplicada a muitos pontos. Uma forma eficiente de reduzir as oscilações que surgem na interpolação polinomial com pontos igualmente espaçados é utilizar os polinômios de Chebyshev. Esses polinômios fazem uso de pontos de interpolação especialmente distribuí- dos, que evitam o aumento do erro nas extremidades do intervalo e tornam a aproximação mais estável (RODRIGUES, 2022). Dessa forma, os nós de Chebyshev constituem uma alternativa simples e eficaz para contornar o Fenômeno de Runge (RODRIGUES, 2022) e motivam o uso de bases polinomiais ortogonais, que serão discutidas na seção seguinte. 

# 2.3.2 Aproximação de Curvas com Polinômios de Chebyshev

Os polinômios de Chebyshev de primeira espécie, definidos pela relação $T _ { n } ( x ) =$ cos $n ( \operatorname { a r c c o s } x )$ , formam uma família de polinômios ortogonais de grande relevância na análise numérica (RIVLIN, 1990). Segundo Rivlin (1990), uma de suas aplicações mais importantes consiste na aproximação de funções por meio de séries de Chebyshev, nas quais a função é representada como combinação linear dos polinômios $T _ { n } ( x )$ . A escolha dos nós de Chebyshev, correspondentes às raízes desses polinômios, desempenha papel fundamental nesse processo. Esses nós não são igualmente espaçados, em vez disso, concentram-se nas extremidades do intervalo, reduzindo as oscilações do polinômio interpolador e diminuindo substancialmente o erro máximo de aproximação (RODRIGUES, 2022). Essa distribuição não uniforme garante melhor estabilidade numérica e melhora o condicionamento da interpolação, mesmo para graus mais elevados (RODRIGUES, 2022). 

A utilização de Chebyshev para aproximar curvas contínuas é particularmente vantajosa quando se deseja representar trajetórias suavemente moduladas (RODRIGUES, 2022), como os contornos tempo–frequência dos assovios analisados neste trabalho. De acordo com Rivlin (1990), quando uma curva é aproximada por uma série de Chebyshev, como: 

$$
p (x) = \sum_ {k = 0} ^ {n} A _ {k} T _ {k} (x),
$$

Na caso, os coeficientes $A _ { k }$ obtidos tornam-se descritores numéricos compactos e padronizados da forma do contorno. Devido à ortogonalidade dos polinômios $T _ { k } ( x )$ , esses 

coeficientes são determinados de forma estável e representam quantitativamente aspectos relevantes da curva, como sua tendência global, concavidade e variações de frequência . Dessa forma, cada assovio pode ser convertido em um vetor de características diretamente comparável entre diferentes amostras, constituindo uma representação matematicamente robusta para análises subsequentes de agrupamento e de exploração da variabilidade acústica. 

# 2.4 Técnicas de Redução de Dimensionalidade e Agrupamento

A análise de dados de alta dimensionalidade frequentemente demanda técnicas que permitam representar informações complexas de forma mais compacta e interpretável. Nesse contexto, redução de dimensionalidade e agrupamento constituem ferramentas fundamentais para a exploração de estruturas latentes em conjuntos de dados (MCINNES et al., 2018). Conforme estudado por McInnes et al. (2018), métodos lineares como a Análise de Componentes Principais (PCA) fornecem representações simplificadas ao preservar direções de maior variância, enquanto abordagens não lineares, como o UMAP, buscam preservar relações de vizinhança em espaços de alta dimensão, sendo especialmente eficazes em dados com estruturas complexas. Complementarmente, técnicas de agrupamento permitem identificar padrões, relações de similaridade e possíveis categorias emergentes sem necessidade de rótulos prévios (MCINNES; HEALY, 2017). McInnes e Healy (2017) aponta que entre os métodos baseados em densidade, o HDBSCAN destaca-se por detectar clusters de diferentes formas e densidades, além de identificar pontos de ruído de maneira robusta, o que o torna adequado para análises exploratórias em dados acústicos não estruturados. Esses conceitos fundamentam as subseções a seguir, que apresentam os princípios teóricos das técnicas utilizadas neste trabalho. 

# 2.4.1 Técnicas de Redução de Dimensionalidade

A redução de dimensionalidade é uma etapa fundamental na análise de dados de alta dimensão, pois permite transformar representações complexas em estruturas mais compactas e interpretáveis, preservando ao máximo a informação essencial contida no conjunto original (MCINNES et al., 2018). Essa técnica é crucial tanto para pré- processamento em machine learning quanto para visualização de dados, especialmente diante dos efeitos adversos da maldição da dimensionalidade, que prejudica a eficácia de algoritmos baseados em distância (BRENNDOERFER, 2025; MCINNES et al., 2018). Em termos gerais, os métodos de redução podem ser classificados segundo o tipo de estrutura que buscam preservar, variando entre abordagens que mantêm relações globais entre os pontos, preservando distâncias ponto a ponto, e abordagens que privilegiam estruturas locais, enfatizando a proximidade entre vizinhos no espaço de alta dimensão (MCINNES 

et al., 2018). Essa distinção fundamenta a divisão tradicional entre métodos lineares e métodos não lineares, discutidos nas subseções seguintes. 

# 2.4.1.1 Métodos lineares

Os métodos lineares de redução de dimensionalidade têm como objetivo projetar dados de alta dimensão em um subespaço de menor dimensão por meio de transformações lineares que preservam, na medida do possível, a estrutura global do conjunto de dados. Entre essas abordagens, a PCA (Análise de Componentes Principais - Principal Component Analisys), proposta originalmente por Pearson em 1901 e formalizada por Hotelling em 1933, constitui a técnica mais difundida e consolidada na literatura (JOLLIFFE, 2002; BISHOP, 2006). A PCA busca identificar direções ortogonais que maximizam a variância dos dados, permitindo obter uma representação compacta, interpretável e com mínima perda de informação. N figura 4 é possível observar um exemplo de dados que tiveram sua dimensionalidade reduzida pela PCA. 

Dado um conjunto de dados centrado na média, representado pela matriz $X \in R ^ { n \times d }$ , a PCA baseia-se no cálculo da matriz de covariância, que é dada por: 

$$
C = \frac {1}{n - 1} X ^ {\top} X. \tag {2.4}
$$

Conforme mostrado por Bishop (2006), a redução de dimensionalidade decorre da decomposição espectral de $C$ , na qual seus autovetores associados aos maiores autovalores representam as direções de maior variabilidade do conjunto de dados. Seja $W \in R ^ { d \times k }$ a matriz cujas colunas correspondem aos $k$ autovetores principais; a projeção dos dados no novo subespaço é dada por: 

$$
Z = X W.
$$

A PCA apresenta diversas vantagens, incluindo eficiência computacional, robustez matemática e interpretabilidade direta dos componentes principais. Entretanto, sua natureza linear limita sua capacidade de modelar estruturas complexas que residem em variedades não lineares do espaço de alta dimensão. Em conjuntos de dados nos quais relações de vizinhança local são mais importantes que direções globais de variância, como ocorre frequentemente em dados bioacústicos, técnicas não lineares tornam-se mais adequadas, conforme discutido a seguir. 

# 2.4.1.2 Métodos não lineares

Ao contrário das técnicas lineares, os métodos não lineares de redução de dimensionalidade assumem que os dados não ocupam todo o espaço de alta dimensão que estão representados. Nesses casos, preservar apenas direções globais de variância pode ser 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/d5da99b360ab2ca79943863b9945b6171006adf0e0373811d6d959bed88f98e6.jpg)



Figura 4 – Exemplo de uma redução com PCA, onde o dataset original possuia 7 dimensões. Fonte: Adaptado de Jolliffe (2002).


insuficiente para capturar relações estruturais relevantes. Técnicas não lineares buscam, portanto, preservar relações de vizinhança local, permitindo reconstruir representações que refletem adequadamente a geometria intrínseca dos dados (TENENBAUM; SILVA; LANGFORD, 2000; BELKIN; NIYOGI, 2001). 

Entre os métodos não lineares modernos, o UMAP (Uniform Manifold Approximation and Projection) destaca-se por sua fundamentação matemática baseada em geometria Riemanniana e topologia algébrica, bem como por sua eficiência computacional e capacidade de preservar simultaneamente estruturas locais e globais (MCINNES et al., 2018). O UMAP opera em duas etapas principais: 

1. Construção de um grafo de vizinhança fuzzy no espaço original; 

2. Otimização de uma representação em baixa dimensão que aproxima esse grafo. 

Na primeira etapa, para cada ponto $x _ { i }$ , determina-se um conjunto de $k$ vizinhos mais próximos, denotado por $N _ { k } ( x _ { i } )$ . Em seguida, constrói-se uma medida de afinidade local entre pontos, dada pela função suavizada (ver equação 2.5), sendo $d ( \cdot , \cdot )$ é uma métrica de distância, $\rho _ { i }$ representa a distância ao vizinho mais próximo e $\sigma _ { i }$ é o parâmetro de normalização que controla a largura da vizinhança (MCINNES et al., 2018). O grafo fuzzy resultante combina afinidades direcionais, preservando a estrutura de conectividade local. 

$$
w _ {i j} = \exp \left(- \frac {\operatorname * {m a x} (0 , d (x _ {i} , x _ {j}) - \rho_ {i})}{\sigma_ {i}}\right) \tag {2.5}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/c9e1978844b55453f1ff090df75e5cfc91ba586e177859bd8d546bf09e6e51ea.jpg)



Figura 5 – Exemplo de aplicações UMAP com diferentes parâmetros.



Fonte: Adaptado de McInnes et al. (2018).


Na segunda etapa, o UMAP busca uma representação em baixa dimensão que minimize a divergência entre o grafo fuzzy original e um grafo análogo no espaço projetado. Essa otimização é feita por meio da minimização de uma função de perda que aproxima a similaridade entre pares de pontos, dada pela equação 2.6, onde os parâmetros $a$ e $b$ controlam a forma da função de decaimento da similaridade no espaço projetado, na figura 5 é possível ver como diferentes parâmetros podem alterar seu resultado final. 

$$
\mathcal {L} = \sum_ {(i, j)} w _ {i j} \log \frac {1}{1 + a | | y _ {i} - y _ {j} | | ^ {2 b}} + (1 - w _ {i j}) \log \left(1 - \frac {1}{1 + a | | y _ {i} - y _ {j} | | ^ {2 b}}\right) \qquad (2. 6)
$$

A capacidade do UMAP de preservar vizinhanças locais com alta fidelidade, aliada ao seu desempenho computacional, torna-o uma ferramenta extremamente eficaz para dados de alta dimensionalidade, especialmente em cenários de análise exploratória (MCINNES et al., 2018). Em aplicações bioacústicas, em que contornos tempo-frequência capturam variações complexas ao longo do tempo, métodos não lineares como o UMAP são particularmente adequados para revelar padrões estruturais e facilitar etapas subsequentes de agrupamento. 

# 2.4.2 Métodos de Agrupamento

O agrupamento é uma técnica de aprendizado não supervisionado cujo objetivo central é identificar estruturas de similaridade em um conjunto de dados, organizando amostras em grupos internamente homogêneos e externamente distintos (MCINNES; HE-ALY, 2017). Ainda segundo McInnes e Healy (2017), trata-se de uma ferramenta essencial na EDA, uma vez que permite revelar padrões latentes, sugerir categorias emergentes e orientar a formulação de novas hipóteses de pesquisa. Em cenários de alta dimensionalidade, o agrupamento é frequentemente aplicado após técnicas de redução de dimensionalidade, 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/af189e4ea54ad6b54cbb10bebd6ac236facbb21d6f36e6bac68f7fb306ffc4e0.jpg)



Figura 6 – Exemplo de agrupamento com K-Means



Fonte: Adaptado de Brenndoerfer (2025).


como o UMAP, que transformam os dados originais em representações mais compactas, preservando relações locais e globais de interesse (MCINNES; HEALY, 2017; MCINNES et al., 2018). Essa etapa prévia facilita a identificação visual e computacional de agrupamentos naturais na projeção de baixa dimensão, permitindo explorar estruturas que ficariam obscurecidas no espaço original. 

Diversas abordagens de clustering foram propostas na literatura, refletindo diferentes interpretações sobre o que constitui um agrupamento natural. Entre essas abordagens encontram-se os métodos particionais, como o K-Means, os métodos hierárquicos, que constroem representações em níveis sucessivos de granularidade, e os métodos baseados em densidade, como o Density-Based Spatial Clustering of Applications with Noise (DBS-CAN) e o HDBSCAN (KERSHENBAUM; SAYIGH; JANIK, 2013; MCINNES; HEALY, 2017). Para dados complexos e potencialmente ruidosos, como aqueles provenientes de estudos biológicos (SANCHEZ-GENDRIZ, 2021), os métodos baseados em densidade são especialmente relevantes, pois não exigem suposições rígidas sobre a forma dos grupos e são capazes de distinguir regiões densamente povoadas de regiões esparsas, identificando explicitamente pontos de ruído (MCINNES; HEALY, 2017). Além disso, segundo Brenndoerfer (2025), métodos hierárquicos baseados em densidade, como o HDBSCAN, têm a vantagem adicional de não requerer a definição prévia do número de clusters, o que é uma característica desejável em contextos exploratórios nos quais o número de estruturas presentes nos dados é desconhecido. Os trechos a seguir aprofundam as limitações dos métodos tradicionais e apresentam os fundamentos teóricos que tornam o HDBSCAN particularmente adequado para análise de dados projetados pelo UMAP e, de maneira geral, para o estudo de fenômenos bioacústicos complexos. 

# 2.4.2.1 Limitações de métodos tradicionais

Os métodos tradicionais de clustering apresentam limitações substanciais quando aplicados a dados de alta dimensionalidade, especialmente após projeções não lineares 

como as geradas pelo UMAP (MCINNES; HEALY, 2017). O algoritmo K-Means, por exemplo, pressupõe implicitamente que os clusters possuem formatos aproximadamente esféricos, isotrópicos e de tamanhos semelhantes (BRENNDOERFER, 2025)(ver figura 6, uma suposição raramente satisfeita por dados com estrutura complexa. Sua formulação busca minimizar a soma das distâncias quadráticas entre cada ponto e o centróide do cluster (MCINNES; HEALY, 2017) (ver equação 2.7), o que induz fronteiras lineares entre clusters e torna o método inadequado para dados cuja geometria apresenta curvatura ou padrões não lineares (ver figura 6). Além disso, o K-Means exige a definição prévia do número de clusters, é sensível à inicialização e, por ser um método de partição rígida, atribui ruído e outliers a algum cluster (MCINNES; HEALY, 2017), comprometendo a interpretação exploratória. 

$$
J (C, \mu) = \sum_ {i = 1} ^ {k} \sum_ {x \in C _ {i}} \| x - \mu_ {i} \| ^ {2} \tag {2.7}
$$

Métodos hierárquicos, como Agrupamento Aglomerativo, oferecem uma representação em múltiplas escalas por meio de dendrogramas, porém enfrentam dificuldades semelhantes (KERSHENBAUM; SAYIGH; JANIK, 2013). Critérios de ligação como single linkage são suscetíveis ao efeito de encadeamento (MCINNES; HEALY, 2017), conectando regiões densas por meio de cadeias artificiais de pontos esparsos, enquanto métodos como complete linkage, segundo McInnes e Healy (2017) aponta, tendem a formar grupos excessivamente compactos. Esses algoritmos também apresentam alto custo computacional, baixa robustez a ruído e forte dependência da métrica adotada, tornando-se pouco escaláveis e inadequados para bases de grande volume ou para dados com geometria intrincada (MCINNES; HEALY, 2017). 

# 2.4.2.2 HDBSCAN: fundamentos e vantagens

O HDBSCAN é um método de agrupamento baseado em densidade que supera as limitações do DBSCAN ao incorporar princípios de agrupamento hierárquico (BRENN-DOERFER, 2025). De acordo com Brenndoerfer (2025), sua formulação permite lidar de forma robusta com clusters de densidades variáveis, identificar explicitamente pontos de ruído e, sobretudo, não exige a definição prévia do número de clusters, característica particularmente valiosa em cenários exploratórios. Ao substituir o parâmetro global $\epsilon$ do DBSCAN por uma abordagem adaptativa baseada em densidade local, o HDBSCAN tornase capaz de modelar estruturas complexas de forma mais precisa e estável (MCINNES; HEALY, 2017). 

O algoritmo inicia-se com o cálculo da distância core, definida para cada ponto $x$ como a distância até seu $k$ -ésimo vizinho mais próximo, onde $k$ corresponde ao parâmetro min_samples, ver equação 2.8 (BRENNDOERFER, 2025). Essa métrica traduz a densidade 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/2d9231dfa1b5645e14583d4ca7a3ea3c20320cfe8c25facd88d4345ae0ecf548.jpg)



Figura 7 – Árvore de clusters (em vermelho) induzida pela função de densidade (em azul).



Fonte: McInnes e Healy (2017).


local, ou seja, quanto mais densa a região, menor é a distância core (BRENNDOERFER, 2025). Em seguida, o algoritmo redefine a métrica de distância entre pares de pontos, utilizando a distância de alcançabilidade mútua (ver equação 2.9). Essa transformação “estica” distâncias em regiões esparsas e preserva conectividades naturais em regiões densas, permitindo detectar clusters com densidades heterogêneas sem depender de um único limiar global (BRENNDOERFER, 2025). 

$$
c o r e _ {k} (x) = d (x, k N N (x)) \tag {2.8}
$$

$$
d _ {m r e a c h} (x, y) = \max  \left\{c o r e _ {k} (x), c o r e _ {k} (y), d (x, y) \right\} \tag {2.9}
$$

Com base nessa métrica densidade-consciente, o HDBSCAN constrói uma Árvore Geradora Mínima (MST), ver Figura 7, sobre o grafo completo dos dados, minimizando o custo total das arestas (BRENNDOERFER, 2025; MCINNES; HEALY, 2017), conforme mostrado na equação 2.10. A hierarquia de clusters surge ao remover, iterativamente, arestas da árvore em ordem decrescente de peso, revelando agrupamentos estáveis em diferentes níveis de densidade (BRENNDOERFER, 2025). Para selecionar os clusters mais representativos, o algoritmo utiliza o conceito de estabilidade, que conforme Brenndoerfer (2025) mostra, quantifica a persistência de um cluster à medida que a densidade mínima exigida varia. Para cada ponto $x$ , registra-se o limiar de densidade $\lambda _ { b i r t h } ( x )$ no qual ele entra no cluster, e $\lambda _ { d e a t h } ( x )$ no qual o abandona, com $\lambda = 1 / ( d i s t \hat { \mathrm { a } } n c i a \_ c o r e )$ . A estabilidade total de um cluster $C$ $\mathrm { é }$ dada pela equação 2.11 (BRENNDOERFER, 2025; MCINNES; HEALY, 2017). Selecionando como clusters finais aqueles que maximizam essa medida, sob a restrição de que os grupos escolhidos não sejam subconjuntos uns dos outros (MCINNES; HEALY, 2017). Esse critério elimina a necessidade de ajustes manuais complexos e garante que apenas estruturas realmente persistentes sejam consideradas. 

$$
\min  _ {T} \sum_ {(x, y) \in T} d _ {\mathrm {m r e a c h}} (x, y) \tag {2.10}
$$

$$
e s t a b i l i d a d e (C) = \sum_ {x \in C} \left(\lambda_ {d e a t h} (x) - \lambda_ {b i r t h} (x)\right) \tag {2.11}
$$

A aplicação do HDBSCAN é especialmente vantajosa em ambientes de alta complexidade estrutural, como dados bioacústicos derivados de assovios de golfinhos. Contornos tempo–frequência apresentam geometria altamente variável (MORON, 2015), com inflexões, modulações abruptas e densidades desbalanceadas, características incompatíveis com métodos como K-Means ou DBSCAN. Após a redução de dimensionalidade via UMAP, que projeta os dados preservando relações locais não lineares, a estrutura resultante forma clusters de formas arbitrárias, frequentemente aninhados e separados por regiões de baixa densidade (BRENNDOERFER, 2025). O HDBSCAN opera precisamente nesse contexto: identifica automaticamente grupos de densidades distintas, é robusto a ruído e não impõe suposições rígidas sobre a forma dos clusters (BRENNDOERFER, 2025; MCINNES; HEALY, 2017). Com base nesses fundamentos, a próxima seção apresenta estudos que aplicam técnicas semelhantes em contextos bioacústicos ou em tarefas de modelagem e agrupamento de sinais, evidenciando o estado da arte relacionado a este trabalho. 

# 2.5 Trabalhos Relacionados

A análise bioacústica de assovios, constitui um passo fundamental para caracterizar o comportamento acústico das espécies de golfinhos (ANDRIOLO et al., 2018), sendo essencial para compreender relações sociais, coesão de grupo, estrutura populacional e padrões de variação intra e interespecífica (CAMARGO, 2008). Tradicionalmente, essa análise baseia-se na visualização do sinal por meio de espectrogramas (SANCHEZ-GENDRIZ, 2021), representações tempo-frequência que permitem uma exploração inicial dos dados, prática comum em Ecoacústica. A partir dessa visualização, a literatura segue duas abordagens principais: a anotação manual e classificação visual subjetiva dos contornos em categorias qualitativas (CAMARGO, 2008; MORON, 2015); e a extração quantitativa de medidas acústicas, incluindo parâmetros de frequência, tempo e estrutura, como frequência inicial, final, mínima, máxima, variação de frequência e duração, além de descritores discretos como número de pontos de inflexão, quebras no contorno, alças e presença de harmônicos (MORON, 2015). A escolha dessas variáveis decorre de sua fácil mensuração em espectrogramas e de sua ampla utilização na literatura, o que favorece comparações entre populações e estudos distintos (MORON, 2015; CAMARGO, 2008). 

# 2.5.1 Métodos de detecção e extração de contornos

A detecção automática de assovios de odontocetos tem avançado significativamente nos últimos anos, acompanhando o crescimento das técnicas de processamento de sinais e aprendizagem profunda aplicadas a dados bioacústicos. Entre os métodos recentes, destacam-se abordagens baseadas em redes neurais convolucionais (CNNs), capazes de identificar assovios mesmo em ambientes acusticamente complexos e com sobreposição de vocalizações, superando algoritmos tradicionais (KORKMAZ et al., 2022; JIN et al., 2022). Outros trabalhos exploram métricas de entropia como uma alternativa não supervisionada para detectar assovios e cliques em gravações ruidosas (SIDDAGANGAIAH et al., 2020), enquanto métodos de transformada de Hough, contornos ativos e filtros bayesianos/sequenciais têm sido empregados para rastrear automaticamente vocalizações individuais ao longo do espectrograma, inclusive em situações de múltiplos alvos (KORKMAZ et al., 2022; SERRA; MARTINS; PADOVESE, 2020; ROCH et al., 2011). 

Após a detecção, a extração do contorno tonal, costuma ser realizada por técnicas de peak tracking, que conectam picos de energia para reconstruir a trajetória da frequência fundamental (ROCH et al., 2011; MELLINGER et al., 2011). Embora o rastreamento manual em softwares como Raven Pro ainda seja utilizado como referência e validação (KORKMAZ et al., 2022), métodos totalmente automáticos têm sido cada vez mais adotados, incluindo segmentação semântica baseada em CNNs, pyknogramas e filtros de partículas, além de rotinas de processamento de imagem para realce e seguimento das cristas espectrais (JIN et al., 2022). Uma vez extraído, o contorno pode ser suavizado ou representado matematicamente, por exemplo, por meio de curvas polinomiais ou splines, facilitando análises quantitativas e comparações entre diferentes vocalizações (LI et al., 2020). 

# 2.5.2 Representações paramétricas

A representação do contorno tonal por curvas suaves é amplamente empregada na literatura para facilitar a análise quantitativa de assovios. Métodos baseados em polinômios ajustados por mínimos quadrados buscam gerar uma descrição matemática compacta do assovio, reduzindo ruídos e conectando pontos espectrais de forma contínua (LI et al., 2022). Apesar da simplicidade, esses modelos são sensíveis ao grau do polinômio e tendem a apresentar instabilidades ou superajuste em regiões de alta curvatura (VOLOSHKINA; KOVALOVA; SIPAKOV, 2024). 

De forma complementar, splines, especialmente B-splines e splines cúbicas, têm sido adotadas por oferecerem suavidade, robustez ao ruído e controle local, permitindo ajustar trechos do contorno sem alterar toda a curva (BRIGGER; HOEG; UNSER, 2000). Essas características tornam as splines adequadas para reconstruir assovios com 

descontinuidades ou variações abruptas, e algumas abordagens combinam splines com técnicas de regularização para melhorar a fidelidade em dados esparsos (JOVER et al., 2022). 

Em síntese, tanto polinômios quanto splines constituem ferramentas eficazes para suavizar e representar contornos de assovios, mas diferem quanto ao controle local, estabilidade numérica e capacidade de lidar com regiões complexas. 

# 2.5.3 Caracterização e análise de padrões

A extração de características a partir do contorno tonal dos assovios, como valores de frequência ao longo do tempo, modulação, número de picos, duração ou coeficientes derivados de representações matemáticas, fornece uma base quantitativa para comparar vocalizações e investigar padrões individuais ou populacionais (SERRA; MARTINS; PA-DOVESE, 2020; KERSHENBAUM; SAYIGH; JANIK, 2013). Esses vetores de features costumam ser analisados por técnicas de redução de dimensionalidade, incluindo métodos lineares como PCA (KERSHENBAUM; SAYIGH; JANIK, 2013), que destacam os componentes mais informativos, e abordagens não lineares, como $t$ -Distributed Stochastic Neighbor Embedding (t-SNE) e UMAP (WANG et al., 2020), utilizadas para revelar estruturas locais e subgrupos em conjuntos complexos de assovios. 

Com os dados projetados em espaços de menor dimensão, aplica-se tipicamente alguma forma de clustering para identificar grupos naturais, classificar tipos de assovios ou explorar variações intra e interespecíficas. Algoritmos como k-means são amplamente usados quando se assume um número prévio de categorias (KERSHENBAUM; SAYIGH; JANIK, 2013), enquanto métodos baseados em densidade, como HDBSCAN, permitem detectar agrupamentos sem essa premissa e são mais robustos ao ruído (MCINNES; HEALY, 2017). Abordagens funcionais, que tratam o contorno como uma curva contínua, também têm mostrado bom desempenho na agrupação de assovios suavizados (LABRIOLA et al., 2025). 

# 2.5.4 Síntese final

Apesar dos avanços na extração e análise de contornos de assovios, a literatura ainda carece de padronização na vetorização desses contornos, uma vez que diferentes métodos de extração geram representações heterogêneas e de difícil comparação (LABRIOLA et al., 2025). O uso de máscaras e segmentação robusta também permanece pouco integrado aos pipelines quantitativos, limitando a identificação precisa das regiões relevantes do espectrograma (JIN et al., 2022). Além disso, há pouca exploração sistemática de ajustes polinomiais, sobretudo com bases ortogonais como Chebyshev, para representar e comparar contornos de forma compacta (LABRIOLA et al., 2025). Soma-se a isso a ausência de 

pipelines integrados que unifiquem vetorização, redução de dimensionalidade e clustering, o que reduz a reprodutibilidade e dificulta comparações entre estudos (HUANG et al., 2022). 

Diversos estudos na área de bioacústica têm explorado métodos de vetorização de contornos, técnicas de redução de dimensionalidade e algoritmos de agrupamento para caracterizar e comparar assovios. Entretanto, ainda há pouca uniformidade quanto à forma de representar matematicamente essas curvas e à integração entre as etapas do processamento. À luz dessas abordagens, este trabalho se apoia em estratégias consolidadas — como o ajuste de curvas por polinômios de Chebyshev, métodos de manifold learning como o UMAP e algoritmos de clusterização robustos como o HDBSCAN — para construir um pipeline coerente e reprodutível. Assim, buscou-se alinhar práticas já presentes na literatura, ampliando sua aplicabilidade ao propor uma padronização na vetorização dos contornos e uma combinação estruturada entre vetorização, redução de dimensionalidade e agrupamento. 

# 3 METODOLOGIA

O presente capítulo descreve detalhadamente os procedimentos metodológicos adotados para a análise das vocalizações tonais de odontocetos utilizadas neste estudo. A metodologia foi estruturada de forma sequencial, iniciando pela aquisição e organização dos dados acústicos, seguida da geração de espectrogramas e das etapas de anotação manual e vetorização dos assovios. Em seguida, apresenta-se o processo de conversão das máscaras binárias para coordenadas no domínio tempo–frequência e a modelagem matemática dos contornos por meio de técnicas de suavização e ajuste polinomial. Finalmente, descrevem-se os métodos de redução de dimensionalidade e agrupamento não supervisionado empregados para investigar padrões latentes na morfologia dos assovios. 

# 3.1 Aquisição e Organização dos Dados Acústicos

Os dados utilizados neste trabalho provêm do acervo do Laboratório de Bioacústica da Universidade Federal do Rio Grande do Norte (EarHub), resultante de campanhas de PAM. As gravações foram obtidas por meio de um arranjo do tipo Drifting Acoustic Spar Buoy Recorder (DASBR), um sistema autônomo de aquisição acústica desenvolvido para registrar séries temporais contínuas de pressão sonora em ambientes marinhos. 

O DASBR consiste em uma boia de deriva com equipamentos de rastreio (como GPS) e sinalização, acoplada a um cabo subaquático de tamanho variável, com um gravador, hidrofones e um lastro na extremidade para que o sistema permaneça vertical na coluna d’água. Diferentemente dos sistemas rebocados por embarcações, o DASBR deriva junto com as correntes, o que elimina o ruído mecânico gerado pelo arrasto. Essa característica confere ao sistema uma plataforma de gravação acusticamente silenciosa, favorecendo a detecção de sinais de baixa e alta frequência emitidos por cetáceos — incluindo espécies evasivas ou de difícil observação direta (ver Figura 8). Como uma plataforma de baixo custo e longa duração de operação, o DASBR possibilita o monitoramento acústico extensivo em regiões oceânicas profundas ou costeiras onde a presença constante de embarcações seria logisticamente inviável. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/a86535e3ee6c3d588b1c9b056290b30bb475d4791ca470fcb0c8f23036793def.jpg)



Figura 8 – Ilustração do arranjo de gravação DASBR.



Fonte: Elaborado pelo autor (2025).


As gravações utilizadas neste estudo referem-se aos dias 10, 11 e 12 de dezembro de 2024, coletadas durante a expedição “Araguari Dezembro 2024”, na região do entorno de Fernando de Noronha, Pernambuco, Brasil. O sistema DASBR utilizado era composto por um gravador modelo SoundTrap, com dois hidrofones, registrando a uma taxa amostral de 384 kHz, 16 bits, em arquivos WAV. O equipamento foi deixado talingado ao navio atracado por um cabo de aproximadamente 50 m, posicionando o gravador a uma profundidade de cerca de 17 m. Em conjunto com os registros acústicos, foi fornecida uma planilha de detecção preliminar de assovios, contendo marcações de horário e observações que orientaram a seleção inicial dos segmentos analisados. 

Os registros obtidos correspondem muito provavelmente à população residente de golfinhos-rotadores (Stenella longirostris) de Fernando de Noronha, amplamente documentada na literatura como socialmente estruturada e de ocorrência regular na região (CAMARGO, 2008). 

Após a organização dos arquivos, procedeu-se ao pré-processamento, que envolveu a segmentação dos trechos de interesse e a padronização dos arquivos para garantir compatibilidade com as etapas seguintes. Apenas os segmentos contendo assovios previamente identificados foram mantidos para análise. 

Em seguida, foram gerados os espectrogramas (ver figura 9), etapa fundamental para a representação tempo–frequência dos assovios. Para cada trecho selecionado, aplicou-se a STFT utilizando os parâmetros definidos no processamento: tamanho da janela com 

1 

4096 pontos, com passo de avanço igual a 10% do tamanho da janela (410 amostras), e janela do tipo Hann, adequada para a redução de descontinuidades entre fatias sucessivas. A profundidade temporal de cada espectrograma foi definida a partir de uma janela de análise de 1,0 segundo, acrescida de uma margem de 0,2 s antes e depois do trecho de interesse, de modo a garantir que toda a emissão fosse registrada mesmo em detecções aproximadas. 

Os espectrogramas foram calculados com frequência de amostragem nativa de cada arquivo e exibidos no intervalo de 3 kHz a 20 kHz, faixa correspondente à região onde se concentra a energia fundamental dos assovios analisados. A sobreposição implícita entre janelas correspondeu a 90%, resultante do valor de tamanho da janela adotado. Cada matriz espectral foi então convertida para escala logarítmica (dB) e plotada com eixos, otimizando a visualização do contorno tonal. Foram produzidos 774 espectogramas, que serviram de base para as etapas subsequentes de anotação manual, geração das máscaras binárias e modelagem matemática dos contornos acústicos. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/c4786038bb6a1df7f6f176fb8f4af87f93eb9b859d1bfca0d76e3c142880e7a1.jpg)



Figura 9 – Exemplo de um espectograma produzido para anotação manual.



Fonte: Elaborado pelo autor (2025).


# 3.2 Geração das Máscaras Binárias

A anotação manual dos assovios foi realizada utilizando o software LabelMe, uma ferramenta amplamente empregada para a marcação de polígonos em imagens. Os espectrogramas produzidos na etapa anterior foram importados para o ambiente de anotação, e 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/da9768ef15f88a15b1b9601c9da9ea8475b29450e525046df9741183759d00ba.jpg)



Figura 10 – Exemplo de uma assovio com marcação manual no LabelMe.



Fonte: Elaborado pelo autor (2025).


cada contorno tonal visível foi delimitado por meio de polígonos desenhados manualmente ao redor de sua região no domínio tempo–frequência (ver figura 10). Além da marcação espacial, cada polígono recebeu um rótulo correspondente a um dos seis tipos de contorno de assovio descritos na seção 2.1.3: constante, ascendente, descendente, côncavo, convexo ou múltiplo (ver Figura 1). Permitindo associar, desde a etapa de anotação, a categoria qualitativa do assovio ao segmento marcado. 

A marcação foi realizada pelo autor com o apoio dos pesquisadores do EarHub/U-FRN, que contribuíram no processo de revisão e validação das anotações, assegurando consistência e qualidade nas identificações visuais. Como muitos espectrogramas apresentavam mais de um assovio na mesma imagem, cada polígono foi tratado individualmente, garantindo que diferentes emissões fossem separadas e posteriormente analisadas como instâncias distintas. 

Concluída a etapa de anotação, os arquivos JavaScript Object Notation (JSON) gerados pelo LabelMe foram processados para produzir as máscaras binárias correspondentes. Para cada polígono, foi criada uma imagem em que os pixels pertencentes à área delimitada eram marcados com o valor 1 (assovio), enquanto o restante da imagem recebia o valor 0 (imagem de fundo), como é ilustrado na figura 11. Esse procedimento permitiu gerar, para cada emissão anotada, uma representação binária precisa de sua forma no espectrograma automaticamente. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/bfe5ea040d6706a7c651c505dbdf820588e44bd9c9060974d7f70749964344ff.jpg)



Figura 11 – Exemplo de uma máscara binária.



Fonte: Elaborado pelo autor (2025).


Ao final do processo, a separação dos polígonos individuais resultou em mais de 1500 assovios isolados, cada um representado por sua respectiva máscara binária e associado ao tipo de contorno anotado. Esse conjunto estruturado constituiu a base para as etapas subsequentes de extração dos contornos tempo–frequência, modelagem matemática com polinômios e construção do dataset final. 

# 3.2.1 Vetorização das Máscaras e Conversão para Tempo–Frequência

Após a geração das máscaras binárias, cada assovio foi submetido ao processo de vetorização, no qual os pixels pertencentes à região marcada (valor 1) foram transformados em um conjunto de coordenadas discretas. A partir de cada máscara, extraiu-se o contorno externo da região delimitada, obtendo-se uma curva em coordenadas de imagem (x, y) representando o formato bidimensional do assovio no espectrograma. 

Essa vetorização permitiu recuperar, para cada emissão, uma descrição geométrica precisa da forma tonal registrada. Contudo, como as máscaras existem no espaço de pixels, foi necessário convertê-las para o domínio físico de interesse (tempo e frequência) a partir dos parâmetros utilizados na geração dos espectrogramas. 

Essa conversão garante que todos os assovios possam ser comparados entre si de forma consistente, independentemente de variações nos espectrogramas originais, na resolução gráfica ou nos limites de exibição. A conversão foi realizada considerando: 

• a resolução temporal da STFT, dada pelo valor do tamanho da janela (hop_length), pela taxa de amostragem do sinal; 

• pela resolução espectral, definida pelo tamanho da FFT (n_fft = 4096) e pelo mapeamento entre índice de frequência e bins espectrais; 

• o intervalo de visualização utilizado na geração dos espectrogramas (FMIN = 3000 Hz e FMAX = 20000 Hz); 

• o tamanho da janela de análise de 1 segundo acrescida de margens de 0,2 s antes e depois da vocalização. 

Assim, cada ponto (x, y) do contorno em pixel foi transformado nas coordenadas correspondentes no tempo (ver equação 3.2) e na frequência (ver equação ) 

$$
t = x \times \frac {\text {h o p ＿ l e n g t h}}{f _ {s}} \tag {3.1}
$$

$$
f = \frac {y}{N _ {\text {f r e q}}} \times \left(F _ {\max } - F _ {\min }\right) + F _ {\min } \tag {3.2}
$$

O número de bins verticais ( $N _ { f r e q } )$ ) utilizados na conversão para o eixo de frequência corresponde ao número de pixels presentes no eixo vertical da imagem do espectrograma após o recorte do intervalo $[ F _ { m i n } , F _ { m a x } ]$ . Dessa forma, a resolução espectral efetiva é determinada simultaneamente pelo tamanho da STFT e pela resolução gráfica do espectrograma exportado. 

O resultado desse processo foi a obtenção de curvas discretizadas representando, em unidades reais, o contorno tonal de cada assovio, agora prontos para serem tratados como séries de pontos em tempo e frequência, constituindo a base necessária para as etapas seguintes de suavização, interpolação e modelagem matemática. 

# 3.3 Ajuste e Suavização dos Contornos Acústicos

Após a obtenção das curvas tempo–frequência provenientes da vetorização das máscaras binárias, cada assovio passou por um processo de suavização, padronização e modelagem matemática com o objetivo de gerar uma representação contínua e estável do seu contorno tonal. 

# 3.3.1 Construção da Curva Representativa

Os contornos extraídos diretamente das máscaras apresentam uma densidade variável de pontos e podem conter pequenas flutuações decorrentes de ruído ou artefatos da STFT. Para obter uma representação consistente, aplicou-se um método robusto de construção da linha central, definido em três etapas: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/76283b28f05044aa88add2b9c311f58d2ec8e8e34edfbee26502783c066cc1e2.jpg)



Figura 12 – Exemplo de uma máscara com sua curva representativa Fonte: Elaborado pelo autor (2025).


1. Discretização temporal adaptativa: O intervalo total do assovio foi subdividido em um número de janelas proporcional à sua duração, garantindo densidade uniforme ao longo do tempo. 

2. Cálculo robusto da frequência representativa por janela: Para cada janela temporal, foram extraídos todos os valores de frequência pertencentes ao contorno vetorizarizado. A frequência representativa foi calculada como a média entre os quantis 25% e 75% [(Q25 + Q75)/2]. 

3. Interpolação de valores ausentes e suavização: Janelas sem valores válidos foram preenchidos via interpolação linear, e a curva resultante foi suavizada com um filtro gaussiano unidimensional ( $\sigma = 1$ ,2), produzindo uma linha central contínua e regularizada. 

O resultado desse procedimento é uma curva (tempo, frequência) suave, com resolução uniforme, que representa o curso principal do assovio, como mostrado na figura 12. 

# 3.3.2 Normalização e Ajuste por Polinômios de Chebyshev

Antes da modelagem matemática, o eixo temporal foi normalizado para que cada contorno iniciasse em $\mathrm { { t } = 0 }$ . Essa padronização facilita o ajuste polinomial e a comparação entre diferentes vocalizações, além de simplificar o domínio dos polinômios utilizados. 

Para representar os contornos de forma compacta e matematicamente bem condicionada, adotou-se o ajuste por polinômios de Chebyshev, amplamente utilizados em aproximação numérica devido à sua estabilidade em comparação à interpolação polinomial clássica. 

$$
f (t) \approx T _ {n} (t) \tag {3.3}
$$

O ajuste foi realizado utilizando a equação 3.3. Onde $T _ { n }$ é um polinômio de Chebyshev de grau 9, definido no domínio temporal com a duração do assovio. O grau 9 foi selecionado empiricamente como o menor valor capaz de capturar a variação principal dos contornos sem induzir oscilações artificiais. 

Para cada assovio, o erro do ajuste foi calculado via Root Mean Square Error (RMSE), ver equação 3.4, entre a linha central suavizada e os valores previstos pelo polinômio. 

$$
R M S E = \sqrt {\frac {1}{N} \sum \left(f _ {r e a l} - f _ {a j u s t a d a}\right) ^ {2}} \tag {3.4}
$$

Esse valor foi armazenado como um atributo do dataset, permitindo avaliar a qualidade da aproximação e identificar eventuais casos atípicos. 

# 3.3.3 Extração de Atributos Finais

Além dos coeficientes do polinômio, foram calculados para cada assovio: 

• Duração total; 

• Frequência mínima; 

• Frequência máxima; 

• Largura de banda; 

• Erro de ajuste (RMSE); 

• Rótulo original da anotação e 

• Nome do arquivo de origem; 

A partir desses atributos, foi construído o dataset final no formato JSON Lines (JSONL), no qual cada linha corresponde a um assovio individual, contendo tanto sua representação matemática (coeficientes polinomiais) quanto seus parâmetros acústicos básicos e metadados. Esse dataset estruturado serviu como base para as etapas posteriores 

da análise, descritas na sequência da metodologia, incluindo os procedimentos de redução de dimensionalidade aplicados aos coeficientes gerados e os algoritmos de agrupamento utilizados para investigar padrões latentes na morfologia dos assovios. 

# 3.4 Redução de Dimensionalidade e Agrupamento

Após a construção do dataset final contendo os coeficientes do polinômio de Chebyshev e os atributos acústicos derivados, procedeu-se à etapa de redução de dimensionalidade e agrupamento não supervisionado. O objetivo dessa etapa é investigar padrões latentes na morfologia dos assovios a partir de suas representações matemáticas, avaliando se diferentes tipos de contornos dão origem a estruturas separáveis no espaço vetorial. 

# 3.4.1 Redução de Dimensionalidade

A projeção dos vetores de características em um espaço de dimensionalidade inferior foi realizada utilizando o método UMAP em modo não supervisionado. O procedimento foi dividido em duas etapas: 

1. Primeira projeção para 10 dimensões: redução inicial do vetor padronizado para um espaço intermediário de 10 dimensões, preservando grande parte da variância estrutural do dataset. 

2. Projeção para 2 dimensões: Utilização do espaço 10D como entrada para uma segunda aplicação do UMAP, desta vez reduzindo para duas dimensões, a fim de possibilitar inspeção visual e facilitar interpretações posteriores. 

A escolha do espaço intermediário de 10 dimensões como entrada para o clustering (em vez do embedding 2D) visa preservar uma quantidade maior de estrutura geométrica, permitindo que os algoritmos de agrupamento identifiquem padrões mais robustos. Além disso, a seleção dos parâmetros do UMAP (especialmente n_neighbors = 15, min_dist = 0.1 e a métrica euclidiana) buscou equilibrar a preservação da estrutura local dos dados com a manutenção de relações globais, permitindo que variações sutis da morfologia dos assovios fossem representadas no espaço reduzido sem gerar fragmentação excessiva. 

# 3.4.2 Agrupamento via HDBSCAN

Com os embeddings de 10 dimensões obtidos pelo UMAP, aplicou-se o algoritmo HDBSCAN, um método de agrupamento baseado em densidade capaz de identificar clusters de formatos arbitrários, sem a necessidade de pré-definir o número de grupos. Essa 

característica é especialmente relevante para dados bioacústicos, nos quais não há garantia de que os assovios se organizem em estruturas esféricas ou bem separadas. O HDBSCAN foi configurado com os seguintes parâmetros principais: 

• min_cluster_size: valores testados entre 10 e 30 com valor escolhido de 20; 

• min_samples: valores testados entre 1 e 5, com o valor escolhido de 3; 

• Métrica euclidiana; 

• cluster_selection_method = ’leaf’, que favorece agrupamentos mais granulares. 

Para cada combinação de parâmetros, o algoritmo produziu um conjunto de rótulos de cluster, um índice de ruído (pontos classificados como outliers) e métricas descritivas utilizadas posteriormente na análise dos resultados. A escolha final dos parâmetros levou em consideração o equilíbrio entre o número de clusters, consistência estrutural, percentual de pontos rotulados como ruído e interpretabilidade acústica dos agrupamentos. 

# 3.4.3 Integração com o Modelo Acústico

A aplicação conjunta de UMAP e HDBSCAN permitiu projetar o conjunto de assovios em um espaço morfológico reduzido, revelando agrupamentos estruturais derivados exclusivamente dos contornos matemáticos e atributos acústicos modelados nas etapas anteriores. Essa organização não supervisionada serviu como base analítica para a interpretação e discussão apresentadas no Capítulo 4, possibilitando a comparação empírica entre os clusters gerados e as categorias tradicionais de contornos descritas no referencial teórico. 

# 4 RESULTADOS E DISCUSSÃO

Este capítulo apresenta os resultados obtidos na caracterização dos assovios de golfinhos a partir das máscaras tempo-frequência vetorizadas, dos contornos suavizados e das features derivadas do ajuste polinomial. São descritos os principais achados do pré-processamento, incluindo a estabilidade dos contornos após a suavização e a adequação do conjunto final de atributos acústicos. Em seguida, são analisadas as projeções em baixa dimensionalidade, destacando-se o desempenho superior do UMAP na organiza-ção estrutural dos assovios. Por fim, são discutidos os agrupamentos identificados pelo HDBSCAN, bem como a relação entre clusters e classes acústicas, a partir da geração de perfis médios e da inspeção de exemplos reais. Os resultados são apresentados de forma integrada, buscando evidenciar padrões relevantes para a compreensão da variabilidade acústica dos assovios e avaliar a eficácia do pipeline desenvolvido. 

# 4.1 Pré-processamento e Construção do Dataset

Após o processamento das máscaras tempo–frequência vetorizadas, um total de 1.515 contornos apresentou qualidade suficiente para ser incluído no dataset final. Os contornos passaram por normalização temporal e pela construção de uma linha central suavizada, obtida a partir da distribuição dos pontos do envelope de cada assovio. A aplicação de uma suavização gaussiana mostrou-se importante para reduzir irregularidades locais do traçado, resultando em curvas mais estáveis e representativas da tendência geral do assovio; exemplos dessas curvas suavizadas podem ser vistos na Figura 13. 

A partir dessas curvas suavizadas, cada vocalização foi ajustada por um polinômio de Chebyshev de grau 9, gerando 10 coeficientes que sintetizam sua forma temporal e constituem a base do conjunto de atributos (Figura 14). Para ilustrar essa representação compacta, a Tabela 1 apresenta os coeficientes obtidos para os seis exemplos exibidos na Figura 14, correspondentes às classes manuais A, AD, C, D, DA e M. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/b51f03f31c25bc110c2be96cdf3931ad693d144a0581a0bf7bbb8ad02482dc48.jpg)



Figura 13 – Exemplos reais $+$ curva suavizada.



Fonte: Elaborado pelo autor (2025).



Tabela 1 – Coeficientes do polinômio de Chebyshev de grau 9 para os seis exemplos ilustrados na Figura 14.


<table><tr><td>Classe</td><td>c0</td><td>c1</td><td>c2</td><td>c3</td><td>c4</td><td>c5</td><td>c6</td><td>c7</td><td>c8</td><td>c9</td></tr><tr><td>A</td><td>16,791</td><td>1,295</td><td>-0,058</td><td>0,043</td><td>0,060</td><td>-0,046</td><td>-0,006</td><td>-0,016</td><td>-0,030</td><td>0,026</td></tr><tr><td>AD</td><td>15,539</td><td>0,503</td><td>0,150</td><td>0,111</td><td>-0,011</td><td>0,006</td><td>-0,005</td><td>-0,001</td><td>0,018</td><td>-0,008</td></tr><tr><td>C</td><td>17,899</td><td>0,014</td><td>-0,010</td><td>0,031</td><td>0,013</td><td>0,008</td><td>-0,005</td><td>-0,003</td><td>0,004</td><td>-0,004</td></tr><tr><td>D</td><td>17,918</td><td>-0,590</td><td>-0,280</td><td>-0,044</td><td>0,040</td><td>0,027</td><td>-0,020</td><td>-0,005</td><td>0,005</td><td>-0,001</td></tr><tr><td>DA</td><td>16,009</td><td>-0,694</td><td>-0,058</td><td>0,123</td><td>-0,048</td><td>0,023</td><td>0,012</td><td>-0,018</td><td>0,001</td><td>0,002</td></tr><tr><td>M</td><td>13,879</td><td>-0,332</td><td>-0,314</td><td>0,727</td><td>0,347</td><td>0,087</td><td>-0,124</td><td>-0,008</td><td>0,044</td><td>-0,019</td></tr></table>


Fonte: Elaborado pelo autor (2025). 


Além desses descritores paramétricos, foram extraídas parâmetros acústicos diretas a partir dos valores reais dos contornos, incluindo duração, frequência mínima, frequência máxima e largura de banda. O dataset também incorporou o erro do ajuste polinomial, o nome do arquivo correspondente e o rótulo manual atribuído ao assovio, pertencente a um dos seis tipos descritos no referencial teórico. Esse conjunto de atributos serviu como representação final de cada assovio para as etapas subsequentes de redução de dimensionalidade e agrupamento; um diagrama ilustrando esse processo pode ser visto na Figura 15. 

Apesar da boa qualidade geral dos contornos suavizados e dos ajustes polinomiais, observou-se que ambos os processos apresentaram instabilidades localizadas no segmento final de alguns assovios. Esse comportamento ocorreu principalmente em vocalizações cujo trecho final apresenta variação tonal reduzida, aproximando-se de uma região quase constante do contorno, como é possível ver no contorno C da figura 14. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/6e1b4f4943f3a0e250b1831d5fca5bed855421ac168511ea0d9d8e8ba4928025.jpg)



Figura 14 – Exemplos reais + polinômio ajustado.



Fonte: Autor (2025)


No caso da suavização gaussiana, a baixa variabilidade nos instantes finais faz com que pequenas oscilações residuais sejam levemente amplificadas pelo filtro. Como consequência, a curva apresenta um encurvamento artificial ou pequenas flutuações que não refletem a trajetória real do assovio. 

De forma semelhante, o ajuste por polinômios de Chebyshev de grau 9 mostrouse mais suscetível a oscilações espúrias nas extremidades. Como esse modelo é global, pequenas irregularidades próximas às bordas do domínio afetam de maneira desproporcional os coeficientes, especialmente quando o trecho final da vocalização é quase plano. Esse efeito é conhecido na literatura como instabilidade de borda (ANDRIOLO et al., 2018; RODRIGUES, 2022), sendo mais evidente em assovios curtos ou com uma inclinação final muito sutil. 

Essas instabilidades, embora restritas ao final da curva e sem impacto significativo, na maioria dos casos, sobre a forma global do assovio, indicam a necessidade de cautela na interpretação das extremidades e sugerem possíveis aprimoramentos futuros, como ajustes ponderados, suavização adaptativa ou o uso de modelos locais baseados em polinômios por partes. 

# 4.2 Redução de Dimensionalidade

A projeção dos assovios em um espaço de menor dimensão teve como objetivo facilitar a visualização da variabilidade tonal e avaliar se o conjunto de atributos derivados dos contornos suavizados e dos coeficientes polinomiais continha estrutura suficiente para separar diferentes padrões acústicos. Inicialmente, três métodos foram testados: PCA, 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/7b212d90cbb903d8e5614018b68fc8427add9a3ca33d4016d2de4b108f7a28e8.jpg)



Figura 15 – Fluxograma ilustrativo do processo de criação e estruturação do dataset de assovios bioacústicos.



Fonte: Elaborado pelo autor (2025).


t-SNE e UMAP, cada um representando abordagens distintas de preservação da geometria dos dados. 

A PCA, por ser uma técnica linear, produziu projeções em que grande parte dos assovios permaneceu sobreposta. Essa forte sobreposição indica que a variabilidade dos contornos não é bem explicada por combinações lineares, o que limita a capacidade da PCA de revelar grupos estruturados no espaço acústico. 

O t-SNE, por outro lado, apresentou separações locais mais evidentes, conseguindo isolar subconjuntos de assovios com curvas tonalmente semelhantes. Contudo, a técnica mostrou fragilidade na preservação da estrutura global, fragmentando o espaço em múltiplas ilhas pouco relacionadas entre si e exibindo forte sensibilidade aos hiperparâmetros. Alterações moderadas em perplexity e learning rate resultaram em mapas substancialmente diferentes, o que dificultou a interpretação dos padrões de similaridade entre os assovios. 

Entre as técnicas avaliadas, o UMAP apresentou o melhor desempenho, tanto na organização global quanto na coerência local das projeções. A representação obtida preservou relações de vizinhança relevantes, agrupando assovios com contornos semelhantes de forma contínua e revelando regiões de maior e menor densidade. A estrutura emergente mostrou transições suaves entre diferentes formas tonais e evidenciou padrões consistentes com tendências acústicas descritas na literatura. Por essa razão, o UMAP foi selecionado como método principal para a etapa de redução de dimensionalidade e serviu como base para o agrupamento posterior com HDBSCAN. 

Antes da análise visual das projeções, cada assovio foi representado como um ponto no espaço reduzido e as cores atribuídas aos pontos correspondem às classes manuais 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/fe01736181c620df853d1cee899c55d9fdb2a2a08929ca013a551d44f1d9e29b.jpg)



Figura 16 – Resultado do processo de redução de dimensionalidade com o PCA.



Fonte: Elaborado pelo autor (2025).


rotuladas previamente. Essas classes refletem tendências gerais da trajetória tonal e foram codificadas da seguinte forma: 

• A — Ascendente 

• D — Descendente 

• C — Constante 

• M — Múltiplo 

• DA — Convexo 

• AD — Côncavo 

Essa coloração permitiu avaliar rapidamente se as técnicas de redução de dimensionalidade mantiveram alguma separabilidade entre os diferentes perfis acústicos. 

Para fins comparativos, as figuras 16 e 17 apresentam as projeções obtidas com PCA e t-SNE, respectivamente. Já a projeção obtida pelo UMAP (Figura 18) evidenciou uma estrutura mais coerente e contínua, justificando sua escolha como método principal para as etapas subsequentes de clustering. 

# 4.3 Agrupamento com HDBSCAN

Com a representação dos assovios no espaço reduzido pelo UMAP, foi aplicada a técnica de agrupamento HDBSCAN, escolhida por sua capacidade de identificar grupos de diferentes densidades e por lidar naturalmente com regiões de transição e outliers. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/d2d6011631db6179e492f1567cd753746b2ba3e2c70d94ae90489c973e783025.jpg)



Figura 17 – Resultado do processo de redução de dimensionalidade com o t-SNE.



Fonte: Autor (2025)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/4ab46673be4639e9a7dcc891a9a287ade647a489fe0b41de1badb06de5de4734.jpg)



Figura 18 – Resultado do processo de redução de dimensionalidade com o UMAP.



Fonte: Autor (2025)


A Figura 19 apresenta o resultado do agrupamento no espaço bidimensional do UMAP, considerando todos os pontos do dataset. Cada cor representa um cluster distinto identificado pelo algoritmo, enquanto o rótulo $- 1$ (tom mais escuro de azul) corresponde aos pontos classificados como ruído, ou seja, assovios cuja distribuição local não foi suficientemente densa para formar um grupo estável. Observa-se que o HDBSCAN identificou regiões bem definidas no espaço reduzido, separando agrupamentos mais densos e revelando tramas estruturais coerentes com padrões tonais semelhantes. 

Entretanto, a presença dos pontos rotulados como ruído afeta visualmente a organização global e pode dificultar a interpretação das regiões de maior consistência. Por essa razão, a Figura 20 mostra a mesma projeção após a remoção dos pontos com rótulo –1. Nesse caso, os clusters tornam-se mais evidentes, revelando limites mais claros e uma 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/adf2959ac7dd035af4bb6ad9db9db3ef977320afe36b8a4a86bc6739306efd40.jpg)



Figura 19 – Resultado do processo de agrupamento com HDBSCAN e com dimensão reduzida por UMAP.



Fonte: Elaborado pelo autor (2025).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/79f2d387c4326eaeb5a739b1ff9f619766ae3ef83bfccd71cfcc860bd7246c79.jpg)



Figura 20 – Resultado do processo de agrupamento com HDBSCAN e com dimensão reduzida por UMAP, sem o cluster de ruído.



Fonte: Elaborado pelo autor (2025).


estrutura interna mais homogênea. Essa visualização facilitou a análise das características acústicas predominantes em cada agrupamento e serviu de base para a etapa seguinte, dedicada à caracterização dos clusters. 

Em ambos os cenários, o HDBSCAN mostrou-se adequado ao tipo de dado analisado, identificando tanto grupos bem estruturados quanto regiões de transição entre diferentes padrões de contorno. O percentual de assovios rotulados como ruído (23,04%) é compatível com a expectativa de que uma parcela das vocalizações não apresenta forma tonal suficientemente regular para compor agrupamentos densos, seja por variação natural do comportamento acústico ou por características marginais do sinal. 

Além disso, parte dessa proporção pode ser atribuída às limitações inerentes ao 

processo de anotação manual. Em alguns casos, a visualização do assovio é dificultada pela presença de ruído de fundo, sobreposição com outras vocalizações ou baixa intensidade do sinal, o que pode levar a contornos imprecisos ou incompletos. Há também situações em que a vocalização não pôde ser registrada integralmente na gravação, resultando em traçados parciais que não refletem a trajetória tonal completa. Esses fatores contribuem para a dispersão de pontos no espaço reduzido e aumentam a probabilidade de tais assovios serem classificados como ruído pelo algoritmo. 

Dessa forma, o HDBSCAN não apenas agrupou de maneira eficaz os assovios com padrões consistentes, mas também destacou vocalizações atípicas, incompletas ou de difícil interpretação, separando-as do conjunto principal. Isso reforça a utilidade do método para lidar com a heterogeneidade intrínseca ao registro de sinais bioacústicos e com as variações introduzidas durante o processo de anotação. 

# 4.4 Caracterização dos Clusters

O processo de agrupamento resultou em 22 clusters principais (excluindo o ruído), com tamanhos variando de 20 a 185 assovios. De maneira geral, observou-se que os clusters mais numerosos apresentaram maior compactação no espaço UMAP, indicando forte consistência tonal e menor variabilidade intra-cluster. Em contraste, agrupamentos menores tenderam a formar estruturas mais alongadas ou dispersas, sugerindo maior diversidade de formas de contorno e variações mais sutis entre os assovios individuais. 

Como exemplo, o cluster 17 apresenta 48 assovios com duração média de $0 , 7 7 \pm 0 , 1 6$ segundos, e frequências variando entre 15, 90±0.36 kHz e 17, 87±0, 43 kHz, caracterizandose principalmente por perfis ascendentes. Já o cluster 5, com 35 assovios, possui duração média de $0 , 5 6 \pm 0 , 2 2$ segundos e frequências situadas entre 15, 25±1, 59 kHz e 18, 11±1, 35 kHz, predominando curvas côncavas (ver Figura 21). Esses dois clusters ilustram bem como diferentes padrões de curvatura se separam naturalmente no espaço de características. 

A análise das curvas médias reforça essas distinções. Alguns clusters exibiram perfis claramente ascendentes ou descendentes, com pequena variabilidade em torno da curva central, sugerindo vocalizações com estrutura estável e bem definida. Outros grupos apresentaram contornos convexos, côncavos ou com múltiplas inflexões, frequentemente associados a modulações mais complexas, resultando em maior dispersão dentro do cluster. 

Entre as classes manuais, os assovios do tipo constante mostraram-se os mais desafiadores de representar de forma estável, apresentando grande variação entre indivíduos — possivelmente acentuada pelo fenômeno de Runge. Esse comportamento contribuiu para a maior dispersão observada nos clusters associados a essa classe. 

A Tabela 2 apresenta a distribuição dos rótulos manuais dentro de cada cluster. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/e77de99401c582f74e495f88c888a32c08f7f505306246799b6c5479dbb0b317.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/bb18751341cfc146ac6a291242695a043148c2afacba167febaa78f9f02f5cbb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/6c27367da9764274be5e74f5db4a11b8d710ab5cfe1244484f546fe795131bf8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/bfb6f76ade55b5f552db95b3c2d6b2262028ea571e28918ab0d6527797f16bec.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/fe951b6b6ff375f8dae263bd732e3e0e460aac654c89b7226f597da6b469906d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/73d267411b6b6e62892813a5a98977f33a84b9039498f4677483c28da0688a65.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/c96d3fe0a9b7ca6d44dd82f5ceedaee880fc3e290a8b926a67045ec53e3fbde5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/3ad04df4a88f42a583a57dee1acb4c55fdb4fd14dbbfb52efc9c0a055e967372.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/b4d8fd5407887747140f57e6a549c7b1110f828f9a56f9346c97aab632dd6eb6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/9c190e5c76f75a07f70494d8c455e5cc8bd853a5c8d0e655aacf380d0dd5d632.jpg)



Figura 21 – Comparação de 5 curvas dos clusters 17 e 5.



Fonte: Elaborado pelo autor (2025).


Observa-se que alguns agrupamentos exibem forte predominância de uma única classe — como os clusters 17, 18 e 19, quase exclusivamente ascendentes — indicando que o modelo capturou padrões tonais coerentes com a categorização humana. Em contrapartida, vários clusters mistos surgiram, especialmente entre formas ascendentes longas, contornos convexos e côncavos. Esses casos sugerem zonas de transição em que diferentes classes compartilham características intermediárias, refletindo a continuidade natural das vocalizações. 


Tabela 2 – Distribuição das classes manuais em cada grupo identificado pelo HDBSCAN, com total de assovios e porcentagem relativa.


<table><tr><td>Cluster</td><td>A</td><td>AD</td><td>C</td><td>D</td><td>DA</td><td>M</td><td>Total</td><td>%</td></tr><tr><td>-1</td><td>178</td><td>46</td><td>37</td><td>23</td><td>54</td><td>9</td><td>347</td><td>23,04</td></tr><tr><td>0</td><td>2</td><td>39</td><td>0</td><td>94</td><td>6</td><td>17</td><td>158</td><td>10,49</td></tr><tr><td>1</td><td>0</td><td>3</td><td>0</td><td>18</td><td>1</td><td>1</td><td>23</td><td>1,53</td></tr><tr><td>2</td><td>13</td><td>3</td><td>15</td><td>12</td><td>4</td><td>0</td><td>47</td><td>3,12</td></tr><tr><td>3</td><td>36</td><td>0</td><td>1</td><td>0</td><td>17</td><td>6</td><td>60</td><td>3,98</td></tr><tr><td>4</td><td>56</td><td>1</td><td>8</td><td>1</td><td>16</td><td>1</td><td>83</td><td>5,51</td></tr><tr><td>5</td><td>0</td><td>30</td><td>1</td><td>2</td><td>0</td><td>2</td><td>35</td><td>2,32</td></tr><tr><td>6</td><td>38</td><td>3</td><td>0</td><td>0</td><td>2</td><td>1</td><td>44</td><td>2,92</td></tr><tr><td>7</td><td>8</td><td>0</td><td>13</td><td>0</td><td>14</td><td>1</td><td>36</td><td>2,39</td></tr><tr><td>8</td><td>2</td><td>0</td><td>18</td><td>0</td><td>0</td><td>0</td><td>20</td><td>1,33</td></tr><tr><td>9</td><td>18</td><td>3</td><td>44</td><td>7</td><td>6</td><td>0</td><td>78</td><td>5,18</td></tr><tr><td>10</td><td>32</td><td>2</td><td>0</td><td>0</td><td>3</td><td>0</td><td>37</td><td>2,46</td></tr><tr><td>11</td><td>20</td><td>6</td><td>1</td><td>0</td><td>1</td><td>0</td><td>28</td><td>1,86</td></tr><tr><td>12</td><td>14</td><td>1</td><td>2</td><td>2</td><td>1</td><td>0</td><td>20</td><td>1,33</td></tr><tr><td>13</td><td>21</td><td>0</td><td>4</td><td>0</td><td>1</td><td>0</td><td>26</td><td>1,72</td></tr><tr><td>14</td><td>1</td><td>0</td><td>22</td><td>0</td><td>1</td><td>0</td><td>24</td><td>1,59</td></tr><tr><td>15</td><td>69</td><td>4</td><td>91</td><td>17</td><td>3</td><td>1</td><td>185</td><td>12,28</td></tr><tr><td>16</td><td>19</td><td>22</td><td>5</td><td>15</td><td>2</td><td>2</td><td>65</td><td>4,32</td></tr><tr><td>17</td><td>48</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>48</td><td>3,19</td></tr><tr><td>18</td><td>53</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>53</td><td>3,52</td></tr><tr><td>19</td><td>27</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>28</td><td>1,86</td></tr><tr><td>20</td><td>31</td><td>0</td><td>0</td><td>0</td><td>6</td><td>0</td><td>37</td><td>2,46</td></tr><tr><td>21</td><td>23</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>24</td><td>1,59</td></tr></table>


Fonte: Elaborado pelo autor (2025). 


As curvas médias reconstruídas para cada cluster revelam padrões tonais distintos e coerentes com a organização observada no espaço reduzido. Clusters mais populosos, como 0, 9, 15 e 16, exibem contornos suaves, com envelopes estreitos e baixa variabilidade intra-cluster, indicando vocalizações estruturalmente estáveis e bem definidas. Diversos clusters apresentam perfis predominantemente ascendentes (6, 10, 13, 17, 18, 19, 20, 21), caracterizados por elevação contínua da frequência ao longo do tempo, sugerindo classes tonais consistentes e facilmente separáveis pelo HDBSCAN. Outros grupos mostram curvaturas específicas: o cluster 5 apresenta um perfil convexo (subida inicial seguida de queda suave), enquanto os clusters 0 e 1 exibem formas descendentes mais sutis. Há também clusters com comportamento mais heterogêneo, como 2, 7 e 8, cujas curvas médias apresentam leve modulação, refletindo maior diversidade interna ou transições entre padrões tonais. Esses resultados evidenciam que o processo de redução de dimensionalidade e agrupamento capturou adequadamente as características essenciais dos contornos dos assovios, separando grupos com estrutura tonal clara e identificando zonas de maior 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/5fb1ea4e92de4e0121cd4d27c37d03c89413d7782979e9aac34880b7bf7809f9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/2e8d5ceb4ce3fece46b1017c1a7099745deffc9abed4c392102bc284cbed0722.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/94b283b0f961c01680cf12c284dbc63aaf1778949e33bea3c7d438be37063111.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/cee8429922bfda32f7504c31fd93bb015940ba44236526bd6c8918ba877f637c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/66034e3887619d3f15784527014e1df3658aba116027a2592c053c55e5031c64.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/abdb178be9146a2ecc79a5518e324345cb5235a0ad556cfb2c76e3719994d753.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/ba649e870a0306c6f77c78d41cc450a930c772e61e5fc62456a6d9db85113420.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/4146c79b1a651bcf16acc18dfc25b997862bd381b756055da20bfa725e6bb111.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/4240038edcfcad79d7336f367f03f1745e3b547a3003942d1385f0c7c2f0f5fb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/2483d82c5fb321a23ac688bbec9c4fe707f4bd82f49c973afa8c8b62e213a733.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/6012915537312d749f6da3ef287d01410a27e0d4751459f4ef18e1966e668f4d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/3ca5a733db31c7b0f4171d5e8a8469f22a15c214331def544a9fbe405ddc0e79.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/bc8ffc148e280057770d51163e7d2866879864f4d43928897196b76ddcc9ec40.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/98470912271c336c01260cba8bd4288cc3c194f6a10fa78854f65c67f34252a6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/ce8e6e6997373791a5d864599b8405ee13a264a34022de6080a1656c6a1fd5ca.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/87ae366361085a793b55b3f3cbce9352d53092b4fdf693c384ffb70404d30663.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/d34378f2eaff023c080d90ddcdf129aeffecc6ca28ff93da98f19a96fa9b3abc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/96c665918d823df64f61537d04ba01310fe3c5d78795cbdc760ba099101181b9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/6a606875819fccb7899d66372d40c225d6e0c53e7cf83434d0d9a4ff10ff18c1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/79c5c34356b17caf359aa7aad4112b75d1067f55a0525265ca1c927c16478df6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/2449ec1b8df66a228629d1fef35162142e6afd270647f9737d58516a45f44d63.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/dd949ae172bc74dfaf0836bf7579131fd69ed4ad8ec88b90307c898a4af47128.jpg)



Figura 22 – Curvas médias e desvios padrão dos contornos de assovios agrupados pelo HDBSCAN, reconstruídos via polinômios de Chebyshev em domínio temporal real.


Fonte: Elaborado pelo autor (2025). 

variação onde diferentes tipos de modulação tendem a se sobrepor. É possível ver a curva média de todos os grupos na Figura 22. 

No conjunto, os resultados mostram que o espaço reduzido pelo UMAP preservou relações tonais relevantes: clusters bem definidos emergiram para padrões estáveis, enquanto grupos mais heterogêneos foram associados a modulações complexas e perfis intermediários. Essa organização sugere que os assovios de golfinhos apresentam gradientes estruturais contínuos, nos quais classes manuais tradicionais se aproximam ou se sobrepõem, e que técnicas de agrupamento podem revelar tanto categorias discretas quanto transições entre elas. 

Para ilustrar visualmente as características acústicas associadas a cada agrupamento, foram selecionados exemplos representativos de espectrogramas para todos os 22 clusters identificados pelo HDBSCAN. A escolha desses exemplos foi realizada de forma objetiva: para cada cluster, os assovios mais próximos da curva média reconstruída foram considerados candidatos ideais. A partir desses, foram escolhidos manualmente um dentre três assovios com melhor qualidade visual no espectrograma, de modo a evitar casos com sobreposição de sinais, ruído impulsivo ou baixa relação sinal-ruído. Assim, os exemplos apresentados refletem fielmente o padrão tonal predominante em cada cluster, mantendo, ao mesmo tempo, boa legibilidade visual para interpretação. 

As imagens agrupadas (ver Figura 23) apresentam espectrogramas reais dos assovios utilizados no processo de agrupamento, permitindo uma comparação direta entre os contornos polinomiais reconstruídos e sua manifestação no domínio tempo-frequência. Esses exemplos evidenciam a diversidade estrutural dos assovios analisados, incluindo padrões claramente ascendentes, descendentes, convexos, côncavos e com modulações mais sutis. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-23/ba84e744-2e08-4456-b1b2-183be322a395/838ef3a52fcdcfad2f5b060d740ebf13a9db09cd1a0ed2b00f984d5d6c2e99b1.jpg)



Figura 23 – Exemplos de espectrogramas representativos dos 22 clusters identificados pelo HDBSCAN.


Fonte: Elaborado pelo autor (2025). 

# 5 CONCLUSÃO E TRABALHOS FUTUROS

Este trabalho apresentou um pipeline completo para a caracterização automática de assovios de golfinhos, integrando etapas de pré-processamento, extração de atributos, redução de dimensionalidade e agrupamento não supervisionado. A partir das máscaras tempo–frequência e dos contornos suavizados, foi possível construir uma representação robusta para cada vocalização, baseada tanto em atributos acústicos diretos quanto nos coeficientes de um polinômio de Chebyshev de grau fixo, capaz de sintetizar a forma tonal de cada assovio de maneira compacta e comparável. 

Os resultados demonstram que o conjunto de atributos gerado preserva informações relevantes da estrutura temporal e espectral das vocalizações, permitindo que técnicas de redução de dimensionalidade revelem padrões acústicos coerentes. Entre os métodos avaliados, o UMAP apresentou desempenho superior, proporcionando uma organização mais estável e interpretável do espaço de assovios e preservando tanto relações locais quanto globais. Essa representação reduziu a sobreposição entre curvas tonais distintas e evidenciou gradientes de variação contínua, características importantes em comportamentos acústicos naturais. 

Na etapa de agrupamento, o HDBSCAN mostrou-se especialmente adequado ao tipo de dado analisado. O algoritmo identificou 22 clusters principais, além de um conjunto substancial de assovios classificados como ruído, o que é compatível com a variabilidade natural das gravações e com limitações inerentes ao processo de anotação manual. Os clusters exibiram padrões tonais distintos e coerentes: alguns apresentaram forte homogeneidade interna, com perfis claramente ascendentes, descendentes ou convexos, enquanto outros refletiram maior diversidade tonal ou transições entre diferentes formas de modulação. As curvas médias reconstruídas e os espectrogramas representativos confirmaram visualmente essas tendências, reforçando a validade da abordagem utilizada para distinguir grupos de vocalizações a partir de suas propriedades tonais. 

Apesar dos resultados promissores, algumas limitações emergem da análise do conjunto final. Uma delas refere-se ao grau de correspondência entre os clusters obtidos e as classes manuais atribuídas previamente. Embora alguns agrupamentos apresentem predomínio claro de um único tipo de assovio, outros se mostraram mais heterogêneos, especialmente entre contornos convexos, côncavos ou ascendentes longos. Essa heterogeneidade sugere que, embora os atributos utilizados capturem aspectos estruturais relevantes, ainda há espaço para aprimorar a capacidade discriminativa do pipeline, possivelmente com a ampliação do dataset, com o uso de representações híbridas que combinem contornos e propriedades espectrais de maior resolução, ou por meio de abordagens multiescalares. 

Além disso, instabilidades observadas nos trechos finais dos contornos suavizados e dos ajustes polinomiais demonstram a necessidade de modelos mais robustos a variações locais e ao comportamento quase plano de algumas vocalizações. 

Como perspectivas futuras, três caminhos principais se destacam. O primeiro referese à incorporação de um módulo automático de detecção de assovios, capaz de identificar vocalizações diretamente no espectrograma completo, eliminando a necessidade de um detector externo e tornando o pipeline inteiramente autônomo. Detectores modernos baseados em redes neurais convolucionais ou arquiteturas híbridas CNN–Transformer poderiam substituir a etapa manual ou semiautomática de seleção dos trechos contendo assovios (LI et al., 2023), aumentando a escalabilidade do processo. 

O segundo avanço promissor diz respeito à substituição do processo de marcações manuais por um modelo de segmentação automática de espectrogramas. Abordagens como U-Net, DeepLab ou métodos baseados em Vision Transformers podem ser treinadas para segmentar automaticamente regiões contendo assovios, extraindo máscaras tempo–frequência com maior consistência e reduzindo substancialmente o esforço humano na anotação (CHOI et al., 2025; NIZAMANI et al., 2023; CHEN et al., 2024). 

Por fim, destaca-se o potencial de métodos baseados em análise de tendências, como a Qualitative Trend Analysis (QTA), que utiliza derivadas sucessivas para caracterizar mudanças de concavidade, inflexões e padrões de modulação (JANUSZ; VENKATA-SUBRAMANIAN, 1991). Essa abordagem pode ser integrada ao pipeline para rotular automaticamente os assovios segundo categorias tonais (A, D, C, M, DA, AD), substituindo ou complementando a classificação manual. Em conjunto com os agrupamentos obtidos, algoritmos baseados em QTA podem oferecer uma taxonomia automatizada mais robusta, ancorada em propriedades matemáticas da forma tonal (ANDRIOLO et al., 2018; JANUSZ; VENKATASUBRAMANIAN, 1991). 

De forma geral, o pipeline desenvolvido demonstrou ser eficaz para a organização e análise estrutural de assovios de golfinhos, oferecendo uma base consistente para estudos posteriores em bioacústica, reconhecimento automático de vocalizações e análise de comportamento acústico. Os resultados obtidos corroboram tendências conhecidas da literatura e mostram que técnicas modernas de aprendizado de máquina podem revelar padrões sutis, além de fornecer uma perspectiva quantitativa e escalável para o estudo de vocalizações cetáceas. Os aprimoramentos propostos, aliados à expansão do dataset e à integração de modelos mais avançados, têm potencial para tornar o sistema inteiramente automatizado, mais robusto e aplicável a cenários de grande volume de dados, como monitoramento acústico passivo em larga escala. 

# REFERÊNCIAS



ANDRIOLO, A. et al. Marine mammal bioacustics using towed array systems in the western south atlantic ocean. In: . Advances in Marine Vertebrate Research in Latin America: Technological Innovation and Conservation. Cham: Springer International Publishing, 2018. p. 113–147. ISBN 978-3-319-56985-7. Disponível em: <https://doi.org-/10.1007/978-3-319-56985-7 5>https://doi.org/10.1007/978-3-319-56985-7_5. 





ATKINSON, K. E. An Introduction to Numerical Analysis. 2nd. ed. New York: John Wiley & Sons, 1989. ISBN 0-471-50023-2. 





BAZúA-DURáN, C. Differences in the whistle characteristics and repertoire of bottlenose and spinner dolphins. Anais da Academia Brasileira de Ciências, Academia Brasileira de Ciências, v. 76, n. 2, p. 386–392, Jun 2004. ISSN 0001-3765. Disponível em: <https://doi.org/10.1590/S0001-37652004000200030>https://doi.org/10.1590/S0001- 37652004000200030. 





BELKIN, M.; NIYOGI, P. Laplacian eigenmaps and spectral techniques for embedding and clustering. In: Advances in Neural Information Processing Systems (NIPS). [S.l.: s.n.], 2001. p. 585–591. 





BIOACOUSTICS, U. F. d. R. G. d. N. LaB – Laboratory of. LaB – Laboratory of Bioacoustics. 2025. Acesso em: 28 nov. 2025. Disponível em: <https://www.lab.bio.br-/>https://www.lab.bio.br/. 





BISHOP, C. M. Pattern Recognition and Machine Learning. New York: Springer, 2006. (Information Science and Statistics). ISBN 978-0387310732. 





BRENNDOERFER, M. HDBSCAN Clustering: Complete Guide to Hierarchical Density-Based Clustering with Automatic Cluster Selection. 2025. Accessed: 2025-11-22. Disponível em: <https://mbrenndoerfer.com/writing/hdbscan-hierarchical-density-basedclustering-automatic-cluster-selection>https://mbrenndoerfer.com/writing/hdbscanhierarchical-density-based-clustering-automatic-cluster-selection. 





BRIGGER, P.; HOEG, J.; UNSER, M. B-spline snakes: a flexible tool for parametric contour detection. IEEE transactions on image processing : a publication of the IEEE Signal Processing Society, v. 9 9, p. 1484–96, 2000. 





CAMARGO, F. P. de. Estudo das vocalizações de golfinhos-rotadores, Stenella longirostris (Cetacea, Delphinidae), no arquipélago de Fernando de Noronha. Tese (Doutorado) — Instituro de Biociências, Universidade de São Paulo, São Paulo, SP, 2008. Disponível em: <https://www.teses.usp.br/teses/disponiveis/41/41133/tde-17062008-093152/publico-/fernanda camargo.pdf>https://www.teses.usp.br/teses/disponiveis/41/41133/tde-17062008-093152/publico/fernanda_camargo.pdf. 





CHEN, J. et al. Transunet: Rethinking the u-net architecture design for medical image segmentation through the lens of transformers. Medical image analysis, v. 97, p. 103280, 2024. 





CHOI, J. et al. Model-guided deep learning for line segment detection in time–frequency spectrograms of an ocean waveguide. IEEE Journal of Oceanic Engineering, v. 50, p. 1812–1821, 2025. 





HUANG, H. et al. Towards a comprehensive evaluation of dimension reduction methods for transcriptomic data visualization. Communications Biology, v. 5, 2022. 





JANUSZ, M. E.; VENKATASUBRAMANIAN, V. Automatic generation of qualitative descriptions of process trends for fault detection and diagnosis. Engineering Applications of Artificial Intelligence, Pergamon Press, v. 4, n. 5, p. 329–339, 1991. ISSN 0952-1976. 





JIN, C. et al. Semantic segmentation-based whistle extraction of indo-pacific bottlenose dolphin residing at the coast of jeju island. Ecological Indicators, v. 137, p. 108792, 2022. ISSN 1470-160X. Disponível em: <https://doi.org/10.1016/j.ecolind.2022- .108792>https://doi.org/10.1016/j.ecolind.2022.108792. 





JOLLIFFE, I. T. Principal Component Analysis. 2. ed. New York: Springer, 2002. (Springer Series in Statistics). 





JOVER, I. L. et al. Coupled splines for sparse curve fitting. IEEE Transactions on Image Processing, v. 31, p. 4707–4718, 2022. 





KERSHENBAUM, A.; SAYIGH, L. S.; JANIK, V. M. The encoding of individual identity in dolphin signature whistles: How much information is needed? PLoS ONE, v. 8, n. 10, p. e77671, 2013. Disponível em: <https://journals.plos.org/plosone/article?id=10.1371/journal.pone-.0077671>https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0077671. 





KORKMAZ, B. N. et al. Automated detection of dolphin whistles with convolutional networks and transfer learning. Frontiers in Artificial Intelligence, v. 6, 2022. 





LABRIOLA, M. S. et al. A functional data analysis approach for modelling frequencymodulated tonal sounds in animal communication. Methods in Ecology and Evolution, v. 16, p. 558 – 572, 2025. 





LI, L. et al. Robust unsupervised tursiops aduncus whistle-event detection using gammatone multi-channel savitzky-golay based whistle enhancement. The Journal of the Acoustical Society of America, v. 151 5, p. 3509, 2022. 





LI, P. et al. Using deep learning to track time $\times$ frequency whistle contours of toothed whales without human-annotated training data. The Journal of the Acoustical Society of America, v. 154, n. 1, p. 502–517, 07 2023. ISSN 0001-4966. Disponível em: <https://doi.org/10.1121/10.0020274>https://doi.org/10.1121/10.0020274. 





LI, P. et al. Learning deep models from synthetic data for extracting dolphin whistle contours. 2020 International Joint Conference on Neural Networks (IJCNN), p. 1–10, 2020. 





MCINNES, L.; HEALY, J. Accelerated hierarchical density based clustering. In: 2017 IEEE International Conference on Data Mining Workshops (ICDMW). IEEE, 2017. p. 33–42. Disponível em: <http://dx.doi.org/10.1109/ICDMW.2017- .12>http://dx.doi.org/10.1109/ICDMW.2017.12. 





MCINNES, L. et al. Umap: Uniform manifold approximation and projection. Journal of Open Source Software, v. 3, n. 29, p. 861, 2018. Disponível em: <https://doi.org/10.21105- /joss.00861>https://doi.org/10.21105/joss.00861. 





MELLINGER, D. et al. A method for detecting whistles, moans, and other frequency contour sounds. The Journal of the Acoustical Society of America, v. 129 6, p. 4055–61, 2011. 





MORON, J. R. Caracterização dos parâmetros acústicos do golfinho-rotador: registro na quebra da plataforma continental sul brasileira. Dissertação (Mestrado) — Universidade Federal de Juiz de Fora, Juiz de Fora, MG, 2015. Disponível em: <https://repositorio.ufjf.br/jspui/bitstream/ufjf/129/1/julianarodriguesmoron-.pdf>https://repositorio.ufjf.br/jspui/bitstream/ufjf/129/1/julianarodriguesmoron.pdf. 





NIZAMANI, A. H. et al. Advance brain tumor segmentation using feature fusion methods with deep u-net model with cnn for mri data. J. King Saud Univ. Comput. Inf. Sci., v. 35, p. 101793, 2023. 





REEVES, R. R. et al. Guide to Marine Mammals of the World. New York: Alfred A. Knopf, 2002. 528 p. (National Audubon Society Field Guides). ISBN 978-0375411410. 





RIVLIN, T. J. Chebyshev Polynomials: From Approximation Theory to Algebra and Number Theory. 2nd. ed. New York: John Wiley Sons, 1990. ISBN 0471628964. 





ROCH, M. et al. Automated extraction of odontocete whistle contours. The Journal of the Acoustical Society of America, v. 130 4, p. 2212–23, 2011. 





RODRIGUES, B. C. S. Monografia, Aproximação de funções e o fenômeno de Runge. 2022. Disponível em: <https://repositorio.ufsc.br/bitstream-/handle/123456789/244206/TCC Beatriz Carolina%20Souza%20Rodrigues-.pdf?sequence=1>https://repositorio.ufsc.br/bitstream/handle/123456789/244206/TCC Beatriz 





RODRIGUES, G. M. Monografia, COMPORTAMENTO ACÚSTICO DE Sotalia guianensis (VAN BÉNÉDEN, 1864) (Cetacea: Delphinidae) NO ENTORNO DE UNIDADES DE CONSERVAÇÃO, LITORAL DO PARANÁ, SUL DO BRASIL. 2014. Disponível em: <https://acervodigital.ufpr.br-/xmlui/bitstream/handle/1884/95392/RODRIGUES%2C%20Gabrieli%20Messias-.pdf?sequence=1&isAllowed=y>https://acervodigital.ufpr.br/xmlui/bitstream/handle/1884/95392/R 





SANCHEZ-GENDRIZ, I. Signal processing basics applied to ecoacoustics. Ecological Informatics, v. 66, p. 101445, 2021. Disponível em: <https://doi.org/10.1016/j.ecoinf-.2021.101445>https://doi.org/10.1016/j.ecoinf.2021.101445. 





SERRA, O. M.; MARTINS, F.; PADOVESE, L. Active contour-based detection of estuarine dolphin whistles in spectrogram images. Ecol. Informatics, v. 55, 2020. 





SIDDAGANGAIAH, S. et al. Automatic detection of dolphin whistles and clicks based on entropy approach. Ecological Indicators, v. 117, p. 106559, 2020. 





TENENBAUM, J. B.; SILVA, V. de; LANGFORD, J. C. A global geometric framework for nonlinear dimensionality reduction. Science, American Association for the Advancement of Science, v. 290, n. 5500, p. 2319–2323, 2000. 





VOLOSHKINA, O.; KOVALOVA, A.; SIPAKOV, R. Leveraging quadratic polynomials in python for advanced data analysis. F1000Research, v. 13, 2024. 





WANG, Y. et al. Understanding how dimension reduction tools work: An empirical approach to deciphering t-sne, umap, trimap, and pacmap for data visualization. J. Mach. Learn. Res., v. 22, p. 201:1–201:73, 2020. 

