# - *- coding: utf- 8 - *-
import argparse
import subprocess

print("Definindo as variaveis de ambiente...")

from object_detection.utils import xml_to_csv
from object_detection.utils import generate_tf_record
from object_detection import model_main as train

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", help="Nome do modelo que será treinado.")
    parser.add_argument("--steps", type=int,
                        help="Numero de passos para o treinamento.")
    args = parser.parse_args()

    if args.model:
        model_name = args.model
    if args.steps:
        train_steps = args.steps

    print("Gerando os CSVs a partir dos XMLs...")

    xml_to_csv.main('workspace/images/train',
                    'workspace/annotations/train_labels.csv')

    xml_to_csv.main('workspace/images/test',
                    'workspace/annotations/test_labels.csv')

    print("Gerando os TFRecords...")

    generate_tf_record.main('workspace/annotations/train_labels.csv', 'workspace/images/train', 'workspace/annotations/train.record')

    generate_tf_record.main(
        'workspace/annotations/test_labels.csv', 'workspace/images/test', 'workspace/annotations/test.record')

    print("Iniciando o treinamento...")

    training_folder = 'workspace/intermediate_files/training'
    config = 'workspace/{model_name}.config'.format(model_name=model_name)

    subprocess.run(["python", "./object_detection/model_main.py", "--model_dir=workspace/intermediate_files/training", "--pipeline_config_path=workspace/{model_name}.config".format(model_name=model_name)])
