import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. FIXED BEAM PARAMETERS (LRFD SYSTEM)
# ==========================================
L = 120.0        # Total beam span length in inches (10 ft)
E = 29000.0      # Young's Modulus in ksi (FE Civil Standard)
Ix = 68.9        # Moment of Inertia for a W10x15 in in^4

# Factored LRFD Load magnitudes
wu = 0.50        # Factored rectangular uniform load (kips/in)
Pu = 16.0        # Factored concentrated point load (kips)

# Geometrical boundaries (inches)
rect_end = 60.0  # End of rectangular uniform load
point_loc = 90.0 # Point load placement

# ==========================================
# 2. STATIC EQUILIBRIUM & SUPPORT REACTIONS
# ==========================================
# Total resultant of the rectangular load acts at x = 30 inches
Rua = (45.0 * wu) + (0.25 * Pu)  # Left support factored force (kips)
Rub = (15.0 * wu) + (0.75 * Pu)  # Right support factored force (kips)

# ==========================================
# 3. GENERATE PIECEWISE ANALYSIS DATA
# ==========================================
# Create 1,000 sampling calculation points across the 120 inch span
x = np.linspace(0, L, 1000)

# Initialize arrays to store the results
V = np.zeros_like(x)
M = np.zeros_like(x)
y = np.zeros_like(x)

# Evaluate beam properties step-by-step using Macaulay/Singularity rules
for i, xi in enumerate(x):
    # --- Factored Shear Force V(x) ---
    term_w1 = xi if xi > 0 else 0
    term_w2 = (xi - rect_end) if xi > rect_end else 0
    term_P = 1.0 if xi > point_loc else 0
    V[i] = Rua - wu * term_w1 + wu * term_w2 - Pu * term_P
    
    # --- Factored Bending Moment M(x) ---
    term_M_w1 = (xi**2) if xi > 0 else 0
    term_M_w2 = ((xi - rect_end)**2) if xi > rect_end else 0
    term_M_P = (xi - point_loc) if xi > point_loc else 0
    M[i] = Rua * xi - (wu / 2.0) * term_M_w1 + (wu / 2.0) * term_M_w2 - Pu * term_M_P
    
    # --- Unfactored Elastic Deflection y(x) ---
    # Deflection checks must use service load conditions per NCEES rules
    w_service = wu / 1.2
    P_service = Pu / 1.6
    R_service = (45.0 * w_service) + (0.25 * P_service)
    
    mac_w1 = (xi**4) if xi > 0 else 0
    mac_w2 = ((xi - rect_end)**4) if xi > rect_end else 0
    mac_P = ((xi - point_loc)**3) if xi > point_loc else 0
    
    # Global integration equation derived from elastic boundary conditions
    EI_y = ((R_service / 6.0) * xi**3 - (w_service / 24.0) * mac_w1 
            + (w_service / 24.0) * mac_w2 - (P_service / 6.0) * mac_P - 22500.0 * xi)
    y[i] = EI_y / (E * Ix)

# ==========================================
# 4. PLOT STRUCTURAL PLOTS IN SPYDER
# ==========================================
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# Plot 1: Factored Shear Diagram
ax1.plot(x, V, color='crimson', lw=2)
ax1.fill_between(x, V, color='crimson', alpha=0.15)
ax1.axhline(0, color='black', lw=0.8, ls='--')
ax1.set_ylabel('Factored Shear V [kips]', fontweight='bold')
ax1.set_title('LRFD Rectangular Load Beam Design Profile (W10x15)', fontweight='bold', fontsize=12)
ax1.grid(True, ls=':')

# Plot 2: Factored Moment Diagram
ax2.plot(x, M, color='navy', lw=2)
ax2.fill_between(x, M, color='navy', alpha=0.15)
ax2.axhline(0, color='black', lw=0.8, ls='--')
ax2.set_ylabel('Factored Moment M [kip-in]', fontweight='bold')
ax2.grid(True, ls=':')

# Plot 3: Service Deflection Curve
ax3.plot(x, y, color='darkgreen', lw=2)
ax3.fill_between(x, y, color='darkgreen', alpha=0.15)
ax3.axhline(0, color='black', lw=0.8, ls='--')
ax3.set_xlabel('Beam Position x [inches]', fontweight='bold')
ax3.set_ylabel('Elastic Deflection y [in]', fontweight='bold')
ax3.grid(True, ls=':')

# Adjust layout and display in Spyder plot pane
plt.tight_layout()
plt.show()

# Print design values directly to the Spyder Console
print("============================================")
print("        LRFD DESIGN SUMMARY OUTPUT          ")
print("============================================")
print(f"Left Factored Support Force (Rua) : {Rua:.2f} kips")
print(f"Right Factored Support Force (Rub): {Rub:.2f} kips")
print(f"Maximum Factored Moment (Mu)      : {np.max(M):.2f} kip-in")
print("Worst-Case Downward Deflection    : {np.min(y):.3f} inches")
print("============================================")
