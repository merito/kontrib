class ConfigFileDamagedError(Exception):
    """ Configuration file content is not sufficient. """

class HostingNotSupported(Exception):
    """ Hosting currently not supported. """

class VcsNotSupported(Exception):
    """ VCS currently not supported. """
