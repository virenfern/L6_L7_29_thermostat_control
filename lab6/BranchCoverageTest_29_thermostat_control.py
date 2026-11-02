
from thermostat_control import (
    target_temperature,
    hvac_action,
    energy_alert,
)


# Branch tests for target_temperature()

def test_away_mode_branch():
    assert target_temperature("away", True, 12) == 16


def test_sleep_mode_branch():
    assert target_temperature("sleep", True, 12) == 20


def test_sleep_before_6_branch():
    assert target_temperature("sleep", True, 5) == 18


def test_sleep_after_22_branch():
    assert target_temperature("sleep", True, 22) == 18


def test_unoccupied_branch():
    assert target_temperature("home", False, 12) == 18


def test_morning_branch():
    assert target_temperature("home", True, 6) == 22


def test_not_morning_branch():
    assert target_temperature("home", True, 12) == 20


def test_evening_branch():
    assert target_temperature("home", True, 17) == 21


def test_not_evening_branch():
    assert target_temperature("home", True, 12) == 20


# Branch tests for hvac_action()

def test_idle_branch():
    assert hvac_action(20, 20.5, 25) == "idle"


def test_not_idle_branch():
    assert hvac_action(20, 22, 25) == "heat"


def test_heating_branch():
    assert hvac_action(20, 22, 2) == "heat_boost"


def test_normal_heating_branch():
    assert hvac_action(20, 22, 5) == "heat"


def test_cooling_branch():
    assert hvac_action(22, 20, 35) == "cool_boost"


def test_normal_cooling_branch():
    assert hvac_action(22, 20, 30) == "cool"


# Branch tests for energy_alert()

def test_empty_readings_branch():
    assert energy_alert([], 10) == "ok"


def test_no_readings_over_limit_branch():
    assert energy_alert([5, 8, 10], 10) == "ok"


def test_reading_over_limit_branch():
    assert energy_alert([12, 8], 10) == "warning"


def test_exactly_half_over_limit_branch():
    assert energy_alert([12, 15, 8, 9], 10) == "warning"


def test_more_than_half_over_limit_branch():
    assert energy_alert([12, 15, 18, 8], 10) == "critical"
