  Feature: Selecionar Produto
  
      Scenario: Selecionar  "Sauce Labs Backpack"
      Given que acesso o site Sauce Demo
      When preencho os dados de login com usuario standard_user e senha secret_sauce
      Then sou direcionado para pagina Home  

      Scenario: Login com senha invalida
      Given que acesso o site Sauce Demo
      When preencho os dados de login com usuario standard_user e senha senhaerrada
      Then exibe mensagem de erro

      Scenario Outline: login negativo
      Given que acesso o site Sauce Demo
      When preencho os dados de login com usuario <usuario> e senha <senha>
      Then exibe <mensagem> de erro

      Examples:
      | id | usuario       | senha       | mensagem                                                                |
      | 01 | standard_user | senhaerrada |Epic sadface: Username and password do not match any user in this service| 
      | 02 | usuarioerrado | secret_sauce|Epic sadface: Username and password do not match any user in this service|
      | 03 |               | secret_sauce|Epic sadface: Username is required                                       |   
      | 04 | standart_user |             |Epic sadface: Password is required                                       |

      Scenario Outline: login negativo com IF
      Given que acesso o site Sauce Demo
      When digito os dados de login com usuario <usuario> e senha <senha> com IF
      Then exibe <mensagem>  de erro

      Scenario Outline: login negativo com IF
      Given que acesso o site Sauce Demo
      When digito os dados de login com usuario <usuario> e senha <senha>
      Then exibe <mensagem> de erro

      Examples:
      | id | usuario       | senha       | mensagem                                                                |
      | 01 | <branco>      | secret_sauce|Epic sadface: Username is required                                       |   
      | 02 | standart_user |  <branco>   |Epic sadface: Password is required                                       |

      Scenario Outline: login negativo com IF
      Given que acesso o site Sauce Demo
      When digito os dados de login com usuario <usuario> e senha <senha> com IF
      Then exibe <mensagem>  de erro
