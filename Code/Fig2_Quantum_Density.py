import numpy as np
import matplotlib.pyplot as plt

# Configuración
r = np.logspace(-2, 2, 500)  # Escala logarítmica desde 0.01 hasta 100 (en unidades de ℓ_Planck)
rho_quantum = 1e-5 * np.exp(-(r - 10)**2 / 2)  # Densidad cuántica (pico en r=10ℓ_p)
rho_classical = 0.1 / (r**3 + 1e-6)           # Densidad clásica (∝ 1/r³)

# Gráfico
plt.figure(figsize=(10, 6))
plt.loglog(r, rho_quantum, 'orange', label='Quantum Density $\\langle T_{\\mu\nu} \\rangle$', linewidth=2)
plt.loglog(r, rho_classical, 'blue', label='Classical Density $\\rho_{\\text{capsule}}$', linewidth=2)
plt.axvline(x=10, color='red', linestyle='--', label='$r = 10\\ell_{\\text{Planck}}$')
plt.xlabel('$r$ (en unidades de $\\ell_{\\text{Planck}}$)', fontsize=12)
plt.ylabel('Energy Density', fontsize=12)
plt.title('Quantum vs. Classical Energy Density', fontsize=14)
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('Fig2_Quantum_Density.png', dpi=300, bbox_inches='tight')
plt.show()