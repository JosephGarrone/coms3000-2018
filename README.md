# COMS3000 2018 - Assignment 3

>TODO: About the project

## Requirements

- Python3 (Probably not though)

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
|-- python (Probably not needed)
    |-- target_processor.py (Converts raw into targets.json)
|-- target
    |-- processed (Probably not needed)
        |-- targets.json (Processed JSON file with user and pwd info)
    |-- raw
        |-- passwd9 (Raw user info)
        |-- shadow9 (Raw password info)
```

## Running

1. Open a command prompt in `<repo>\bin\john-the-ripper\windows\`
2. Run `john.exe ..\..\..\targets\raw\shadow`
3. Profit?

## Configuration

Modify `<repo>\bin\john-the-ripper\windows\john.conf` (To add rules etc) and `<repo>\bin\john-the-ripper\windows\password.lst` (To add password guesses)

## Commands to run

**Show cracked passwords to date:**
```bash
john.exe --show ..\..\..\targets\raw\shadow
```