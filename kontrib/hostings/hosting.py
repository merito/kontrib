from kontrib.hostings import GithubHosting, GitlabHosting
from kontrib.exceptions import HostingNotSupported


class Hosting():
    AVAILABLE_HOSTINGS = ['github', 'gitlab']

    def __init__(self):
        pass

    def get_hosting(self, hosting_type):
        if hosting_type == 'github':
            return GithubHosting()
        elif hosting_type == 'gitlab':
            return GitlabHosting()

        raise HostingNotSupported(hosting_type)
