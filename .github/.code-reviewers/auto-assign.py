import os
import yaml

from github import Auth, Github

# using an access token
auth = Auth.Token(os.environ["GITHUB_TOKEN"])

# Public Web Github
g = Github(auth=auth)

print(os.environ)
