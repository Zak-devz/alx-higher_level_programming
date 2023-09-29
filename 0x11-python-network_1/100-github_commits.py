#!/usr/bin/python3
"""A script to list the 10 most recent commits on a GitHub repository."""
import sys
import requests


def main():
    """Main function to fetch and display commits."""
    if len(sys.argv) != 3:
        print("Usage: ./script.py <repository name> <repository owner>")
        sys.exit(1)

    repo = sys.argv[1]
    owner = sys.argv[2]
    limit = 10
    url = (
        f'https://api.github.com/repos/{repo}/{owner}/commits'
        f'?per_page={limit}'
    )

    try:
        response = requests.get(url)
        response.raise_for_status()

        commits = response.json()
        for commit in commits:
            name = commit.get("commit").get("author").get("name")
            print(f'{commit.get("sha")}: {name}')
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
