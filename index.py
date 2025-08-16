import streamlit as st

import requests

from issue_card import issue_card
from issue_filter import IssueFilter, MultiselectMode
from models import Issue

st.set_page_config(
    page_title="Good First Issues",
    page_icon=":material/thumb_up:",
)


def is_issue_valid(issue: Issue) -> bool:
    if not issue.issue_repo.repo_langs.nodes:
        return False
    return True


@st.cache_data(ttl=600)
def get_issues(url) -> list[Issue]:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    res = []
    for item in data:
        try:
            issue = Issue(**item["Issue"])
            if is_issue_valid(issue):
                res.append(issue)
        except Exception:
            continue
    return res


if 'issues_response' not in st.session_state:
    st.session_state.issues_response = get_issues(st.secrets.data_url)

all_languages = set()
for issue in st.session_state.issues_response:
    for lang in issue.issue_repo.repo_langs.nodes:
        all_languages.add(lang.repo_prog_language)

with st.sidebar:
    st.subheader(":material/filter_list: Filters")
    with st.container(border=True):
        st.multiselect(
            "Programming Languages",
            options=sorted(all_languages),
            key="languages",
            help="Filter issues by programming languages.",
        )
        # TODO: using st.segmented_control here will cause ridiculous UI issues, report this to streamlit
        st.toggle(
            "Allow Either",
            key="allow_either",
        )

    with st.container(border=True):
        st.toggle("Hide assigned", key="hide_assigned")

    st.divider()
    st.subheader(":material/sort: Sort")
    with st.container(border=True):
        st.write("Sorting options will be available soon!")

st.title("Good First Issues")

issue_filter = IssueFilter(
    languages=st.session_state.languages,
    language_multiselect_mode=MultiselectMode.OR if st.session_state.allow_either else MultiselectMode.AND,
    hide_assigned=st.session_state.hide_assigned,
)
issues_to_display = issue_filter.filter_issues(st.session_state.issues_response)

st.caption(f"Found {len(issues_to_display)} issues.")
for issue in issue_filter.filter_issues(st.session_state.issues_response):
    issue_card(issue)
