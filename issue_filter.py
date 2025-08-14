from models import Issue
from enum import Enum


class MultiselectMode(Enum):
    OR = "Or"
    AND = "And"


class IssueFilter:
    def __init__(
            self,
            languages: list[str] = None,
            language_multiselect_mode: MultiselectMode = "Or",
            hide_assigned: bool = False,
    ):
        self.languages = languages
        self.language_multiselect_mode = language_multiselect_mode
        self.hide_assigned = hide_assigned

    def filter_issues(self, issues: list[Issue]):
        filtered_issues = []
        for issue in issues:
            # filter languages
            issue_languages = {lang.repo_prog_language for lang in issue.issue_repo.repo_langs.nodes}
            if not issue_languages:
                continue
            if self.languages:
                if self.language_multiselect_mode == MultiselectMode.OR:
                    if not any(lang in issue_languages for lang in self.languages):
                        continue
                elif self.language_multiselect_mode == MultiselectMode.AND:
                    if not all(lang in issue_languages for lang in self.languages):
                        continue
            else:  # No languages selected, include all issues
                pass

            # filter assigned issues
            if self.hide_assigned and issue.assignees.issue_assignees_count > 0:
                continue

            filtered_issues.append(issue)

        return filtered_issues
