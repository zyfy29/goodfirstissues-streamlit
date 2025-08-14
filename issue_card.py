import streamlit as st
from datetime import datetime, timezone

from models import Issue


def label_to_badge(label: str) -> str:
    label = label.lower().strip()
    # https://docs.streamlit.io/develop/api-reference/text/st.badge
    # colors: blue, green, orange, red, violet, gray
    # badges: good first issue, help wanted, bug, enhancement, documentation
    if label == "good first issue":
        return ":blue-badge[:material/thumb_up: Good First Issue]"
    elif label == "bug":
        return ":red-badge[:material/bug_report: Bug]"
    elif label == "enhancement":
        return ":green-badge[:material/add_circle: Enhancement]"
    elif label == "documentation":
        return ":orange-badge[:material/article: Documentation]"
    elif label == "help wanted":
        return ":violet-badge[:material/help: Help Wanted]"
    else:
        return f":gray-badge[{label.title()}]"


def language_to_badge(language: str) -> str:
    return f":blue-badge[{language.title()}]"


def format_relative_time(created_at: datetime) -> str:
    now = datetime.now(timezone.utc)
    if created_at.tzinfo is None:
        created_at = created_at.replace(tzinfo=timezone.utc)

    diff = now - created_at
    hours = int(diff.total_seconds() // 3600)
    days = diff.days

    if days > 0:
        return f"{created_at.strftime('%B %d, %Y')} ({days} days ago)"
    elif hours > 0:
        return f"{created_at.strftime('%B %d, %Y')} ({hours} hours ago)"
    else:
        minutes = int(diff.total_seconds() // 60)
        return f"{created_at.strftime('%B %d, %Y')} ({minutes} minutes ago)"


def issue_card(issue: Issue):
    with st.container(border=True):
        st.subheader(issue.issue_title)
        st.write(
            f"Repository: [{issue.issue_repo.owner.repo_owner}/{issue.issue_repo.repo_name}]({issue.issue_repo.repo_url})"
        )
        desc = issue.issue_repo.repo_desc
        if desc:
            st.write(f"Description: {issue.issue_repo.repo_desc}")
        st.caption(format_relative_time(issue.issue_created_at))
        st.write(
            f":material/star: {issue.issue_repo.repo_stars} :material/comment: {issue.comments.issue_comment_count}")
        labels_markdown = "Labels: " + " ".join(
            [label_to_badge(label.label_name) for label in issue.issue_labels.nodes]
        )
        st.markdown(labels_markdown)
        laguages_markdown = "Languages: " + " ".join(
            [language_to_badge(lang.repo_prog_language) for lang in issue.issue_repo.repo_langs.nodes]
        )
        st.markdown(laguages_markdown)
        st.link_button(
            "View Issue",
            url=str(issue.issue_url),
            icon=":material/launch:",
        )
