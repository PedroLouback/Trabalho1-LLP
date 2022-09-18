# Trabalho 1 de Laboratorio de Linguagens de Programação

## Instruções
1. Este é um trabalho avaliativo e deve ser entregue em formato relatório.
2. Respostas idênticas serão anuladas.
2. Ao término do prazo final estabelecido para resolução do trabalho, o aluno
deverá apresentar a solução para os colegas e a sua nota terá base na solução
apresentada.

## Etapa 1

a. Entender a aplicação e escolher 2 linguagens com características diferentes e fazer os cálculos de acordo com as instruções.<br>
b. Estudar a especificação das linguagens e avaliar a sua capacidade de resolução da aplicação;<br>
c. Argumentar sobre o critério de escolha de tais linguagens.<br>
d. Avaliar as linguagens de acordo com os critérios de:<br>
&emsp;i. Nível de segurança;<br>
&emsp;ii. Confiabilidade;<br>
&emsp;iii. Paradigma da linguagem;<br>
&emsp;iv. Classe ( Compilada, interpretada ou híbrida);<br>

## Etapa 2

a. Escolhidas as linguagens, ler o arquivo “FECHAMENTO_MAIS_NEGOCIADAS 5minutos” com a base de dados.<br>
b. Tratar os dados e retirar possíveis NAN.<br>
c. Construir n matrizes 12x12 deslizando por todo o arquivo ( a cada passo de tempo).<br>
d. A cada matriz gerada, calcular a sua inversa.<br>
e. Avaliar os seguintes aspectos na resolução deste problema específico:<br>
&emsp;i. Custo de execução de cada linguagem (Pode ser tempo de processamento).<br>
&emsp;ii. Tratamento de erros.<br>
&emsp;iii. Tratamento de exceções.<br>
&emsp;iv. Verificação de erros.<br>
&emsp;v. Verificação de tipo.<br>
&emsp;vi. Confiabilidade.<br>
&emsp;vii. Legibilidade.<br>
&emsp;viii. Facilidade de escrita.<br>
&emsp;ix. Simplicidade<br>

### Resolução Etapa 1:

Para a introdução da primeira etapa foi feita diversas pesquisas para que fosse encontrada uma linguagem em que solucionaria a proposta dada na <a href="#etapa-2">etapa 2</a> com maior simplicidade, com essas pesquisas foi concluido que seria utilizada as linguagens Python e SciLab vendo que tanto Python como Scilab são linguagens para soluções de problemas matematicas e possui uma certa facilidade para manipulação de matrizes e leitura de arquivos, seus critérios são caracterizados da seguinte forma:<br>
**Nível de segurança:** A linguagem Python é bastante conhecida por programadores do mundo inteiro e é a linguagem de programação mais impotante em cibersegurança e a mais usada em ciberataques, mostrando que além da sua facilidade de uso ela se torna ideal para a área de segurança da informação por possuir agilidade para combater ameaças e por possuir uma extensa comunidade onde há um grande compartilhamento de conhecimento entres profissionais, aumentando o nível de segurança dessa linguagem. Já para Scilab não foi encontrado nenhum tipo de depoimento relacionado ao seu nível de segurança, acreditando que seja baixo por ter prioridade em apenas resoluções de problemas envolvendo matematica.<br>
**Confiabilidade:** Por Python ser uma linguagem de programação de alto nível, interpretada, imperativa, orientada a objetos e de tipagem dinâmica são algumas das características afetam a confiabilidade do Python, onde a mesma possui também mecanismos para tratamentos de exceções e apesar da sua tipagem dinâmica ela é fortemente tipada e possui uma facil legibilidade, tornando uma linguagem confiante para manipulação. A linguagem Scilab já consiste em uma linguagem provida de um software e é usada em diversos ambientes industriais necessitando possuir uma confiabilidade maior, sendo uma linguagem fortemente e bastante confiavel por ser comparadas como C, Fortran e C++ que se trata de linguagens confiaveis pela suas características.
**Paradigma da linguagem:** A linguagem Python e Scilab consistem em linguagens multiparadigma, sendo Python uma linguagem orientada a objetos, imperativa e funcional e Scilab uma linguagem de programação estruturada, orientada a objetos e orientada a eventos

### Resolução Etapa 2:

