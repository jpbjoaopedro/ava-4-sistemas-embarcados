Semáforo com IHM — Sistemas Embarcados
Projeto da Prática 4 da disciplina Sistemas Embarcados, da Universidade Veiga de Almeida, desenvolvido por João Pedro Bandeira dos Santos.
O sistema utiliza uma Raspberry Pi Pico programada em MicroPython para controlar três LEDs, ler um botão e exibir uma contagem regressiva em um display de sete segmentos.
Simulação no Wokwi
Abrir o projeto e executar a simulação
1. Abra o projeto no Wokwi.
2. Clique em Start the simulation.
3. Observe o LED verde aceso e o display apagado.
4. Pressione o botão verde do circuito.
5. Acompanhe a transição para amarelo, o vermelho com contagem regressiva e o retorno ao verde.
O Wokwi executa a cópia salva no próprio simulador. Alterações neste repositório precisam ser aplicadas também ao projeto Wokwi.
Arquivos
Arquivo	Conteúdo
[main.py](main.py)	Configuração dos GPIOs, padrões dos dígitos e controle do semáforo.
[diagram.json](diagram.json)	Componentes e conexões do circuito no Wokwi.


Componentes
- Raspberry Pi Pico.
- Três LEDs: verde, amarelo e vermelho.
- Botão momentâneo.
- Display de sete segmentos de um dígito, com cátodo comum.
- Dois resistores de 220 Ω e fios de conexão.
Mapeamento dos pinos
Os identificadores GP indicam GPIOs, e não posições físicas na placa.
Elemento	GPIO
LED verde	GP2
LED amarelo	GP3
LED vermelho	GP4
Botão	GP5
Segmento A	GP28
Segmento B	GP27
Segmento C	GP26
Segmento D	GP22
Segmento E	GP21
Segmento F	GP20
Segmento G	GP19


O botão usa Pin.PULL_UP: em repouso, a leitura é 1; quando pressionado, é 0. O display é de cátodo comum e seus segmentos são ativados em nível lógico 1.
Metodologia e organização do código
O [código completo está em main.py](main.py). A implementação utiliza machine.Pin para controlar as entradas e saídas e time.sleep() para as temporizações.
- numeros armazena os padrões dos segmentos A a G para os dígitos de 0 a 9.
- mostrar_numero() aplica o padrão do dígito ao display.
- apagar_display() desliga os sete segmentos.
- semaforo_verde(), semaforo_amarelo() e semaforo_vermelho() definem as cores do sinal.
- piscar_led(), apesar do nome, produz o efeito de piscar no display, usando o valor de contador.
- O laço principal mantém o verde aceso, verifica o botão e executa a sequência quando detecta nível lógico 0.
Funcionamento da versão atual
Etapa	Comportamento
Repouso	Verde aceso e display apagado até o acionamento do botão.
Após o acionamento	O verde permanece aceso por mais 5 segundos.
Atenção	Amarelo aceso por 3 segundos.
Contagem regressiva	Vermelho aceso e display contando de 9 a 1.
Últimos dígitos	Os valores de 4 a 1 piscam, com duas chamadas de piscar_led() por valor.
Reinício	O laço retorna ao verde e apaga o display.


Tempos e relação com o enunciado
O enunciado solicita amarelo por 3 segundos e vermelho por 10 segundos após a solicitação.
Na versão atual, os dígitos de 9 a 5 permanecem por 1 segundo cada. Para cada dígito de 4 a 1, as duas chamadas de piscar_led() somam 1,2 segundo. Portanto, as esperas programadas no vermelho totalizam 9,8 segundos, além do tempo das instruções.
O código também inclui uma espera inicial de 5 segundos e não exibe o zero, pois utiliza range(9, 0, -1). Para adequação aos tempos do enunciado, os ajustes sugeridos são remover essa espera inicial e exibir de 9 a 0 durante dez intervalos de 1 segundo.
A implementação atual não inclui debounce explícito nem espera pela liberação do botão. Se ele continuar pressionado ao final, poderá iniciar outro ciclo. Esses pontos descrevem a versão existente; os ajustes sugeridos ainda precisam ser implementados.
Observação sobre a montagem física
O circuito simulado utiliza resistores nos caminhos comuns dos LEDs e do display. Para uma montagem física, revise a limitação de corrente e utilize resistores dimensionados para cada LED e segmento.
Referências
- Enunciado da Prática 4 — Semáforo com IHM, Universidade Veiga de Almeida.
- MicroPython — machine.Pin
- MicroPython — time
- Wokwi — display de sete segmentos
