
import pytest

from thermostat_control import (
    target_temperature,
    hvac_action,
    energy_alert,
)


# Tests for target_temperature()

def test_away_mode():
    assert target_temperature("away", True, 12) == 16


def test_sleep_mode_before_6():
    assert target_temperature("sleep", True, 5) == 18


def test_sleep_mode_after_22():
    assert target_temperature("sleep", True, 23) == 18


def test_sleep_mode_during_day():
    assert target_temperature("sleep", True, 12) == 20


def test_unoccupied():
    assert target_temperature("home", False, 12) == 18


def test_morning_temperature():
    assert target_temperature("home", True, 7) == 22


def test_evening_temperature():
    assert target_temperature("home", True, 18) == 21


def test_normal_temperature():
    assert target_temperature("home", True, 12) == 20


# Tests for hvac_action()

def test_idle_action():
    assert hvac_action(20, 20.5, 25) == "idle"


def test_heating_boost():
    assert hvac_action(18, 22, 2) == "heat_boost"


def test_normal_heating():
    assert hvac_action(18, 22, 10) == "heat"


def test_cooling_boost():
    assert hvac_action(25, 20, 35) == "cool_boost"


def test_normal_cooling():
    assert hvac_action(25, 20, 25) == "cool"


# Tests for energy_alert()

def test_no_readings():
    assert energy_alert([], 10) == "ok"


def test_no_readings_above_limit():
    assert energy_alert([5, 8, 10], 10) == "ok"


def test_warning_alert():
    assert energy_alert([12, 8], 10) == "warning"


def test_critical_alert():
    assert energy_alert([12, 15, 8], 10) == "critical"
