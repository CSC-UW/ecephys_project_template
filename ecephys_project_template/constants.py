from pathlib import Path
from ecephys.plot import state_colors
import os

PACKAGE_DIRECTORY = Path(os.path.abspath(__file__)).parent
PARAMS_DIRECTORY = Path(PACKAGE_DIRECTORY)/"params"

PROJECT = "ecephys_project_template"
SORTING_PROJECT = "ecephys_project_template"

CLUSTER_GROUPS = ['unsorted', 'good', 'mua']
SELECTION_INTERVALS = {
    'fr': (-float('Inf'), float('Inf')),
}

STATES = [
    "Wake", "qWk", "aWk", "W", "N2", "NREM", "REM",
]
STATE_COLORS = {
    state: color
    for state, color in state_colors.items()
    if state in STATES
}