import abc


class RepositoryInterface(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def reads():
        raise NotImplementedError()

    @abc.abstractmethod
    def read():
        raise NotImplementedError()

    @abc.abstractmethod
    def create():
        raise NotImplementedError()

    @abc.abstractmethod
    def update():
        raise NotImplementedError()

    @abc.abstractmethod
    def delete():
        raise NotImplementedError()


class ServiceInterface(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def reads():
        raise NotImplementedError()

    @abc.abstractmethod
    def read():
        raise NotImplementedError()

    @abc.abstractmethod
    def create():
        raise NotImplementedError()

    @abc.abstractmethod
    def update():
        raise NotImplementedError()

    @abc.abstractmethod
    def delete():
        raise NotImplementedError()
