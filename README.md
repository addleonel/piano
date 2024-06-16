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


**Make the Script Executable**: Make the shell script executable by running:

```
chmod +x run_piano.sh
./run_piano.sh
```

**Create a systemd Service Unit**: Create a systemd service unit file to define the service. For example, create a file named `piano.service` in the `/etc/systemd/system/` directory

**Reload systemd,enable the Service, and Run**: After creating the service unit file, reload systemd to load the new configuration and enable the service to start automatically at boot time:

```
sudo systemctl daemon-reload 
sudo systemctl enable piano1.service
sudo systemctl start piano1.service
sudo systemctl status piano1.service
sudo journalctl -u piano1.service

```

Options to run a script on startup in linux

https://www.baeldung.com/linux/run-script-on-startup

