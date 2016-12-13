from abc import ABCMeta, abstractmethod


class Action(object, metaclass=ABCMeta):
    @property
    @abstractmethod
    def action_required(self):
        pass


class FullAction(Action, metaclass=ABCMeta):
    @property
    def action_required(self):
        return FullAction


class QuickAction(Action, metaclass=ABCMeta):
    @property
    def action_required(self):
        return QuickAction


class QuickSpellAction(Action, metaclass=ABCMeta):
    @property
    def action_required(self):
        return QuickSpellAction
