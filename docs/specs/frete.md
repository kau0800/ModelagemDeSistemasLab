# Especificação: Sistema de Cálculo de Frete

## Requisitos Funcionais

*   **RF-01 (Event-Driven):** **WHEN** o usuário solicitar o cálculo de frete para um valor de carrinho igual ou superior ao limite da região, **THE SYSTEM SHALL** definir o valor do frete como R$ 0,00.
*   **RF-02 (Event-Driven):** **WHEN** o usuário interagir com a página HTML fornecendo o valor do carrinho e a região, **THE SYSTEM SHALL** exibir na tela o valor final calculado e o status do frete.

## Regras de Negócio e Exceções

*   **RB-01 (State-Driven):** **WHILE** a região selecionada for 'Norte', **THE SYSTEM SHALL** considerar R$ 300,00 como valor limite para frete grátis. Para as demais regiões, o limite é R$ 200,00.
*   **RB-02 (Unwanted Behavior):** **IF** o valor total do carrinho for inferior ao limite da região, **THEN** **THE SYSTEM SHALL** aplicar a taxa fixa de R$ 20,00.
*   **RB-03 (Unwanted Behavior):** **IF** o valor do carrinho for menor ou igual a R$ 0,00, **THEN** **THE SYSTEM SHALL** rejeitar a operação e exibir mensagem de erro "Valor de carrinho inválido".

---