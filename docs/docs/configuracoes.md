# Configuração

A api é configurada utilizando variávei de ambiente.


## Variáveis de ambiente

* **PROJECT_NAME**(Padrão: ImageDatasetApi): Nome do projeto
* **SECRET_KEY**(Padrão: valor aleatório): Chave utilizada na asinatura do token JWT.
* **DATABASE_URL**(Padrão: sqlite:///db.sqlite): URL para a conexão com o banco de dados.
* **TEST_DATABASE**(Padrão: False): Indica se o banco de dados está sendo utilizado para testes. Se for verdadeiro, o banco não irá persistir os dados.
* **ACCESS_TOKEN_EXPIRE_HOURS**(Padrão: 24): Validade do token JWT.
* **THUMBNAIL_SIZE**(Padrão: 36): Tamanho do maior lado da imagem gerada para o thumbnail.
* **ADMIN_PASSWORD**(Padrão: admin): Password gerado para o admin criado durante a criação do sistema.