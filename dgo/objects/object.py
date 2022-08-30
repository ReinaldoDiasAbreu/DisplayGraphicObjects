from abc import ABC, abstractmethod

class Object():
    
    def __init__(self) -> None:
        pass

    @abstractmethod
    def show():
        pass

    def get_tipo() -> str:
        return "Objeto"
    