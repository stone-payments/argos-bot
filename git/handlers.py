"""Bot starts a telegram bot."""
import os
from github import Github
import requests
from datetime import datetime, timedelta
from collections import defaultdict
import logging

g = Github(os.getenv('GITHUB_USER', ''), os.getenv('GITHUB_PASSWORD', ''))

BASE_URL = 'https://api.github.com'
log = logging.getLogger(__name__)
org = os.getenv('GITHUB_ORG', '')
team_id = int(os.getenv('GITHUB_TEAM_ID', '0'))

def pull_requests(bot, update):
    """Return open PRs."""
    log.info("Got message")
    repos = g.get_organization(org).get_team(team_id).get_repos()
    msg = ''
    for repo in repos:
        for pr in repo.get_pulls():
            msg += '{} \n {}\n\n'.format(pr.title, pr.html_url)
    log.info(msg)
    update.message.reply_text(msg)