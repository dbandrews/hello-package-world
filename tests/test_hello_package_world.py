from hello_package_world import __version__
from hello_package_world import hello_package_world
import pandas as pd
import numpy as np


def test_version():
    assert __version__ == "0.1.0"


def test_better_hist():
    assert (
        hello_package_world.better_hist(
            pd.DataFrame(np.random.randint(0, 100, size=(100, 10)))
        )
    ).shape == (4, 3)

