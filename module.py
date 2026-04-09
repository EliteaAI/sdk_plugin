""" Module """

from pylon.core.tools import log  # pylint: disable=E0611,E0401
from pylon.core.tools import module  # pylint: disable=E0611,E0401


class Module(module.ModuleModel):
    """ Pylon module """

    def init(self):
        """ Initialize module """
        log.info(
            "EliteA SDK plugin ready (v%s)",
            self.descriptor.metadata.get("version", "unknown"),
        )

    def deinit(self):
        """ De-init module """
        pass
