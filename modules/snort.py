from time import sleep
from modules.telegram import Telegram
from modules.firewall import Firewall
import re
    
class Snort:    
    def __init__(self, logFile: str) -> None:
        self.__logFile = logFile
        self.__prevLog = self.__getLogCount()
        self.__currLog = self.__prevLog
        
    def __getAllLog(self) -> list:
        with open(self.__logFile, "r") as file:
            return file.read().splitlines()
        
    def __getLogCount(self) -> int:
        return len(self.__getAllLog())
        
    def __getLogByIndex(self, index: int) -> str:
        return self.__getAllLog()[index]
    
    def __parseIPAttacker(self, log: str) -> str:
        regex = r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})'
        result = re.findall(regex, log)
        return result[0]
    
    def analyze(self, callback) -> None:
        ''' @param callback: def (logs: [{log, ipAttacker}]) -> None '''
        
        # infinit loop untuk pengecekan
        while True:
            # get data jumlah data log terbaru mas=
            self.__currLog = self.__getLogCount()
                        
            # cek jika terdapat penyerangan
            if self.__currLog > self.__prevLog:
                logs = []
                for i in range(self.__prevLog, self.__currLog):
                    log = self.__getLogByIndex(i)
                    ipAttacker = self.__parseIPAttacker(log)
                    
                    logs.append({ 
                        'log': log, 
                        'ipAttacker': ipAttacker 
                    })
                    
                callback(logs)
                    
            self.__prevLog = self.__currLog
                
            # istirahat 2 detik
            sleep(2)