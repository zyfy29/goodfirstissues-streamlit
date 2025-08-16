import json

import pytest
from streamlit.testing.v1 import AppTest
from pytest_mock import MockerFixture


@pytest.fixture
def app(mocker: MockerFixture):
    at = AppTest.from_file("../index.py")
    at.secrets["data_url"] = "https://www.example.com/issues.json"
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.status_code = 200
    with open("data.json", "r") as f:
        mock_get.return_value.json.return_value = json.load(f)
    return at


def test_run(app):
    app.run()
    assert not app.exception


def test_countup_caption(app):
    app.run()
    assert len(app.caption) > 0
    assert app.caption[0].value == "Found 10 issues."


def test_hide_assigned_toggle(app):
    app.run()
    # fixme
    # app.sidebar.toggle[0].set_value(True).run()
    # assert app.caption[0].value == "Found 10 issues."
