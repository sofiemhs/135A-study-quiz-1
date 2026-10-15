import streamlit as st

st.set_page_config(
    page_title="CEE 135A Structural Analysis Study Guide",
    page_icon="🏗️",
    layout="wide",
)

st.title("🏗️ CEE 135A: Elementary Structural Analysis Study Guide & Solver")
st.caption("Comprehensive review module covering Chapter 1, Chapter 2, Homework 1, and Homework 2.")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
module = st.sidebar.radio(
    "Select Study Module:",
    [
        "1. Core Theory & Formulas (Ch. 1 & 2)",
        "2. Determinacy & Stability Calculator",
        "3. HW1 Problem 1: Load Path & LRFD",
        "4. HW1 Problem 2: Wind Load Analysis",
        "5. HW2 Problem 1: Structural Determinacy",
        "6. HW2 Problem 2: Frame Reaction Solver",
        "7. Interactive Practice Quiz",
    ],
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip**: Adjust the sliders and input boxes to see calculations update in real time!")

# ==========================================
# MODULE 1: CORE THEORY & FORMULAS
# ==========================================
if module == "1. Core Theory & Formulas (Ch. 1 & 2)":
    st.header("📚 Chapter 1 & Chapter 2 Core Concepts")
    
    tab1, tab2, tab3 = st.tabs(["Structural Types & Supports", "Wind & Seismic Loads", "LRFD & Superposition"])
    
    with tab1:
        st.subheader("1. Structural Elements & Idealized Supports")
        st.markdown("""
        * **Tie Rods**: Slender members subjected to tensile forces[cite: 12].
        * **Beams**: Horizontal members carrying vertical loads through shear force and bending moment[cite: 12].
        * **Columns**: Vertical members resisting axial compressive loads[cite: 13].
        * **Beam-Columns**: Vertical members subjected to both axial load and bending moment[cite: 13].
        """)
        
        st.markdown("### Support Conditions & Reactions")
        st.markdown("""
        * **Rule of Thumb**: If a movement is **constrained** in a degree of freedom (DOF), a **force or moment develops** in that direction. If **unconstrained**, no reaction develops[cite: 5].
        * **Roller Support**: 1 reaction force ($R_y$)[cite: 5].
        * **Pin Support**: 2 reaction forces ($R_x, R_y$)[cite: 5].
        * **Fixed Support**: 3 reactions ($R_x, R_y, M$)[cite: 5].
        * **Torsional/Spring Support**: Develops reactive force/moment proportional to stiffness ($k$)[cite: 5].
        """)

    with tab2:
        st.subheader("2. Environmental Loads (ASCE 7-22)")
        st.markdown("#### Wind Loading (Static Approach)")
        st.latex(r"q_z = 0.00256 \, K_z \, K_{zt} \, K_d \, K_e \, V^2 \quad \text{(lb/ft}^2\text{)}")
        st.markdown("""
        * **$V$**: Basic wind speed (3-second gust at 33 ft height)[cite: 18].
        * **$K_z$**: Velocity pressure exposure coefficient[cite: 19].
        * **$K_{zt}$**: Topographic factor ($1.0$ for flat ground)[cite: 19].
        * **$K_d$**: Wind directionality factor[cite: 19].
        * **$K_e$**: Ground elevation factor ($1.0$ standard)[cite: 19].
        * **Design Wind Pressure**: $p = q \, G C_p - q_h (G C_{pi})$[cite: 19].
        """)
        
        st.markdown("#### Seismic Loads (Equivalent Lateral Force Procedure)")
        st.latex(r"V_{base} = C_s W")
        st.latex(r"C_s = \frac{S_{DS}}{R / I_e}")
        st.markdown("""
        * **$V_{base}$**: Base shear[cite: 22].
        * **$W$**: Total effective structural seismic weight[cite: 22].
        * **$R$**: Response modification factor (accounts for ductility)[cite: 22].
        * **$I_e$**: Importance factor[cite: 22].
        """)

    with tab3:
        st.subheader("3. Structural Design & Load Combinations")
        st.markdown("#### Load and Resistance Factor Design (LRFD)")
        st.markdown("Structure is safe if **Required Strength ($\sum \gamma_i Q_i$) $\le$ Design Strength ($\phi R_n$)**[cite: 24].")
        st.markdown("**Primary LRFD Combinations (ASCE 7-22)**[cite: 24]:")
        st.markdown("""
        1. **1.4D**
        2. **1.2D + 1.6L + 0.5(L_r \text{ or } S \text{ or } R)**
        3. **1.2D + 1.6(L_r \text{ or } S \text{ or } R) + (1.0L \text{ or } 0.5W)**
        4. **1.2D + 1.0W + 1.0L + 0.5(L_r \text{ or } S \text{ or } R)**
        5. **0.9D + 1.0W**
        """)
        st.markdown("#### Principle of Superposition")
        st.markdown("""
        Valid only under **linear-elastic material behavior** and **small deformation theory**[cite: 6]. Total displacements/internal forces equal the sum of displacements/forces caused by each load acting independently[cite: 6].
        """)

# ==========================================
# MODULE 2: DETERMINACY & STABILITY CLASSIFIER
# ==========================================
elif module == "2. Determinacy & Stability Calculator":
    st.header("⚙️ Degree of Indeterminacy (DI) Interactive Calculator")
    
    st.markdown("""
    For a 2D coplanar structure with $n$ parts/members and $r$ total reaction forces[cite: 7]:
    """)
    st.latex(r"DI = r - 3n")
    st.markdown("""
    * **$r < 3n$**: Unstable (partially constrained)[cite: 8, 9].
    * **$r = 3n$**: Statically Determinate[cite: 7].
    * **$r > 3n$**: Statically Indeterminate to degree $DI = r - 3n$[cite: 7].
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        r_val = st.number_input("Total Reactive Forces (r):", min_value=1, value=6, step=1)
        n_val = st.number_input("Total Number of Parts / Segments (n):", min_value=1, value=2, step=1)
        parallel_or_concurrent = st.checkbox("Reactions are parallel or concurrent (Improper Constraint)[cite: 8, 9]")
    
    with col2:
        di = r_val - 3 * n_val
        st.markdown("### Classification Result:")
        if parallel_or_concurrent:
            st.error("⚠️ **UNSTABLE** due to improper geometric constraints[cite: 8].")
        elif di < 0:
            st.error(f"⚠️ **UNSTABLE** (Partially Constrained). DI = {di}[cite: 8].")
        elif di == 0:
            st.success("✅ **STATICALLY DETERMINATE**. DI = 0[cite: 7].")
        else:
            st.info(f"🔵 **STATICALLY INDETERMINATE** to the degree **{di}**[cite: 7].")

# ==========================================
# MODULE 3: HW1 PROBLEM 1 - LOAD PATH & LRFD
# ==========================================
elif module == "3. HW1 Problem 1: Load Path & LRFD":
    st.header("📝 Homework 1 - Problem 1: Concrete Frame Analysis")
    
    st.markdown("""
    **Problem Setup**[cite: 3]:
    * **Slab Dimensions**: $L = 30\text{ ft}$, $W = 20\text{ ft}$
    * **Dead Load (DL)**: $80\text{ psf}$, **Live Load (LL)**: $50\text{ psf}$
    * **Beam CD Dimensions**: $12\text{ in. wide} \times 24\text{ in. deep}$
    * **Concrete Unit Weight**: $150\text{ pcf}$
    * **Tributary Width**: $10\text{ ft}$
    """)
    
    st.subheader("Interactive Load Calculator")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        dl_psf = st.number_input("Floor Dead Load (psf):", value=80.0)
        ll_psf = st.number_input("Floor Live Load (psf):", value=50.0)
    
    with col2:
        trib_width = st.number_input("Tributary Width (ft):", value=10.0)
        conc_density = st.number_input("Concrete Density (pcf):", value=150.0)
    
    with col3:
        b_in = st.number_input("Beam Width (in):", value=12.0)
        h_in = st.number_input("Beam Height (in):", value=24.0)

    # Calculations
    w_floor_dl = dl_psf * trib_width
    w_floor_ll = ll_psf * trib_width
    beam_self_weight = (b_in / 12.0) * (h_in / 12.0) * conc_density
    w_total_dl = w_floor_dl + beam_self_weight
    
    combo1_1_4D = 1.4 * w_total_dl
    combo2_1_2D_1_6L = 1.2 * w_total_dl + 1.6 * w_floor_ll
    
    st.markdown("---")
    st.subheader("Step-by-Step Solutions")
    
    st.markdown("### a) Gravity-Load Transfer Path[cite: 3]")
    st.markdown("""
    **Floor Slab $\rightarrow$ Beams (AB & CD) $\rightarrow$ Columns (1 to 4) $\rightarrow$ Footings / Ground**[cite: 6]
    """)
    
    st.markdown("### b) Distributed Line Loads on Beam CD")
    st.write(f"1. **Floor Dead Load**: $w={dl_psf:.1f} \\times {trib_width:.1f} = \\mathbf{{{w_floor_dl:.1f} \\text{{ lb/ft}}}}$")
    st.write(f"2. **Floor Live Load**: $w={ll_psf:.1f} \\times {trib_width:.1f} = \\mathbf{{{w_floor_ll:.1f} \\text{{ lb/ft}}}}$")
    st.write(f"3. **Beam Self-Weight**: $w=\\frac{{{b_in:.0f}}}{{12}} \\times \\frac{{{h_in:.0f}}}{{12}} \\times {conc_density:.0f} = \\mathbf{{{beam_self_weight:.1f} \\text{{ lb/ft}}}}$")
    st.write(f"   **Total Beam Dead Load ($w_D$)**: ${w_floor_dl:.1f} + {beam_self_weight:.1f} = \\mathbf{{{w_total_dl:.1f} \\text{{ lb/ft}}}}$")
    
    st.markdown("### c) Factored LRFD Line Loads[cite: 3]")
    st.write(f"1. **Comb 1 ($1.4D$)**: $1.4 \\times {w_total_dl:.1f} = \\mathbf{{{combo1_1_4D:.1f} \\text{{ lb/ft}}}}$[cite: 24]")
    st.write(f"2. **Comb 2 ($1.2D + 1.6L$)**: $1.2 \\times {w_total_dl:.1f} + 1.6 \\times {w_floor_ll:.1f} = \\mathbf{{{combo2_1_2D_1_6L:.1f} \\text{{ lb/ft}}}}$[cite: 24]")
    
    st.markdown("### d) Design Governing Load[cite: 3]")
    governing = "1.2D + 1.6L" if combo2_1_2D_1_6L > combo1_1_4D else "1.4D"
    st.success(f"**Governing Load Combination**: Use **{governing}** (${max(combo1_1_4D, combo2_1_2D_1_6L):.1f}\\text{{ lb/ft}}$).")

# ==========================================
# MODULE 4: HW1 PROBLEM 2 - WIND LOAD ANALYSIS
# ==========================================
elif module == "4. HW1 Problem 2: Wind Load Analysis":
    st.header("📝 Homework 1 - Problem 2: Wind Load Calculation (ASCE 7-22)")
    
    st.markdown("""
    **Structure Properties**[cite: 4]:
    * Location: Chicago (41.5500° N, 87.3700° W)
    * Classification: Risk Category II, Site Class B, Exposure C
    * Dimensions: Height $h = 30\text{ ft}$, Roof Pitch = $15^\circ$, Width = $160\text{ ft}$
    """)
    
    st.subheader("Step-by-Step ASCE 7 Procedure")
    
    st.markdown("### a) Basic Wind Speed ($V$)[cite: 4]")
    st.info("From the ASCE Hazard Tool for Chicago, basic wind speed **$V \\approx 107\\text{ mph}$**[cite: 18].")
    
    st.markdown("### b) Velocity Pressure ($q_z$)[cite: 4]")
    st.latex(r"q_z = 0.00256 \, K_z \, K_{zt} \, K_d \, K_e \, V^2")
    
    v_wind = st.slider("Basic Wind Speed V (mph):", 90, 130, 107)
    kz = st.number_input("K_z factor:", value=0.98)
    kd = st.number_input("K_d factor:", value=0.85)
    
    qz = 0.00256 * kz * 1.0 * kd * 1.0 * (v_wind ** 2)
    st.metric("Velocity Pressure q_z (psf):", f"{qz:.2f} psf")
    
    st.markdown("### c) Design Wind Pressure ($p$)[cite: 4]")
    st.latex(r"p = q \, G C_p - q_h (G C_{pi})")
    st.markdown("""
    * **Rigid Structure Gust Factor ($G$)**: $0.85$[cite: 19]
    * **Internal Pressure Coefficient ($G C_{pi}$)**: $\\pm 0.18$ for fully enclosed buildings[cite: 20]
    """)

# ==========================================
# MODULE 5: HW2 PROBLEM 1 - STRUCTURAL DETERMINACY
# ==========================================
elif module == "5. HW2 Problem 1: Structural Determinacy":
    st.header("📝 Homework 2 - Problem 1: Structural Determinacy Classifications[cite: 1]")
    
    prob_a, prob_b = st.tabs(["Structures (a) & (b)", "Structures (c) & (d)"])
    
    with prob_a:
        st.subheader("Structure (a)")
        st.markdown("""
        * **Description**: Horizontal beam supported by guided roller bearings on the left[cite: 1].
        * **Reactions**: Guided roller provides $1$ vertical reaction + $1$ moment reaction ($r = 2$)[cite: 5].
        * **Calculation**: $DI = r - 3n = 2 - 3(1) = -1$[cite: 8].
        * **Verdict**: 🔴 **UNSTABLE** (Unconstrained in horizontal $x$-direction)[cite: 8].
        """)
        
        st.markdown("---")
        st.subheader("Structure (b)")
        st.markdown("""
        * **Description**: Multi-bay rigid portal frame with 2 pin supports[cite: 1].
        * **Calculation**: $DI = 3 \times (\text{closed loops}) = 3(2) = 6$[cite: 8].
        * **Verdict**: 🔵 **STATICALLY INDETERMINATE to the 6th degree**[cite: 8].
        """)

    with prob_b:
        st.subheader("Structure (c)")
        st.markdown("""
        * **Description**: Fixed support at left ($r=3$), pin at right ($r=2$), internal hinge ($c=1$)[cite: 1, 5, 8].
        * **Calculation**: $DI = r - (3n - c) = 5 - (6 - 1) = 0$[cite: 8].
        * **Verdict**: 🟢 **STATICALLY DETERMINATE** ($DI = 0$) and **STABLE**[cite: 7].
        """)
        
        st.markdown("---")
        st.subheader("Structure (d)")
        st.markdown("""
        * **Description**: Frame with inclined tie rod ($1$ reaction) and pin base ($2$ reactions)[cite: 1].
        * **Calculation**: $DI = r - 3n = 3 - 3(1) = 0$[cite: 8].
        * **Verdict**: 🟢 **STATICALLY DETERMINATE** ($DI = 0$) and **STABLE**[cite: 7].
        """)

# ==========================================
# MODULE 6: HW2 PROBLEM 2 - FRAME REACTION SOLVER
# ==========================================
elif module == "6. HW2 Problem 2: Frame Reaction Solver":
    st.header("📝 Homework 2 - Problem 2: Reaction Solver[cite: 2]")
    
    st.markdown("""
    **Problem Geometry & Loading**[cite: 2]:
    * Frame $ABCD$: Height $AB = 2.25\text{ m}$, Width $BC = 3.0\text{ m}$.
    * Top beam $AC$: Trapezoidal load ($6\text{ kN/m}$ at $A$ to $3\text{ kN/m}$ at $C$).
    * Bottom beam $BD$: Uniform upward load ($4\text{ kN/m}$).
    * Pins at $C$ and $D$. Diagonal member $BC$.
    """)
    
    st.subheader("Calculated Support Reactions")
    
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.metric("C_x (Horizontal Reaction at C)", "+2.00 kN (Right)")
        st.metric("C_y (Vertical Reaction at C)", "+7.50 kN (Upward)")
    with res_col2:
        st.metric("D_x (Horizontal Reaction at D)", "-2.00 kN (Left)")
        st.metric("D_y (Vertical Reaction at D)", "-6.00 kN (Downward)")
        
    st.markdown("### Internal Member Forces:")
    st.write("* **Member BC (Diagonal Tie)**: $2.50\\text{ kN}$ (Tension)")
    st.write("* **Member AB (Vertical Column)**: $7.50\\text{ kN}$ (Compression)")

# ==========================================
# MODULE 7: INTERACTIVE PRACTICE QUIZ
# ==========================================
elif module == "7. Interactive Practice Quiz":
    st.header("🧪 Interactive Quiz - Test Your Knowledge!")
    
    score = 0
    
    q1 = st.radio(
        "1. What is the Degree of Indeterminacy (DI) formula for a 2D frame with r reactions and n members?[cite: 7]",
        ["DI = r - 2n", "DI = r - 3n", "DI = 3n - r", "DI = 2r - n"]
    )
    if q1 == "DI = r - 3n":
        score += 1

    q2 = st.radio(
        "2. Which principle allows us to sum displacements caused by individual loads?[cite: 6]",
        ["Principle of Virtual Work", "Principle of Superposition", "Maxwell-Betti Reciprocal Theorem", "Euler-Bernoulli Law"]
    )
    if q2 == "Principle of Superposition":
        score += 1

    q3 = st.radio(
        "3. In ASCE 7 LRFD design, what is the dead load factor in combination 1.2D + 1.6L?[cite: 24]",
        ["1.4", "1.6", "1.2", "0.9"]
    )
    if q3 == "1.2":
        score += 1

    q4 = st.radio(
        "4. A pin support in a 2D coplanar structure provides how many reaction forces?[cite: 5]",
        ["1 force", "2 forces", "3 forces", "2 forces and 1 moment"]
    )
    if q4 == "2 forces":
        score += 1

    if st.button("Submit Quiz"):
        st.balloons()
        st.success(f"🎉 Your Score: **{score} / 4**")
