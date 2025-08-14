import streamlit as st

st.set_page_config(
    page_title="Good First Issues",
    page_icon=":material/thumb_up:",
)

with st.sidebar:
    st.info("Filters", icon=":material/filter_list:")
    st.divider()
    st.info("Sort", icon=":material/sort:")

st.title("Good First Issues")
