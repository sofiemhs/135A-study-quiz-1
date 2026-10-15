import streamlit as st
import math

# Page setup
st.set_page_config(
    page_title="CEE 135A Structural Analysis Study Guide",
    page_icon="🏗️",
    layout="wide"
)

# App Title & Overview
st.title("🏗️ CEE 135A Elementary Structural Analysis Exam Study Guide")
st.markdown("""
Welcome to the interactive study guide for **CEE 135A**! Navigate through the tabs below to review key lecture concepts, interactive calculators, step-by-step homework solutions, and self-assessment quizzes.
""")

# Tabs for Navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📚 Module 1: Ch 1 - Types of Structures & Loads",
    "📐 Module 2: Ch 2 - Determinacy, Stability & Equilibrium",
    "✏️ Module 3: Homework 1 Solutions",
    "⚙️ Module 4: Homework 2 Solutions",
    "🎯 Module 5: Interactive Practice Quiz"
])

# ==========================================
# MODULE 1: CHAPTER 1 NOTES & CALCULATORS
# ==========================================
with tab1:
    st.header("Module 1: Types of Structures & Loads (Chapter 1)")
    
    st.subheader("1. Classification of Structures")
    st.markdown("""
    - **Tie Rods**: Slender elements subjected to pure tension[cite: 12].
    - **Beams**: Straight horizontal members resisting loads primarily through shear and bending moment[cite: 12].
    - **Columns & Beam-Columns**: Vertical members in compression (columns) or combined axial compression and bending (beam-columns)[cite: 13].
    - **Trusses**: Framework of slender members connected at joints, carrying loads primarily in tension or compression[cite: 13].
    - **Cables & Arches**: Cables carry loads in pure tension (flexible, cannot buckle)[cite: 14]. Arches carry loads mainly in compression[cite: 14].
    """)
    
    st.subheader("2. Structural Design Methodologies & Load Combinations")
    st.markdown("""
    - **Allowable Stress Design (ASD)**: Uses a single safety factor ($S.F.$)[cite: 23]:
      $$\text{Calculated Elastic Stress} \le \text{Allowable Stress}$$
    - **Load and Resistance Factor Design (LRFD)**: Uses load factors ($\gamma > 1$) for load uncertainty and resistance factors ($\phi < 1$) for material uncertainty[cite: 24]:
      $$\text{Required Strength } (R_u) \le \text{Design Strength } (\phi R_n)$$
    
    **Primary LRFD Load Combinations (ASCE 7-22)**[cite: 24]:
    1. $1.4 D$[cite: 24]
    2. $1.2 D + 1.6 L + 0.5(L_r \text{ or } S \text{ or } R)$[cite: 24]
    3. $1.2 D + 1.6(L_r \text{ or } S \text{ or } R) + (L \text{ or } 0.5 W)$[cite: 24]
    4. $1.2 D + 1.0 W + L + 0.5(L_r \text{ or } S \text{ or } R)$[cite: 24]
    5. $0.9 D + 1.0 W$[cite: 24]
    """)
    
    st.subheader("3. Wind Load Equations (ASCE 7-22)")
    st.markdown("""
    **Velocity Pressure Formula (US Customary)**[cite: 18]:
    $$q_z = 0.00256 \cdot K_z \cdot K_{zt} \cdot K_d \cdot K_e \cdot V^2 \quad (\text{psf})$$
    - $V$: Basic wind speed (3-second gust at 33 ft in mph)[cite: 18]
    - $K_z$: Velocity pressure exposure coefficient[cite: 19]
    - $K_{zt}$: Topographic factor ($1.0$ for flat ground)[cite: 19]
    - $K_d$: Wind directionality factor ($1.0$ for wind alone)[cite: 19]
    - $K_e$: Ground elevation factor ($1.0$ standard)[cite: 19]
    
    **Design Wind Pressure for Enclosed Buildings**[cite: 19]:
    $$p = q \cdot G \cdot C_p - q_h \cdot (G C_{pi}) \quad (\text{psf})$$
    - $G$: Gust-effect factor ($\approx 0.85$ for rigid structures)[cite: 19]
    - $C_p$: External pressure coefficient[cite: 20]
    - $G C_{pi}$: Internal pressure coefficient ($\pm 0.18$ for enclosed structures)[cite: 20]
    """)
    
    st.markdown("---")
    st.subheader("🧮 Interactive Wind Velocity Pressure Calculator ($q_z$)")
    col1, col2 = st.columns(2)
    with col1:
        V_input = st.number_input("Basic Wind Speed V (mph)", value=107.0, step=1.0)
        Kz_input = st.number_input("Exposure Coeff K_z", value=0.98, step=0.01)
        Kzt_input = st.number_input("Topographic Factor K_zt", value=1.0, step=0.05)
    with col2:
        Kd_input = st.number_input("Directionality Factor K_d", value=1.0, step=0.05)
        Ke_input = st.number_input("Elevation Factor K_e", value=1.0, step=0.05)
    
    qz_calc = 0.00256 * Kz_input * Kzt_input * Kd_input * Ke_input * (V_input ** 2)
    st.success(f"**Calculated Velocity Pressure $q_z$:** {qz_calc:.2f} psf")

