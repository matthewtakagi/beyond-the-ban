# pages/4_The_Construction_of_Merit.py
# Beyond the Ban | Page 4
# THE CONSTRUCTION OF MERIT (SAT CASE STUDY — 2022 COLLEGE BOARD DATA)

import streamlit as st
import pandas as pd
import altair as alt

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="The Construction of Merit",
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

.page-header {
    text-align: center;
    padding: 20px 0 10px 0;
}

.page-header h1 {
    font-size: 3rem;
    font-weight: 800;
    color: #1a2a6c;
}

.page-header p {
    font-size: 1.2rem;
    color: #666;
    max-width: 950px;
    margin: auto;
    line-height: 1.6;
}

.section-title {
    font-size: 1.7rem;
    font-weight: 800;
    color: #1a2a6c;
    margin-top: 40px;
    margin-bottom: 15px;
}

.text-block {
    font-size: 1.05rem;
    line-height: 1.9;
    color: #333;
    margin-bottom: 15px;
    text-align: justify;
}

.insight-box {
    padding: 18px;
    background-color: #f0f4f8;
    border-left: 5px solid #1a2a6c;
    border-radius: 8px;
    margin-top: 15px;
}

.justice-box {
    padding: 22px;
    background-color: #f8f9fc;
    border-left: 6px solid #8B0000;
    border-radius: 8px;
    margin: 25px 0;
}

.big-stat {
    font-size: 2.5rem;
    font-weight: 900;
    color: #8B0000;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown("""
<div class="page-header">
    <h1>The Construction of Merit</h1>
    <p>
        A case study using official College Board SAT 2022 data to examine a central question:
        is merit measured, or is it produced through unequal systems of preparation?
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# SECTION I — CORE CLAIM
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">I. What the SAT Actually Measures</div>

<div class="text-block">
The SAT is often treated as a neutral proxy for academic ability.
However, 2022 College Board data reveals something more complicated:
performance is not evenly distributed both in scores, as well as in who participates in the test at all.
</div>

<div class="text-block">
The SAT evaluates merit <i>after inequality has already shaped access to preparation, opportunity, and participation.</i>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION II — PARTICIPATION BY GROUP
# ---------------------------------------------------------
st.markdown('<div class="section-title">II. Who Takes the SAT?</div>', unsafe_allow_html=True)

participation = pd.DataFrame({
    "Group": ["White", "Hispanic", "Black", "Asian", "2+ Races", "No Response"],
    "Percent": [42, 23, 12, 10, 4, 8]
})

chart_participation = alt.Chart(participation).mark_bar().encode(
    x=alt.X("Group:N", sort="-y"),
    y=alt.Y("Percent:Q", title="Percent of SAT Test Takers"),
    tooltip=["Group", "Percent"]
).properties(height=600, title="SAT Test Takers by Race")

st.altair_chart(chart_participation, use_container_width=True)

st.markdown("""
<div class="text-block">
Participation itself is unequal.
Some groups are overrepresented in the SAT pool relative to population,
while others are underrepresented, meaning comparisons of merit begin on an uneven basis.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION III — MEAN SCORES BY RACE
# ---------------------------------------------------------
st.markdown('<div class="section-title">III. Mean SAT Scores by Race/Ethnicity</div>', unsafe_allow_html=True)

scores = pd.DataFrame({
    "Group": ["Asian", "2+ Races", "White", "Hispanic", "NHPI", "AIAN", "Black"],
    "Mean_SAT": [1229, 1102, 1098, 964, 945, 936, 926]
})

chart_scores = alt.Chart(scores).mark_bar().encode(
    x=alt.X("Group:N", sort="-y"),
    y=alt.Y("Mean_SAT:Q"),
    tooltip=["Group", "Mean_SAT"]
).properties(height=650)

st.altair_chart(chart_scores, use_container_width=True)

st.markdown("""
<div class="text-block">
The SAT is often interpreted as ranking ability.
But these averages also reflect structural differences in:
<ul>
<li>School funding</li>
<li>Test prep access</li>
<li>Language environment</li>
<li>Neighborhood opportunity</li>
<li>Historical inequality in education systems</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION IV — SCORE DISTRIBUTION SHAPES (FIXED)
# ---------------------------------------------------------
st.markdown('<div class="section-title">IV. Score Distributions</div>', unsafe_allow_html=True)

# Ordered score bands from low → high
score_band_order = ["600-790", "800-990", "1000-1190", "1200-1390", "1400-1600"]

dist = pd.DataFrame({
    "Band": score_band_order,
    "Black": [24, 45, 22, 7, 1],
    "Hispanic": [18, 42, 27, 10, 2],
    "White": [5, 26, 38, 24, 7],
    "Asian": [3, 13, 26, 31, 27],
    "Multiracial": [6, 27, 34, 23, 10]
})

# Convert to long format
dist_long = dist.melt(
    id_vars="Band",
    var_name="Group",
    value_name="Percent"
)

# Explicit category ordering
dist_long["Band"] = pd.Categorical(
    dist_long["Band"],
    categories=score_band_order,
    ordered=True
)

# Side-by-side grouped bars
chart_dist = alt.Chart(dist_long).mark_bar().encode(
    x=alt.X(
        "Band:N",
        sort=score_band_order,
        title="SAT Score Band"
    ),
    y=alt.Y(
        "Percent:Q",
        title="Percent of Students in Score Band"
    ),
    color=alt.Color(
        "Group:N",
        title="Race / Ethnicity"
    ),
    xOffset="Group:N",
    tooltip=[
        alt.Tooltip("Group:N", title="Group"),
        alt.Tooltip("Band:N", title="Score Band"),
        alt.Tooltip("Percent:Q", title="% of Students")
    ]
).properties(
    height=800,
    title="2022 SAT Score Distribution by Race/Ethnicity"
)

st.altair_chart(chart_dist, use_container_width=True)

st.markdown("""
<div class="text-block">
Looking only at average SAT scores can obscure how opportunity is distributed across entire populations.
This visualization instead shows where students are concentrated across score bands.
</div>

<div class="text-block">
At their core, the differences are structural shifts in where large portions of students fall within the score spectrum.
Because selective colleges often rely on score thresholds, benchmark expectations,
or holistic comparisons influenced by academic ranges,
these distribution differences can compound dramatically in admissions outcomes.
</div>

<div class="insight-box">
This is one of the clearest illustrations of this project's broader claim:
academic merit is not merely an isolated measurement of talent.
It is shaped by the unequal distribution of preparation long before an admissions office reviews an application.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION VI — FINAL ARGUMENT
# ---------------------------------------------------------
st.markdown('<div class="section-title">What This Case Study Shows</div>', unsafe_allow_html=True)

st.markdown("""
<div class="text-block">
Merit is a dependent outcome of unequal systems of preparation.
</div>

<div class="text-block">
The SAT itself does not create inequality.
But it reflects inequalities that are already embedded in educational access.
</div>

<div class="text-block">
Therefore, treating SAT scores as purely individual achievement
ignores the systems that produced those scores.
</div>

<div class="text-block">
From this perspective, affirmative action is not a distortion of merit.
It is a response to how merit is constructed in the first place.
</div>
""", unsafe_allow_html=True)