# pages/5_Whats_Next.py
# Beyond the Ban | Page 5
# WHAT'S NEXT?

import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="What's Next?",
    page_icon="⚖️",
    layout="wide"
)

# ---------------------------------------------------------
# STYLE
# ---------------------------------------------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(to bottom, #fdfdfd, #ffffff);
}

/* PAGE HEADER */
.page-header {
    text-align: center;
    margin-top: 10px;
    margin-bottom: 35px;
}

.page-header h1 {
    font-size: 3rem;
    font-weight: 800;
    color: #1a2a6c;
    margin-bottom: 8px;
}

.page-header p {
    font-size: 1.2rem;
    color: #666;
    max-width: 950px;
    margin: auto;
    line-height: 1.8;
}

/* SECTION TITLE */
.section-title {
    font-size: 1.8rem;
    font-weight: 800;
    color: #1a2a6c;
    margin-top: 45px;
    margin-bottom: 18px;
    text-align: center;
}

/* TEXT BLOCK */
.text-block {
    font-size: 1.08rem;
    line-height: 1.9;
    color: #333;
    margin-bottom: 18px;
    text-align: justify;
}

/* QUESTION CARD */
.question-card {
    background: white;
    padding: 22px;
    border-radius: 12px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
    border-top: 5px solid #1a2a6c;
    height: 100%;
}

.question-card h3 {
    color: #1a2a6c;
    font-size: 1.25rem;
    margin-bottom: 12px;
}

/* JUSTICE BOX */
.justice-box {
    background-color: #f8f9fc;
    border-left: 6px solid #8B0000;
    padding: 28px;
    border-radius: 10px;
    margin: 35px 0;
    line-height: 1.9;
    font-size: 1.08rem;
}

/* TAKEAWAY BOX */
.takeaway-box {
    background-color: #f0f4f8;
    border-left: 6px solid #1a2a6c;
    padding: 24px;
    border-radius: 10px;
    margin-top: 25px;
    line-height: 1.9;
}

/* FINAL STATEMENT */
.final-box {
    background: linear-gradient(135deg, #1a2a6c, #2c3e90);
    color: white;
    padding: 35px;
    border-radius: 16px;
    margin-top: 50px;
    text-align: center;
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

.final-box h2 {
    font-size: 2rem;
    margin-bottom: 15px;
}

.final-box p {
    font-size: 1.15rem;
    line-height: 1.9;
    max-width: 950px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown("""
<div class="page-header">
    <h1>What’s Next?</h1>
    <p>
        If affirmative action was never solely about admissions,
        then its future is not about whether race-conscious admissions remain legal.
        The deeper question is what justice requires in a society where inequality
        is structurally produced long before opportunity is distributed.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# INTRO REFLECTION
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">Where This Project Leads</div>

<div class="text-block">
Across this project, one pattern has remained consistent:
inequality is a years-long accumulation. From Reconstruction to the Supreme Court,
from parental education to SAT scores,
from application behavior to labor-market outcomes,
what appears to be individual merit is often shaped by systems
that distribute preparation unevenly across race, class, geography, historical access, and much more.
This does not mean individual achievement is meaningless.
It means achievement exists within context.
And if context is unequal, then institutions must confront whether neutrality alone can produce fairness.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# BIG QUESTIONS
# ---------------------------------------------------------
st.markdown('<div class="section-title">What America Still Has to Answer</div>', unsafe_allow_html=True)

q1, q2, q3 = st.columns(3)

with q1:
    st.markdown("""
    <div class="question-card">
        <h3>1. If not affirmative action, then what?</h3>
        Race-neutral alternatives like class-based admissions,
        percentage plans, targeted outreach,
        and geographic diversity policies can soften inequality,
        but can they address racialized structural disparities
        in the same way that affirmative action can?
    </div>
    """, unsafe_allow_html=True)

with q2:
    st.markdown("""
    <div class="question-card">
        <h3>2. What does merit really measure?</h3>
        Should admissions and hiring systems treat scores,
        grades, and resumes as pure indicators of talent,
        or as outputs shaped by unequal educational,
        social, and financial opportunity?
    </div>
    """, unsafe_allow_html=True)

with q3:
    st.markdown("""
    <div class="question-card">
        <h3>3. Where should justice intervene?</h3>
        At the endpoint through admissions?
        Earlier through K–12 funding?
        Through wealth redistribution?
        Through hiring reform?
        Or through some combination of all three?
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# JUSTICE SYNTHESIS
# ---------------------------------------------------------

st.markdown('<div class="section-title">The Justice Problem</div>', unsafe_allow_html=True)

st.markdown("""
<div class="text-block">
The debate over affirmative action is often framed too narrowly,
as though the issue is simply whether race should be considered
in a single institutional decision.

But this project suggests something broader:
affirmative action emerged because inequality itself was already structured.

In that sense, affirmative action did not invent unfairness.
It represented one attempt, though
imperfect, controversial, and contested,
to respond to systems that had already distributed advantage unequally.
The post-2023 era therefore did not end the justice debate, but instead, it intensified it.
</div>

""", unsafe_allow_html=True)

# ---------------------------------------------------------
# FUTURE PATHWAYS
# ---------------------------------------------------------
st.markdown('<div class="section-title">Possible Futures</div>', unsafe_allow_html=True)

st.markdown("""
<div class="text-block">
The end of race-conscious admissions may reshape how institutions pursue diversity,
but it does not eliminate the inequalities that made diversity policy relevant.
</div>


<div class="text-block">
Future interventions may increasingly focus on:
</div>
""", unsafe_allow_html=True)

st.markdown("""
- **Class-based affirmative action** to address wealth inequality  
- **K–12 educational investment** to equalize preparation earlier  
- **Targeted recruitment pipelines** for underrepresented communities  
- **Place-based admissions models** tied to neighborhood opportunity  
- **Holistic definitions of merit** that contextualize achievement  
""")

st.markdown("""
<div class="takeaway-box">
Each path carries trade-offs.
Some may better address class inequality than racial inequality.
Others may preserve diversity while avoiding explicit racial classifications.
But all force the same underlying question, one that we have discussed over the course of this project:
<b>Can a society committed to equal opportunity remain passive
when opportunity is unequally constructed?</b>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HUMAN DIMENSION
# ---------------------------------------------------------
st.markdown('<div class="section-title">The Human Stakes</div>', unsafe_allow_html=True)

st.markdown("""
<div class="text-block">
Behind every dataset in this project are real lives:
students deciding whether to reveal identity,
families navigating systems they did not design,
workers confronting labor markets shaped by credentialism,
and communities debating what fairness should actually mean.
</div>

<div class="text-block">
The future of affirmative action is therefore not only legal,
statistical, or political.
It is deeply human.
It concerns belonging,
representation,
mobility,
and the boundaries of who gets seen as deserving.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# FINAL CLAIM
# ---------------------------------------------------------
st.markdown("""
<div class="final-box">
    <h2>Final Thought</h2>
    <p>
        The core question was never simply whether affirmative action is fair.
        The deeper question is this:
        <strong>How should a society respond when the competition it calls meritocratic
        begins on unequal ground?</strong>
        If merit is shaped long before selection, then justice may require more than neutrality.
        Beyond the ban lies the real challenge, deciding what fairness should look like going forward.
        <br><br>
        Thank you for taking the time to learn and think about this important issue. Our thanks
            goes out to Professor Daniel Roddy, GSI Daniel Lobo, and the rest of the community in
            the Spring 2026 Data C4AC cohort for their support and feedback throughout this project's
            development.
    </p>
</div>
""", unsafe_allow_html=True)