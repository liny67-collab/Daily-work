import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def multi_slit_intensity(x, N, a, d, wavelength, D, I0=1.0):
    """
    General formula for N-slit diffraction intensity distribution:
    I = I0 * (sin(N * beta) / sin(beta))^2 * (sin(alpha) / alpha)^2
    """
    sin_theta = x / np.sqrt(x**2 + D**2)
    
    # 1. Single-slit diffraction envelope term: (sin(alpha) / alpha)^2
    alpha = (np.pi * a * sin_theta) / wavelength
    diffraction = np.ones_like(alpha)
    mask_a = ~np.isclose(alpha, 0, atol=1e-12)
    diffraction[mask_a] = (np.sin(alpha[mask_a]) / alpha[mask_a])**2
    
    # 2. Multi-slit interference term: (sin(N * beta) / sin(beta))^2
    if N == 1:
        interference = np.ones_like(alpha)
    else:
        beta = (np.pi * d * sin_theta) / wavelength
        interference = np.zeros_like(beta)
        # Principal maxima occur when sin(beta) = 0, limit is N^2
        mask_b = np.isclose(np.sin(beta), 0, atol=1e-10)
        interference[mask_b] = N**2
        interference[~mask_b] = (np.sin(N * beta[~mask_b]) / np.sin(beta[~mask_b]))**2
        
    return I0 * interference * diffraction

def plot_diffraction(N=2, wavelength=632.8e-9, a=0.1e-3, d=0.5e-3, D=1.0, I0=1.0):
    """
    Plots the theoretical intensity curve and simulated fringe pattern for any N slits.
    Default parameters match the experimental setup in the paper.
    """
    x = np.linspace(-0.015, 0.015, 3000)  # Screen range: -15 mm to +15 mm
    I = multi_slit_intensity(x, N, a, d, wavelength, D, I0)
    
    fig = plt.figure(figsize=(10, 5))
    gs = gridspec.GridSpec(2, 1, height_ratios=[4, 0.6], hspace=0.15)
    
    # Top: Theoretical Intensity Distribution Curve
    ax1 = fig.add_subplot(gs[0])
    ax1.plot(x * 1000, I, color='#1f77b4', linewidth=1.8, label=f'N = {N} Slits')
    ax1.set_title(f"Multi-Slit Diffraction Pattern (N = {N})", fontsize=13, fontweight='bold')
    ax1.set_ylabel("Relative Intensity", fontsize=11)
    ax1.set_xlim(-15, 15)
    ax1.set_ylim(-0.05 * (N**2 * I0), 1.1 * (N**2 * I0))
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.axvline(0, color='gray', linewidth=0.8, alpha=0.7)
    ax1.legend(loc='upper right')
    ax1.set_xticks([])
    
    # Bottom: Simulated Optical Fringe Pattern
    ax2 = fig.add_subplot(gs[1])
    # Gamma correction (0.4) to make secondary fringes visually clear
    fringe_visual = np.power(I / np.max(I), 0.4)
    ax2.imshow(fringe_visual[np.newaxis, :], aspect='auto', cmap='gray', extent=[-15, 15, 0, 1])
    ax2.set_yticks([])
    ax2.set_xlabel("Position on Screen x (mm)", fontsize=11)
    
    filename = f"diffraction_N{N}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Plot saved successfully as '{filename}'")
    plt.show()

if __name__ == "__main__":
    print("=== General Multi-Slit Diffraction Simulator ===")
    try:
        user_n = int(input("Enter the number of slits N (e.g., 1, 2, 3, 4, 20): "))
        if user_n < 1:
            raise ValueError
    except ValueError:
        print("Invalid input. Defaulting to N = 2 (Double-Slit).")
        user_n = 2
        
    # Run simulation with default paper parameters (wavelength=632.8nm, a=0.1mm, d=0.5mm, D=1.0m)
    plot_diffraction(N=user_n)
