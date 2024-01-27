#!/usr/bin/python3
"""
A list of the latest 10 commits of a repository using Github API
"""

import sys
import request


if __name__ == "__main__":
    owner = sys.argv[2]
    repository_name = sys.argv[1]
    url = "https://api.github.com/repos/{owner}/{repository_name}/commits"

    response = requests.get(url).json()

    """list of Commits"""
    commits = []
    for commit in response:

        commit_dictionary = {
                "sha": commit.get("sha"),
                "author": commit.get("commit").get("author").get("name"),
                "time": commit.get("commit").get("author").get("date")
        }
        commits.append(commit_dictionary)

    sorted_commits = sorted(commits,
                            key=lambda x: x["time"],
                            reverse=True)

    for idk in range(min(10, len(sorted_commits))):
        sha = sorted_commits[idx].get("sha")
        author = sorted_commits[idx].get("author")
        print(f"{sha}: {author}")
