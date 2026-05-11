# pages/3_Selective_College_Pipeline.py
# Beyond the Ban | Page 3
# STRUCTURES OF INEQUALITY

import streamlit as st
import pandas as pd
import altair as alt
import os

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Structures of Inequality",
    page_icon="📊",
    layout="wide"
)

DATA_PATH = "assets/CollegeAdmissions_Data.csv"

# ---------------------------------------------------------
# GLOBAL STYLE (MATCH TIMELINE PAGE CLEAN AESTHETIC)
# ---------------------------------------------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(to bottom, #fdfdfd, #ffffff);
}

/* CENTER TITLE */
.page-header {
    text-align: center;
    margin-top: 10px;
    margin-bottom: 30px;
}

.page-header h1 {
    font-size: 3rem;
    font-weight: 800;
    color: #1a2a6c;
    margin-bottom: 5px;
}

.page-header p {
    font-size: 1.2rem;
    color: #666;
}

/* SECTION HEADERS */
.section-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: #1a2a6c;
    margin-top: 35px;
    margin-bottom: 10px;
}

/* TEXT BLOCKS */
.text-block {
    font-size: 1.05rem;
    line-height: 1.8;
    color: #333;
    margin-bottom: 15px;
    text-align: justify;
}

/* INSIGHT BOX */
.insight-box {
    background-color: #f0f4f8;
    padding: 15px;
    border-radius: 8px;
    border-left: 4px solid #1a2a6c;
    margin: 15px 0;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown("""
<div class="page-header">
    <h1>Structures of Inequality</h1>
    <p>Affirmative action is a pipeline shaped before, during, and after applications are even submitted.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# INTRODUCTION
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">What's actually measured here?</div>

<div class="text-block">
Selective college admissions are often discussed as if they are the starting point of inequality debates.
But the data suggests something different: by the time students reach application and enrollment,
much of the distribution has already been shaped.
</div>

<div class="text-block">
This page traces how opportunity changes across three stages:
<b>application behavior → admissions results → conditional enrollment</b>.
Each step reveals a different layer of structural inequality.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------
if not os.path.exists(DATA_PATH):
    st.error("Dataset not found. Please place CollegeAdmissions_Data.csv in assets/")
    st.stop()

df = pd.read_csv(DATA_PATH)

required_cols = ["par_income_bin", "par_income_lab", "rel_attend", "rel_apply", "rel_att_cond_app"]
df = df.dropna(subset=[c for c in required_cols if c in df.columns])

df["par_income_bin"] = pd.to_numeric(df["par_income_bin"], errors="coerce")
df = df.sort_values("par_income_bin")

# ---------------------------------------------------------
# SECTION 1
# ---------------------------------------------------------
st.markdown('<div class="section-title">1. Representation Across Selective Colleges</div>', unsafe_allow_html=True)

tier_income = (
    df.groupby(["tier_name", "par_income_lab", "par_income_bin"], as_index=False)
      .agg({"rel_attend": "mean"})
)

chart1 = alt.Chart(tier_income).mark_line(point=True).encode(
    x=alt.X("par_income_lab:N", sort=alt.SortField("par_income_bin"), title="Parental Income Group"),
    y=alt.Y("rel_attend:Q", title="Relative Attendance (1.0 = expected)"),
    color="tier_name:N",
    tooltip=["tier_name", "par_income_lab", "rel_attend"]
).properties(height=450)

st.altair_chart(chart1, use_container_width=True)

data = pd.DataFrame({

    "Race/Ethnicity": [
        "U.S. Average",
        "Asian",
        "White (not Hispanic)",
        "Black",
        "Hispanic"
    ],

    "2023": [63030, 83110, 70860, 53310, 48100],
    "2024": [63360, 86560, 71260, 52370, 50430]

})

# Convert to long format for Altair

data_long = data.melt(
    id_vars="Race/Ethnicity",
    var_name="Year",
    value_name="Median Income"

)

chart = alt.Chart(data_long).mark_bar().encode(
    x=alt.X("Race/Ethnicity:N", title="Race / Ethnicity", sort=None),
    y=alt.Y("Median Income:Q", title="Median Income (USD)"),
    color=alt.Color("Year:N", title="Year"),
    xOffset="Year:N",
    tooltip=["Race/Ethnicity", "Year", "Median Income"]

).properties(
    height=450
)

st.subheader("Median Income by Race/Ethnicity (2023-2024)")

st.altair_chart(chart, use_container_width=True)

st.markdown("""
<div class="insight-box">
If representation were fully meritocratic after controlling for potential confounding factors,
all income groups would cluster near 1.0, creating an even distribution. Yet, at the highest bins of
income groups, this is nowhere near the results that are seen.
The widening gaps at higher tiers suggest that selectivity amplifies the inequality that exists
between income groups at colleges across the country. Given the income disparaties that exist between
different races and ethnicities here in the United States, this makes the disparities in representation
all the more important.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION 2
# ---------------------------------------------------------
st.markdown('<div class="section-title">2. Applications vs Enrollment</div>', unsafe_allow_html=True)

pipeline = (
    df.groupby(["par_income_lab", "par_income_bin"], as_index=False)
      .agg({"rel_apply": "mean", "rel_attend": "mean"})
)

pipeline_long = pipeline.melt(
    id_vars=["par_income_lab", "par_income_bin"],
    value_vars=["rel_apply", "rel_attend"],
    var_name="Stage",
    value_name="Value"
)

pipeline_long["Stage"] = pipeline_long["Stage"].map({
    "rel_apply": "Application Rate",
    "rel_attend": "Attendance Rate"
})

chart2 = alt.Chart(pipeline_long).mark_line(point=True).encode(
    x=alt.X("par_income_lab:N", sort=alt.SortField("par_income_bin"), title="Parental Income Group"),
    y=alt.Y("Value:Q", title="Relative Rate (1.0 = expected)"),
    color=alt.Color("Stage:N"),
    tooltip=["par_income_lab", "Stage", "Value"]
).properties(height=450)

st.altair_chart(chart2, use_container_width=True)

st.markdown("""
<div class="insight-box">
This visualization separates two mechanisms:
<ul>
<li><b>Application differences</b>: who enters the pipeline</li>
<li><b>Attendance differences</b>: who ultimately enrolls</li>
</ul>
Given that the gap between income groups already exists at the application stage,
then inequality is not only an admissions issue; it is also a pre-admissions system.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION 3
# ---------------------------------------------------------
st.markdown('<div class="section-title">3. The Conditions After Applying</div>', unsafe_allow_html=True)

cond = (
    df.groupby(["par_income_lab", "par_income_bin"], as_index=False)
      .agg({"rel_att_cond_app": "mean"})
)

chart3 = alt.Chart(cond).mark_bar().encode(
    x=alt.X("par_income_lab:N", sort=alt.SortField("par_income_bin")),
    y=alt.Y("rel_att_cond_app:Q", title="Attendance Conditional on Application"),
    tooltip=["par_income_lab", "rel_att_cond_app"]
).properties(height=420)

st.altair_chart(chart3, use_container_width=True)

st.markdown("""
<div class="insight-box">
This visualization isolates what happens after students have already made it into the applicant pool.
Even here, income gradients persist, suggesting that disparities are not only about who applies,
but also about how institutions evaluate similar applicants.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION 4 (REBUILT + SIMPLIFIED)
# ---------------------------------------------------------
st.markdown('<div class="section-title">4. The Income Gradient in Elite Access</div>', unsafe_allow_html=True)

top = (
    df.groupby("par_income_lab", as_index=False)
      .agg({"rel_attend": "mean"})
)

chart4 = alt.Chart(top).mark_bar().encode(
    x=alt.X("par_income_lab:N", sort="-y", title="Parental Income Group"),
    y=alt.Y("rel_attend:Q", title="Relative Attendance"),
    tooltip=["par_income_lab", "rel_attend"]
).properties(height=420)

st.altair_chart(chart4, use_container_width=True)

st.markdown("""
<div class="insight-box">
The steepness of this gradient reveals a significant question of the affirmative action debate.
Is selective education distributing opportunity solely based on achievement,
or is it also reinforcing pre-existing economic hierarchies?
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# CONCLUSION
# ---------------------------------------------------------
st.markdown('<div class="section-title">The Takeaway</div>', unsafe_allow_html=True)

st.markdown("""
<div class="text-block">
From these four visualizations, there exists a consistent pattern:
inequality is not concentrated in a single stage of the college pipeline.
It accumulates, starting from years before an individual applies for college and
and continuing through the years after they've graduated.
</div>

<div class="text-block">
By the time admissions decisions are made, much of the distribution has already been shaped by
access to preparation, information, and institutional signaling long before the application is submitted.
</div>

<div class="insight-box">
Thus, affirmative action is reframed from a question of “who gets in” to a much deeper one:
<b>where in the pipeline should justice intervene?</b>
</div>
""", unsafe_allow_html=True)