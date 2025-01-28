from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Credenciais do Instagram (fixas para este exemplo)
INSTAGRAM_USERNAME = ""
INSTAGRAM_PASSWORD = ""

# Configuração do Flask
app = Flask(__name__)

# Variável global para armazenar a instância do driver
driver = None

# Função para realizar login
def login_instagram():
    global driver
    if driver is None:
        # Configurar o WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Rodar em modo headless (sem abrir o navegador)
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

        try:
            # Acessar o Instagram
            driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(5)

            # Fazer login
            driver.find_element(By.NAME, "username").send_keys(INSTAGRAM_USERNAME)
            driver.find_element(By.NAME, "password").send_keys(INSTAGRAM_PASSWORD + Keys.RETURN)
            time.sleep(5)
            print("Login realizado com sucesso")
        except Exception as e:
            print(f"Erro ao fazer login: {e}")

# Função para buscar a URL da imagem de perfil
def fetch_profile_image(target_username):
    global driver
    if driver is None:
        login_instagram()

    try:
        # Acessar o perfil do usuário
        target_url = f"https://www.instagram.com/{target_username}"
        driver.get(target_url)
        time.sleep(5)

        # Buscar a imagem de perfil
        img_element = driver.find_element(By.CSS_SELECTOR, f"img[alt='Foto do perfil de {target_username}']")
        img_url = img_element.get_attribute("src")
        return img_url

    except Exception as e:
        return str(e)

# Endpoint da API
@app.route("/get-profile-image", methods=["POST"])
def get_profile_image():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "O campo 'username' é obrigatório"}), 400

    username = data["username"]
    img_url = fetch_profile_image(username)

    if "http" in img_url:
        return jsonify({"username": username, "image_url": img_url})
    else:
        return jsonify({"error": f"Não foi possível obter a imagem para {username}", "details": img_url}), 500

# Iniciar o servidor
if __name__ == "__main__":
    login_instagram()  # Realizar o login antes de iniciar o servidor
    app.run(debug=True)
