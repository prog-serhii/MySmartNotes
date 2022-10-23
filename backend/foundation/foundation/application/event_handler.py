import abc
from collections import defaultdict
from typing import Dict, Generic, List, Type, TypeVar

from foundation.domain.events import Event
from foundation.application.utils import get_message_cls


E = TypeVar('E', bound=Event)


class EventHandler(abc.ABC, Generic[E]):

    @abc.abstractmethod
    def handle(self, event: E) -> None:
        raise NotImplementedError


class EventBus:

    def __init__(self) -> None:
        self._handlers: Dict[Type[Event], List[EventHandler]] = defaultdict(list)

    def register(self, handler: EventHandler) -> None:
        self._handlers[get_message_cls(type(handler), Event)].append(handler)

    def publish(self, event: Event) -> None:
        for handler in self._handlers[type(event)]:
            handler.handle(event)
