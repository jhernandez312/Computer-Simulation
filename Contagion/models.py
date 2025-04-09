import numpy as np

def derivative(X, t, τ, k):
    S, I, R = X
    dS = -τ * S * I
    dI = τ * S * I - I / k
    dR = I / k
    return np.array([dS, dI, dR])

def derivativeNew(X, t, τ, k):
    S, I, R, V = X
    v = 1 / (τ * k * 0.99)
    f = v * I * R / (I + R)
    dS = -τ * S * I - f
    dI = τ * S * I - I / k
    dR = I / k
    dV = f
    return np.array([dS, dI, dR, dV])
