from agency_swarm.tools import BaseTool
from pydantic import Field
import requests
import os
import time

class GitHubApiTool(BaseTool):
    """
    This tool uses the GitHub API to fetch repository details using the provided access token.
    It makes authenticated requests to the GitHub API to retrieve information about a specific repository,
    such as its structure, key components, and functionalities.
    """

    access_token: str = Field(
        ..., description="GitHub access token for authentication."
    )
    owner: str = Field(
        ..., description="Owner of the repository."
    )
    repo: str = Field(
        ..., description="Name of the repository."
    )

    def authenticate(self):
        """
        Authenticate using the provided access token.
        """
        headers = {
            "Authorization": f"token {self.access_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        return headers

    def fetch_repo_details(self):
        """
        Fetch repository details from GitHub API.
        """
        headers = self.authenticate()
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}"
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 403 and 'X-RateLimit-Remaining' in response.headers and response.headers['X-RateLimit-Remaining'] == '0':
            reset_time = int(response.headers['X-RateLimit-Reset'])
            sleep_time = max(0, reset_time - time.time())
            time.sleep(sleep_time)
            return self.fetch_repo_details()
        else:
            response.raise_for_status()

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform the task.
        """
        try:
            repo_details = self.fetch_repo_details()
            return repo_details
        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"

# Example usage:
# tool = GitHubApiTool(access_token="your_access_token", owner="octocat", repo="Hello-World")
# print(tool.run())