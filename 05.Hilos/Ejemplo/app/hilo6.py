import subprocess
from threading import Timer

kill = lambda process: process.kill()
cmd = ['ping', 'www.uip.edu.pa']
ping = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

mi_timer = Timer(60, kill, [ping])

try:
    mi_timer.start()
    stdout, stderr = ping.communicate()
finally:
    mi_timer.cancel()

print(str(stdout))