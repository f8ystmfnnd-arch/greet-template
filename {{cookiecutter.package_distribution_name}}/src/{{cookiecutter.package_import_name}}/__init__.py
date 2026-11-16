"""{{ cookiecutter.package_description }}."""


def greet(name: str) -> str:
    """Return a greeting for the supplied name."""
    display_name = name.strip() or "world"
    return f"Hello, {display_name}!"
