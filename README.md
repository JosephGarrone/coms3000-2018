# COMS3000 2018 - Assignment 3

>TODO: About the project

## Folder Overview

```bash
<repo>
|-- bin
    |-- john-the-ripper
        |-- windows
            <All the john-the-ripper files>
            |-- john.pot (cracked passwords)
            |-- john.rec (john save file so you can resume later)
            |-- john.conf (configuration file)
            |-- john.log (output log)
            |-- passwords.lst (list of passwords to try)
|-- output
    |-- cracked-passwords.txt (Cracked passwords so far)
|-- password-lists
    |-- password.lst (Dictionary to be used)
    |-- crackstation files (torrent files to be downloaded)
|-- target
    |-- raw
        |-- passwd (Raw user info)
        |-- shadow (Raw password info)
        |-- hashes-only.txt (Hashes without user info)
```

## Running

1. Open a command prompt in `<repo>\bin\john-the-ripper\windows\`
2. Run `.\john ..\..\..\target\raw\shadow --wordlist=..\..\..\password-lists\password.lst --rules:COMS3000`
3. Profit?

## Configuration

Modify `<repo>\bin\john-the-ripper\windows\john.conf` (To add rules etc) and `<repo>\bin\john-the-ripper\windows\password.lst` (To add password guesses)

## Commands to run

**Crack passwords using our rules:**
```bash
john.exe ..\..\..\targets\raw\shadow --wordlist=dictionary.txt --rules=COMS3000
```

**Show cracked passwords to date:**
```bash
john.exe --show ..\..\..\targets\raw\shadow
```

## VM Instructions
```bash
gcloud compute instances create gpu-instance-1 --machine-type n1-standard-8 --zone us-west1-b --accelerator type=nvidia-tesla-v100,count=8 --image-family ubuntu-1604-lts --image-project ubuntu-os-cloud --maintenance-policy TERMINATE --boot-disk-size 250GB
```