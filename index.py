import streamlit as st

import requests

from issue_card import issue_card
from models import Issue


def is_issue_valid(issue: Issue) -> bool:
    if not issue.issue_repo.repo_langs.nodes:
        return False
    return True


@st.cache_data(ttl=3600)
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


issues_response = get_issues(st.secrets.data_url)

st.set_page_config(
    page_title="Good First Issues",
    page_icon=":material/thumb_up:",
)

with st.sidebar:
    st.info("Filters", icon=":material/filter_list:")
    st.divider()
    st.info("Sort", icon=":material/sort:")

st.title("Good First Issues")

for issue in issues_response:
    issue_card(issue)
