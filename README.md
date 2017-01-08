# SmartClub - Pi

This is the Raspberry Pi module of the SmartClub project. This module collects audio from the crowd, and sends the amplitudes
to the server.

The master repo for this project is located at https://github.com/meggrasse/smartclub.

## Requirements

Microphone, I2C and Pi. I am using a MAX4466 amp, a PCF8591 converter and a Pi 3B. Explaining how to wire I2C is out of the
scope of this README, but there are a ton of resources on Google.

## Setup

Edit the URL to represent your server location.

## Usage

Use git clone to get this script into the root directory of your Pi. Then, in your Pi's root directory, run:

```bash
$ python rasp.py
```
