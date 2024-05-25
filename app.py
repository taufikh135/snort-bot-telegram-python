from modules.firewall import Firewall
from modules.snort import Snort
from modules.telegram import Telegram

# Configurasi
logFile = "/var/log/snort/snort.alert.fast"
telegramConfig = {
    "apiKey": "", # API Key Telegram
    "chatId": -4244121384 # Chat ID Telegram
}
ips = False

# Inisialisasi class module
snort = Snort(logFile)
telegram = Telegram(telegramConfig["apiKey"])
firewall = Firewall()

def callback(logs: list) -> None:
    message = 'Hallo Tim Cyber Security. Saat ini terdeteksi penerangan pada Server.\n'
    
    for log in logs:
        logMessage: str = log['log']
        ipAttacker: str = log['ipAttacker']
        
        if ips:
            firewall.blockIP(ipAttacker)
        
        message += '\n\n' + logMessage
        
    telegram.sendMessage(telegramConfig["chatId"], message)
    
# Analisis Log
snort.analyze(callback)