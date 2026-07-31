import numpy as np
import matplotlib.pyplot as plt

# --- 1. STRUCTURAL PARAMETERS ---
L = 10.0      # Length of the beam (meters)
w = 15.0      # Uniformly distributed load (kN/m)

# --- 2. CALCULATIONS ---
R_A = R_B = (w * L) / 2      # Support reactions at ends
M_max = (w * (L**2)) / 8     # Maximum bending moment at mid-span
V_max = R_A                  # Maximum shear force occurs at the supports

print("--- ADVANCED ANALYSIS OUTPUT ---")
print(f"Left Support Reaction (R_A):  {R_A:.2f} kN")
print(f"Right Support Reaction (R_B): {R_B:.2f} kN")
print(f"Maximum Shear Force (V_max):  {V_max:.2f} kN")
print(f"Max Bending Moment (M_max):   {M_max:.2f} kNm")

# --- 3. GENERATE DIAGRAM DATA ---
x = np.linspace(0, L, 100)   # 100 points along the beam for smooth lines

# Shear Force Equation: V = R_A - (w * x)
V = R_A - (w * x)

# Bending Moment Equation: M = (w*L*x/2) - (w*x^2/2)
M = (w * L * x / 2) - (0.5 * w * x**2)

# --- 4. GRAPH THE DIAGRAMS (SFD & BMD) ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# Top Plot: Shear Force Diagram (SFD)
ax1.plot(x, V, 'b-', linewidth=2.5, label='Shear (V)')
ax1.fill_between(x, V, color='blue', alpha=0.1)
ax1.axhline(0, color='black', linewidth=1)
ax1.set_title('Shear Force Diagram (SFD)', fontsize=11, fontweight='bold')
ax1.set_ylabel('Shear Force (kN)', fontsize=9)
ax1.grid(True, linestyle='--', alpha=0.5)

# Bottom Plot: Bending Moment Diagram (BMD)
ax2.plot(x, M, 'r-', linewidth=2.5, label='Moment (M)')
ax2.fill_between(x, M, color='red', alpha=0.1)
ax2.axhline(0, color='black', linewidth=1)
ax2.set_title('Bending Moment Diagram (BMD)', fontsize=11, fontweight='bold')
ax2.set_xlabel('Beam Length (meters)', fontsize=9)
ax2.set_ylabel('Moment (kNm)', fontsize=9)
ax2.grid(True, linestyle='--', alpha=0.5)
#ax2.invert_yaxis()  # Standard civil engineering convention (positive downward)

plt.tight_layout()
plt.show()
# --- 5. ELASTIC DEFLECTION VERIFICATION ---
# Using the properties matching your MASTAN2 metric model
E_mod = 200000.0  # Modulus of Elasticity
I_val = 0.0001    # Moment of Inertia (Izz)
w_metric = 15.0   # Load (kN/m)
L_metric = 10.0   # Length (meters)

# Calculate max deflection at mid-span (meters)
delta_max = (5 * w_metric * (L_metric**4)) / (384 * E_mod * I_val)

print("\n--- DEFLECTION VERIFICATION ---")
print(f"Python Mid-Span Deflection: {delta_max:.5f} meters")
import handcalcs.render

# Add this rendering block to isolate your hand calculations
w = 15.0       # kN/m
L = 10.0       # meters
R_A = (w * L) / 2
M_max = (w * L**2) / 8
# --- AUTOMATED PDF GENERATOR ---
# --- AUTOMATED PORTFOLIO IMAGE GENERATOR ---
import os
import matplotlib.pyplot as plt

# Define path directly into your master folder layout
img_path = os.path.expanduser("~/Desktop/Structural_Verification/automated_calculations.png")

# Create a clean canvas for text reporting
fig, ax = plt.subplots(figsize=(6, 5))
ax.axis('off')  # Hide graph axes

# Draw the engineering report layout text
ax.text(0.05, 0.90, "STRUCTURAL HAND CALCULATIONS (AUTOMATED)", fontsize=12, fontweight='bold', color='#2c3e50')
ax.text(0.05, 0.80, f"Uniform Distributed Load (w) = {w} kN/m", fontsize=11)
ax.text(0.05, 0.73, f"Beam Length (L) = {L} meters", fontsize=11)

ax.text(0.05, 0.58, "1. Support Reaction Force (R_A):", fontsize=11, fontweight='bold')
ax.text(0.05, 0.50, f"Formula: R_A = (w * L) / 2", fontsize=10, style='italic')
ax.text(0.05, 0.42, f"R_A = ({w} * {L}) / 2 = {R_A:.2f} kN", fontsize=11, color='#e74c3c', fontweight='bold')

ax.text(0.05, 0.28, "2. Maximum Bending Moment (M_max):", fontsize=11, fontweight='bold')
ax.text(0.05, 0.20, f"Formula: M_max = (w * L^2) / 8", fontsize=10, style='italic')
ax.text(0.05, 0.12, f"M_max = ({w} * {L}^2) / 8 = {M_max:.2f} kNm", fontsize=11, color='#e74c3c', fontweight='bold')

# Save as a clean portfolio image card
plt.savefig(img_path, dpi=200, bbox_inches='tight')
plt.close()

print("\n[SUCCESS] automated_calculations.png successfully generated inside your project folder!")
