# by convention our package is to be imported as dp (for Differential Privacy!)
import pydp as dp
from p ydp.algorithms.laplacian import BoundedSum, BoundedMean, Count, Max
import pandas as pd
import statistics  # for calculating mean without applying differential privacy

# get carrots data from our public github repo
url = "https://raw.githubusercontent.com/OpenMined/PyDP/dev/examples/Tutorial_1-carrots_demo/animals_and_carrots.csv"
df = pd.read_csv(url, sep=",", names=["animal", "carrots_eaten"])
df.head()


def mean_carrots() -> float:
    # calculates mean 
    # without applying differential privacy
    return statistics.mean(list(df["carrots_eaten"]))


def private_mean(privacy_budget: float) -> float:
    # calculates mean 
    # applying differential privacy
    x = BoundedMean(privacy_budget, 0, 1, 100)
    return x.quick_result(list(df["carrots_eaten"]))


print("Mean: ", mean_carrots())
print("Private Mean: ", private_mean(0.8))


def count_above(limit: int) -> int:
    # Calculates number of animals who ate more than "limit" carrots 
    # without applying differential privacy.
    return df[df.carrots_eaten > limit].count()[0]


def private_count_above(privacy_budget: float, limit: int) -> int:
    # Calculates number of animals who ate more than "limit" carrots 
    # applying differential privacy.
    x = Count(privacy_budget, dtype="int")
    return x.quick_result(list(df[df.carrots_eaten > limit]["carrots_eaten"]))


print("Above 70: " + str(count_above(70)))
print("private count above: " + str(private_count_above(1, 70)))


def max() -> int:
    # Function to return the maximum of the number of carrots eaten by any one animal 
    # without appyling differential privacy.
    return df.max()[1]


def private_max(privacy_budget: float) -> int:
    # Function to return the maximum of the number of carrots eaten by any one animal 
    # appyling differential privacy.
    # 0 and 150 are the upper and lower limits for the search bound.
    x = Max(epsilon=privacy_budget, lower_bound=0,
            upper_bound=100, dtype="int")
    return x.quick_result(list(df["carrots_eaten"]))


print("Max:\t" + str(max()))
print("private max:\t" + str(private_max(1)))


def sum_carrots() -> int:
    # Function to calculate sum of carrots eaten 
    # without applying differential privacy.
    return df.sum()[1]


def private_sum(privacy_budget: float) -> int:
    # Function to calculate sum of carrots eaten 
    # applying differential privacy.
    x = BoundedSum(epsilon=privacy_budget, delta=0,
                   lower_bound=1, upper_bound=100, dtype="float")
    return x.quick_result(list(df["carrots_eaten"]))


print("Sum:\t" + str(sum_carrots()))
print("Private Sum:\t" + str(private_sum(1)))
