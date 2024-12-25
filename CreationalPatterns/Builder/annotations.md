# Builder Pattern

* Alguns objetos são simples e podem ser criados com uma única chamada ao inicializador.
* Outros objetos requerem muitos passos e configurações para serem criados.
* Ter um objeto com 10 argumentos no inicializador não é produtivo.
* Em vez disso, opte pela construção incremental (piecewise construction).
* O padrão **Builder** fornece uma API para construir um objeto passo a passo.

**Quando a construção de objetos de forma incremental é complicada, forneça uma API para fazê-lo de forma concisa.**

# Resumo

* Um builder é um componente separado para construir um objeto.
* Pode fornecer um inicializador ao builder ou retorná-lo via uma função estática.
* Para tornar o builder fluente, retorne `self`.
* Diferentes aspectos de um objeto podem ser construídos com diferentes builders trabalhando em conjunto por meio de uma classe base.
