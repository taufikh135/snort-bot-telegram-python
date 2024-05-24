import requests
class Telegram:
    def __init__(self, apiKey: str) -> None:
        self.__apiKey = apiKey
        
    def sendMessage(self, chatId: int, message: str) -> None:
        url = f"https://api.telegram.org/bot{self.__apiKey}/sendMessage"
        params = {
            "chat_id": chatId, 
            "text": message
        }
        
        response = requests.get(url, params=params)
        print('message sent status code:', response.status_code)