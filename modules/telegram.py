class Telegram:
    def __init__(self, apiKey: str) -> None:
        self.__apiKey = "API_KEY"
        
    def sendMessage(self, chatId: int, message: str) -> None:
        pass