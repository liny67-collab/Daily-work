# Multi-Slit Diffraction Simulation

## 📐 Physics Principles & Formulas
This project provides a general Python simulation of the optical diffraction and interference patterns produced by monochromatic light passing through $N$ parallel slits.

* **General Intensity Distribution Formula**:
  $$I(\theta) = I_0 \left(\frac{\sin(N\beta)}{\sin\beta}\right)^2 \left(\frac{\sin\alpha}{\alpha}\right)^2$$

* **Phase Parameters**:
  $$\alpha = \frac{\pi a \sin\theta}{\lambda}, \quad \beta = \frac{\pi d \sin\theta}{\lambda}$$

* **Principal Maxima Intensity**:
  $$I_{\text{max}} = N^2 I_0$$

*(Note: $N$ is the number of slits, $\lambda$ is the laser wavelength, $a$ is the slit width, $d$ is the slit separation, and $I_0$ is the initial central maximum intensity.)*

## ⚙️ Default Simulation Parameters
The default parameters in the script are configured based on standard optical experimental setups:
* **Wavelength ($\lambda$)**: $632.8\text{ nm}$
* **Slit Width ($a$)**: $0.1\text{ mm}$
* **Slit Separation ($d$)**: $0.5\text{ mm}$
* **Screen Distance ($D$)**: $1.0\text{ m}$

## 📊 Output Sample
*(When you run the script for a specific $N$, it automatically generates and saves a plot named `diffraction_N{N}.png`, e.g., `diffraction_N2.png` or `diffraction_N4.png`.)*

![Diffraction Pattern](./diffraction_N2.png)

## 🚀 How to Run

1. **Install the required libraries** (use `pip3` if you are on macOS/Linux):
   ```bash
   pip install -r requirements.txt
   # or
   pip3 install -r requirements.txt
