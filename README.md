*Nome:* Jhully Camilly  Pereira Soares
*Turma:* 35N34
*Disciplina:* Fundamentos da computação 
*Data:* 04/05/2026

# Sistema de Atendimento de Loja - ProgramaEC1

## 1. Lógica de Funcionamento
O sistema simula o atendimento básico de uma loja por meio de um menu interativo no terminal.

1. O programa é iniciado e exibe um menu com três opções para o usuário: Comprar produto, Ver total acumulado e Sair.
2. Ao selecionar a opção 1, o sistema solicita ao usuário o nome do produto, o preço unitário e a quantidade desejada, dados inseridos externamente pelo usuário.
3. Com os dados coletados, o programa realiza o processamento interno: calcula o valor total da compra multiplicando preço pela quantidade e acumula esse valor em um total geral de vendas.
4. Em seguida, o sistema verifica se o valor da compra é superior a R$100,00. Caso seja, uma variável lógica é definida como verdadeira, indicando uma compra de grande valor.
5. Ao selecionar a opção 2, o programa exibe na tela o valor total acumulado de todas as compras realizadas.
6. Ao selecionar a opção 3, o programa encerra sua execução.
7. Caso o usuário insira uma opção inválida, o sistema exibe uma mensagem de erro e retorna ao menu principal.

## 2. Descrição do Programa
O programa utiliza variáveis de diferentes tipos para armazenar informações: strings para o nome do produto, inteiros para a quantidade, números de ponto flutuante para o preço e totais, e booleanos para sinalizar compras de grande valor. 
A estrutura condicional if, elif e else é utilizada para controlar o fluxo do menu e para classificar o tamanho da compra.

## 3. Como Executar
Para executar o programa é necessário ter o Python 3 instalado.
No terminal, navegar até a pasta do projeto e executar o comando:
python app.py

## 4. Exemplo de Uso
Entrada:
Escolha uma opção: 1
Nome do produto: Camiseta
Preço: 50.00
Quantidade: 3

Saída:
Você comprou 3x Camiseta
Total da compra: R$ 150.00
Compra grande: True
Total acumulado: R$ 150.00
