import pandas as pd
import matplotlib.pyplot as plt


def better_hist(df, **kwargs):
    """Generate a more presentation ready version of a histogram of each column in a Pandas DataFrame

    Parameters
    ----------
    df : pandas.DataFrame
        Pandas dataframe to histogram each column by with improved formatting
    **kwargs : 
        Arguments passed onto pandas.DataFrame.hist()

    """
    plt.style.use("seaborn")

    df.hist(**kwargs)

