Feature: Selecionar Produto
 
  Scenario: Selecionar  "Sauce Labs Backpack"
   Given que acesso o site Sauce Demo
   When preencho os dados de login com usuario standard_user e senha secret_sauce
   Then sou direcionado para pagina Home
