Pergunta 2
==========

i) *Anexe os resultados do SSL Server test à sua resposta.*
-----------------------------------------------------------

O grupo decidiu escolher os websites relativos aos ministérios da defesa da Alemanha, Reino Unido e Itália, bem como o ministério da economia da Grécia. A estes dizem respeito, respectivamente, as seguintes hiperligações:<br>
- [Ministério da Defesa da Alemanha](https://www.bmvg.de/de)
- [Ministério da Defesa do Reino Unido](https://www.gov.uk/government/organisations/ministry-of-defence)
- [Ministério da Defesa de Itália](https://www.difesa.it/Pagine/default.aspx)
- [Ministério da Ecónomia da Grécia](https://www.yen.gr/)


Os sumários destas mesmas análises podem ser encontrados nas hiperligações seguintes. Note-se que o ministério da defesa do Reino Unido compreende 4 servidores distintos, possivelmente utilizados para efeitos de load balancing, sendo todos este equivalentes, a análise apresentada para este será, deste modo, relativa ao primeiro servidor apresentado.
- [Análise Ministério da Defesa da Alemanha](https://raw.githubusercontent.com/uminho-miei-engseg/1718-G5/master/Aula03/Pergunta2/Minist%C3%A9rio%20Defesa%20Alemanha.png)
- [Análise Ministério da Defesa do Reino Unido](https://raw.githubusercontent.com/uminho-miei-engseg/1718-G5/master/Aula03/Pergunta2/Minist%C3%A9rio%20Defesa%20UK%20-%20Primeiro.png)
- [Análise Ministério da Defesa de Itália](https://raw.githubusercontent.com/uminho-miei-engseg/1718-G5/master/Aula03/Pergunta2/Minist%C3%A9rio%20Defesa%20It%C3%A1lia.png)
- [Análise Ministério da Economia da Grécia](https://raw.githubusercontent.com/uminho-miei-engseg/1718-G5/master/Aula03/Pergunta2/Minist%C3%A9rio%20Economia%20Gr%C3%A9cia.png)
<br><br><br>


ii) *Analise o resultado do SSL Server test relativo ao site escolhido com pior rating. Que comentários pode fazer sobre a sua segurança. Porquê?*
------------------------------------------------------------------------------------------------------------------------------

O site que obteve a pior classificação diz respeito ao [ministério da defesa de Itália](https://www.difesa.it/Pagine/default.aspx), com a classificação de A. Apesar de ser uma boa classificação, esta foi atribuída uma vez que este *website* é vulnerável a um ataque *Return Of Bleichenbacher's Oracle Threat*, conhecido por [ROBOT](https://robotattack.org/). Esta vulnerabilidade permite decifrar cifras *RSA* e efetuar assinaturas, utilizando a chave privada de servidores *TLS*. Compromete, assim, a segurança de um serviço, visto que um atacante poderá simplesmente guardar os registos de várias interações utilizador/servidor, para que mais tarde proceda à sua decifragem. Uma forma de mitigar este problema passará por adotar métodos alternativos de cifragem, nomeadamente cifras que utilizem curvas elípticas.<br>
Apesar de esta vulnerabilidade apresentar alguns riscos, considera-se que será preciso algum conhecimento técnico para que possa ser explorada. Deste modo compreende-se o porquê de a vulnerabilidade *ROBOT* não causar uma queda dramática no *ranking* deste mesmo *website*.
<br><br><br>

iii) *É natural que tenha reparado na seguinte informação: "BEAST attack" na secção de detalhe do protocolo. O que significa, para efeitos práticos??*
----------------------------------------------------------------------------------------------------------------------------------

*BEAST* é uma vulnerabilidade conhecida desde 2011, que utiliza aspetos das cifras por blocos para explorar comunicações que utilizem o protocolo SSL. O nome advém de *Browser Exploit Against SSL/TLS*, e esta vulnerabilidade pode possibilitar um ataque *man-in-the-middle* de forma a que um utilizador mal intencionado consiga obter credenciais de autenticação que não as suas. Refira-se contudo que esta vulnerabilidade afeta apenas servidores que ainda utilizem a versão 1.0 do protocolo TLS, sendo uma das maneiras mais eficazes de resolver este mesmo problema, a atualização para uma nova versão.
