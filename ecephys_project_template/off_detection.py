import pandas as pd
from on_off_detection import SpatialOffModel
from wisc_ecephys_tools.hg import load_and_concatenate_alias_second_hypnograms

from . import io
from .constants import PROJECT
from .params import get_analysis_params

"""
Detect ON/OFF periods and save on_off_df csv file in alias_subject_dir
"""


DETECTION_NAME = "spatial_off_hmmem_df"
N_JOBS = 100


# def select_on_states(on_off_df, min_off_duration=0):
#     """Select ONs directly preceded by (long enough) OFFs"""
#     on_df = on_off_df.copy()
#     assert np.all(on_off_df['start_time'].values == np.sort(on_off_df['start_time'].values)) # Sorted start times
#     selected_idx = np.empty((len(on_df),), dtype=bool)
#     for i in range(len(on_df)):
#         row = on_df.iloc[i, :]
#         preceding_row = on_df.iloc[i-1, :]
#         selected_idx[i] = (
#             (i > 0)
#             & (row['state'] == 'on')  # On state...
#             & (row['start_time'] == preceding_row['end_time'])  # ...Just following an off state...
#             & (preceding_row['duration'] >= min_off_duration)   # ...That is long enough
#         )
#     return on_df[selected_idx].copy()


def run_spatial_off_detection(
    subject,
    experiment,
    alias,
    probe,
    region=None,
    sorting_name=None,
    detection_name=DETECTION_NAME,
    sorting_project=PROJECT,
    states=None,
):
    """Run on-off periods detection."""
    kwargs = locals()
    print("Run off detection:", kwargs)

    # Detection condition
    p = get_analysis_params(
        'spatial_off_detection',
        detection_name,
    )
    on_off_method = p['method']
    on_off_params = p['on_off_params']
    spatial_params = p['spatial_params']

    # Spike trains
    sorting = io.load_single_probe_sorting(
        subject,
        experiment,
        alias,
        probe,
        sorting_name=sorting_name,
        region=region,
        sorting_project=sorting_project,
    )
    trains = sorting.spikes.spikes.as_trains()
    # Add "depth" column to trains
    trains = pd.merge(trains, sorting.units, left_index=True, right_index=True)

    trains_list = trains.t.values
    cluster_depths = trains.depth.values
    cluster_ids = trains.index
    Tmax = None

    # Load hyp
    if states not in (None, "all"):
        hyp = load_and_concatenate_alias_second_hypnograms(
            subject,
            experiment,
            alias,
        )
        print(f"Hypnogram: {hyp.groupby('state').duration.sum()}")
        bouts_df = hyp[hyp['state'].isin(states)]
        print(f"Subselect N={len(bouts_df)} bouts, total duration={bouts_df.duration.sum()}sec")
    else:
        bouts_df=None

    # Compute
    spatial_off_model = SpatialOffModel(
        trains_list,
        cluster_depths,
        Tmax,
        cluster_ids=cluster_ids,
        on_off_method=on_off_method,
        on_off_params=on_off_params,
        spatial_params=spatial_params,
        bouts_df=bouts_df,
        n_jobs=N_JOBS,
    )
    print(spatial_off_model.windows_df)
    off_df = spatial_off_model.run()

    # Save
    off_df_path = io.get_off_df_path(
        subject,
        experiment,
        alias,
        probe,
        region=region,
        states=states,
        detection_name=detection_name,
    )
    print(f"Save off_df at {off_df_path}")
    off_df_path.parent.mkdir(parents=True, exist_ok=True)
    off_df.to_pickle(off_df_path)

    return off_df
