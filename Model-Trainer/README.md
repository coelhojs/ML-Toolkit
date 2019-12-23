# Build do container
docker build -t model-trainer .


docker run --rm -it -v C:\Workspace:tensorflow/workspace tensorflow python ./object_detection_trainer.py --model=vera_base_itens --steps=30000

docker run --name tensorflow -p 8888:8888 -d tensorflow

# Comando funcional:
docker run -it model-trainer python ./object_detection_trainer.py --model=vera_base_itens --steps=30000
