import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
from simulation import simulate, find_peak_time, timeF

def epidemic_plotting():
    """
    Produce a three-panel line plot for different values of τ and k.
    """
    #style.use('seaborn-darkgrid')
    fig, ax = plt.subplots(1, 3, figsize=(20, 5))
    τList = [0.8, 0.4, 0.8]
    kList = [4, 4, 8]
    t = np.linspace(0, 120, 120)

    for i in range(3):
        # initial conditions
        S0 = 0.99
        I0 = 0.01
        R0 = 0
        X0 = (S0, I0, R0)

        τ, k = τList[i], kList[i]
        res = simulate(τ, k, X0, t)
        S, I, R = res.T
        tmax = find_peak_time(I, t)

        p = ax[i]
        p.plot(t[:tmax], S[:tmax], color='limegreen', linestyle='-', label='S', linewidth=2)
        p.plot(t[:tmax], I[:tmax], color='tomato', linestyle='--', label='I', linewidth=2)
        p.plot(t[:tmax], R[:tmax], color='royalblue', linestyle='-.', label='R', linewidth=2)

        p.set_xlabel('Time', fontsize=14)
        p.set_ylabel('Population Fraction', fontsize=14)
        p.set_xlim([0, t[tmax]])
        p.set_ylim([0, 1])
        p.set_title(f"Transmission Rate (τ) = {τ}, Recovery Time (k) = {k}", fontsize=16)
        p.text(30, 0.5, f"Peak Time ≈ {t[tmax]:.2f}", fontsize=14,
               bbox=dict(facecolor='white', alpha=0.5))
        p.legend(fontsize=12, loc='upper right')
    plt.show()

def epidemic_contourPlot(func):
    """
    Generate a contour plot showing the epidemic length (time until I < 0.0001)
    as a function of τ and k.

    Parameters:
      func: a function that takes meshgrids of τ and k and returns an array of times.
    """
    plt.clf()
    Tlist = np.linspace(0, 4, 40)  # 40 different values for τ
    klist = np.linspace(1, 5, 40)  # 40 different values for k
    Tlist, klist = np.meshgrid(Tlist, klist)

    t_val = func(Tlist, klist)
    levels = np.linspace(0, 240, 20)
    contour_filled = plt.contourf(Tlist, klist, t_val, levels=levels, cmap='jet')
    plt.xlabel('Transmission Rate (τ)', fontsize=14)
    plt.ylabel('Recovery Time (k)', fontsize=14)
    cbar = plt.colorbar(contour_filled)
    cbar.set_label('Time (t)', fontsize=12)
    plt.title('Epidemic Length: Combinations of τ and k', fontsize=16)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.show()
