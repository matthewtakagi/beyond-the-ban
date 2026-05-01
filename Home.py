import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Beyond the Ban",
    page_icon="⚖️",
    layout="wide"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>
.hero {
    padding: 3rem 2rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #4b0000, #8b0000, #c0392b);
    color: white;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    margin-bottom: 2rem;
}

.hero h1 {
    font-size: 3.2rem;
    margin-bottom: 0.5rem;
}

.hero p {
    font-size: 1.25rem;
    line-height: 1.8;
}

.card {
    background: white;
    padding: 1.5rem;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
}

.lens-box {
    background-color: #fff8f0;
    border-left: 6px solid #8B0000;
    padding: 2rem;
    border-radius: 14px;
    margin-top: 1rem;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
    line-height: 1.7;
}

.lens-title {
    font-size: 1.8rem;
    font-weight: 800;
    color: #8B0000;
    margin-bottom: 1rem;
}

.footer {
    text-align: center;
    color: gray;
    font-size: 0.9rem;
    margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>Beyond the Ban: The Data of Affirmative Action</h1>
    <p>
        A project exploring affirmative action's past, present, and future in America.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("## Welcome!")

st.markdown("""
This project explores affirmative action as not just a policy debate, but also
a centuries-long evolution over the meaning of justice itself.
""")

st.markdown("""
Through historical events, landmark court cases, and comparative global policies,
this website examines how societies attempt to correct inequality, define fairness,
and respond to the consequences of those choices.
""")

st.markdown("""
Use the timeline, case studies, and narratives to explore how the idea of justice
has shifted over time, in addition to why it remains deeply contested today.
""")

st.divider()

# ---------------------------------------------------------
# INTERACTIVE JUSTICE LENS
# ---------------------------------------------------------
st.subheader("Lens of Affirmative Action")

lens = st.selectbox(
    "What's your perspective?",
    ["Corrective Justice", "Distributive Justice", "Procedural Justice", "Merit-Based Fairness"]
)

if lens == "Corrective Justice":
    st.markdown("""
    <div class="lens-box">
        <div class="lens-title">Corrective Justice</div>
        Justice is understood as repairing harm caused by historical exclusion and structural inequality.
        <br><br>
        Under this view, affirmative action is a corrective force.
        It responds to systems that previously restricted access to education, jobs, and political power.
        <br><br>
        The priority: <strong>What obligations does a society have to those who have been historically excluded?</strong>
    </div>
    """, unsafe_allow_html=True)

elif lens == "Distributive Justice":
    st.markdown("""
    <div class="lens-box">
        <div class="lens-title">Distributive Justice</div>
        Justice is about how resources and opportunities are distributed across society.
        <br><br>
        Affirmative action is evaluated based on outcomes related to representation, mobility, and access.
        <br><br>
        The priority: <strong>What distribution of opportunity is considered fair?</strong>
    </div>
    """, unsafe_allow_html=True)

elif lens == "Procedural Justice":
    st.markdown("""
    <div class="lens-box">
        <div class="lens-title">Procedural Justice</div>
        In addition to outcomes, justice is defined by fairness in the rules themselves.
        <br><br>
        Policies are evaluated by transparency, consistency, and equal treatment under formal processes.
        <br><br>
        The priority: <strong>Regardless of the outcomes, are the rules fair?</strong>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="lens-box">
        <div class="lens-title">Merit-Based Fairness</div>
        Justice is defined by individual achievement measured without demographic consideration.
        <br><br>
        Affirmative action is often critiqued as interfering with neutral competition.
        <br><br>
        The priority: <strong>Should opportunity be blind to history and identity?</strong>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# CORE QUESTIONS
# ---------------------------------------------------------
st.subheader("Core Questions")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
    <h3>History</h3>
    How did legal systems construct and later attempt to repair inequality?
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h3>Data</h3>
    What do outcomes reveal about access, opportunity, and mobility?
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <h3>Perspective</h3>
    How do different communities define fairness and justice?
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# NAVIGATION BUTTONS
# ---------------------------------------------------------
st.subheader("Explore the Project")

b1, b2, b3, b4 = st.columns(4)

with b1:
    if st.button("Timeline"):
        st.switch_page("pages/1_Timeline.py")

with b2:
    if st.button("Structures of Inequality"):
        st.switch_page("pages/2_Structures_of_Inequality.py")

with b3:
    if st.button("Admissions Data"):
        st.switch_page("pages/3_Admissions_Outcomes.py")

with b4:
    if st.button("Narratives"):
        st.switch_page("pages/4_Narratives.py")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.markdown("""
<div class="footer">
Beyond the Ban: The Data of Affirmative Action
</div>
""", unsafe_allow_html=True)