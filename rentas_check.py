from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

# No funciona con colab debido a que las nuevas versiones ubuntu no soportan chromium

def definir_navegador():
    # DEFINO EL NAVEGADOR Y LAS OPCIONES QUE LO ACOMPAÑAN
    from webdriver_manager.chrome import ChromeDriverManager
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-port-9222')
    options.add_argument('--disable-dev-shm-usage')
    # Ubicacion del driver, se deja comentada una herramienta automatica, falla con el proxi < modificar segun ubi de cada pc
    direct_chrome = r"C:\Users\20325618044\.wdm\drivers\chromedriver\win32\chromedriver.exe"
    driver = webdriver.Chrome(direct_chrome,options=options)
    
        
        
    print("SE DEFINIO EL DRIVER")
    driver.maximize_window()
    driver.set_page_load_timeout(60)
    return driver




driver=definir_navegador()

def consulta(driver,cuit):
    driver=driver
    cuit=cuit
    delay=15
    driver.get("https://www.rentascordoba.gob.ar/gestiones/consulta/situacion-fiscal") # Website used for scraping
    time.sleep(5)
    WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/main/app-situacion-fiscal-container/div/div/div/div[3]/app-situacion-fiscal-input/div/div[1]/div/div/div[2]/div/form/div[1]/kui-hugger/div[1]/div/input")))
    cuadro_cuit = driver.find_element("xpath",'/html/body/app-root/main/app-situacion-fiscal-container/div/div/div/div[3]/app-situacion-fiscal-input/div/div[1]/div/div/div[2]/div/form/div[1]/kui-hugger/div[1]/div/input')
    cuadro_cuit.click()

    cuit_xpath = driver.find_element("xpath",'/html/body/app-root/main/app-situacion-fiscal-container/div/div/div/div[3]/app-situacion-fiscal-input/div/div[1]/div/div/div[2]/div/form/div[1]/kui-hugger/div[1]/div/input')
    cuit_xpath.send_keys(cuit)
    time.sleep(1)
    click_boton = driver.find_element("xpath",'/html/body/app-root/main/app-situacion-fiscal-container/div/div/div/div[3]/app-situacion-fiscal-input/div/div[1]/div/div/div[2]/div/form/div[2]/button')
    click_boton.click()
    try:
        WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/main/app-situacion-fiscal-container/div/div/div/div[3]/app-situacion-fiscal-result/div/div/div[1]')))
        estado = driver.find_element("xpath",'/html/body/app-root/main/app-situacion-fiscal-container/div/div/div/div[3]/app-situacion-fiscal-result/div/div/div[1]/kui-card/div/div/div[1]/div[1]/span')
        print(estado.text)
        return estado.text
    except:
        consulta(driver,cuit)

# Crear una lista con los cuits a controlar
lista_cuit=[numero de cuits, otro numero de cuit, etc,etc]

for cuit in lista_cuit:
    print(f"cuit: {cuit}")
    consulta(driver,cuit)
