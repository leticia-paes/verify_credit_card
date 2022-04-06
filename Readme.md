[EN] This program takes in a credit card number and checks if it is valid. 

In a typical 16-digit credit card number, the first six digits identify the institution that issued the card. 
The next nine digits identify the individual account associated with the card. The last digit, the 16th, is the check digit. 
Credit card issuers plug the first 15 digits into a mathematical formula called the Luhn algorithm, which produces a single-digit 
result. That result is added to the check digit, and if that sum results in an even multiple of 10, we can tell that the
credit card number is valid.

The steps of the Luhn algorithm are shown under the verify_credit_card_number() function.

You can check more information about credit card number validation on https://www.sapling.com/7966257/checksum-credit-card

----------------------------------------------------------------------------------------------------------------------------------

[POR] Este programa recebe um número de cartão de crédito e verifica se ele é válido.

Em um número típico de cartão de crédito de 16 dígitos, os seis primeiros dígitos identificam a instituição que emitiu o cartão.
Os próximos nove dígitos identificam a conta individual associada ao cartão. O último dígito, o 16º, é o dígito verificador.
Os emissores de cartões de crédito inserem os primeiros 15 dígitos em uma fórmula matemática chamada algoritmo de Luhn, que produz 
um dígito como resultado. Esse resultado é adicionado ao dígito verificador e, se essa soma resultar em um múltiplo par de 10, 
podemos dizer que o número do cartão de crédito é válido.

As etapas do algoritmo Luhn são mostradas na função verify_credit_card_number().

Você pode verificar mais informações sobre a validação do número do cartão de crédito em https://www.sapling.com/7966257/checksum-credit-card