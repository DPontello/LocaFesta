import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import time


class TestClientesUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_path = str(Path("chromedriver.exe").resolve())
        service = Service(chrome_path)
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.wait = WebDriverWait(cls.driver, 3)

    def test_01_adicionar_cliente(self):
        self.driver.get("file://" + str(Path("../../clientes.html").resolve()))

        # Abrir modal de adicionar cliente
        botao_add = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Adicionar Novo Cliente')]"))
        )
        botao_add.click()

        # Espera modal visível
        self.wait.until(EC.visibility_of_element_located((By.ID, "nomeCliente")))

        # Preencher formulário
        self.driver.find_element(By.ID, "nomeCliente").send_keys("Carlos")
        self.driver.find_element(By.ID, "cpfCnpjCliente").send_keys("12340008901")
        self.driver.find_element(By.ID, "emailCliente").send_keys("carlos@email.com")
        self.driver.find_element(By.ID, "telefoneCliente").send_keys("11900999999")

        # Clicar em salvar cliente
        botao_salvar = self.driver.find_element(By.XPATH, "//button[contains(., 'Salvar Cliente')]")
        botao_salvar.click()

        # Captura o alerta e aceita para continuar
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Alerta visível: {alert_text}")
            alert.accept()
        except:
            print("Nenhum alerta presente.")

        # Espera até o texto "Carlos" aparecer na tabela clientes
        self.wait.until(
            EC.text_to_be_present_in_element((By.ID, "clientesTableBody"), "Carlos")
        )

        # Busca texto da tabela e verifica se "Carlos" está presente
        tabela = self.driver.find_element(By.ID, "clientesTableBody").text
        self.assertIn("Carlos", tabela)

    def test_02_editar_cliente_para_jorge(self):
        self.driver.get("file://" + str(Path("../../clientes.html").resolve()))

        # Captura e aceita alerta se houver (ex: erro "Failed to fetch")
        try:
            alert = self.wait.until(EC.alert_is_present())
            print(f"Alerta visível no carregamento inicial: {alert.text}")
            alert.accept()
        except:
            print("Nenhum alerta presente no carregamento inicial.")

        # Espera o corpo da tabela clientes estar presente
        self.wait.until(EC.presence_of_element_located((By.ID, "clientesTableBody")))
        time.sleep(1)  # aguarda estabilidade da tabela

        # Clica no botão editar do primeiro cliente encontrado
        botao_editar = self.driver.find_element(By.XPATH, "//button[contains(., 'Editar')]")
        botao_editar.click()

        # Espera modal de edição visível
        self.wait.until(EC.visibility_of_element_located((By.ID, "clienteModal")))

        # Limpa e altera o nome do cliente para "Jorge"
        campo_nome = self.driver.find_element(By.ID, "nomeCliente")
        campo_nome.clear()
        campo_nome.send_keys("Jorge")

        # Salvar edição
        self.driver.find_element(By.XPATH, "//button[contains(., 'Salvar Cliente')]").click()

        # Captura o alerta e aceita
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Alerta visível: {alert_text}")
            alert.accept()
        except:
            print("Nenhum alerta presente após salvar.")

        # Espera até o texto "Jorge" aparecer na tabela clientes
        self.wait.until(
            EC.text_to_be_present_in_element((By.ID, "clientesTableBody"), "Jorge")
        )

        tabela = self.driver.find_element(By.ID, "clientesTableBody").text
        self.assertIn("Jorge", tabela)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
