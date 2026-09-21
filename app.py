import streamlit as st

from blog_generator import generate_blog


st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="✍️"
)

st.title("✍️ AI Blog Generator")

st.write(
    "Generate customized blog articles using Generative AI."
)
topic = st.text_input(
    "Blog Topic",
    placeholder="e.g. The future of renewable energy"
)
audience = st.text_input(
    "Target Audience",
    placeholder="e.g. University students"
)
tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Friendly",
        "Academic",
        "Casual"
    ]
)
word_count = st.number_input(
    "Approximate Word Count",
    min_value=100,
    max_value=5000,
    value=1000,
    step=100
)
keywords = st.text_input(
    "Keywords",
    placeholder="e.g. technology, advancement"
)
if st.button("Generate Blog", type="primary"):

    if not topic:
        st.error("Please enter a blog topic.")

    elif not audience:
        st.error("Please enter the target audience.")

    else:
        with st.spinner("Generating your blog..."):

            try:
                blog = generate_blog(
                    topic,
                    audience,
                    tone,
                    word_count,
                    keywords
                )

                st.session_state["blog"] = blog

            except Exception as e:
                st.error(f"Something went wrong: {e}")
if "blog" in st.session_state:

    st.subheader("Generated Blog")

    st.markdown(st.session_state["blog"])