# Executando com docker-compose

Para rodar a build da api com o docker-compose, rode esse comando na pasta principal do projeto:

```
sudo docker-compose -f docker/docker-compose.prod.yml up
```

Para mudar as configuração, entre no arquivo docker/docker-compose.prod.yml e altere a seção *enviroment* do arquivo.

A api estará disponível em http://localhost:8080
