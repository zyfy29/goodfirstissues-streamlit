import json

import pytest
from streamlit.testing.v1 import AppTest
from pytest_mock import MockerFixture


@pytest.fixture
def app(mocker: MockerFixture):
    at = AppTest.from_file("index.py")
    at.secrets["data_url"] = "https://www.example.com/issues.json"
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.status_code = 200
    with open("tests/data.json", "r") as f:
        mock_get.return_value.json.return_value = json.load(f)
    return at


def test_run(app):
    app.run()
    assert not app.exception


def test_countup(app):
    app.run()
    assert len(app.caption) > 0
    assert app.caption[0].value == "Found 10 issues."


def test_hide_assigned(app):
    app.run()
    app.sidebar.toggle[1].set_value(True).run()  # Hide Assigned
    assert app.caption[0].value == "Found 5 issues."


def test_language_multiselect_one(app):
    app.run()
    app.sidebar.multiselect[0].set_value(["Go"]).run()
    assert len(app.caption) > 0
    assert app.caption[0].value == "Found 6 issues."


def test_language_multiselect_multiple_and(app):
    app.run()
    app.sidebar.multiselect[0].set_value(["Go", "Python"]).run()
    assert len(app.caption) > 0
    assert app.caption[0].value == "Found 1 issues."


def test_language_multiselect_multiple_or(app):
    app.run()
    app.sidebar.multiselect[0].set_value(["Go", "Python"]).run()
    app.sidebar.toggle[0].set_value(True).run()  # Allow Either
    assert len(app.caption) > 0
    assert app.caption[0].value == "Found 10 issues."
