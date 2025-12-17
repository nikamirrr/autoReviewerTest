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
changed_files = pr.get_files()

print(pr)
print(changed_files)

try:
    # Request reviews
    # The method takes two lists: 'reviewers' (users) and 'team_reviewers' (teams)
    users_to_add = ['nikamirrrgwptd']
    pr.request_reviews(reviewers=users_to_add)
    print(f"Successfully requested reviews for PR #{pr.number} from users: {users_to_add}")

except Exception as e:
    print(f"An error occurred: {e}")
