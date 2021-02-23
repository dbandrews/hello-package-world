import pandas as pd
import matplotlib.pyplot as plt


def better_hist(df, **kwargs):
    """
    Generate a more presentation ready version of a histogram of each column in a Pandas DataFrame

    Parameters
    ----------
    df : pandas.DataFrame
        Pandas dataframe to histogram each column by with improved formatting
    **kwargs : 
        Arguments passed onto pandas.DataFrame.hist()

    Returns
    -------
    None : 
        Plot is displayed as side effect

    Examples
    --------
    >>> import pandas as pd
    >>> import numpy as np
    >>> from hello_package_world import hello_package_world
    >>> hello_package_world.better_hist(pd.DataFrame(np.random.randint(0,100,siz=(100,10))))
    """
    plt.style.use("seaborn")

    return df.hist(**kwargs)

