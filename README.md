Monitor de Desempenho do Sistema
Um aplicativo em Python com interface gráfica que monitora o desempenho do sistema em tempo real, exibindo informações sobre o uso de CPU, memória, disco e rede. O monitor também possui alertas visuais e registra os dados em um arquivo de log para análise posterior.

Funcionalidades
Monitoramento em Tempo Real:

Uso da CPU (%)
Uso da Memória (%)
Uso do Disco (%)
Bytes enviados e recebidos pela rede
Alertas Visuais:

Notificações e mudança de cor na interface gráfica quando os limites de CPU ou memória são ultrapassados.
Exibição de um pop-up com os detalhes do alerta.
Registro de Dados:

Salvamento das informações em um arquivo de log (monitoramento_log.txt) com data e hora.
Tecnologias Utilizadas
Linguagem: Python
Bibliotecas:
psutil: Para coletar métricas de desempenho do sistema.
tkinter: Para a interface gráfica.
datetime: Para registro de data e hora.
