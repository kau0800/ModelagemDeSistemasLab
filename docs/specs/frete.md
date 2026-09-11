# Especificação de Requisitos -  Sistema de Frete
## Parâmetros do Sistema
*   **RF-01:** **WHEN** o usuário calcular o frete e o carrinho atingir o limite regional, **THE SYSTEM SHALL** zerar o frete.
*   **RB-01:** **WHILE** a região for 'Norte', o limite é R$ 300,00. Demais regiões: R$ 200,00.
*   **RB-03:** **IF** valor <= 0, **THEN** **THE SYSTEM SHALL** exibir erro 'Valor de carrinho inválido'.

## Requisitos do Fluxo Principal

### Orientados a Eventos
*   **WHEN** o usuário informar um CEP válido, **THE SYSTEM SHALL** calcular o valor e o prazo de entrega.
*   **WHEN** o pagamento for confirmado, **THE SYSTEM SHALL** gerar a ordem de coleta para a transportadora.

### Resposta a Falhas
*   **IF** o CEP informado não for localizado, **THEN** **THE SYSTEM SHALL** exibir a mensagem "CEP não encontrado".
*   **IF** a API de frete estiver indisponível, **THEN** **THE SYSTEM SHALL** aplicar a tabela de preço fixo regional.
