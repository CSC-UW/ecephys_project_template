import ecephys.signal.event_locking as ece_events



def get_locked_spikes(
    sorting,
    event_df,
    on_duration=0.5
):
    assert all([c in event_df for c in ['state', 'start_time', 'end_time', 'duration']]), print(event_df.columns)
    assert hasattr(sorting, 'spikes')
    assert hasattr(sorting, 'units')
    assert all([c in sorting.spikes for c in ['cluster_id', 't']]), print(sorting.spikes.columns)

    return ece_events.get_locked_df(
        sorting.spikes,
        event_df.start_time.values,
        window=(0, on_duration),
        time_colname='t',
        trim='end',
        drop_out_of_window_datapoints=True,
    )


# TODO: Here we assumed that all the events have at least 1 spike
def get_event_firing_rates_df(
    sorting,
    event_df,
    on_duration=1
):
    """Cluster firing rate (raw and zscore) for each event."""

    locked_spikes = get_locked_spikes(
        sorting,
        event_df,
        on_duration=on_duration,
    )

    event_rates_df = ece_events.get_event_firing_rates_df(locked_spikes)

    # Mean/std/zscore
    event_rates_df['event_firing_rate_mean'] = event_rates_df.groupby('cluster_id')['event_firing_rate'].transform('mean')
    event_rates_df['event_firing_rate_std'] = event_rates_df.groupby('cluster_id')['event_firing_rate'].transform('std')
    event_rates_df['event_firing_rate_zscore'] = (
            event_rates_df['event_firing_rate'] - event_rates_df['event_firing_rate_mean']
        ) / event_rates_df['event_firing_rate_std'].replace({0: float('Inf')})  # 0 if cluster STD is 0
    event_rates_df['event_firing_rate_norm'] = event_rates_df['event_firing_rate'] / event_rates_df['event_firing_rate_std'].replace({0: float('Inf')})

    return event_rates_df