from abc import ABC;

class DomainException(Exception, ABC):
    pass

class InvalidMove(DomainException):
    pass
