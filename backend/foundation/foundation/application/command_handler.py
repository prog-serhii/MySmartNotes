import abc
from typing import Dict, Generic, Type, TypeVar

from foundation.domain.commands import Command
from foundation.application.utils import get_message_cls


C = TypeVar('C', bound=Command)


class CommandHandler(abc.ABC, Generic[C]):

    @abc.abstractmethod
    def handle(self, command: C) -> None:
        raise NotImplementedError


class CommandBus:

    def __init__(self) -> None:
        self._handlers: Dict[Type[Command], CommandHandler] = {}

    def register(self, handler: CommandHandler):
        command_cls = get_message_cls(type(handler), Command)
        if command_cls in self._handlers:
            raise ValueError(f'{command_cls} already has a handler!')
        self._handlers[command_cls] = handler

    def execute(self, command: Command) -> None:
        try:
            self._handlers[type(command)].handle(command)
        except KeyError:
            raise Exception(f'No handler for {command}')
