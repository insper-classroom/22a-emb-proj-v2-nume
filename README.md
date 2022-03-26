# Projeto Embarcados

Desenvolvendo um controle remoto.

## Entrega 1

### Integrantes

- Carolina Hirschheimer
- Paulo Kim

### Ideia

O nosso controle será a aplicação de um teclado numérico e um controle de volume como extensão do computador. Com ele, será possível aumentar/abaixar o volume do computador e inputar dígitos de 0 a 9 e botões com diversas outras configurações (enter, backspace, etc.) para os outros pinos do hardware.

### Nome

Nume

### Usuários 

Usuários de computadores.

### Software/Jogo 

Windows.

### Jornada do usuários (3 pts)

### User 1

O usuário 1 trabalha em um restaurante e precisa preencher uma planilha no Excel com as receitas do mês. Ele utiliza o Nume para digitar os dados no Excel e o botão de enter para passar para próxima célula.

### User 2

O usuário 2 é um gamer que gosta de jogos de terror, mas é muito medroso e se assusta com muita facilidade. Então, ele utiliza o Nume para abaixar o volume do computador toda vez que acha que vai tomar um susto. 

### Comandos/ Feedbacks (2 pts)

<!-- 
Quais são os comandos/ operacões possíveis do seu controle?

Quais os feedbacks que seu controle vai fornecer ao usuário?
-->

### Comandos

* Digitar números de 0 a 9;
* Escrever os caracteres "+", "-", "," e ".";
* Controlar volume.

### Feedbacks

* Para cada caracter digitado, ele deve aparecer na tela do computador como se tivesse sido digitado no teclado pelo usuário.
* O volume do computador deve aumentar/diminuir proporcionalmente ao posicionamento da barra no potenciômetro. 

## In/OUT (3 pts)

* IN: Pressionar números de 0 a 9 no teclado matricial. OUT: O respectivo número é digitado e aparece na tela
* IN: Pressionar botão "A" no teclado matricial. OUT: O caracter "+" é digitado e aparece na tela
* IN: Pressionar botão "B" no teclado matricial. OUT: O caracter "-" é digitado e aparece na tela
* IN: Pressionar botão "C" no teclado matricial. OUT: Corresponde à operação "delete" no computador
* IN: Pressionar botão "D" no teclado matricial. OUT: Corresponde à operação "enter" no computador
* IN: Subir/Descer a barra do potenciômetro. OUT: O volume do computador aumenta, conforme subimos e diminui conforme descemos a barra.

### Design (2 pts)

![prototipo](https://user-images.githubusercontent.com/63075579/160221046-f0ff3648-65c4-4a96-a792-e78e4d189e61.jpeg)


