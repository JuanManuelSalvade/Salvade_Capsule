import numpy as np
import matplotlib.pyplot as plt

# Datos simulados (frecuencias QNM para ℓ=2)
omega_kerr = np.array([0.5, 0.8, 1.2])  # Frecuencias de Kerr (arbitrarias)
omega_salvade = omega_kerr * 1.001       # Frecuencias de Salvadé (0.1% shift)

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(omega_kerr, [1, 1.5, 2], 'k-', label='Kerr QNMs', marker='o', linewidth=2)
plt.plot(omega_salvade, [1, 1.5, 2], 'r--', label='Salvadé QNMs', marker='s', linewidth=2)
plt.fill_betweenx([1, 2], omega_kerr[0], omega_salvade[0], color='yellow', alpha=0.3, label='$\\Delta \\omega \\approx 0.1\\%$')
plt.xlabel('Frequency (Re[$\\omega$])', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.title('Quasinormal Mode Spectra: Kerr vs. Salvadé', fontsize=14)
plt.legend()
plt.grid(True)
plt.savefig('Fig4_QNM_Spectra.png', dpi=300, bbox_inches='tight')
plt.show()