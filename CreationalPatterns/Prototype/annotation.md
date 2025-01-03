# Prototype

* Objetos complexos (ex: carros) não são projetados do zero.
  * Eles reiteram designs existentes.
* Um design existente (parcial ou totalmente construído) é um **Protótipo**.
* Nós fazemos uma cópia (clone) do protótipo e o customizamos.
  * Requer suporte a 'cópia profunda' (deep copy).
* Nós tornamos a clonagem conveniente (ex: via uma Fábrica).

##### Um objeto parcial ou totalmente inicializado que você copia (clona) e utiliza.

## Resumo (Implementação do Protótipo)

* Para implementar um Prototype, construa parcialmente um objeto e armazene-o em algum lugar.
* Copie profundamente (deep copy) o Prototype.
* Customize a instância resultante.
* Uma factory fornece uma API conveniente para usar Prototypes.
