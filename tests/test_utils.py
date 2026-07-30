import pytest
import numpy as np
import logging
from src.utils.helpers import set_seed, get_device, timer, ensure_dir, flatten_dict
from src.utils.logger import setup_logger
from src.evaluation.metrics import evaluate_classifier, evaluate_regressor

def test_set_seed():
    set_seed(42)
    val1 = np.random.rand()
    set_seed(42)
    val2 = np.random.rand()
    assert val1 == val2

def test_get_device():
    device = get_device()
    assert device in ["cpu", "cuda", "mps"]

def test_timer_decorator(capfd):
    @timer
    def dummy_func():
        return 42
    
    res = dummy_func()
    out, err = capfd.readouterr()
    assert res == 42
    assert "took" in out

def test_ensure_dir(tmp_path):
    d = tmp_path / "sub"
    ensure_dir(str(d))
    assert d.exists()
    assert d.is_dir()

def test_flatten_dict():
    d = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
    fd = flatten_dict(d)
    assert fd == {'a': 1, 'b_c': 2, 'b_d_e': 3}

def test_setup_logger(tmp_path):
    log_file = tmp_path / "test.log"
    logger = setup_logger("test", str(log_file))
    assert isinstance(logger, logging.Logger)
    assert logger.name == "test"
    assert log_file.exists()

def test_evaluate_classifier():
    y_true = [0, 1, 0, 1]
    y_pred = [0, 1, 0, 0]
    res = evaluate_classifier(y_true, y_pred)
    assert 'accuracy' in res.metrics
    assert res.metrics['accuracy'] == 0.75

def test_evaluate_regressor():
    y_true = [1.0, 2.0, 3.0]
    y_pred = [1.1, 1.9, 3.2]
    res = evaluate_regressor(y_true, y_pred)
    assert 'mse' in res.metrics
