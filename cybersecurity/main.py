s = """adduser.conf
alternatives
apache2
apparmor
apparmor.d
apt
arp-scan
avahi
bash.bashrc
bash_completion
bash_completion.d
bindresvport.blacklist
binfmt.d
bluetooth
ca-certificates
ca-certificates.conf
chatscripts
chromium
chromium.d
cifs-utils
cloud
colord
console-setup
cracklib
credstore
credstore.encrypted
cron.d
cron.daily
cron.hourly
cron.monthly"""

lst = s.split('\n')
print(lst == sorted(lst))
