import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

@dataclass
class ProjectConfig:
    project_name: str = os.getenv("PROJECT_NAME", "machine-learning-journey")
    data_dir: Path = Path(os.getenv("DATA_DIR", "datasets"))
    model_dir: Path = Path(os.getenv("MODEL_DIR", "models"))
    log_dir: Path = Path(os.getenv("LOG_DIR", "logs"))
    random_seed: int = int(os.getenv("RANDOM_SEED", 42))
    device: str = os.getenv("DEVICE", "cpu")

_config_instance = None

def get_config() -> ProjectConfig:
    global _config_instance
    if _config_instance is None:
        _config_instance = ProjectConfig()
    return _config_instance
