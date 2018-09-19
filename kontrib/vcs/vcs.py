from kontrib.vcs import Git, Svn
from kontrib.exceptions import VcsNotSupported


class Vcs():
    AVAILABLE_VCS = ['git', 'svn']

    def __init__(self):
        pass

    def get_vcs(self, vcs_type):
        if vcs_type == 'git':
            return Git()
        elif vcs_type == 'svn':
            return Svn()

        raise VcsNotSupported(vcs_type)
