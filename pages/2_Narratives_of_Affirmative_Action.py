import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Narratives of Affirmative Action",
    page_icon="⚖️",
    layout="wide"
)

# ---------------------------------------------------------
# STYLE (MATCH TIMELINE PAGE)
# ---------------------------------------------------------
st.markdown("""
<style>
.main { background: linear-gradient(to bottom, #fdfdfd, #ffffff); }

/* PAGE HEADER */
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

/* SECTION TITLES */
.section-title {
    text-align: center;
    font-size: 1.8rem;
    font-weight: 800;
    margin-top: 3rem;
    margin-bottom: 1.5rem;
    color: #1a2a6c;
}

/* CARD BLOCK (like timeline blocks) */
.narrative-block {
    padding: 25px;
    border-left: 5px solid #1a2a6c;
    margin-bottom: 25px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

/* PERSON NAME */
.person-title {
    font-size: 1.4rem;
    font-weight: 800;
    color: #333;
    margin-bottom: 10px;
}

/* QUOTE */
.quote {
    font-size: 1.05rem;
    font-style: italic;
    color: #222;
    margin-bottom: 12px;
}

/* CONTEXT */
.context {
    font-size: 1.05rem;
    line-height: 1.8;
    color: #333;
    margin-bottom: 12px;
}

/* SOURCE */
.source {
    font-size: 0.95rem;
    color: #666;
}

.source a {
    color: #1a2a6c;
    text-decoration: none;
    font-weight: 600;
}

.source a:hover {
    text-decoration: underline;
}

/* FINAL INSIGHT */
.final-box {
    margin-top: 3rem;
    padding: 20px;
    background-color: #f0f4f8;
    border-left: 5px solid #b22222;
    border-radius: 6px;
    font-size: 1.05rem;
    line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown("""
<div class="page-header">
    <h1>Narratives of Affirmative Action</h1>
    <p>Quantitative data shows structure, but it is these narratives that show lived experience and the first-hand impact of affirmative action.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================================================
# INTRO
# =========================================================
st.markdown("""
<div class="final-box">
This project is grounded in quantitative evidence, including SAT distributions, income gradients, and admissions pipelines.
However, numbers alone cannot capture how affirmative action is experienced, interpreted, or contested. These narratives show that merit is not only measured statistically, but shaped through qualitative factors, such as identity and perception.
</div>
""", unsafe_allow_html=True)

# =========================================================
# PRO AFFIRMATIVE ACTION
# =========================================================
st.markdown('<div class="section-title">I. Pro-Affirmative Action Narratives</div>', unsafe_allow_html=True)

st.markdown("""
<div class="narrative-block">
<div class="person-title">Jaleel Gomes Cardoso — <a href="https://hechingerreport.org/how-did-students-pitch-themselves-to-colleges-after-last-years-affirmative-action-ruling/" target="_blank">Hechinger Report (2026)</a></div>

<div class="quote">
“If you're not going to see what my race is in my application, then I'm definitely putting it in my writing — because you have to know that this is the person who I am.”
</div>

<div class="context">
Cardoso wanted to write about being part of the Black community for his Yale essay, but felt the ruling made it "a risky decision." He ultimately centered his racial identity anyway, didn't get into Yale, but was accepted to Dartmouth. His essay excerpt included: "I was thrust into a narrative of indifference and insignificance from the moment I entered this world. I was labeled as black, which placed me in the margins of society."
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="narrative-block">
<div class="person-title">Kayla Nguyen — <a href="https://www.newsweek.com/i-was-asian-hurt-affirmative-action-college-usa-1818195" target="_blank">Newsweek (2023)</a></div>

<div class="quote">
“Dismantling programs like affirmative action only furthers ingrained biases in our future generations of students.”
</div>

<div class="context">
A second-generation Asian American at UNC — one of the two universities named in SFFA v. Harvard. She argues the model minority myth creates a false wedge between Asian and Black communities, and that the SFFA lawsuit strategically used Asian American students as proxies to benefit white applicants. She pushes back directly on the narrative that Asian Americans were the primary victims of affirmative action.
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="narrative-block">
<div class="person-title">Justice Ketanji Brown Jackson — <a href="https://www.cbsnews.com/news/read-text-dissent-supreme-court-affirmative-action-ruling-opinions-justices-sotomayor-jackson/" target="_blank">CBS News</a> / <a href="https://www.thenation.com/article/society/kbj-dissent-affirmative-action/" target="_blank">The Nation</a></div>

<div class="quote">
“With let-them-eat-cake obliviousness, today the majority pulls the ripcord and announces 'colorblindness for all' by legal fiat. But deeming race irrelevant in law does not make it so in life.”
</div>

<div class="context">
Jackson dissented in the UNC case (she recused herself from Harvard due to her prior role on Harvard's Board of Overseers). Her 29-page dissent opens with: "Gulf-sized race-based gaps exist with respect to the health, wealth, and well-being of American citizens. They were created in the distant past, but have indisputably been passed down to the present day through the generations." She called the ruling "a tragedy for us all." She also pointedly noted the irony that the ruling carves out an exception for military academies — meaning racial diversity is worth preserving for the bunker, but not the boardroom.
</div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# ANTI AA
# =========================================================
st.markdown('<div class="section-title">II. Anti-Affirmative Action Narratives</div>', unsafe_allow_html=True)

st.markdown("""
<div class="narrative-block">
<div class="person-title">Jon Wang — <a href="https://nextshark.com/jon-wang-asian-student-affirmative-action" target="_blank">NextShark / Fox News (2023)</a></div>

<div class="quote">
“They told me I had a 20% chance of getting into Harvard as an Asian American and a 95% chance as an African American.”
</div>

<div class="context">
Wang had a 4.65 GPA and a 1590 SAT score and was rejected by MIT, Caltech, Princeton, Harvard, Carnegie Mellon, and UC Berkeley. He joined SFFA and became one of the public faces of the anti-affirmative action movement. He has said he risks career backlash for speaking out but believes he's "fighting for future generations of Asian Americans."
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="narrative-block">
<div class="person-title">Abigail Fisher — <a href="https://www.npr.org/2012/10/10/162666053/the-woman-behind-the-affirmative-action-case" target="_blank">NPR</a></div>

<div class="quote">
“I was taught from the time I was a little girl that any good thing that happens to you, you worked for it...”
</div>

<div class="context">
Fisher applied to the University of Texas at Austin in 2008 and was rejected. She filed suit arguing that less-qualified minority students were admitted over her, violating the Equal Protection Clause of the 14th Amendment. Her case went to the Supreme Court twice — in 2013 the Court sent it back to lower courts, and in 2016 the Court narrowly upheld UT's holistic admissions system. She did not ultimately win her case, but her decade-long fight laid critical legal groundwork for SFFA v. Harvard. Fisher later became a leader within Students for Fair Admissions — the organization that ultimately succeeded where her case did not.

</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="narrative-block">
<div class="person-title">Michael Wang — <a href="https://en.wikipedia.org/wiki/Students_for_Fair_Admissions_v._Harvard" target="_blank">Case History</a></div>

<div class="quote">
“A part of me regrets what I've put forward.”
</div>

<div class="context">
Michael Wang was an earlier "poster child" for the anti-affirmative action movement, filing discrimination complaints against three universities with the Department of Education's Office for Civil Rights in 2013 after his own elite college rejections. He later clarified he was not "anti-affirmative action" per se, but supported reforming it — a notable evolution that complicates any simple pro/anti framing.
</div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# COMPLEX
# =========================================================
st.markdown('<div class="section-title">III. Complex Narratives</div>', unsafe_allow_html=True)

st.markdown("""
<div class="narrative-block">
<div class="person-title">Klaryssa Cobian — <a href="https://hechingerreport.org/how-did-students-pitch-themselves-to-colleges-after-last-years-affirmative-action-ruling/" target="_blank">Hechinger Report</a></div>

<div class="quote">
“Which mattress I sleep on has defined my life, my independence, my dependence.”
</div>

<div class="context">
Cobian had originally planned to write about sacrificing her Latino culture and identity in pursuit of education — but hesitated after the ruling. She ultimately chose to write about poverty instead: sleeping in a car, sharing a mattress with her sister, moving from couch to couch. Her essay's opening line: "Which mattress I sleep on has defined my life, my independence, my dependence." She got into UC Berkeley. Her story captures the impossible calculation the ruling forced: identity vs. safety.

</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="narrative-block">
<div class="person-title">Harmony Moore — <a href="https://www.cnn.com/2023/12/26/us/college-admissions-race-essays-reaj/index.html" target="_blank">CNN (2023)</a></div>

<div class="quote">
“I completely just removed that from my essays. I didn't want to have the wrong admissions officer read it...”
</div>

<div class="context">
Moore originally wrote several essays about her experience as a Black student navigating her predominantly white Houston high school. After the ruling, she rewrote them entirely — removing explicit mentions of race while keeping involvement in Black-led organizations like the NAACP in her extracurriculars. Her story illustrates the "chilling effect": not just what students wrote, but what they chose not to write.
</div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# FINAL TAKEAWAY
# =========================================================
st.markdown("""
<div class="final-box">
Even though this project is built on quantitative data, these narratives show what the numbers cannot:
how individuals interpret, adapt to, and are constrained by systems of inequality.
</div>
""", unsafe_allow_html=True)