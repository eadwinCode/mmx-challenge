from abc import ABC, abstractmethod


class Executor(ABC):
    @abstractmethod
    def execute_task(self, task, **kwargs):
        pass


class TaskExecutor(Executor):
    @classmethod
    def execute_task(cls, task, **kwargs):
        if hasattr(task, 'delay') and callable(task.delay):
            return task.delay(**kwargs)


class MockExecutor(Executor):
    @classmethod
    def execute_task(cls, task, **kwargs):
        return task(**kwargs)
