from modules.firewall import Firewall
from modules.snort import Snort
from modules.telegram import Telegram

# Configurasi
logFile = "snort-log.txt"
telegramConfig = {
    "apiKey": "", # API Key Telegram
    "chatId": 0 # Chat ID Telegram
}

# Dependecies yang dibutuhkan
telegram = Telegram(telegramConfig["apiKey"])
firewall = Firewall()

# Inisialisasi class snort dan menginject dependencies yang dibutuhkan
snort = Snort(logFile=logFile, telegram=telegram, firewall=firewall)

# Set Chat ID Telegram untuk notifikasi
snort.setTelegramChatID(telegramConfig["chatId"])

# Analisis Log
snort.analyze(ips=False)