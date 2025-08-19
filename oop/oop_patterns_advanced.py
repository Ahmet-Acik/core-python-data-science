"""
oop_patterns_advanced.py
-----------------------
Advanced OOP patterns and architectures in Python.
Covers: Observer, Strategy, Decorator, Adapter, Command, Dependency Injection, Fluent Interface, Event-driven, and Plugin architectures with practical examples.
"""

from typing import Callable, Any, List
from abc import ABC, abstractmethod

# 1. OBSERVER PATTERN
class Subject:
    def __init__(self):
        self._observers: List[Callable[[Any], None]] = []
    def attach(self, observer: Callable[[Any], None]):
        self._observers.append(observer)
    def detach(self, observer: Callable[[Any], None]):
        self._observers.remove(observer)
    def notify(self, data: Any):
        for observer in self._observers:
            observer(data)

# 2. STRATEGY PATTERN
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass
class QuickSort(SortStrategy):
    def sort(self, data: list) -> list:
        return sorted(data)  # Placeholder for real quicksort
class ReverseSort(SortStrategy):
    def sort(self, data: list) -> list:
        return sorted(data, reverse=True)
class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy
    def sort(self, data: list) -> list:
        return self.strategy.sort(data)

# 3. DECORATOR PATTERN
class Notifier:
    def send(self, msg: str):
        print(f"Sending: {msg}")
class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self._notifier = notifier
    def send(self, msg: str):
        self._notifier.send(msg)
class EmailDecorator(NotifierDecorator):
    def send(self, msg: str):
        super().send(msg)
        print(f"Email sent: {msg}")
class SMSDecorator(NotifierDecorator):
    def send(self, msg: str):
        super().send(msg)
        print(f"SMS sent: {msg}")

# 4. ADAPTER PATTERN
class OldAPI:
    def do_thing(self):
        return "Old API"
class NewAPI:
    def do_new_thing(self):
        return "New API"
class APIAdapter:
    def __init__(self, new_api: NewAPI):
        self.new_api = new_api
    def do_thing(self):
        return self.new_api.do_new_thing()

# 5. COMMAND PATTERN
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
class PrintCommand(Command):
    def __init__(self, msg: str):
        self.msg = msg
    def execute(self):
        print(self.msg)
class Invoker:
    def __init__(self):
        self._commands: List[Command] = []
    def add_command(self, cmd: Command):
        self._commands.append(cmd)
    def run(self):
        for cmd in self._commands:
            cmd.execute()

# 6. DEPENDENCY INJECTION
class Service:
    def do_work(self):
        return "Service did work"
class Client:
    def __init__(self, service: Service):
        self.service = service
    def operate(self):
        return self.service.do_work()

# 7. FLUENT INTERFACE
class QueryBuilder:
    def __init__(self):
        self.query = "SELECT *"
    def where(self, cond: str):
        self.query += f" WHERE {cond}"
        return self
    def order_by(self, col: str):
        self.query += f" ORDER BY {col}"
        return self
    def build(self):
        return self.query

# 8. EVENT-DRIVEN
class EventEmitter:
    def __init__(self):
        self._events = {}
    def on(self, event: str, handler: Callable):
        self._events.setdefault(event, []).append(handler)
    def emit(self, event: str, *args, **kwargs):
        for handler in self._events.get(event, []):
            handler(*args, **kwargs)

# 9. PLUGIN ARCHITECTURE
class PluginBase(ABC):
    @abstractmethod
    def run(self):
        pass
class PluginManager:
    def __init__(self):
        self.plugins: List[PluginBase] = []
    def register(self, plugin: PluginBase):
        self.plugins.append(plugin)
    def run_all(self):
        for plugin in self.plugins:
            plugin.run()

class HelloPlugin(PluginBase):
    def run(self):
        print("Hello from plugin!")

if __name__ == "__main__":
    print("--- Observer Pattern ---")
    subj = Subject()
    subj.attach(lambda d: print(f"Observer 1: {d}"))
    subj.attach(lambda d: print(f"Observer 2: {d}"))
    subj.notify("Event!")

    print("\n--- Strategy Pattern ---")
    sorter = Sorter(QuickSort())
    print(sorter.sort([3, 1, 2]))
    sorter.strategy = ReverseSort()
    print(sorter.sort([3, 1, 2]))

    print("\n--- Decorator Pattern ---")
    notifier = EmailDecorator(SMSDecorator(Notifier()))
    notifier.send("Hello!")

    print("\n--- Adapter Pattern ---")
    old = OldAPI()
    new = NewAPI()
    adapter = APIAdapter(new)
    print(old.do_thing())
    print(adapter.do_thing())

    print("\n--- Command Pattern ---")
    invoker = Invoker()
    invoker.add_command(PrintCommand("First"))
    invoker.add_command(PrintCommand("Second"))
    invoker.run()

    print("\n--- Dependency Injection ---")
    client = Client(Service())
    print(client.operate())

    print("\n--- Fluent Interface ---")
    q = QueryBuilder().where("age > 18").order_by("name").build()
    print(q)

    print("\n--- Event-driven ---")
    emitter = EventEmitter()
    emitter.on("data", lambda x: print(f"Received: {x}"))
    emitter.emit("data", 42)

    print("\n--- Plugin Architecture ---")
    pm = PluginManager()
    pm.register(HelloPlugin())
    pm.run_all()
