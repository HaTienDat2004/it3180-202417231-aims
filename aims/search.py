def search_by_category(items, category):
    """Return DVDs with an exact, case-insensitive category match."""
    return [dvd for dvd in items if dvd.category.casefold() == category.casefold()]


def search_by_title(items, keyword):
    """Return DVDs whose title contains the requested keyword."""
    return [dvd for dvd in items if keyword in dvd.title]
