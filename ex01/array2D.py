def slice_me(family: list, start: int, end: int) -> list:
    """Check and truncate 2D  array
        family: list of list
        start: start index of slicing
        end: end index of slicing

        return : new 2D list after slicing
    """

    if not isinstance(family, list):
        raise ValueError("family must be a list")

    if not all(isinstance(row, list) for row in family):
        raise ValueError("family must be a list")

    if len(set(len(row) for row in family)) != 1:
        raise ValueError("family must have same length")

    if not isinstance(start, int) or not isinstance(end,int):
        raise ValueError("start and end index must be int")

    rows = len(family)
    cols = len(family[0])
    print(f"My shape is : ({rows}, {cols})")

    truncated_family = family[start:end]

    new_row = len(truncated_family)
    print(f"My new shape is : ({new_row}, {cols})")

    return truncated_family