# ==========================================
# MODULE 2: CHAPTER 2 NOTES & CALCULATORS
# ==========================================
with tab2:
    st.header("Module 2: Structural Indeterminacy, Stability & Equilibrium (Chapter 2)")
    
    st.subheader("1. Static Determinacy & Degree of Indeterminacy ($DI$)")
    st.markdown("""
    For a 2D planar structure composed of $n$ members or structural parts and $r$ support reactions:
    $$DI = r + 3m - 3n - r_i$$
    *Or simplified for structures evaluated as free bodies/joints*:
    $$DI = r - 3n$$
    
    - **$DI < 0$**: Unstable (partially constrained)[cite: 7, 8].
    - **$DI = 0$**: Statically Determinate[cite: 7].
    - **$DI > 0$**: Statically Indeterminate to the $DI$-th degree[cite: 7].
    """)
    
    st.subheader("2. Structural Stability Rules")
    st.markdown("""
    A structure can be **unstable** even if $r \ge 3n$ if[cite: 9]:
    1. **Parallel Reactions**: All reaction forces act in parallel directions, leaving horizontal or vertical movement unconstrained[cite: 8, 9].
    2. **Concurrent Reactions**: All reaction force vectors intersect at a single common point $O$, allowing unconstrained rotation about $O$ ($\sum M_O \ne 0$)[cite: 8, 9].
    3. **Internal Collapse Mechanism**: The internal arrangement of hinges/links creates a collapsible structure[cite: 9].
    """)
    
    st.markdown("---")
    st.subheader("🧮 Interactive Indeterminacy Calculator")
    c1, c2, c3 = st.columns(3)
    with c1:
        r_val = st.number_input("Support Reactions (r)", value=3, min_value=0, step=1)
    with c2:
        n_val = st.number_input("Number of Parts / Segments (n)", value=1, min_value=1, step=1)
    with c3:
        ri_val = st.number_input("Internal Releases / Hinges (r_i)", value=0, min_value=0, step=1)
    
    di_calc = r_val - 3 * n_val - ri_val
    if di_calc < 0:
        st.error(f"Degree of Indeterminacy: {di_calc} ➔ **Unstable Structure**")
    elif di_calc == 0:
        st.success(f"Degree of Indeterminacy: {di_calc} ➔ **Statically Determinate**")
    else:
        st.warning(f"Degree of Indeterminacy: {di_calc} ➔ **Statically Indeterminate to the {di_calc} Degree**")

