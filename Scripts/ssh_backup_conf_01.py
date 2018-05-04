import paramiko
import time

with open("cisco.txt") as f:
    res = f.read().split('\n')

for line in res:
    line = line.split()
    hostname = line[0]
    mgmt_ip = line[1]
    username = line[2]
    password = line[3]
    port = line[4]

    print("ssh %s_%s" % (hostname, mgmt_ip)) 
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(mgmt_ip, port, username, password)
    stdin, stdout, stderr = ssh.exec_command("show run")
    output = stdout.read().decode()
    ssh.close()
    
    time = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())
    save = "%s_%s_%s.txt" % (hostname, mgmt_ip, time)
    
    with open(save, "w") as f:
        f.write(output)
    
    print("%s_%s backup configuration success!" % (hostname, mgmt_ip))
