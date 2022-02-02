# Executando a api sem docker

Na pasta raíz do projeto, em um terminal com python 3 rode os seguintes comandos:

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements-dev.txt
```

Caso seja windows, os comandos podem ser diferentes, se estiver no cmd tente os seguintes comnados:

```
python -m venv env
env\Scripts\activate.bat
pip install -r requirements-dev.txt
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