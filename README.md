### Set-target:
Note, you must be able to execute commands as root with sudo to modify .zshrc or .bashrc file.

To begin, you must first have the following variables declared and exported in your .zshrc file like so:

```
trgtdc=X
trgt1=X
trgt2=X
trgt3=X

export trgtdc
export trgt1
export trgt2
export trgt3
```

Make the script executable and store it in the /bin directory

`sudo chmod +x set-target.py`
`sudo cp ./set-target.py /bin/set-target`

usage: 
set-target trgtdc 10.10.10.10
set-target trgt1 192.168.45.101
etc.


### Update-target
save the following command to a file called 'update-target'
`source /home/kali/.zshrc`

sudo cp update-target /bin/update-target
sudo chmod +x /bin/update-target


### View-target
save the following command to a file called 'get-target'
`env | grep trgt`

sudo cp view-target /bin/get-target
sudo chmod +x /bin/get-target


