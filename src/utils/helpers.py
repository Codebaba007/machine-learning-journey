import random
import numpy as np
import os
from pathlib import Path
from typing import Dict, Any
import time
from functools import wraps

def set_seed(seed: int = 42) -> None:
    """Set random seed for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
    except ImportError:
        pass

def get_device() -> str:
    """Return cuda/mps/cpu."""
    try:
        import torch
        if torch.cuda.is_available():
            return "cuda"
        elif torch.backends.mps.is_available():
            return "mps"
        return "cpu"
    except ImportError:
        return "cpu"

def timer(func):
    """Measure function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

def memory_usage() -> str:
    """Report current memory usage."""
    import psutil
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (1024 ** 2)
    return f"Memory usage: {mem:.2f} MB"

def ensure_dir(path: str) -> None:
    """Create directory if not exists."""
    Path(path).mkdir(parents=True, exist_ok=True)

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten nested dict."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
