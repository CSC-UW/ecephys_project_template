from wisc_ecephys_tools.spikesorting.pipeline import run_pipeline
from ecephys_project_template.datasets import get_datasets
import itertools

"""Copy, modify and run to run the whole pipeline for several datasets."""

project = "ecephys_project_template"
prepro_project = "ecephys_project_template"  # Only for (temporary) catGT data.

dataset_name = 'frontal'
datasets_list = get_datasets(dataset_name)
print(datasets_list)

datasets_list = [
    # {
    #     "subject": "CNPIX8-Allan",
    #     "probe": "imec0"
    # },
]
print(datasets_list)

experiment_alias_list = [
    ('novel_objects_deprivation', 'sleep_deprivation'),
]

# Analysis names
prepro_analysis_name = (
    "prepro_df"  # Must be in 'preprocessing' doc in analysis_cfg.yaml
)
sorting_analysis_name = (
    "ks2_5_catgt_df"  # Must be in 'sorting' doc in analysis_cfg.yaml
)
postpro_analysis_name = (
    "postpro_2"  # Must be in 'ks_postprocessing' doc in analysis_cfg.yaml
)

# Misc
clear_preprocessed_data = False  # Rm catGT data after sorting
rerun_existing = True
dry_run = False


if __name__ == "__main__":

    for (
        dataset,
        (experiment, alias),
    ) in itertools.product(datasets_list, experiment_alias_list):

        run_pipeline(
            project=project,
            prepro_project=prepro_project,
            subject=dataset["subject"],
            experiment=experiment,
            alias=alias,
            probe=dataset["probe"],
            prepro_analysis_name=prepro_analysis_name,
            sorting_analysis_name=sorting_analysis_name,
            postpro_analysis_name=postpro_analysis_name,
            clear_preprocessed_data=clear_preprocessed_data,
            rerun_existing=rerun_existing,
            dry_run=dry_run,
        )
