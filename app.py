from modules.firewall import Firewall
from modules.snort import Snort
from modules.telegram import Telegram

# Configurasi
logFile = "snort-alert.log"
telegramConfig = {
    "apiKey": "6555493515:AAGN4uHsTl33xNE5MmnPySJaoixLnlC_LRI", # API Key Telegram
    "chatId": -4244121384 # Chat ID Telegram
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