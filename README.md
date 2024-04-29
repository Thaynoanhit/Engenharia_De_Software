# Engenharia-De-Software

Neste repositório, apresento exemplos de como aplicar os Princípios SOLID Python, com cada exemplo demonstrando um princípio específico.

# Princípio da Inversão de Dependência (DIP)

Dependency Inversion Principle (DIP): Este princípio sugere que as classes de alto nível não devem depender das classes de baixo nível, mas sim de abstrações. Além disso, as abstrações não devem depender de detalhes, mas sim de outras abstrações.

*Exemplo Correto:* A classe PaymentGateway depende da abstração PaymentProcessor, e não de implementações concretas como CreditCardPaymentProcessor ou PayPalPaymentProcessor. Isso permite que a classe PaymentGateway seja flexível e possa trabalhar com diferentes implementações de processamento de pagamentos, sem precisar ser modificada.

*Exemplo Incorreto:* A classe PaymentGateway depende de implementações concretas como CreditCardPaymentProcessor ou PayPalPaymentProcessor, o que é incorreto de acordo com o Princípio de Inversão de Dependência (DIP). Isso torna a classe PaymentGateway menos flexível e mais difícil de manter, pois qualquer mudança nas implementações concretas exigirá uma modificação na classe PaymentGateway.

[Exemplos](https://github.com/Thaynoanhit/Engenharia-De-Software/tree/main/DIP)

# Princípio da Responsabilidade Única (SRP)

Single Responsibility Principle (SRP): Este princípio afirma que uma classe deve ter apenas uma razão para mudar, ou seja, deve ter apenas uma responsabilidade.

*Exemplo correto:* Temos três classes que cada uma tem uma responsabilidade única:

UserBalance: gerencia o saldo de um usuário, permitindo depósitos e saques.

UserAuthenticator: autentica um usuário, verificando se o nome de usuário e senha estão corretos.

UserInfo: gerencia as informações de um usuário, como nome e email.
Cada classe tem métodos que são específicos para sua responsabilidade, e não há overlap entre as responsabilidades das classes. Isso segue o Princípio da Responsabilidade Única (SRP), que diz que uma classe deve ter apenas uma razão para mudar.

*Exemplo Incorreto:* A classe User tem múltiplas responsabilidades:

Gerenciar informações do usuário (nome, email, username, password)
Autenticar o usuário)

Gerenciar o saldo do usuário (depósito, saque, saldo)
Isso viola o Princípio da Responsabilidade Única (SRP), pois a classe User tem mais de uma razão para mudar. Se precisarmos mudar a lógica de autenticação, por exemplo, podemos acabar afetando a lógica de gerenciamento de saldo ou informações do usuário.

[Exemplos](https://github.com/Thaynoanhit/Engenharia-De-Software/tree/main/SRP)

# Princípio da Substituição de Liskov (LSP)

Liskov Substitution Principle (LSP): Afirma que objetos de um tipo base devem ser substituíveis por objetos de um tipo derivado sem afetar a integridade do programa.

*Exemplo Correto:* A classe Vehicle é uma classe abstrata que define a interface para um veículo, com um método move. As classes Car e Airplane são classes concretas que implementam essa interface.

A função move_vehicle pode trabalhar com qualquer veículo, desde que ele implemente a interface Vehicle. Isso significa que podemos passar uma instância de Car 

*Exemplo Incorreto:* As classes Car e Airplane herdam de Vehicle, mas adicionam métodos específicos (drive e fly, respectivamente) que não estão presentes na classe Vehicle. Isso viola o Princípio da Substituição de Liskov (LSP), pois as classes Car e Airplane não são substituíveis por Vehicle sem quebrar a compatibilidade.

[Exemplos](https://github.com/Thaynoanhit/Engenharia-De-Software/tree/main/LSP)

# Princípios Aberto-Fechado (OCP): 

Este princípio preconiza que as entidades de software (classes, módulos, funções, etc.) devem ser abertas para extensão, mas fechadas para modificação.

*Exemplo Correto:* A classe Shape é uma classe abstrata que define a interface para uma forma geométrica, com um método area. As classes Rectangle e Circle são classes concretas que implementam essa interface.

A classe ShapeAreaCalculator é responsável por calcular a área de uma forma geométrica, mas ela não sabe como calcular a área de formas específicas. Em vez disso, ela recebe uma instância de Shape como parâmetro e delega a responsabilidade de calcular a área a essa instância.

Isso permite que a classe ShapeAreaCalculator seja aberta para extensão, mas fechada para modificação. Se precisarmos adicionar um novo método de cálculo de área, podemos simplesmente criar uma nova classe que implemente a interface Shape e passá-la para a classe ShapeAreaCalculator. Não é necessário modificar a classe ShapeAreaCalculator em si.

*Exemplo Incorreto:* A classe PaymentProcessor viola o Princípio Aberto-Fechado (OCP) porque ela precisa ser modificada para suportar novos métodos de pagamento. Se quisermos adicionar um novo método de pagamento, precisamos modificar a classe PaymentProcessor para incluir um novo caso no método process_payment.

[Exemplos](https://github.com/Thaynoanhit/Engenharia-De-Software/tree/main/OCP)
