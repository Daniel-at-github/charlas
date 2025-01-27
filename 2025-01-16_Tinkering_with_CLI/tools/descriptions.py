"""Get package descriptions form pypi"""

import requests


def get_pypi_description(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["info"]["summary"]
    else:
        return f"Error: Unable to fetch description for {package_name}"


def get_descriptions(package_list):
    for package in package_list:
        description = get_pypi_description(package)
        print(f"{package}: {description}")


# Example usage
packages = [
    "black",
    "isort",
    "mypy",
    "ruff",
    "uv",
    "pytest",
    "pyupgrade",
    "datasette",
    "jupyterlab",
    "streamlit",
    "visidata",
    "llm",
    "yt-dlp",
    "lightnovel-crawler",
    "ansitoimg",
    "lektor",
    "markdown-anki-decks",
    "pyxel",
]
get_descriptions(packages)
