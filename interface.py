from abc import ABC, abstractmethod
from typing import Dict, Any


class ISerializable(ABC):
    """
    Interfaz que obliga a las clases a saber convertirse en diccionario
    para poder guardarse en un JSON.
    """

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass

