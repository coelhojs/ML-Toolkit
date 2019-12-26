# Container temporário (com python 3.7 como base)
docker create --name model-trainer python:3.7

# Build do container
docker build -t ml-trainer .

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

# Comando desejado:
    docker run ml-trainer --mount type=bind,source=/C/Workspace,target=/research/workspace -e SCRIPT=object_detection MODEL_NAME=vera_base_itens

# Ubuntu
    docker run --mount type=bind,source=/home/cristiano/development/workspace,target=/research/workspace ml-trainer python3 ./object_detection/object_detection_trainer.py --model=vera_base_itens --steps=30000

# Windows
    docker run -t --rm --mount type=bind,source=/C/Workspace,target=/research/workspace -e MODEL_NAME=vera_base_itens ml-trainer python3 ./object_detection/model_main.py --logtostderr --model_dir=workspace/intermediate_files/training --pipeline_config_path=workspace/vera_base_itens.config


Edição do container:
    Inicia o container
    Copia o arquivo para o container rodando
    Faz um commit das mudanças; será gerado um container sem tag
    Atribui uma tag ao novo container
    Roda o container