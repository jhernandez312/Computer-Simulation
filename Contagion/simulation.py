import numpy as np
from scipy import integrate
from models import derivative

def simulate(τ, k, X0, t):
    """
    Simulate the epidemic model using the ODE defined in models.py.
    """
    res = integrate.odeint(derivative, X0, t, args=(τ, k))
    return res

def find_peak_time(I, t):
    """
    Find the index where I(t) drops below 0.0001.
    """
    tmax = 0
    for j, val in enumerate(I):
        if val < 0.0001:
            tmax = j
            break
    return tmax

def timeF(X, Y):
    """
    For each pair of τ and k values provided in the meshgrids X and Y,
    simulate the epidemic and record the first time index when I < 0.0001.

    Parameters:
      X: 2D array of transmission rates τ.
      Y: 2D array of recovery times k.

    Returns:
      A 40x40 array of time indices.
    """
    t = np.linspace(0, 240, 240)
    arr = np.zeros((40, 40))
    S0 = 0.99
    I0 = 0.01
    R0 = 0
    X0 = (S0, I0, R0)

    for i in range(40):
        for j in range(40):
            τ = X[i][j]
            k = Y[i][j]
            res = integrate.odeint(derivative, X0, t, args=(τ, k))
            S, I, R = res.T
            for f, val in enumerate(I):
                if val < 0.0001:
                    arr[i][j] = f
                    break
    return arr
