import subprocess
#subprocess.call("ifconfig")
f = open("ifconfig.txt", "w+")
p = subprocess.Popen("ifconfig", stdout = f, shell=False)
(output, err) = p.communicate()
f.write(str(output))
f.close()
