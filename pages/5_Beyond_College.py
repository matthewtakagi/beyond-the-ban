import streamlit as st
import pandas as pd
import altair as alt

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Beyond College",
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
    margin-bottom: 0.3rem;
}

.page-header p {
    font-size: 1.2rem;
    color: #666;
    max-width: 950px;
    margin: auto;
    line-height: 1.7;
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
    margin: 20px 0;
    line-height: 1.8;
}

.justice-box {
    padding: 22px;
    background-color: #f8f9fc;
    border-left: 6px solid #8B0000;
    border-radius: 8px;
    margin: 25px 0;
    line-height: 1.8;
}

.big-stat {
    font-size: 2.4rem;
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
    <h1>Beyond College</h1>
    <p>
        If affirmative action debates focus only on admissions,
        they miss the larger structural question:
        <b>what happens beyond just college?</b>
        Education shapes opportunity,
        and labor markets determine whether opportunity converts into income,
        mobility, and long-term security.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# INTRO
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">I. Why Economic Outcomes Matter</div>

<div class="text-block">
One of the most common critiques of affirmative action is that it unfairly alters opportunity at the admissions stage, assuming that once students enter higher education or employment,
systems become more neutral and affirmative action loses its significance.
</div>

<div class="text-block">
This being said, inequality does not end at admission. It continues through wages, hiring patterns, promotion structures,
occupational segregation, and generational wealth accumulation.
</div>

<div class="text-block">
This investigation asks a broader question:
if access becomes more equal, do outcomes become equal too?
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION II — EDUCATION & EARNINGS
# ---------------------------------------------------------
st.markdown('<div class="section-title">II. Education Still Pays (Unevenly)</div>', unsafe_allow_html=True)

edu_income = pd.DataFrame({
    "Education": [
        "No HS Diploma",
        "HS Diploma",
        "Some College",
        "Bachelor's+"
    ],
    "Median Earnings": [40450, 50640, 60220, 91250]
})

chart1 = alt.Chart(edu_income).mark_bar().encode(
    x=alt.X("Education:N", sort=None),
    y=alt.Y("Median Earnings:Q", title="Median Annual Earnings (USD)"),
    tooltip=["Education", "Median Earnings"]
).properties(
    height=650,
    title="2024 Median Earnings by Educational Attainment"
)

st.altair_chart(chart1, use_container_width=True)

st.markdown("""
<div class="text-box">
A bachelor’s degree or higher corresponds to median earnings of roughly <b>$91,250</b>,
compared to <b>$40,450</b> for those without a high school diploma.  
Education remains one of the strongest predictors of earnings, yet access to educational attainment itself is unequal.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION III — RACE & EARNINGS
# ---------------------------------------------------------
st.markdown('<div class="section-title">III. Race and Earnings Among Full-Time Workers</div>', unsafe_allow_html=True)

race_income = pd.DataFrame({
    "Group": ["Asian", "White (Non-Hispanic)", "Hispanic", "Black"],
    "Median Earnings": [86560, 71260, 63140, 52370]
})

chart2 = alt.Chart(race_income).mark_bar().encode(
    x=alt.X("Group:N", sort="-y"),
    y=alt.Y("Median Earnings:Q", title="Median Annual Earnings (USD)"),
    tooltip=["Group", "Median Earnings"]
).properties(
    height=650,
    title="2024 Median Earnings by Race/Ethnicity"
)

st.altair_chart(chart2, use_container_width=True)

gap = 86560 - 52370

st.markdown(f"""
<div class="insight-box">
<div class="big-stat">${gap:,}</div>
gap between Asian and Black median earnings among full-time, year-round workers.
Substantial disparities remain even after labor force participation.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="text-block">
Of course, this does not mean race alone determines outcomes.
It reflects the aforementioned structures, among other things:
educational access, occupational sorting, discrimination,
wealth inheritance, social capital, and geography.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION IV — GENDER GAP
# ---------------------------------------------------------
st.markdown('<div class="section-title">IV. Gender and the Wage Gap</div>', unsafe_allow_html=True)

gender_df = pd.DataFrame({
    "Group": ["Male", "Female"],
    "Median Earnings": [71090, 57520]
})

chart3 = alt.Chart(gender_df).mark_bar().encode(
    x=alt.X("Group:N"),
    y=alt.Y("Median Earnings:Q"),
    tooltip=["Group", "Median Earnings"]
).properties(
    height=650,
    title="2024 Median Earnings by Gender"
)

st.altair_chart(chart3, use_container_width=True)

st.markdown("""
<div class="text-box">
Women earned approximately <b>80.9%</b> of male earnings in 2024,
according to U.S. Census data.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION V — PIPELINE ARGUMENT
# ---------------------------------------------------------
st.markdown('<div class="section-title">The Pipeline Does Not End at College</div>', unsafe_allow_html=True)

st.markdown("""
<div class="text-block">
Earlier pages examined how inequality shapes the different processes through education, 
but labor market outcomes reveal that inequality is not solved simply by access.
Even after entering the workforce,
earnings remain stratified.
</div>

<div class="justice-box">
This complicates the “meritocracy” argument:
if opportunity is unequal before college,
and outcomes remain unequal after college,
then justice cannot be reduced to a single admissions decision.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECTION VI — WEALTH VS INCOME
# ---------------------------------------------------------
st.markdown('<div class="section-title">Income Is Not Wealth</div>', unsafe_allow_html=True)

st.markdown("""
<div class="text-block">
As a reminder, income measures yearly earnings.
Wealth measures accumulated security, not limited to but including
home ownership, savings, inherited assets,
business ownership, and intergenerational transfer.
</div>

<div class="text-block">
This distinction matters because even similar salaries
can produce radically different life outcomes
depending on debt, family support, and inherited resources.
</div>

<div class="insight-box">
Affirmative action debates often focus on immediate access,
but structural inequality is also reproduced through wealth,
not just wages. We would encourage further exploration into this crucial distinction and discrepancy that exists today.
</div>
""", unsafe_allow_html=True)

st.divider()

st.caption("Sources: U.S. Census Bureau, Income in the United States: 2024 (P60-286); CPS ASEC Table A-6.")