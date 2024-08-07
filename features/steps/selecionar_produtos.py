import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
        context.driver= webdriver.Chrome()
        context.driver.maximize_window() 
        #context.driver.implicitly_wait(5)
        context.driver.get("https://www.saucedemo.com/")

@when(u'preencho os dados de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
       context.driver.find_element(By.ID , "user-name").send_keys(usuario)
       context.driver.find_element(By.ID , "password").send_keys(senha) 
       context.driver.find_element(By.ID , "login-button").click() 

@when(u'preencho os dados de login com usuario  e senha {senha}')
def step_impl(context, senha):
       context.driver.find_element(By.ID , "password").send_keys(senha) 
       context.driver.find_element(By.ID , "login-button").click() 

@when(u'preencho os dados de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
        context.driver.find_element(By.ID , "user-name").send_keys(usuario) 
        context.driver.find_element(By.ID , "login-button").click() 

@when(u'digito os dados de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
       if usuario != '<branco>':
         context.driver.find_element(By.ID , "user-name").send_keys(usuario)
       if senha != '<branco>':  
         context.driver.find_element(By.ID , "password").send_keys(senha) 
       context.driver.find_element(By.ID , "login-button").click()   

@then(u'sou direcionado para pagina Home')
def step_impl(context):
        assert  context.driver.find_element (By.CSS_SELECTOR, "span.title").text =="Products"
        time.sleep(2)
        context.driver.quit()

@then(u'exibe mensagem de erro')
def step_impl(context):
      assert context.driver.find_element (By.CSS_SELECTOR, "h3").text =="Epic sadface: Username and password do not match any user in this service"    
      time.sleep(2)
      context.driver.quit()

@then(u'exibe {mensagem} de erro')
def step_impl(context, mensagem):
      assert context.driver.find_element (By.CSS_SELECTOR, "h3").text == mensagem    
      time.sleep(2)
      context.driver.quit()
