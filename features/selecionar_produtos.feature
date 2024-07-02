Feature: Selecionar Produto
 
  Scenario: Selecionar  "Sauce Labs Backpack"
   Given que acesso o site Sauce Demo
   When preencho os dados de login com usuario standard_user e senha secret_sauce
   Then sou direcionado para pagina Home
   
 Scenario: Login com senha invalida
   Given que acesso o site Sauce Demo
   When preencho os dados de login com usuario standard_user e senha senhaerrada
   Then exibe msg de erro
   