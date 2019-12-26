# - *- coding: utf- 8 - *-
import argparse
import subprocess
import os
import sys

from utils import xml_to_csv
from utils import generate_tf_record
from legacy import train

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