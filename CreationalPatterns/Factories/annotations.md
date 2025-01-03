## Problemas na Criação de Objetos e Soluções

### Complexidade da Lógica de Criação

A lógica responsável por criar novos objetos pode se tornar **excessivamente complexa** com o tempo, dificultando a compreensão e manutenção do código.

### Limitações dos Inicializadores

* **Nome padrão:** O uso frequente do nome `init` para métodos construtores pode tornar o código menos expressivo e autodocumentado.
* **Sobrecarga limitada:** A impossibilidade de sobrecarregar métodos construtores com os mesmos tipos de argumentos, mas com nomes diferentes, restringe as opções de criação de objetos.
* **"Inferno dos parâmetros opcionais":** A adição de muitos parâmetros opcionais a um construtor pode levar a um código difícil de ler e entender.

### Soluções com Padrões de Fábrica

Uma abordagem comum para resolver esses problemas é utilizar **padrões de fábrica**. Ao delegar a criação de objetos a métodos ou classes separadas, é possível:

* **Simplificar a lógica:** A lógica de criação fica encapsulada em um único lugar, tornando o código mais limpo e fácil de entender.
* **Criar hierarquias de fábricas:** O padrão Abstract Factory permite criar famílias de objetos relacionados, oferecendo mais flexibilidade e reusabilidade.

# Summary

* Um *método fábrica* (factory method) é um método estático que cria objetos.
* Uma *fábrica* (factory) é qualquer entidade que pode cuidar da criação de objetos.
* Uma fábrica pode ser externa ou residir dentro do objeto como uma classe interna.
* Hierarquias de fábricas podem ser usadas para criar objetos relacionados.
