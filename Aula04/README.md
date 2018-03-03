## Experiência 1.1
- 1 - Podemos verificar que sem inicializar o serviço _TOR_ o nosso IP reflete a posição atual, real. [Ver imagem](https://raw.githubusercontent.com/uminho-miei-engseg/1718-G5/master/Aula04/Images/Screenshot%20at%202018-02-26%2014-23-08.png)
- 3 - Inicializando o serviço, pode-se verificar que nosso endereço IP mudou. [Ver imagem](https://raw.githubusercontent.com/uminho-miei-engseg/1718-G5/0c598b617fbf5fef87f143590522197bf989c104/Aula04/Images/experiencia_3.PNG)
- 5 - Efetuando a atualização dos nossos dados, o IP muda, novamente. [Ver imagem](https://raw.githubusercontent.com/uminho-miei-engseg/1718-G5/0c598b617fbf5fef87f143590522197bf989c104/Aula04/Images/experiencia_5.PNG)
- 7 - Terminando o processo, tal como esperado o nosso IP volta ao real. [Ver imagem](https://raw.githubusercontent.com/uminho-miei-engseg/1718-G5/master/Aula04/Images/Screenshot%20at%202018-02-26%2014-24-56.png)
<br>
<br>

## Pergunta 1.1

O protocolo TOR escolhe Onion Routers (OR) de modo a garantir a anonimidade ponto-a-ponto (ao nível não aplicacional) de um utilizador na Internet. Tendo em conta que os OR são computadores de outros utilizadores que se disponibilizam a serem utilizados pelo protocolo TOR, a localização de cada OR não depende do protocolo em si. A localização após a utilização do protocolo, depende da localização do OR usado na comunicação.<br>
Tendo em conta estas informações, é possível garantir que está localizado nos EUA, utilizando o protocolo TOR, desde que haja um OR nos EUA, fazendo reload do protocolo, ou pedindo para mudar a sua localização, até que, por acaso, o protocolo escolha um OR, com localização nos EUA. É de salientar que é impossível escolher a localização a cada reload, mas caso o faça até se situar nos EUA, pode garantir que se situa de facto no EUA. No entanto, é preciso ter cuidado que, alguns serviços que usam o protocolo TOR fazem reload da sua localização após alguns minutos ou após alguns pedidos.
<br>
<br>

## Pergunta 1.2

Para responder a esta questão, o grupo acedeu ao primeiro [link](http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page) disponibilizado.<br>
A existência de 6 routers intermédios e de 7 saltos, deve-se à existência dos chamados rendezvous points. Quando um servidor pretende anunciar os seus serviços, este escolhe vários pontos de introdução (Introduction Points), e anuncia-os ao Directory Server. Cada ligação entre o servidor e um ponto de introdução compreende 3 ORs intermediários. Quando um utilizador pretende aceder a um domínio .onion, acederá ao directory server, obtendo informações sobre quais os pontos de introdução do servidor ao qual se pretende conectar. O utilizador escolhe ainda um ponto de rendezvous, novamente com 3 ORs intermediários. Posteriormente notifica o servidor sobre o ponto de rendezvous escolhido, este último constrói um novo caminho até este ponto, com novos ORs. Considera-se que o utilizador escolheu 3 onion routers, bem como o servidor, deste modo ambos comunicam através de uma rede composta pela escolha de ambos, o que prefaz um total de 6 routers intermédios e 7 saltos.<br>
Refira-se ainda que o utilizador apenas tem conhecimento sobre as 3 máquinas adjacentes à sua que servirão para realizar a comunicação entre os intervenientes. O mesmo se verifica no lado do servidor. Assim justifica-se o motivo de apenas ser possível obter informação relativa a 3 servidores intermédios, para saber os outros 3 seria necessário ter acesso à máquina na qual se encontra o servidor. [Esta imagem](https://raw.githubusercontent.com/uminho-miei-engseg/1718-G5/master/Aula04/Images/server.PNG) apresenta os resultados obtidos.<br>
Este processo pode ser verificado mais detalhadamente [aqui](https://www.torproject.org/docs/onion-services.html.en), ou nos [slides da disciplina](https://github.com/uminho-miei-engseg/1718-EngSeg/blob/master/slides/2018.EngSeguranca.04.pdf).
Sendo assim, para realizar uma conexão até ao site Onion, são precisos 6 Onion Rings, que entre si realizam 5 saltos, mais o salto do cliente para o primeiro Onion Ring dele e do primeiro Onion Ring do servidor para o servidor, fazendo assim 7 saltos.
<br>
<br>

## Pergunta 2

O grupo seleccionou o projeto 2, **Gestor de passwords com base em QrCodes**.


