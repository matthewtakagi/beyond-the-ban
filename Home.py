import streamlit as st
import altair as alt
import pandas as pd

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Beyond the Ban | Home",
    page_icon="⚖️",
    layout="wide"
)

# ---------------------------------------------------------
# CUSTOM CSS (UNIFIED WITH TIMELINE / SITE STYLE)
# ---------------------------------------------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(to bottom, #fdfdfd, #ffffff);
}

/* HERO */
.hero {
    padding: 4rem 2rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #1a2a6c, #2b5876, #4e4376);
    color: white;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    margin-bottom: 2rem;
}

.hero h1 {
    font-size: 3.5rem;
    font-weight: 900;
    margin-bottom: 0.75rem;
}

.hero p {
    font-size: 1.25rem;
    line-height: 1.8;
    max-width: 950px;
    margin: auto;
}

/* SECTION HEADERS */
.section-title {
    font-size: 2rem;
    font-weight: 800;
    color: #1a2a6c;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

/* BODY TEXT */
.text-block {
    font-size: 1.08rem;
    line-height: 1.9;
    color: #333;
    text-align: justify;
    margin-bottom: 1rem;
}

/* CLAIM BOX */
.claim-box {
    background-color: #f0f4f8;
    padding: 2rem;
    border-left: 6px solid #b22222;
    border-radius: 10px;
    margin-top: 1rem;
    margin-bottom: 2rem;
    box-shadow: 0 4px 14px rgba(0,0,0,0.05);
}

.claim-title {
    font-size: 1.8rem;
    font-weight: 800;
    color: #b22222;
    margin-bottom: 1rem;
}

/* INFO CARD */
.info-card {
    background: white;
    padding: 1.5rem;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    height: 100%;
}

/* NEXT BUTTON */
.next-section {
    text-align: center;
    margin-top: 3rem;
    margin-bottom: 2rem;
}

/* FOOTER */
.footer {
    text-align: center;
    color: gray;
    font-size: 0.9rem;
    margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>Beyond the Ban: The Data of Affirmative Action</h1>
    <p>
        Affirmative action is often framed as a challenge to merit in college admissions 
            and the job hunt.
        This project, our final project for the Data C4AC: Data and Justice course
            argues something different:
        affirmative action does not challenge the existing meritocracy, but it
        intervenes in a system where merit has already been shaped
        by unequal access to education, wealth, opportunity, and much, much more.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION 1 — WHY THIS MATTERS
# ---------------------------------------------------------
st.markdown('<div class="section-title">Why This Matters</div>', unsafe_allow_html=True)

st.markdown("""
<div class="text-block">
In 2023, as the Supreme Court decided <i>Students for Fair Admissions v. Harvard</i>,
affirmative action became one of the most visible justice debates in modern America.
Yet visibility did not mean clarity.
According to  <a href="https://www.pewresearch.org/short-reads/2023/06/16/americans-and-affirmative-action-how-the-public-sees-the-consideration-of-race-in-college-admissions-hiring/" target="_blank">Pew Research polling</a>, while most Americans had heard of affirmative action,
roughly one in five had not heard the term at all, and approximately one-third did not take a clear position.
</div>

<div class="text-block">
This matters because affirmative action is frequently debated by policymakers and individuals in positions of power,
when in reality, public understanding is fragmented at best.
If many Americans are unfamiliar, undecided, or interpreting the policy through significantly different definitions of fairness,
then the issue is both about policy and how people understand the topic of inequality itself.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# PEW DATA VISUALIZATIONS (AWARENESS + OPINION)
# ---------------------------------------------------------
col1, col2 = st.columns(2)

# -------------------------
# Chart 1: Awareness
# -------------------------
with col1:
    awareness_data = pd.DataFrame({
        "Category": [
            "Heard of affirmative action",
            "Not heard of affirmative action",
            "No answer"
        ],
        "Percent": [79, 20, 1]
    })

    awareness_chart = alt.Chart(awareness_data).mark_arc(innerRadius=55).encode(
        theta=alt.Theta("Percent:Q"),
        color=alt.Color("Category:N", title="Survey Response"),
        tooltip=["Category", "Percent"]
    ).properties(
        title="Have Americans Heard the Phrase 'Affirmative Action'?",
        height=400
    )

    st.altair_chart(awareness_chart, use_container_width=True)


# -------------------------
# Chart 2: Opinion Among Those Aware
# -------------------------
with col2:
    opinion_data = pd.DataFrame({
        "Category": [
            "Good thing",
            "Bad thing",
            "Don't know"
        ],
        "Percent": [36, 29, 33]
    })

    opinion_chart = alt.Chart(opinion_data).mark_arc(innerRadius=55).encode(
        theta=alt.Theta("Percent:Q"),
        color=alt.Color("Category:N", title="Opinion"),
        tooltip=["Category", "Percent"]
    ).properties(
        title="Among Those Familiar, Public Opinion Remains Divided",
        height=400
    )

    st.altair_chart(opinion_chart, use_container_width=True)

# ---------------------------------------------------------
# SECTION 2 — CORE CLAIM
# ---------------------------------------------------------
st.markdown("""
<div class="claim-box">
    <div class="claim-title">Our Claim</div>
    Affirmative action is not a misrepresentation or falsification of merit and the existing meritocracy. Instead, it is an intervention in a system where “merit” (namely, academic merit) is shaped long before college admissions or job applications, influenced by the existence of inequalities such as unequal access to education, income, language environments, and preparation resources.
As a result, affirmative action functions as a corrective mechanism aimed at addressing inequality that has already been structurally produced. It does not create inequality itself.

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION 3 — JUSTICE FRAME
# ---------------------------------------------------------
st.markdown('<div class="section-title">Framing the Question Through Justice</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
    <h3>Merit-Based Fairness</h3>
    Does fairness mean evaluating everyone by the same formal standards,
    regardless of unequal starting conditions?
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
    <h3>Corrective & Distributive Justice</h3>
    Or does fairness require acknowledging that “equal treatment”
    inside unequal systems can reproduce inequality rather than eliminate it?
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="text-block" style="margin-top: 1.5rem;">
This project explores affirmative action as a much deeper question:
<b>When systems shape opportunity unequally, what does justice actually require?</b>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION 4 — HOW TO USE THIS WEBSITE
# ---------------------------------------------------------
st.markdown('<div class="section-title">How to Use This Project</div>', unsafe_allow_html=True)

st.markdown("""
<div class="text-block">
This website is designed as a narrative.
Rather than jumping between disconnected pages,
each section builds on the previous one.
</div>

<div class="text-block">
To understand the present debate over affirmative action,
it is necessary to trace how legal systems, educational structures,
and economic outcomes collectively shape what society calls merit.
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

if st.button("Let's Begin →"):
    st.switch_page("pages/1_How_We_Got_Here.py")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.divider()

st.markdown("""
<div class="footer">
Beyond the Ban: The Data of Affirmative Action<br>
Data C4AC Final Project<br>
Ricardo Barrientos, Matthew Takagi, Steven Yip
</div>
""", unsafe_allow_html=True)