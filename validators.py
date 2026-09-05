def validate_name(name: str) -> tuple[bool, str]:
    """
    Validates a user's name.

    Returns:
        (True, "") if valid
        (False, error_message) if invalid
    """

    name = name.strip()

    if not name:
        return False, "Please enter your name."

    if len(name) < 2:
        return False, "Name must be at least 2 characters long."

    if not all(char.isalpha() or char.isspace() for char in name):
        return False, "Name can only contain letters and spaces."

    return True, ""
