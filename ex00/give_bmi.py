def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    """take 2 lists of integers or floats in input and returns a list
        of BMI values."""

    if not isinstance(height, list) or not isinstance(weight, list):
        raise AssertionError("the arguments are bad")

    if len(height) != len(weight):
        raise AssertionError("list has to the same length")

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise AssertionError("value has to be a number (int or float)")

        if h <= 0:
            raise AssertionError("height has to be positive")

    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if each BMI exceeds a certain limit.

    :param bmi: List of BMI values (int or float).
    :param limit: Limit value to compare against (int).
    :return: List of booleans (True if BMI > limit, otherwise False).
    :raises AssertionError: If the types are incorrect.
    """
    if not isinstance(bmi, list):
        raise AssertionError("first argument must be a list")

    if not isinstance(limit, int):
        raise AssertionError("The limit must be an integer.")

    for value in bmi:
        if not isinstance(value, (int, float)):
            raise AssertionError("The values in the list must "
                                 "be numbers (int or float).")

    # check limit with lambda + comprehension list
    return list(map(lambda x: x > limit, bmi))
