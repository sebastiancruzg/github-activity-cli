import sys

import pytest

from gactivity.activity import parse_args


def test_parse_args_valid_username(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, "argv", ["gactivity", "sebastian"])
        assert parse_args() == "sebastian"

def test_parse_args_no_username(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, "argv", ["gactivity", ""])
        assert parse_args() in "the following arguments are required: username"

