import abc


from graph.application.graph_repository import AbstractGraphRepository


class AbstractUnitOfWork(abc.ABC):

    graph_repository: AbstractGraphRepository

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
