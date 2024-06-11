### SWAP SDCARD

```
sudo mkswap -L sdswap /dev/mmcblk1
sudo swapon /dev/mmcblk1
```
More info about this: [Adding a swapfile](https://github.com/f0cal/google-coral/issues/5)
### Mounting USB Driver

```
sudo apt update
sudo apt install exfat-fuse exfat-utils
sudo lsblk
sudo mkdir /mnt/usb
sudo mount /dev/sda1 /mnt/usb
```

### Open an audio file

```
sudo apt update
sudo apt-get install mplayer
mplayer your-audio-file.mp3
```
### Activate Bluetooth

```
sudo apt update
sudo apt install bluetooth bluez blueman
sudo systemctl enable bluetooth
sudo systemctl start bluetooth
sudo systemctl status bluetooth

bluetoothctl
power on
discoverable on
scan on
pair <MAC>
connect <MAC>
quit
```

### To run a script automatically

**Create a shell script:** Create `run_piano.sh` file
```
#!/bin/bash python /path/to/your/runv1.py
```

**Make the Script Executable**: Make the shell script executable by running:

```
chmod +x run_piano.sh
```

**Create a systemd Service Unit**: Create a systemd service unit file to define the service. For example, create a file named `myservice.service` in the `/etc/systemd/system/` directory

**Reload systemd and Enable the Service**: After creating the service unit file, reload systemd to load the new configuration and enable the service to start automatically at boot time:

```
sudo systemctl daemon-reload 
sudo systemctl enable myservice
```
 
 **Start the Service**: You can start the service manually using:
 
```
sudo systemctl start myservice
```
