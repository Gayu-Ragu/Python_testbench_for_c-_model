import pytest
import accel
import random
from testbench import reference, directed_stimulus, random_stimulus, run_test

# ---------- 1. Simple tests with assert ----------
def test_one_g():
    assert accel.read_accel(1.0) == 16384

def test_zero():
    assert accel.read_accel(0.0) == 0

def test_saturation():
    assert accel.read_accel(3.0) == 32767
    assert accel.read_accel(-3.0) == -32768

# ---------- 2. Tests that use our testbench ----------
def test_directed():
    sb = run_test("directed", directed_stimulus())
    assert sb.failed == 0

# @pytest.mark.parametrize("seed", [1, 2, 3, 4, 5])
#def test_random(seed):
    #sb = run_test(f"random seed={seed}", random_stimulus(10000, seed))
    #assert sb.failed == 0 

def test_random_seed():
    seed = random.randint(1,1000)
    sb = run_test(f"random seed={seed}", random_stimulus(1000,seed))
    assert sb.failed == 0, f"FAILED with seed={seed}" 
