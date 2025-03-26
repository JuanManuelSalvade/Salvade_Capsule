import numpy as np
import matplotlib.pyplot as plt

# Configuración
r = np.linspace(0, 10, 1000)
mu = 0.5  # Compactness parameter

# Cálculo de componentes métricos
g_tt = 1 - (2 * mu * np.exp(-r**2 / 2)) / (r + 1e-6)  # Evita división por cero
g_phiphi = r**2 * (1 - 0.3 * np.exp(-r**2 / 2))

# Plot
plt.figure(figsize=(8, 6))
plt.plot(r, g_tt, 'b', label='$g_{tt}(r)$', linewidth=2)
plt.plot(r, g_phiphi, 'r', label='$g_{\phi\phi}(r)$', linewidth=2)
plt.fill_between(r, g_phiphi, where=(g_phiphi < 0), color='red', alpha=0.3, label='CTC Region')
plt.xlabel('$r$ (GM/c²)', fontsize=12)
plt.ylabel('Metric Components', fontsize=12)
plt.title('Gaussian Metric Profiles', fontsize=14)
plt.legend()
plt.grid(True)
plt.savefig('Fig1_Metric_Profiles.png', dpi=300, bbox_inches='tight')
plt.show()