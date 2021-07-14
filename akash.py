#!/usr/bin/python3

import cgi
from subprocess import getoutput
import subprocess

print("content-type:text/html")
print("Access-Control-Allow-Origin:*")
print("")

form = cgi.FieldStorage()

cmd = form.getvalue("command")
def kube(custom_cmd):
    print(getoutput(f"sudo kubectl {custom_cmd} --kubeconfig /root/admin.conf"))

if ("launch" in cmd or "run" in cmd or "create" in cmd or "make" in cmd)  and "pod" in cmd:
    if "name" in cmd  and "is" in cmd:
        cmd1 = cmd.split()
        #print(cmd1)
        cmd_index = cmd1.index("name")
        name = cmd1[cmd_index+2]
        #print(name)
        img_name = cmd1[cmd1.index("image")+1]
        kube(f"run {name} --image {img_name}")
        
    
    elif "name" in cmd:
        cmd1 = cmd.split()
        #print(cmd1)
        cmd_index = cmd1.index("name")
        name = cmd1[cmd_index+1]
        #print(name)
        kube(f"run {name} --image centos")
        img_name = cmd1[cmd1.index("image")+1]
        kube(f"run {name} --image {img_name}")



elif ("create" in cmd  or  "launch" in cmd or  "make" in cmd) and  "deployment" in cmd:
        if "name" in cmd  and "is" in cmd and "image" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+2]
            img_name = cmd1[cmd1.index("image")+1]
            kube(f"create deployment {name} --image {img_name}")
        elif "name" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+1]
            img_name = cmd1[cmd1.index("image")+1]
            kube(f"create deployment {name} --image {img_name}")

        else:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("deployment")
            name = cmd1[cmd_index+1]
            img_name = cmd1[cmd1.index("image")+1]
            kube(f"create deployment {name} --image {img_name}")
            

elif "expose" in cmd and  "deployment" in cmd:
        if "name" in cmd  and "is" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+2]
            port = cmd1[cmd1.index("port")+1]
            kube(f"expose deployment {name} --port={port} --type=NodePort")
            kube(f"get service  {name}")
        elif "name" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+1]
            port = cmd1[cmd1.index("port")+1]
            kube(f"expose deployment {name} --port={port} --type=NodePort")
            kube(f"get service  {name}")
        else:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("deployment")
            name = cmd1[cmd_index+1]
            port = cmd1[cmd1.index("port")+1]
            kube(f"expose deployment {name} --port={port} --type=NodePort")
            kube(f"get service  {name}")

elif ("increase" in cmd or "scale" in cmd or  "replicate" in cmd ) or  "replica" in cmd or "decrease" in cmd:
        cmd1 = cmd.split()

        number = cmd1[cmd1.index("to")+1]
        if "name" in cmd  and "is" in cmd and "image" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+2]
            img_name = cmd1[cmd1.index("image")+1]
            kube(f"scale deployment {name} --replicas={number}")
            kube("get pods")
        elif "name" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+1]
            kube(f"scale deployment {name} --replicas={number}")
            kube("get pods")
        else:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("deployment")
            name = cmd1[cmd_index+1]
            kube(f"scale deployment {name} --replicas={number}")
            kube("get pods")
elif ("get" in cmd or "show" in cmd or "display" in cmd) and "pod" in cmd:
    kube("get pods")

elif ("get" in cmd or "show" in cmd or "display" in cmd) and "deployment" in cmd:
    kube("get deployments")

elif ("delete" in cmd or "destroy" in cmd)  and ("everything" in cmd or "entire" in cmd):
    kube("delete all --all")

elif "delete" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("delete")
            name = cmd1[cmd_index+2]
            name1 = cmd1[cmd_index+1]
            kube(f"delete {name1} {name}")
