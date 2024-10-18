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

    # TODO
    if not(isinstance(X,np.ndarray)):
        raise ValueError ("le parametre n'est pas un array")
    
    np.unravel_index(np.argmax(X), X.shape)
    
    return i, j

