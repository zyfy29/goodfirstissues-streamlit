from typing import List
from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl


class Repo(BaseModel):
    class RepoLanguage(BaseModel):
        repo_prog_language: str = Field(alias="repo_prog_language")

    class RepoLanguages(BaseModel):
        nodes: List['Repo.RepoLanguage'] = Field(alias="Nodes")

    class RepoOwner(BaseModel):
        repo_owner: str = Field(alias="repo_owner")

    repo_name: str = Field(alias="repo_name")
    repo_desc: str = Field(alias="repo_desc")
    repo_url: HttpUrl = Field(alias="repo_url")
    repo_stars: int = Field(alias="repo_stars")
    repo_langs: RepoLanguages = Field(alias="repo_langs")
    owner: RepoOwner = Field(alias="Owner")


class Issue(BaseModel):
    class IssueLabel(BaseModel):
        label_name: str = Field(alias="label_name")

    class IssueLabels(BaseModel):
        nodes: List['Issue.IssueLabel'] = Field(alias="Nodes")
        label_total_count: int = Field(alias="label_totalcount")

    class IssueComments(BaseModel):
        issue_comment_count: int = Field(alias="issue_comment_count")

    class IssueAssignees(BaseModel):
        issue_assignees_count: int = Field(alias="issue_assignees_count")

    issue_url: HttpUrl = Field(alias="issue_url")
    issue_created_at: datetime = Field(alias="issue_createdAt")
    issue_repo: Repo = Field(alias="issue_repo")
    issue_title: str = Field(alias="issue_title")
    issue_labels: IssueLabels = Field(alias="issue_labels")
    comments: IssueComments = Field(alias="Comments")
    assignees: IssueAssignees = Field(alias="Assignees")
