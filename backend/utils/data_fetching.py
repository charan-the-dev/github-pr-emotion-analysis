from github import Github
import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# GitHub token
GITHUB_TOKEN = os.environ.get('SECRET_GITHUB_TOKEN')

# Initialize GitHub client
g = Github(GITHUB_TOKEN)

def fetch_pr_comments_for_repo(repo_full_name, max_comments=20):
    """
    Fetch PR comments from a specific repository.
    repo_full_name: 'owner/repo' (e.g., 'octocat/Hello-World')
    max_comments: number of comments to fetch
    """
    repo = g.get_repo(repo_full_name)
    pr_comments = repo.get_pulls_comments()
    
    pr_data = []
    
    count = 0
    for comment in pr_comments:
        pr_data.append({
            'repo_name': repo.name,
            'pr_number': comment.pull_request_url.split('/')[-1],
            'comment_id': comment.id,
            'user': comment.user.login,
            'body': comment.body,
            'created_at': comment.created_at
        })
        count += 1
        if count >= max_comments:
            break

    return pr_data
