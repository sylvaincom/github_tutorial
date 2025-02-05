"""Assignment - using numpy and making a PR.

The goals of this assignment are:
    * Use numpy in practice with one easy exercise.
    * Submit a Pull-Request on github to practice `git`.

The function below is a skeleton function. The docstring explains what
are the inputs, the outputs and the expected error. Fill the function to
complete the assignment. The code should be able to pass the test that we
wrote. To run the tests, use `pytest test_numpy_question.py` at the root of
the repo. It should say that 1 test ran with success.
"""

import numpy as np


def max_index(X):
    """Return the index of the maximum in a numpy array.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        The input array.

    Returns
    -------
    (i, j) : tuple(int)
        The row and columnd index of the maximum.

    Raises
    ------
    ValueError
        If the input is not a numpy array or
        if the shape is not 2D.
    """
    i = 0
    j = 0

    # Validate input
    if not isinstance(X, np.ndarray):
        raise ValueError("Input must be a numpy array.")
    if X.ndim != 2:
        raise ValueError("Input must be a 2D numpy array.")
    
    # Find the index of the maximum value
    max_index_flat = np.argmax(X)  # Index in the flattened array
    i, j = divmod(max_index_flat, X.shape[1])  # Convert to 2D index
    
    return i, j
