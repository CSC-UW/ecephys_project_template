import os
from pathlib import Path

import yaml

DATASETS_DIRECTORY = Path(os.path.abspath(__file__)).parent

def get_datasets(dataset_name):
    with open(DATASETS_DIRECTORY/'datasets.yaml', 'r') as f:
        return yaml.load(
            f,
            Loader=yaml.SafeLoader,
        )[dataset_name]
