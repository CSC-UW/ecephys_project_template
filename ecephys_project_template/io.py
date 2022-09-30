import pandas as pd
import wisc_ecephys_tools.spikesorting as wet_sorting
import wisc_ecephys_tools.hg as hg
from wisc_ecephys_tools.projects import get_alias_subject_directory

from .constants import (CLUSTER_GROUPS, PROJECT,
                    SELECTION_INTERVALS, SORTING_PROJECT,
                    STATE_COLORS)

# sorting

def load_single_probe_sorting(
    subject, experiment, alias, probe, region, 
    sorting_name=None,
    sorting_project=SORTING_PROJECT,
    cluster_groups=CLUSTER_GROUPS,
    selection_intervals=SELECTION_INTERVALS
):
    return wet_sorting.load_single_probe_sorting(
        subject,
        experiment,
        alias,
        probe,
        region=region,
        sorting_project=sorting_project,
        sorting_name=sorting_name,
        cluster_groups=cluster_groups,
        selection_intervals=selection_intervals
    )

## Hyp stuff

from .constants import STATE_COLORS

def load_hypnogram_as_generic_events(subject, experiment, alias):
    hyp = hg.load_hypnogram_as_generic_events(
        subject,
        experiment,
        alias,
    )
    return pd.DataFrame(hyp.loc[hyp['state'].isin(STATE_COLORS.keys())])


# PSTH stuff

def get_psth_dat_dir(
    subject,
    experiment,
    alias,
    project=PROJECT,
):
    return get_alias_subject_directory(
        project,
        experiment,
        alias,
        subject,
    )/'psth_data'


def get_psth_dat_filename(
    probe,
    region,
    hyp_state=None,
    off_size_interval=None,
    only_isolated_events=False,
    # extension='pkl'
):
    return f"psth_dat_{hyp_state}_{off_size_interval}_{only_isolated_events}.{probe}.{region}.pkl"

def get_psth_dat_path(
    subject,
    probe,
    region,
    hyp_state=None,
    off_size_interval=None,
    only_isolated_events=False,

):
    return get_psth_dat_dir(
        subject
    )/get_psth_dat_filename(
        probe,
        region,
        hyp_state=hyp_state,
        off_size_interval=off_size_interval,
        only_isolated_events=only_isolated_events,
    )


## ON OFF STUFF


def assign_hypnogram_state(hyp, off_df):
    off_df = off_df.copy()
    for _, bout in hyp.iterrows():
        off_df.loc[
            (off_df['start_time'].between(bout.start_time, bout.end_time)),
            'hyp_state'
        ] = bout.state
    for state, color in STATE_COLORS.items():
        nrows = sum(off_df["hyp_state"] == state)
        off_df.loc[
            (off_df['hyp_state'] == state),
            'color'
        ] = off_df.loc[
            (off_df['hyp_state'] == state)
        ].apply(lambda x: color, axis=1)  # Sorry ugly but other way doesnt work smh
        off_df.loc[
            (off_df['hyp_state'] == state),
            'hyp_state_total_time'
        ] = hyp[hyp['state'] == state].duration.sum()
    return off_df[off_df['hyp_state'].isin(hyp.state.unique())].reset_index(
        drop=True
    )


def load_off_df_as_generic_events(
        subject,
        experiment,
        alias,
        probe,
        region=None,
        hyp=None,
        detection_name=None,
        states=None,
    ):
        off_df_path = get_off_df_path(
            subject,
            experiment,
            alias,
            probe,
            region=region,
            states=states,
            detection_name=detection_name,
        )
        off_df = pd.read_pickle(off_df_path)
        off_df.loc[:, 't1'] = off_df.loc[:, 'start_time']
        off_df.loc[:, 't2'] = off_df.loc[:, 'end_time']
        off_df.loc[:, 'description'] = off_df.loc[:, 'state']

        if hyp is not None:
            off_df = assign_hypnogram_state(hyp, off_df)
            off_df.loc[:, 'description'] = off_df.loc[:, 'hyp_state']

        return off_df

def get_off_df_dir(
    subject,
    experiment,
    alias,
    project=PROJECT,
):
    return get_alias_subject_directory(
        project,
        experiment,
        alias,
        subject,
    )/'spatial_off_detection'


def get_off_df_filename(
    probe,
    region,
    states,
    detection_name,
    # extension='pkl'
):
    return f"off_df.states={states}.detection={detection_name}.{region}.{probe}.pkl"

def get_off_df_path(
    subject,
    experiment,
    alias,
    probe,
    region=None,
    project=PROJECT,
    states=None,
    detection_name=None,
):
    return get_off_df_dir(
        subject,
        experiment,
        alias,
        project=project,
    )/get_off_df_filename(
        probe,
        region,
        states=states,
        detection_name=detection_name
    )
