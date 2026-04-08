from pathlib import Path
import pandas as pd
DATASET_PATH = Path(__file__).resolve().parent.parent / "data" / "IMDb_Dataset.csv"
REQUIRED_COLUMNS = ["Title", "IMDb Rating", "Year", "Genre"]
_dataset = None

def load_dataset(force_reload: bool = False):
    """Load the dataset once and cache it for API usage."""
    global _dataset
    if _dataset is None or force_reload:
        if not DATASET_PATH.exists():
            raise FileNotFoundError(f"Dataset not found: {DATASET_PATH}")
        dataframe = pd.read_csv(DATASET_PATH)
        missing_columns = [col for col in REQUIRED_COLUMNS if col not in dataframe.columns]
        if missing_columns:
            raise ValueError(
                "Dataset is missing required columns: " + ", ".join(missing_columns)
            )
        _dataset = dataframe
    return _dataset
def get_dataset():
    """Return the cached dataset, loading it on first access."""
    if _dataset is None:
        return load_dataset()
    return _dataset
