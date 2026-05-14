import streamlit as st
import pandas as pd
import altair as alt
import os

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Structures of Inequality",
    page_icon="⚖️",
    layout="wide"
)

DATA_PATH = "assets/CollegeAdmissions_Data.csv"

# ---------------------------------------------------------
# STYLE
# ---------------------------------------------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(to bottom, #fdfdfd, #ffffff);
}

/* HEADER */
.page-header {
    text-align: center;
    margin-top: 10px;
    margin-bottom: 35px;
}

.page-header h1 {
    font-size: 3rem;
    font-weight: 800;
    color: #1a2a6c;
    margin-bottom: 6px;
}

.page-header p {
    font-size: 1.2rem;
    color: #666;
}

/* SECTIONS */
.section-title {
    font-size: 1.7rem;
    font-weight: 750;
    color: #1a2a6c;
    margin-top: 40px;
    margin-bottom: 12px;
}

/* TEXT */
.text-block {
    font-size: 1.08rem;
    line-height: 1.9;
    color: #333;
    margin-bottom: 16px;
    text-align: justify;
}

/* INSIGHT BOX */
.insight-box {
    background-color: #f0f4f8;
    padding: 16px;
    border-radius: 8px;
    border-left: 4px solid #1a2a6c;
    margin: 18px 0;
    font-size: 1.02rem;
    line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown("""
<div class="page-header">
    <h1>Structures of Inequality</h1>
    <p>Affirmative action operates not at the moment of a college admissions decision, but in response to inequality that is already structurally produced.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# INTRODUCTION (EXPANDED)
# ---------------------------------------------------------
st.markdown('<div class="section-title">What does the data actually show?</div>', unsafe_allow_html=True)

st.markdown("""
<div class="text-block">
Discussions about affirmative action often begin at the point of college admissions decisions.
However, this framing can be misleading; it assumes that students arrive at the admissions stage with
comparable preparation, opportunity, and access.
</div>

<div class="text-block">
The data used on this page suggests something more structural: by the time students apply to selective colleges,
the distribution of opportunity has already been shaped by factors far outside the admissions office.
These include differences in household income, school quality, access to advanced coursework,
test preparation resources, among other factors.
</div>

<div class="text-block">
This means that merit, often treated as an objective measure of ability, is itself partially the outcome of
unequal conditions long before any college application is submitted.
</div>

<div class="insight-box">
This page uses data from the Opportunity Insights project to examine how inequality accumulates across the college pipeline.
Rather than treating admissions as the origin of disparity, it treats it as one stage in a longer structural process.
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
st.markdown('<div class="section-title">1. Representation in Selective Colleges</div>', unsafe_allow_html=True)

tier_income = (
    df.groupby(["tier_name", "par_income_lab", "par_income_bin"], as_index=False)
      .agg({"rel_attend": "mean"})
)

chart1 = alt.Chart(tier_income).mark_line(point=True).encode(
    x=alt.X("par_income_lab:N", sort=alt.SortField("par_income_bin"), title="Parental Income Group"),
    y=alt.Y("rel_attend:Q", title="Relative Attendance (1.0 = expected)"),
    color="tier_name:N",
    tooltip=["tier_name", "par_income_lab", "rel_attend"]
).properties(
    height=600,
    title="Selective College Attendance by Income Group"
)

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
    height=600,
    title="Median Income by Race/Ethnicity"
)

st.altair_chart(chart, use_container_width=True)

st.markdown("""
<div class="text-block">
At selective colleges, attendance is not evenly distributed across income groups.
Higher-income students are consistently overrepresented relative to their population share,
while lower-income students are underrepresented.
</div>

<div class="text-block">
This pattern is not explained solely by admissions decisions.
Instead, it reflects earlier inequalities in preparation and access that shape who becomes
a competitive applicant in the first place.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION 2
# ---------------------------------------------------------
st.markdown('<div class="section-title">2. Applications vs. Enrollment</div>', unsafe_allow_html=True)

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
).properties(height=600, title="Application, Attendance Rate by Income Group")

st.altair_chart(chart2, use_container_width=True)

st.markdown("""
<div class="text-block">
One of the most important distinctions in the pipeline is between application behavior and enrollment outcomes.
Even before admissions committees evaluate students, application rates themselves differ substantially by income.
</div>

<div class="text-block">
This means inequality is not solely a product of institutional selection.
It is also embedded in who perceives selective colleges as accessible, who has the resources to apply,
and who receives guidance to navigate the process.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION 3
# ---------------------------------------------------------
st.markdown('<div class="section-title">3. Conditional Outcomes After Application</div>', unsafe_allow_html=True)

cond = (
    df.groupby(["par_income_lab", "par_income_bin"], as_index=False)
      .agg({"rel_att_cond_app": "mean"})
)

chart3 = alt.Chart(cond).mark_bar().encode(
    x=alt.X("par_income_lab:N", sort=alt.SortField("par_income_bin")),
    y=alt.Y("rel_att_cond_app:Q", title="Attendance Conditional on Application"),
    tooltip=["par_income_lab", "rel_att_cond_app"]
).properties(height=600)

st.altair_chart(chart3, use_container_width=True)

st.markdown("""
<div class="text-block">
Even after controlling for who applies, the disparities remain.
This suggests that evaluation and admission processes do not fully counteract existing inequalities.
</div>

<div class="text-block">
Of course, this does not imply intentional bias alone.
It reflects the difficulty of separating merit from its determining conditions,
where preparation, environment, and resources are already unevenly distributed.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION 4
# ---------------------------------------------------------
st.markdown('<div class="section-title">4. Income Gradient in Elite Access</div>', unsafe_allow_html=True)

top = (
    df.groupby("par_income_lab", as_index=False)
      .agg({"rel_attend": "mean"})
)

chart4 = alt.Chart(top).mark_bar().encode(
    x=alt.X("par_income_lab:N", sort="-y", title="Parental Income Group"),
    y=alt.Y("rel_attend:Q", title="Relative Attendance"),
    tooltip=["par_income_lab", "rel_attend"]
).properties(
    height=600,
    title="Income Gradient in Elite College Attendance"
)

st.altair_chart(chart4, use_container_width=True)

st.markdown("""
<div class="text-block">
The steep gradient in elite attendance illustrates a core claim of this project:
selective education operates on a playing field already shaped by broader socioeconomic inequality.
</div>

<div class="text-block">
Affirmative action, in this context, is an attempt to respond to the fact that merit itself is something that is socially and economically produced.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# CONCLUSION
# ---------------------------------------------------------
st.markdown('<div class="section-title">Key Takeaway</div>', unsafe_allow_html=True)

st.markdown("""
<div class="text-block">
Across all stages of the college pipeline, inequality accumulates rather than appears at a single decision point.
By the time admissions decisions are made, much of the variation in outcomes has already been shaped by structural conditions
outside the control of applicants.
</div>

<div class="text-block">
This reframes this problem as a response to its pre-existing limitations.
It functions as an intervention in a system where inequality is already embedded.
</div>

<div class="insight-box">
The central question is not whether affirmative action introduces inequality, but where in the process society chooses to address inequality that already exists.
</div>
""", unsafe_allow_html=True)
