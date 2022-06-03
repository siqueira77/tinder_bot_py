from time import sleep
from selenium import webdriver

class TinderBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get('https://www.tinder.com')
        sleep(2)
    def login(self):
        login_btn = self.driver.find_element_by_xpath('//*[@id="s-522567612"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        sleep(1)
        login_btn.click()
        sleep(1)
    def login_cell(self):
        login_cell=self.driver.find_element_by_xpath('//*[@id="s2044018608"]/div/div/div[1]/div/div/div[3]/span/div[3]/button') 
        sleep(1)
        login_cell.click()
        sleep(1)
    def wait_input(self):
        input()
    def close_location(self):
        permitir_localizacao = self.driver.find_element_by_xpath(
            '//*[@id="s2044018608"]/div/div/div/div/div[3]/button[1]')
        sleep(1)
        permitir_localizacao.click()
        sleep(1)
    def close_pop_up(self):
        pop_up_notificacoes = self.driver.find_element_by_xpath(
            '//*[@id="s2044018608"]/div/div/div/div/div[3]/button[1]')
        sleep(1)
        pop_up_notificacoes.click()
        sleep(1)
    def like(self):
        try:
            sleep(1)
            botao_like = self.driver.find_elements_by_xpath(
                '//div[@class="Mx(a) Fxs(0) Sq(70px) Sq(60px)--s Bd Bdrs(50%) Bdc($c-like-green)"]//button')[1]
        except:
            try:
                sleep(1)
                botao_like = self.driver.find_element_by_xpath(
                    '//div[@class="Mx(a) Fxs(0) Sq(70px) Sq(60px)--s Bd Bdrs(50%) Bdc($c-like-green)"]')
            except:
                pass
        finally:
            sleep(1)
            botao_like.click()
            try:
                sleep(1)
                if self.driver.find_element_by_xpath("//label[text()='Say something nice!']") is not None:
                    sleep(1)
                    fechar_janela_match = self.driver.find_element_by_xpath(
                        "//button[@title='Back to Tinder']")
                    sleep(1)
                    fechar_janela_match.click()
                    sleep(1)
            except:
                pass
            try:
                sleep(1)
                if self.driver.find_element_by_xpath('//*[@id="s2044018608"]/div/div/div[2]/button[2]') is not None:
                    say_not = self.driver.find_element_by_xpath('//*[@id="s2044018608"]/div/div/div[2]/button[2]')
                    say_not.click()
            except:
                pass 

bot = TinderBot()
bot.login()
bot.login_cell()
bot.wait_input()
bot.close_location()
bot.close_pop_up()

while True:
    bot.like()