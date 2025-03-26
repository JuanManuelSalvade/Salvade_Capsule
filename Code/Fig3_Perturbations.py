import numpy as np
import matplotlib.pyplot as plt

# Configuración
t = np.linspace(0, 10, 100)
h_m1 = np.exp(-0.5 * t) * np.cos(t)  # Modo estable (m=1)
h_m2 = np.exp(0.1 * t) * np.cos(t)   # Modo inestable (m=2)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(t, h_m1, 'g', label='m=1 (Stable)', linewidth=2)
plt.plot(t, h_m2, 'r', label='m=2 (Unstable)', linewidth=2)
plt.xlabel('Time', fontsize=12)
plt.ylabel('$h_{\phi\phi}$', fontsize=12)
plt.title('Perturbation Evolution', fontsize=14)
plt.legend()
plt.grid(True)
plt.savefig('Fig3_Perturbations.png', dpi=300, bbox_inches='tight')
plt.show()