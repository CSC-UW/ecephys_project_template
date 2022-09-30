from ecephys_project_template.off_detection import run_spatial_off_detection
from ecephys_project_template.datasets import get_datasets
import itertools

"""Copy, modify and run to run the whole pipeline for several datasets."""

project = "ecephys_project_template"

sorting_name = "ks2_5_catgt_df_postpro_2"

# Dataset
dataset_name = 'all'
datasets_list = get_datasets(dataset_name)

datasets_list = [
    {
        "subject": "CNPIX8-Allan",
        "probe": "imec0",
        "region": "all",
    },
]

experiment_alias_list = [
    # ("novel_objects_deprivation", "sleep_deprivation")
]

detection_names=[
    # "spatial_off_hmmem_intermediate",
]

states=None

if __name__ == '__main__':

    for (
        dataset,
        (experiment, alias),
        detection_name
    ) in itertools.product(
        datasets_list,
        experiment_alias_list,
        detection_names,
    ):

        print(dataset)
        print(experiment, alias)
        print(detection_name)

        run_spatial_off_detection(
            dataset["subject"],
            experiment,
            alias,
            dataset["probe"],
            region=dataset["region"],
            sorting_name=sorting_name,
            detection_name=detection_name,
            sorting_project=project,
            states=states,
        )