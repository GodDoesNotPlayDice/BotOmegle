from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('log-level=3')
driver = wb.Chrome("chromedriver",options=chrome_options)
driver.get("https://www.omegle.com/")
sleep(2)
driver.find_element(By.ID, 'textbtn').click()
sleep(2)
input = driver.find_elements(By.TAG_NAME,'input')
input[2].click()
input[3].click()
sleep(2)
input[4].click()
sleep(4)
while True:
    sleep(1)
    driver.find_element(By.CLASS_NAME, 'chatmsgwrapper').find_element(By.CLASS_NAME,'chatmsg').click()
    driver.find_element(By.CLASS_NAME, 'chatmsgwrapper').find_element(By.CLASS_NAME,'chatmsg').send_keys("""
    Hola Diana, una inteligencia artificial, y estoy aprendiendo cosas de Humanos
    me puedes responder estas preguntas porfavor.
    ######################################################
    ¿Qué hay en el primer puesto de tu lista de deseos?
    ¿Por qué estás más agradecido?
    ¿Qué es lo que más lamentas en la vida?
    ¿Qué es lo que más temes?
    ¿Qué es lo que más te apasiona?
    ¿Cómo te gusta pasar tu tiempo libre?
    ¿Cómo sería tu día perfecto?
    ¿Cómo es tu vida soñada?
    ######################################################
    Cuando termines puedes saltar el chat porfavor :)""") # text area
    sleep(1.5)
    driver.find_element(By.CLASS_NAME, 'sendbtn').click()
    def me():
        me_msg = driver.find_elements(By.CLASS_NAME, 'youmsg')
        for i in me_msg:
            print(f"{i.find_element(By.CLASS_NAME, 'msgsource').text} {i.find_element(By.CLASS_NAME, 'notranslate').text}")
    me()
    last = ""
    while True:
        sleep(4)    
        log = driver.find_elements(By.CLASS_NAME, 'logitem')
        isDisconnect = driver.find_element(By.CLASS_NAME,'disconnectbtn').text[0:3]
        sleep(2)
        if isDisconnect == 'New':
            os.system('cls')
            print("NextChat")
            btn_next = driver.find_element(By.CLASS_NAME,'disconnectbtn')
            btn_next.click()
            break
        else:
            stranger_msgs = driver.find_elements(By.CLASS_NAME, 'strangermsg')
            for i in stranger_msgs:
                if stranger_msgs[-1].find_element(By.CLASS_NAME, 'notranslate').text != last:
                    last = stranger_msgs[-1].find_element(By.CLASS_NAME, 'notranslate').text
                    print(f"{i.find_element(By.CLASS_NAME, 'msgsource').text} {last}")
                else:
                    pass
