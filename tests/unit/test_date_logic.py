from datetime import date, timedelta

def get_weeks_within_date_range(start_date: date, end_date: date) -> list[tuple[date, date]]:
    """Return a list of dates representing the start of each week within the given date range.

    The returned weeks are inclusive of the start and end dates.
    """
    weeks: list[tuple[date, date]] = []
    current_date = start_date

    while True:
        week_start_date = current_date
        week_end_date = week_start_date + timedelta(days=6)
        
        if week_end_date > end_date:
            break
        
        weeks.append((week_start_date, week_end_date))
        current_date = week_end_date + timedelta(days=1)
    
    return weeks

def test_get_weeks_within_date_range__can_get_weeks_within_date_range() -> None:
    # Arrange
    start_date = date(2025, 6, 4)
    end_date = date(2025, 6, 21)

    expected_weeks = [
        (date(2025, 6, 4), date(2025, 6, 10)),
        (date(2025, 6, 11), date(2025, 6, 17)),
    ]

    # Act
    actual_weeks = get_weeks_within_date_range(start_date, end_date)

    # Assert
    assert actual_weeks == expected_weeks, f"Expected {expected_weeks}, but got {actual_weeks}"