import streamlit as st
import os

st.set_page_config(
    page_title="US Affirmative Action | Beyond the Ban",
    page_icon="⚖️",
    layout="wide"
)

MEDIA_DIR = "media"

st.markdown("""
<style>
.main { background: linear-gradient(to bottom, #fdfdfd, #ffffff); }
.timeline-header { text-align: center; padding: 20px 0 10px 0; }
.timeline-block {
    padding: 25px;
    border-left: 5px solid #1a2a6c;
    margin-left: 30px;
    margin-bottom: 20px;
    position: relative;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.timeline-dot {
    position: absolute;
    left: -15px;
    top: 30px;
    height: 24px;
    width: 24px;
    background: #1a2a6c;
    border: 4px solid white;
    border-radius: 50%;
}
.timeline-year { font-size: 2.2rem; font-weight: 900; color: #1a2a6c; line-height: 1; }
.news-banner {
    background-color: #000;
    color: #fff;
    padding: 12px;
    font-family: 'Courier New', Courier, monospace;
    text-transform: uppercase;
    font-size: 1.1rem;
    letter-spacing: 1px;
    margin: 10px 0;
    border-radius: 4px;
}
.news-meta { font-size: 0.85rem; color: #aaa; margin-bottom: 15px; font-style: italic; }
.context-box { font-size: 1.05rem; line-height: 1.8; color: #333; margin-top: 15px; text-align: justify; }
.significance {
    margin-top: 15px;
    padding: 15px;
    background-color: #f0f4f8;
    border-radius: 6px;
    font-size: 0.95rem;
    border-left: 4px solid #b22222;
}
.era-header {
    text-align: center;
    margin: 60px 0 40px 0;
    font-family: 'Georgia', serif;
    color: #b22222;
    border-top: 2px solid #eee;
    padding-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="timeline-header">
    <h1>How We Got Here</h1>
    <p style="font-size:1.2rem; color:#666;">From the 1800s until now, a history of race-conscious policy, legal pivots, and the quest for equity in the United States.</p>
</div>
""", unsafe_allow_html=True)