Após serem desenvolvidos códigos para a proposta da <a href="#etapa-2">etapa 2</a> nas linguagens Python e Scilab foi possivel avaliar os seguintes aspectos:<br>
**Custo de execução:** O primeiro código finalizado e que possibilitou a observação desse aspecto foi feita na linguagem Pyton, onde foi possivel observar que o programa obteve um total de 35.944 segundos para ser executado e informar as respostas corresponde ao propósito passado.
**Tratamento de erros:** Em relação ao programa desenvolvido na linguagem Python, inicialmente foi obtida uma grande dificuldade relacionada aos erros de sintaxe pois se trata de uma linguagem bastante diferente de linguagens conhecidas por mim como por exemplo a manipulação de matrizes possui diferençãs em relações a manipulação dos seus arrays que é diferente da linguagem em C mas ao se familiarizar um pouco mais com a linguagem obtendo uma grande facilidade em encontrar instruções de manipulação, foi tranquilo de finalizar o código sem problemas com a sintaxe. Já na implementação do algoritmo usando Scilab foi encontrada uma facilidade por se tratar de uma linguagem que se assemelha com C, uma linguagem que sou familiarizado, permitindo concluir a solução do problema em menos tempo do que foi necessário em Python e onde era encontrado alguma dificuldade, era possível encontrar muitos documentos contendo instruções de diferentes maneira com pouca pesquisa.
**Tratamento de exceções:** Inicialmente em Python foi encontrada uma grande dificuldade em tratamento de execeções, pois através da proposta passada de ler um arquivo .xls que continha dados, foi encontrado um obstáculo onde no mesmo possuia dados em formato de data não permitindo a leitura total em tipo float e nem operações como a inversão da matriz, onde foi possível observar por messagens reportadas ao rodar o código que não era mensagens diretas, dificultando ainda mais a resolução do problema pois abria interpretação para várias coisas onde depois de várias pesquisas foi possível solucionar o problema com apenas duas linhas de código. Em Scilab por possuir um vasto material de instrução não foi encontrado quase nenhum erro de exceção e também pelo programa ter sido feito após o programa em Python foi melhor, pois já foi desenvolvido pensando nos obstaculos enfretados anteriormente onde a plataforma do Scilab também oferece diversas ferramentas que possibilitava a consulta das váriaveis para que fosse possível evitar esses problemas.
**Verificação de erros:** A verificação de erros em Python possui muito detalhamento para pouco erro, onde foi presenciado por mim ao encontrar problemas relacionado a tipos de variaveis e multiplicação de matrizes com esses tipos, onde era possível ver várias linhas reportadas com diversos erros, encontrado dificuldade para a resolução do problema por não demonstrar clareza, mas por Python possuir um vasto material de ajuda na internet, foi possível resolver facilmente esses problemas. Já em Scilab a verificação de erros em quase nula, onde em algumas vezes não era encontrado nenhuma mensagem reportando o erro mas em compensação quando era reportado possuia objetividade e facilidade em encontrar o erro, evitando até pesquisas na literatura para encontrar a solução.
**Confiabilidade:** Na minha opnião, Python por não possuir tipagens em suas variaveis e nenhuma forma de consulta de seus tipos em execução, se tornou um pouco menos confiavel para mim, mas em compensação por se tratar de uma linguagem de fácil escrita, fácil implementação de instruções e tratamento para diversas exceções foi possível recuperar a confiabilidade ao longo do desenvovimento do código. Já em Scilab por possuir uma plataforma com um extenso número de ferramentas e formas de consultas para os tipos de váriaveis e seus valores, se tornou uma linguagem bastante confiavel para mim desde o começo do desenolvimento do programa, tornando a resolução mais fácil e rápida, possuindo faciliadde na implementação da escrita e funções.
**Legibilidade:** Em Python o seu nível de legibilidade é bastante positivo pois todas as suas funções de implementações possui objetividade em seus nomes e também foi visto que ao tentar aprender a linguagem foi encontrado grande facilidade por sua legibilidade, compreendendo bem a identação e sua simplicidade relacionada a recursos para operação. Por Scilab possuir similiaridade com a linguagem C, sua legibilidade para mim se tornou fácil mas creio que para alguém que está aprendendo do zero vai encontrar certas dificuldades pois não possui muito tratamento de erros nem verificação de tipos, sendo necessário recorrer a ferramentas do Scilab para melhor interpretação.

