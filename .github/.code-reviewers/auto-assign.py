import os
import yaml

from github import Auth, Github

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
GITHUB_REPOSITORY = os.environ["GITHUB_REPOSITORY"]
PR_NUMBER = int(os.environ["PR_NUMBER"])

# using an access token
auth = Auth.Token(GITHUB_TOKEN)

# Public Web Github
g = Github(auth=auth)

repo = g.get_repo(GITHUB_REPOSITORY)
pr = repo.get_pull(PR_NUMBER)

print(pr)
