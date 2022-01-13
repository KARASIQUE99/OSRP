from abc import *


class IMainView(metaclass=ABCMeta):
    @abstractmethod
    def attach_presenter(self):
        """Переместить объект"""

