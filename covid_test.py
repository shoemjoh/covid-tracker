from covid_tracker import get_cases


def test_get_cases():
    assert get_cases(country_id="USA") == "37,021,829"
