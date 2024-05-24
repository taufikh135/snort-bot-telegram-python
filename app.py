from modules.firewall import Firewall
from modules.snort import Snort
from modules.telegram import Telegram

# Configurasi
apiKeyTelegram = ""
logFile = "log.txt"

# Dependecies yang dibutuhkan
telegram = Telegram(apiKeyTelegram)
firewall = Firewall()

# Inisialisasi class snort dan menginject dependencies yang dibutuhkan
snort = Snort(logFile=logFile, telegram=telegram, firewall=firewall)

# Set Chat ID Telegram untuk notifikasi
snort.setTelegramChatID(123456789)

# Analisis Log
snort.analyze(ips=False)