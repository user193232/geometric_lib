import math


def area(r):
    """Вычисляет площадь круга.

    Args:
        r (float | int): Радиус круга.

    Returns:
        float: Площадь круга.

    Examples:
        >>> area(5)
        78.53981633974483
    """
    return math.pi * r * r


def perimeter(r):
    """Вычисляет периметр круга.

    Args:
        r (float | int): Радиус круга.

    Returns:
        float: Периметр круга.

    Examples:
        >>> perimeter(5)
        31.41592653589793
    """
    return 2 * math.pi * r

