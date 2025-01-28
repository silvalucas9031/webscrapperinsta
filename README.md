Este é um scraper simples, desenvolvido em Python, utilizando o Flask e o Selenium para buscar a URL da imagem de perfil de um usuário do Instagram. 
A ferramenta realiza o login automaticamente, mantendo a sessão aberta para tornar o processo mais rápido e eficiente. A partir de uma requisição HTTP POST, o scraper recupera a URL da imagem de perfil de qualquer usuário do Instagram fornecido.

Funcionalidades
Login automático: O scraper realiza o login no Instagram apenas uma vez, mantendo a sessão ativa para futuras requisições.
Rápido e eficiente: Evita logins repetidos, economizando tempo e recursos.

API simples: A API Flask expõe um endpoint (/get-profile-image) para que qualquer aplicação possa acessar a URL da imagem de perfil de um usuário específico.
Modo Headless: O Selenium é executado no modo headless (sem interface gráfica), tornando o scraper mais rápido e ideal para uso em servidores ou automações.

Requisitos<br>
Python 3.x <br>
Selenium<br>
Flask<br>
WebDriver (ChromeDriver)

Faça uma requisição POST para o endpoint /get-profile-image com o corpo JSON contendo o nome de usuário do Instagram:

{<br>
  "username": "nomedousuario"<br>
}<br>


Exemplo de resposta<br>
{<br>
  "username": "nomedousuario",<br>
  "image_url": "https://instagram.com/.../profile_pic.jpg"<br>
}<br>
<br><br>
Observações<br>
Segurança: As credenciais do Instagram estão hardcoded no código. É recomendado usar variáveis de ambiente ou outro método seguro para gerenciar senhas em um ambiente de produção.
Limitações: Este scraper depende da estrutura atual do Instagram, portanto, mudanças na página podem quebrar a funcionalidade. A automação de login pode ser bloqueada se detectada como atividade suspeita.
