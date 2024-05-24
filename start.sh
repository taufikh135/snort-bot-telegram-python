sudo snort -i enp0s3 -c /etc/snort/snort.conf -l /var/log/snort -d -A console > ./snort-log.txt
python app.py