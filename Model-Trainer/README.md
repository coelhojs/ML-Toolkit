# Container temporário (com python 3.7 como base)
docker create --name model-trainer python:3.7

# Build do container
docker build -t ml-trainer .


docker run --rm -it -v C:\Workspace:/workspace ml-trainer python3 ./object_detection/object_detection_trainer.py --model=vera_base_itens --steps=30000

docker run --name tensorflow -p 8888:8888 -d tensorflow

# Para copiar arquivos para o container ativo:
docker cp ./ unruffled_nash:/model-trainer/

# Remover arquivos do host
docker exec <container> rm -rf <YourFile>

docker exec xenodochial_bassi rm -rf /model-trainer

# Commit changes
docker commit unruffled_nash

# Adicionar tag ao novo container
docker tag 75874ec model-trainer-1.0

# Comando funcional:
docker run --rm -it -v "/develpment/workspace/:/research/workspace" -w "/research/workspace" ml-trainer python3 ./object_detection/object_detection_trainer.py --model=vera_base_itens --steps=30000


Edição do container:
    Inicia o container
    Copia o arquivo para o container rodando
    Faz um commit das mudanças; será gerado um container sem tag
    Atribui uma tag ao novo container
    Roda o container