
import math
from hypothesis import given, strategies as st

from thermostat_control import (
    parse_setpoint,
    average_temperature,
    schedule_slot
)


# 1. Tests for arbitrary inputs (no-crash properties)

@given(st.text() | st.none())
def test_parse_setpoint_no_crash(s):
    parse_setpoint(s)


@given(st.text() | st.none())
def test_average_temperature_no_crash(s):
    average_temperature(s)


@given(st.text() | st.none())
def test_schedule_slot_no_crash(s):
    schedule_slot(s)


# 2. Tests for valid Celsius and Fahrenheit inputs

@given(st.floats(
    min_value=-100,
    max_value=200,
    allow_nan=False,
    allow_infinity=False
))
def test_parse_celsius(value):
    result = parse_setpoint(f"{value}C")
    assert result == round(value, 1)


@given(st.floats(
    min_value=-100,
    max_value=300,
    allow_nan=False,
    allow_infinity=False
))
def test_parse_fahrenheit(value):
    result = parse_setpoint(f"{value}F")
    expected = round((value - 32) * 5 / 9, 1)
    assert result == expected


# 3. Test average temperature calculation

@given(st.lists(
    st.floats(
        min_value=-50,
        max_value=100,
        allow_nan=False,
        allow_infinity=False
    ),
    min_size=1,
    max_size=20
))
def test_average_temperature_correctness(readings):
    csv_input = ",".join(str(value) for value in readings)

    result = average_temperature(csv_input)
    expected = sum(readings) / len(readings)

    assert math.isclose(result, expected, rel_tol=1e-9)


# 4. Test schedule slot boundaries

@given(
    st.integers(min_value=0, max_value=23),
    st.integers(min_value=0, max_value=59)
)
def test_schedule_slot_correctness(hour, minute):
    time_text = f"{hour:02d}:{minute:02d}"

    expected = "night" if hour < 6 else "day"

    assert schedule_slot(time_text) == expected
