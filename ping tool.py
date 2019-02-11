import ping
import re
ip = "114.114.114.114"
info = ping.cmd_command(ip)
rematch = re.search(r"时间(.*?)",info,re.S)
print(rematch)