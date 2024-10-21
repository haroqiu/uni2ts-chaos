from ._base import ChaosDatasetBuilder
from uni2ts.data.dataset import TimeSeriesDataset
from collections import defaultdict
from functools import partial
import os

class ChaosTinyDatasetBuilder(ChaosDatasetBuilder):
    dataset_list = [
        "chaos_tiny",
    ]
    dataset_type_map = defaultdict(lambda: TimeSeriesDataset)
    dataset_load_func_map = defaultdict(lambda: partial(TimeSeriesDataset))

    def build_dataset(self, dataset: str, num_proc: int = os.cpu_count()):
        # This function will never be allocated
        raise NotImplementedError("This function will never be allocated")