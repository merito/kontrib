import sys
from settings import Settings
from kontrib.hostings.hosting import Hosting
from kontrib.vcs.vcs import Vcs


class Kontrib():
    def __init__(self):
        self.settings = None
        self.vcs = None
        self.hosting = None

    def set_vcs(self, vcs):
        self.vcs = Vcs().get_vcs(vcs)

    def set_hosting(self, hosting):
        self.hosting = Hosting().get_hosting(hosting)

    def run(self, argv):
        self.settings = Settings.set_settings(argv)
        self.set_vcs(self.settings.repo['vcs'])
        self.set_hosting(self.settings.repo['hosting'])
        if self.settings.new_pr:
            self.vcs.new_pr()



if __name__ == "__main__":
    import ipdb;ipdb.set_trace()
    kontrib = Kontrib()
    kontrib.run(sys.argv)
