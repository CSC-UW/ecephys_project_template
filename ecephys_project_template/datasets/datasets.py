from ..constants import PARAMS_DIRECTORY
import yaml

def get_datasets_list(dataset_name):
    with open(PARAMS_DIRECTORY/'datasets.yaml', 'r') as f:
        return yaml.load(
            f,
            Loader=yaml.SafeLoader,
        )[dataset_name]
