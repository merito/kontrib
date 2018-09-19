import logging
from git import Repo
from ..settings import SettingsDict as settings


class Git():
    UPSTREAM_NAME = 'kontrib_upstream'

    def __init__(self):
        self.repo = None

    def set_upstream(self, upstream):
        try:
            self.repo.remote(self.UPSTREAM_NAME).set_url(upstream)
        except ValueError:
            self.repo.create_remote(self.UPSTREAM_NAME, upstream)
        return self.repo.remote(self.UPSTREAM_NAME)

    def new_pr(self):
        self.repo = Repo(settings.repo_path)
        if settings.repo['upstream']:
            remote = self.set_upstream(settings.repo['upstream'])
        else:
            remote = self.repo.remote()
        remote.fetch()

