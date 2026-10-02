Pet API

API simples para cadastro de pets feita com FastApi

# Como rodar

bash
pip install -r requeriments.txt
uvicorn main:app --reload

Documentação: http://127.0.0.1:8000/docs

Routers

GET "/pets" - Lista todos os pets cadastrados
POST "/pets" - Cria um pet novo
PUT "/pets/{id}" - Atualiza um pet
DELETE "/pets/{id}" - Deleta um pet

* Frontend simples apenas para testes, foco do projeto é a API
para testar use - /docs