TIMELINE_DATA = [
    {
        "year": "1865",
        "title": "Establishment of the Freedmen’s Bureau",
        "news_headline": "FREEDMEN'S BUREAU BILL ADOPTED",
        "news_source": "New York Daily Tribune",
        "news_date": "March 4, 1865",
        "context": """In the chaotic wake of the Civil War, Congress established the Bureau of Refugees, Freedmen, and Abandoned Lands. This was the first time the U.S. government undertook a massive relief and social welfare program aimed at a specific group. Led by General Oliver O. Howard, the Bureau was tasked with transforming a slave society into a free labor system. It issued millions of rations, established over 1,000 schools (founding many HBCUs), and managed medical care for four million newly freed people. However, the agency was constantly under fire from President Andrew Johnson, who vetoed its expansion, arguing that the federal government should not provide special assistance to one race over another, a rhetorical seed that would grow into modern anti-affirmative action arguments.""",
        "significance": "It represented the very first federal experiment in proactive equity, proving that freedom required tangible resources like land and education to be meaningful.",
        "image_file": "freedmens_bureau.jpg"
    },
    {
        "year": "1896",
        "title": "Plessy v. Ferguson",
        "news_headline": "SEPARATE COACH LAW UPHELD",
        "news_source": "The Washington Post",
        "news_date": "May 19, 1896",
        "context": """The Supreme Court's 7-1 ruling in Plessy v. Ferguson codified the doctrine of 'separate but equal.' Homer Plessy challenged a Louisiana law requiring segregated train cars. The Court ruled that as long as facilities were 'equal,' segregation did not violate the 14th Amendment. This ruling essentially gave a constitutional green light to Jim Crow laws, systematically excluding Black Americans from the economic and educational opportunities that affirmative action would later try to restore. Crucially, Justice John Marshall Harlan’s (pictured) lone dissent famously stated, 'Our Constitution is color-blind,' a phrase that ironically would be used decades later to strike down the very programs designed to fix the damage Plessy caused.""",
        "significance": "Plessy institutionalized the structural inequality that made race-conscious interventions necessary in the 20th century.",
        "image_file": "plessy.jpg"
    },
    {
        "year": "1941",
        "title": "Executive Order 8802",
        "news_headline": "ASSERTED DISCRIMINATION IN DEFENSE INDUSTRIES CONDEMNED BY PRESIDENT",
        "news_source": "Los Angeles Times",
        "news_date": "June 16, 1941",
        "context": """Facing a massive march on Washington threatened by labor leader A. Philip Randolph, President FDR signed E.O. 8802. This was the first major federal action against employment discrimination since Reconstruction. It banned racial discrimination in the nation's defense industry, then booming for WWII, and created the Fair Employment Practice Committee (FEPC). For the first time, the federal government asserted that if you took government money, you could not choose your workers based on race. It opened the doors to high-paying industrial jobs for hundreds of thousands of Black workers and established the precedent for using executive power to enforce workplace fairness.""",
        "significance": "It shifted the government from a passive observer of discrimination to an active regulator of industrial equality.",
        "image_file": "fdr_8802.jpg"
    },
    {
        "year": "1954",
        "title": "Brown v. Board of Education",
        "news_headline": "COURT'S 1896 DOCTRINE REVERSED",
        "news_source": "The Minneapolis Morning Tribune",
        "news_date": "May 18, 1954",
        "context": """In a unanimous decision led by Chief Justice Earl Warren, the Court ruled that 'separate educational facilities are inherently unequal.' This decision overturned the 'separate but equal' doctrine of Plessy v. Ferguson. The Court relied on social science data suggesting that segregation instilled a sense of inferiority in Black children. While 'Brown II' later called for desegregation with 'all deliberate speed,' the ruling served as the legal catalyst for the entire Civil Rights Movement. It established that the 14th Amendment's Equal Protection Clause required the government to actively dismantle systems of racial exclusion in public education.""",
        "significance": "Brown provided the constitutional mandate for integration, which later evolved into the affirmative action policies used to ensure diverse classrooms.",
        "image_file": "brown_board.jpg"
    },
    {
        "year": "1961",
        "title": "Executive Order 10925",
        "news_headline": "PRESIDENT ACTS TO END BIAS IN FIRMS, UNIONS",
        "news_source": "New York Herald Tribune",
        "news_date": "March 7, 1961",
        "context": """President John F. Kennedy issued E.O. 10925, which introduced the term 'affirmative action' into the American lexicon. The order required government contractors to take 'affirmative action to ensure that applicants are employed... without regard to their race, creed, color, or national origin.' This was a subtle but massive shift in philosophy: it wasn't enough to simply be neutral; institutions had to take positive, energetic steps to find and include talent that had been historically suppressed. It created the President's Committee on Equal Employment Opportunity, chaired by Vice President Lyndon B. Johnson.""",
        "significance": "This order transformed 'Affirmative Action' from a vague concept into a mandatory federal policy requirement.",
        "image_file": "jfk_10925.jpg"
    },
    {
        "year": "1964",
        "title": "Civil Rights Act of 1964",
        "news_headline": "CONTROVERSIAL CIVIL RIGHTS BILL BECOMES LAW",
        "news_source": "Philadelphia Tribune",
        "news_date": "July 4, 1964",
        "context": """Signed by President Lyndon B. Johnson following a record-breaking filibuster, the Civil Rights Act was the most comprehensive civil rights legislation in U.S. history. Title VI prohibited discrimination in programs receiving federal funds, and Title VII banned employment discrimination based on race, color, religion, sex, or national origin. It established the Equal Employment Opportunity Commission (EEOC) as an enforcement body. During the signing, LBJ noted that the law was a step toward 'total justice.' The Act provided the legislative machinery that allowed for the subsequent expansion of race-conscious hiring and admissions policies as a means of 'voluntary compliance.'""",
        "significance": "It codified the end of Jim Crow and created the statutory foundation for all future anti-discrimination and equity enforcement.",
        "image_file": "civil_rights_act.jpg"
    },
    {
        "year": "1969",
        "title": "The Philadelphia Plan",
        "news_headline": "U.S. TAKES NEW STEP TO END DISCRIMINATION IN FEDERALLY AIDED CONSTRUCTION PROGRAMS",
        "news_source": "Wall Street Journal",
        "news_date": "June 28, 1969",
        "context": """The Nixon administration implemented the 'Philadelphia Plan,' requiring federal construction contractors to meet specific 'goals and timetables' for hiring minority workers. Assistant Secretary of Labor Arthur Fletcher (the 'Father of Affirmative Action') argued that because labor unions were built on exclusion, the government had to mandate numerical targets to break the monopoly. While critics called them 'quotas,' Nixon defended the plan as a necessary tool to integrate the workforce. It was a rare moment where a Republican administration aggressively expanded race-conscious enforcement to bypass union resistance.""",
        "significance": "It introduced the controversial 'numerical goals' phase of affirmative action, moving from general promises to hard metrics.",
        "image_file": "philadelphia_plan.jpg"
    },
    {
        "year": "1972",
        "title": "Title IX of the Education Amendments",
        "news_headline": "CONGRESS CRITICIZED: BIG EDUCATION BILL IS SIGNED BY NIXON",
        "news_source": "Chicago Tribune",
        "news_date": "June 24, 1972",
        "context": """Title IX states: 'No person in the United States shall, on the basis of sex, be excluded from participation in, be denied the benefits of, or be subjected to discrimination under any education program or activity receiving Federal financial assistance.' While famously known for revolutionizing women's sports, it applied to every aspect of education, including admissions and faculty hiring. Drafted by Representative Patsy Mink and Senator Birch Bayh, it was a direct response to the exclusion of women from elite graduate and professional programs. Title IX shifted the affirmative action debate to include gender equity, proving that structural barriers affected multiple identity groups.""",
        "significance": "It drastically expanded the equality framework to ensure that federal funding could no longer support gender-based exclusion.",
        "image_file": "title_ix.jpg"
    },
    {
        "year": "1978",
        "title": "Regents of UC v. Bakke",
        "news_headline": "BAKKE WINS BUT JUSTICES UPHOLD AFFIRMATIVE ACTION",
        "news_source": "Los Angeles Times",
        "news_date": "June 29, 1978",
        "context": """The landmark case of Allan Bakke, a white applicant rejected from UC Davis Medical School, brought affirmative action to a crossroads. The Supreme Court delivered a splintered 5-4 verdict: Justice Lewis Powell ruled that while explicit quotas (set-aside seats) were unconstitutional, race could still be used as a 'plus factor' in a holistic review process. This decision pivoted the legal justification for affirmative action away from correcting past slavery and toward the educational benefits of a diverse student body. This shift from remedial justice to diversity would define the next four decades of campus policy.""",
        "significance": "This ruling created the 'Diversity' framework that higher education relied on until 2023.",
        "image_file": "bakke.jpg"
    },
    {
        "year": "1996",
        "title": "California Proposition 209",
        "news_headline": "CALIFORNIANS BACKING AFFIRMATIVE-ACTION BAN",
        "news_source": "Chicago Tribune",
        "news_date": "November 6, 1996",
        "context": """California voters passed Prop 209, a constitutional amendment banning the state from considering race, sex, or ethnicity in public employment, contracting, and education. Led by Ward Connerly, the initiative was the first successful state-level backlash against affirmative action. Following its passage, minority enrollment at elite campuses like UC Berkeley and UCLA plummeted. The UC system was forced to pioneer 'race-neutral' alternatives, such as the Top 4% plan and increased outreach to low-income ZIP codes. Prop 209 served as a national bellwether, signaling that public support for race-conscious policies was deeply divided.""",
        "significance": "It acted as the first major laboratory for a post-affirmative action world, showing the difficulty of maintaining diversity through neutral means alone.",
        "image_file": "prop209.jpg"
    },
    {
        "year": "2003",
        "title": "Grutter v. Bollinger",
        "news_headline": "AFFIRMATIVE ACTION FOR DIVERSITY IS UPHELD",
        "news_source": "The Washington Post",
        "news_date": "June 24, 2003",
        "context": """In a 5-4 decision, Justice Sandra Day O’Connor upheld the University of Michigan Law School's holistic admissions process. The Court reaffirmed that universities have a 'compelling interest' in obtaining the educational benefits that flow from a diverse student body. O’Connor famously wrote that 'race-conscious admissions policies must be limited in time,' suggesting that in 25 years, the use of racial preferences might no longer be necessary. The decision was a major victory for the Diversity rationale, though it also required that programs be 'narrowly tailored' and avoid mechanistic point systems (as seen in the companion case, Gratz v. Bollinger).""",
        "significance": "It provided a temporary safe harbor for affirmative action, while simultaneously setting an expiration date on the policy.",
        "image_file": "grutter.jpg"
    },
    {
        "year": "2013",
        "title": "Fisher v. University of Texas",
        "news_headline": "SUPREME COURT SENDS AFFIRMATIVE ACTION CASE BACK TO LOWER COURTS",
        "news_source": "Sun Reporter",
        "news_date": "June 27, 2013",
        "context": """Abigail Fisher, a white student, challenged UT Austin's 'Top Ten Percent' plan combined with holistic review. The Supreme Court did not strike down affirmative action but instead clarified the 'Strict Scrutiny' standard. Justice Kennedy's opinion stated that universities must prove that 'no workable race-neutral alternatives' would produce the same diversity benefits. This put the burden of proof squarely on the university to show that their program was the only way to achieve their goals. While Fisher eventually lost her case in 2016 (Fisher II), the 2013 ruling significantly raised the legal bar and signaled the Court's growing skepticism of any racial classification.""",
        "significance": "It introduced the 'Strict Scrutiny' trap, requiring schools to exhaust all other options before considering race.",
        "image_file": "fisher.jpg"
    },
    {
        "year": "2023",
        "title": "Students for Fair Admissions v. Harvard",
        "news_headline": "SUPREME COURT REJECTS COLLEGE AFFIRMATIVE ACTION PROGRAMS",
        "news_source": "Philadelphia Tribune",
        "news_date": "June 29, 2023",
        "context": """In a 6-3 decision, the Supreme Court effectively ended race-conscious admissions in higher education. Chief Justice John Roberts wrote that Harvard and UNC’s programs 'lack sufficiently focused and measurable objectives justifying the use of race' and 'unavoidably employ race in a negative manner.' The Court ruled that the Equal Protection Clause does not allow for racial preferences, even for the goal of diversity. While the Court noted that students could still discuss how race affected their lives in essays, the systematic use of race as a 'plus factor' was declared unconstitutional. This decision forced a total reimagining of diversity strategies across American universities and corporate boardrooms.""",
        "significance": "The definitive closure of the Bakke Era, marking a return to a legal standard of formal colorblindness.",
        "image_file": "sffa_2023.jpg"
    }
]

ERA_BREAKS = {
    "1865": "I. The Reconstruction Era",
    "1941": "II. The Executive Era",
    "1972": "III. The Diversity Era",
    "1996": "IV. The Era of Backlash & Strict Scrutiny",
    "2023": "V. The Post-Affirmative Action Era"
}

for event in TIMELINE_DATA:
    if event["year"] in ERA_BREAKS:
        st.markdown(f"<div class='era-header'><h2>{ERA_BREAKS[event['year']]}</h2></div>", unsafe_allow_html=True)

    st.markdown(f"""
        <div class="timeline-block">
            <div class="timeline-dot"></div>
            <div class="timeline-year">{event['year']}</div>
            <h3 style="margin-top:10px; color:#333;">{event['title']}</h3>
            <div class="news-banner">{event['news_headline']}</div>
            <div class="news-meta">— {event['news_source']}, {event['news_date']}</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        img_path = os.path.join(MEDIA_DIR, event["image_file"])
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.info(f"Historical Asset: {event['image_file']}")

    with col2:
        st.markdown(f"<div class='context-box'>{event['context']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='significance'><strong>Historical Impact:</strong> {event['significance']}</div>", unsafe_allow_html=True)