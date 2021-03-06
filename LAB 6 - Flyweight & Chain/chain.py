from abc import ABC, abstractmethod
from better_profanity import profanity

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, text):
        pass

class AbstractHandler(Handler):

    next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, text):
        if self.next_handler:
            return self.next_handler.handle(text)
        return None 

class BadWordsHandler(AbstractHandler):
    def handle(self, text):
        bw = ['lista', 'przeklenstwo']
        if profanity.contains_profanity(text):
            return "Contained bad words"
        return super().handle(text)

class SemiColonHandler(AbstractHandler):
    def handle(self, text):
        if ";" in text:
            return "Contained semicolonss"
        else:
            return super().handle(text)

class SQLHandler(AbstractHandler):
    def handle(self, text):
        sql_syntax = ['select', 'insert', 'update', 'delete', 'truncate', 'drop', 'create', 'database', 'alter']
        if any(sql in text.lower() for sql in sql_syntax ):
            return "Contained sql syntax"  
        return super().handle(text)

def client_code(handler, text):
    result = handler.handle(text)
    if result:
        print(result)
        return False
    else:
        print("G00D N1CK")
        return True


if __name__ == "__main__":
    bwh = BadWordsHandler()
    sch = SemiColonHandler()
    sqlh = SQLHandler()
    bwh.set_next(sch).set_next(sqlh)
    _bool = False
    while not _bool:
        _bool = client_code(bwh, input("Write your nick: "))