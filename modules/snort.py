from time import sleep
from modules.telegram import Telegram
from modules.firewall import Firewall
    
class Snort:    
    def __init__(self, logFile: str, telegram: Telegram, firewall: Firewall) -> None:
        self.__logFile = logFile
        self.__prevLog = self.__getLogCount()
        self.__currLog = self.__prevLog
        self.__telegram = telegram
        self.__firewall = firewall
        
    def setTelegramChatID(self, chatId: int) -> None:
        self.__TelegramChatID = chatId
        
    def __getAllLog(self) -> list:
        with open(self.__logFile, "r") as file:
            return file.read().splitlines()
        
    def __getLogCount(self) -> int:
        return len(self.__getAllLog())
        
    def __getLogByIndex(self, index: int) -> str:
        return self.__getAllLog()[index]
    
    def analyze(self, ips: bool = False) -> None:
        # infinit loop untuk pengecekan
        while True:
            # get data jumlah data log terbaru mas=
            self.__currLog = self.__getLogCount()
            
            print('prev:', self.__prevLog)
            print('curr:', self.__currLog)
            
            # pesan notifikasi
            message = 'Hallo Tim Cyber Security. Saat ini terjadi penyerangan pada server.\n'
            
            # cek jika terdapat penyerangan
            if self.__currLog > self.__prevLog:
                print("Serangan terdeteksi.")
                
                # ambil semua log penyerangan terbaru
                for i in range(self.__prevLog, self.__currLog):
                    message += f'\n{self.__getLogByIndex(i)}'
                
                # kirimkan pesan ke telegram
                self.__telegram.sendMessage(chatId=self.__TelegramChatID, message=message)
                    
                # perbarui log sebelumnya
                self.__prevLog = self.__currLog
            
            if self.__currLog < self.__prevLog:
                self.__prevLog = self.__currLog
                
            # istirahat 2 detik
            sleep(2)