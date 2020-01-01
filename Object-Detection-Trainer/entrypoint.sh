#!/bin/bash
set -e

echo "Inicializando variaveis"
protoc object_detection/protos/*.proto --python_out=.
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
echo "Preparando arquivos do treinamento"
python3 object_detection/object_detection_trainer.py --model=vera_base_itens --steps=30000
echo "Iniciando treinamento"
python3 object_detection/model_main.py --logtostderr --model_dir=workspace/intermediate_files/training --pipeline_config_path=workspace/vera_base_itens.config

# exec "$@"