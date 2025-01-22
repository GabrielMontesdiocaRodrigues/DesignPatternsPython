# Singleton

* Para alguns componentes, só faz sentido ter um no sistema.
  * Repositório de banco de dados.
  * Fábrica de objetos.
* Ex.: a chamada do inicializador é custosa.
  * Nós fazemos isso apenas uma vez.
  * Nós fornecemos a todos a mesma instância.
* Queremos prevenir que alguém crie cópias adicionais.
* Precisamos cuidar da instanciação preguiçosa (lazy instantiation).

## Resumo

* Diferentes implementações do Singleton: alocador customizado, decorator, metaclasse.
* Instanciação preguiçosa (lazy initialization) é fácil, basta inicializar na primeira requisição.
* Variação Monostate.
* Problemas de testabilidade.
