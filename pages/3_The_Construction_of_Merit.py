# pages/4_The_Construction_of_Merit.py
# Beyond the Ban | Page 4
# THE CONSTRUCTION OF MERIT
# SAT Scores, Family Background, and the Myth of Equal Preparation

import streamlit as st
import pandas as pd
import altair as alt
import os

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="The Construction of Merit | Beyond the Ban",
    page_icon="📘",
    layout="wide"
)

# ---------------------------------------------------------
# STYLE — streamlined to match site aesthetic
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
    color: #1a2a6c;
    font-size: 3rem;
    margin-bottom: 0.2rem;
}
.page-header p {
    font-size: 1.2rem;
    color: #666;
    max-width: 900px;
    margin: auto;
}
.section-box {
    padding: 22px;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    margin-bottom: 25px;
}
.justice-box {
    padding: 25px;
    background-color: #f8f9fc;
    border-left: 6px solid #8B0000;
    border-radius: 8px;
    margin: 25px 0;
    line-height: 1.8;
}
.insight-box {
    padding: 18px;
    background-color: #f0f4f8;
    border-left: 5px solid #1a2a6c;
    border-radius: 8px;
    margin-top: 15px;
    line-height: 1.7;
}
.big-stat {
    font-size: 2.4rem;
    font-weight: 800;
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
        Standardized testing has often been framed as an objective measure of merit.
        But what if merit itself reflects unequal access to preparation,
        educational resources, and inherent structural advantage?
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# JUSTICE FRAME
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">
    <h3 style='color:#8B0000;'>Is merit measured, or is it manufactured?</h3>
    <p>
        SAT scores are frequently treated as unbiased indicators of college readiness.
        Yet, test performance is deeply shaped by parental education,
        economic resources, school quality, language environment,
        and long-term, persistent structural inequalities.
    </p>
    <p>
        If students do not begin from the same baseline,
        then numerical data may not simply identify talent.
            They also reflect the notion of unequal opportunity that exists in America today.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------
DATA_PATH = "assets/SAT_Data.csv"

if not os.path.exists(DATA_PATH):
    st.error("SAT_Data.csv not found in assets folder.")
    st.stop()

# ---------------------------------------------------------
# CLEAN RAW CSV
# ---------------------------------------------------------
raw = pd.read_csv(DATA_PATH, header=None)

# Pull relevant parental education rows manually
rows = raw[raw[0].astype(str).str.contains(
    "No high school diploma|High school diploma|Associate's degree|Bachelor's degree|Graduate degree",
    na=False
)].copy()

# Column map for 2022:
# col18 = number, col19 = %, col20 = total, col21 = ERW, col22 = Math
# Since CSV indexing starts at 0, actual columns are 16–20
parent_ed = pd.DataFrame({
    "Parental Education": rows[0].astype(str).str.strip(),
    "Participation_2022": rows[16].astype(str).str.replace(",", "", regex=False),
    "Percent_2022": rows[17],
    "Total_2022": rows[18],
    "ERW_2022": rows[19],
    "Math_2022": rows[20]
})

# Numeric cleanup
for col in ["Participation_2022", "Percent_2022", "Total_2022", "ERW_2022", "Math_2022"]:
    parent_ed[col] = pd.to_numeric(parent_ed[col], errors="coerce")

parent_ed = parent_ed.dropna()

# Ordered categories
education_order = [
    "No high school diploma",
    "High school diploma",
    "Associate's degree",
    "Bachelor's degree",
    "Graduate degree"
]

parent_ed["Parental Education"] = pd.Categorical(
    parent_ed["Parental Education"],
    categories=education_order,
    ordered=True
)

parent_ed = parent_ed.sort_values("Parental Education")

# ---------------------------------------------------------
# SECTION 1 — SAT SCORE BY PARENT EDUCATION
# ---------------------------------------------------------
st.subheader("1. SAT Scores Rise Dramatically with Parental Education")

chart1 = alt.Chart(parent_ed).mark_bar().encode(
    x=alt.X(
        "Parental Education:N",
        sort=education_order,
        title="Highest Level of Parental Education"
    ),
    y=alt.Y(
        "Total_2022:Q",
        title="Average Total SAT Score (2022)"
    ),
    tooltip=[
        alt.Tooltip("Parental Education:N"),
        alt.Tooltip("Total_2022:Q", title="SAT Score")
    ]
).properties(
    height=500
)

st.altair_chart(chart1, use_container_width=True)

score_gap = int(
    parent_ed[parent_ed["Parental Education"] == "Graduate degree"]["Total_2022"].iloc[0] -
    parent_ed[parent_ed["Parental Education"] == "No high school diploma"]["Total_2022"].iloc[0]
)

st.markdown(f"""
<div class="insight-box">
    <div class="big-stat">{score_gap}-point gap</div>
    Students whose parents hold graduate degrees score dramatically higher on average
    than students whose parents did not complete high school.
    <br><br>
    This gap is larger than many admissions margins at selective colleges.
</div>
""", unsafe_allow_html=True)

st.markdown("""
**Interpretation:**  
This does not mean intelligence is inherited by educational status.  
It suggests that preparation, educational environment, tutoring access,
school funding, and accumulated social capital profoundly shape measurable outcomes.
""")

st.divider()

# ---------------------------------------------------------
# SECTION 2 — SAT PARTICIPATION
# ---------------------------------------------------------
st.subheader("2. Who Even Enters the Meritocracy? SAT Participation by Family Background")

chart2 = alt.Chart(parent_ed).mark_line(point=True).encode(
    x=alt.X(
        "Parental Education:N",
        sort=education_order,
        title="Highest Level of Parental Education"
    ),
    y=alt.Y(
        "Percent_2022:Q",
        title="% of SAT Test-Taking Population"
    ),
    tooltip=[
        alt.Tooltip("Parental Education:N"),
        alt.Tooltip("Percent_2022:Q", format=".1f")
    ]
).properties(
    height=500
)

st.altair_chart(chart2, use_container_width=True)

st.markdown("""
**Why this matters:**  
Merit systems do not simply reward performance —
they first depend on participation.

Students from more educated households are often more likely to:
- Take college entrance exams  
- Receive application guidance  
- Access preparation resources  
- View selective college as attainable  

This means inequality can shape not only scores,
but who enters the competitive arena at all.
""")

st.divider()

# ---------------------------------------------------------
# SECTION 3 — ERW vs MATH
# ---------------------------------------------------------
st.subheader("3. Merit Is Multi-Dimensional: Section Performance by Family Background")

long_scores = parent_ed.melt(
    id_vars=["Parental Education"],
    value_vars=["ERW_2022", "Math_2022"],
    var_name="Section",
    value_name="Score"
)

long_scores["Section"] = long_scores["Section"].replace({
    "ERW_2022": "ERW",
    "Math_2022": "Math"
})

chart3 = alt.Chart(long_scores).mark_line(point=True).encode(
    x=alt.X(
        "Parental Education:N",
        sort=education_order,
        title="Highest Level of Parental Education"
    ),
    y=alt.Y("Score:Q", title="Average Section Score"),
    color=alt.Color("Section:N"),
    tooltip=["Parental Education", "Section", "Score"]
).properties(
    height=500
)

st.altair_chart(chart3, use_container_width=True)

st.markdown("""
**Key Observation:**  
Both reading and math performance rise consistently with parental education,
suggesting broad structural influence rather than isolated subject-specific differences.
""")

st.divider()

# ---------------------------------------------------------
# SECTION 4 — JUSTICE SYNTHESIS
# ---------------------------------------------------------
st.subheader("4. So What Does This Mean for Meritocracy?")

st.markdown("""
<div class="justice-box">
    <h3 style='color:#8B0000;'>Merit is not created in a vacuum.</h3>
    <p>
        Standardized scores may measure performance,
        but performance itself develops through unequal systems:
        household stability, parental knowledge, school quality,
        tutoring, neighborhood opportunity, and financial security.
    </p>
    <p>
        When admissions rely heavily on metrics shaped by unequal preparation,
        institutions may reward prior advantage while appearing neutral.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# FINAL CLAIM
# ---------------------------------------------------------
st.divider()

st.subheader("What This Page Argues")

st.markdown("""
### Meritocracy can reproduce inequality when opportunity is unequal.

This page suggests that:
- Test scores are powerful predictors  
- But predictors are socially conditioned  
- Structural inequality shapes measurable “merit”  
- Equal treatment at the endpoint does not guarantee fairness at the starting line  

## Bottom Line:
**Affirmative action does not necessarily distort meritocracy.  
It can function as an intervention within a system where merit itself has been unevenly constructed.**
""")