# Executando com docker para desenvolvimento

Para executar a api com docker no modo de desenvolvimento, rode o comando abaixo na raiz do projeto.

```
docker run --rm -it -u $UID:$UID -p 5000:5000 -v $(pwd):/app python:3.10-slim-buster bash
```

No terminal do container, rode esses comandos para criar o venv e instalar as dependências:

```
cd /app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements-dev.txt
```

Para configurar a aplicação, rode o script configure_app, será criado um usuário admin@mail.com com senha igual a variável de ambiente **ADMIN_PASSWORD**. Caso a variável de ambiente não seja atribuida, a senha padrão é admin.

Por padrão, o banco utilizado será o SQLite criado no arquivo db.sqlite. Caso queira utilizar outro arquivo, sobrescreva a variável de ambiente **DATABASE_URL**

```
python3 configure_app.py
```

Para executar a api, rode o comando:

```
python3 main.py
```

A documentação da api pode ser acessada pelo navegador no http://localhost:5000/docs