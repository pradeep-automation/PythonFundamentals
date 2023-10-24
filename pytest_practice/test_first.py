import pytest

class TestFirst:

    def test_first(self, set_up):
        actual_value = "pradeep"
        expected_value = "PRADEEP"
        assert actual_value == expected_value.lower(), "Was expecting pradeep"