# ==========================================
# MODULE 3: HOMEWORK 1 SOLUTIONS
# ==========================================
with tab3:
    st.header("✏️ Homework 1 Complete Solutions & Walkthroughs")
    
    st.subheader("Problem 1: Slab Load Transfer & Beam Frame LRFD Analysis")
    st.markdown("""
    **Given Parameters:**
    - Slab Dimensions: $30\text{ ft (length)} \times 20\text{ ft (width)}$ supported by beams AB and CD[cite: 3].
    - Dead Load ($DL_{slab}$): $80\text{ psf}$, Live Load ($LL_{slab}$): $50\text{ psf}$[cite: 3].
    - Beam Cross-Section: $12\text{ in.} \times 24\text{ in.}$, Concrete Density: $150\text{ pcf}$[cite: 3].
    """)
    
    with st.expander("📌 Part (a): Gravity-Load Transfer Path"):
        st.markdown("""
        **Transfer Path:**
        $$\text{Floor Slab} \longrightarrow \text{Beams AB \& CD (Tributary Width = } 10\text{ ft)} \longrightarrow \text{Columns 1-4} \longrightarrow \text{Footings} \longrightarrow \text{Ground}$$
        - Since the slab is supported by beams along two parallel edges (30 ft length), it acts as a **one-way slab**[cite: 3, 6].
        - Tributary width for beam CD $= 20\text{ ft} / 2 = 10\text{ ft}$[cite: 3].
        """)
        
    with st.expander("📌 Part (b): Line Load Calculations"):
        st.markdown("""
        1. **Floor Dead Load line load ($w_{D,floor}$):**
           $$w_{D,floor} = 80\text{ psf} \times 10\text{ ft} = 800\text{ lb/ft}$$
        2. **Floor Live Load line load ($w_L$):**
           $$w_L = 50\text{ psf} \times 10\text{ ft} = 500\text{ lb/ft}$$
        3. **Beam Self-Weight ($w_{beam}$):**
           $$A_{beam} = \frac{12\text{ in.}}{12} \times \frac{24\text{ in.}}{12} = 1\text{ ft} \times 2\text{ ft} = 2\text{ ft}^2$$
           $$w_{beam} = 2\text{ ft}^2 \times 150\text{ pcf} = 300\text{ lb/ft}$$
        4. **Total Dead Load ($w_D$):**
           $$w_D = w_{D,floor} + w_{beam} = 800 + 300 = 1100\text{ lb/ft}$$
        """)
        
    with st.expander("📌 Part (c) & (d): LRFD Load Combinations & Governing Load"):
        st.markdown("""
        - **Combination 1 ($1.4D$):**
          $$w_{u1} = 1.4 \times 1100\text{ lb/ft} = 1540\text{ lb/ft} = 1.54\text{ kips/ft}$$
        - **Combination 2 ($1.2D + 1.6L$):**
          $$w_{u2} = (1.2 \times 1100) + (1.6 \times 500) = 1320 + 800 = 2120\text{ lb/ft} = 2.12\text{ kips/ft}$$
        
        **Governing Load Case for Design:**
        Case (2) ($1.2D + 1.6L = 2120\text{ lb/ft}$) governs the design because $2120\text{ lb/ft} > 1540\text{ lb/ft}$.
        """)

    st.markdown("---")
    st.subheader("Problem 2: Wind Load Analysis (ASCE 7-22)")
    st.markdown("""
    **Given Parameters:** Storage Building in Chicago, IL ($41.5500^\circ\text{N}, 87.3700^\circ\text{W}$)[cite: 4].
    - Risk Category II, Site Class B, Exposure C[cite: 4].
    - Dimensions: Length $= 150\text{ ft}$, Width $= 160\text{ ft}$ ($80\text{ ft} + 80\text{ ft}$), Eave Height $= 30\text{ ft}$, Roof Pitch $= 15^\circ$[cite: 4].
    """)
    
    with st.expander("📌 Step-by-Step Wind Calculations"):
        st.markdown("""
        1. **Basic Wind Speed ($V$):** From ASCE Hazard Tool for Chicago, $V \approx 107\text{ mph}$[cite: 4].
        2. **Mean Roof Height ($h$):**
           $$h_{roof, peak} = 30 + 80 \times \tan(15^\circ) = 30 + 80(0.2679) = 51.43\text{ ft}$$
           $$h = \frac{30 + 51.43}{2} = 40.72\text{ ft}$$
        3. **Velocity Pressure ($q_z$ at eave height $z=30\text{ ft}$ & $q_h$ at $h=40.72\text{ ft}$):**
           - For Exposure C: $K_z(30\text{ ft}) \approx 0.98$, $K_h(40.72\text{ ft}) \approx 1.04$.
           - $q_z = 0.00256 \times 0.98 \times 1.0 \times 1.0 \times 1.0 \times (107)^2 = 28.72\text{ psf}$[cite: 18, 19]
           - $q_h = 0.00256 \times 1.04 \times 1.0 \times 1.0 \times 1.0 \times (107)^2 = 30.48\text{ psf}$[cite: 18, 19]
        """)

# ==========================================
# MODULE 4: HOMEWORK 2 SOLUTIONS
# ==========================================
with tab4:
    st.header("⚙️ Homework 2 Complete Solutions & Walkthroughs")
    
    st.subheader("Problem 1: Structural Classification (Determinacy & Stability)")
    
    p1_a, p1_b = st.columns(2)
    with p1_a:
        st.markdown("""
        **(a) Cantilevered Beam with Sleeve / Guide Support**[cite: 1]
        - **Reactions ($r$):** 2 reactions at sleeve guide (vertical force + moment)[cite: 1, 5].
        - **Equations ($3n$):** 3 equilibrium equations[cite: 7].
        - **$r < 3n$ ($2 < 3$):** **Unstable** (partially constrained against horizontal force)[cite: 8].
        
        **(b) Two-Bay Portal Frame on Pin Supports**[cite: 1]
        - **Reactions ($r$):** 2 pin supports = 4 reactions[cite: 1, 5].
        - **Members ($m$):** 7 rigid members forming closed loops[cite: 1].
        - **Degree of Indeterminacy:** Using $DI = 3(\text{loops}) - \text{releases} = 3(2) - 0 = \mathbf{6}$[cite: 8].
        - **Result:** **Statically Indeterminate to the 6th Degree**[cite: 1, 7].
        """)
    with p1_b:
        stHere is a single, self-contained Python Streamlit application (`app.py`) designed to serve as an interactive, fully detailed study guide for your quiz on **CEE 135A: Elementary Structural Analysis**.

This interactive app covers all concepts, formulas, step-by-step problem breakdowns, and quiz questions directly from your 4 documents (Homework 1[cite: 3, 4], Homework 2[cite: 1, 2], Chapter 1 Notes[cite: 11], Chapter 2 Notes[cite: 5]).

---

### Instructions to Run Locally & Push to GitHub / Streamlit Community Cloud

1. **Install Dependencies**:
   ```bash
   pip install streamlit
