import numpy as np

def normalize(a: np.ndarray, is_test: bool = False) -> np.ndarray:
    """
    Normalize the input array to the range [-0.5, 0.5]
    :param a: Input array
    :return: Normalized array
    """
    if is_test:
        return a - 1
    return (a / 9) - 0.5

def denormalize(a: np.ndarray) -> np.ndarray:
    """
    Denormalize the input array to the range [0, 9],
    centered around around 0 to the range [-0.5, 0.5]
    :param a: Input array
    :return: Denormalized array
    """
    return (a + 0.5) * 9