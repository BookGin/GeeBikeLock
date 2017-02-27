# 2017 Make NTU - GeeBikeLock

[Make NTU](https://www.facebook.com/makentu.ntuee/) is a hackathon competition in Taipei, Taiwan.

## Team Members

- Chin Ning
- bookgin
- exe1023
- Vincy

## Our Product

![GeeBikeLock-logo](http://i.imgur.com/GZ3bOg2.png)

In this hackathon, we made an anti-theft IoT device *GeeBikeLock* which can be installed on a bike. Its main features are:

- It can be installed on any bike.
- It's equipped with GPS and accelerometer in order to detect if it's stolen.
- Equipped with RFID. You can lock/unlock it with your student ID card.
- We also have a cloud server. You can login the website to fully control the lock.

## Directory Structure
- `demo.mp4`: The live demo video. (in Mandarin)
- `GeeBikeLock.pdf`: The slide.
- `geebikelock.ino`: The source code running on Arduino, our IoT lock.
- `website`: The cloud backend server as well as the website.
- `sock_server.py`: The "bridge" which connects between the IoT lock and the server.
```
+---------+     +--------+    +---------+
|   IoT   |     |  sock  |    |  web    |
|   Lock  +-----+ server +----+ server  |
|(Arduino)|     |  .py   |    |(backend)|
+---------+     +--------+    +---------+
```
- `addBike.py`: A test script to emulate an IoT lock returning its current state.
- `usb2remote`: Because we encounter some problem when installing Arduino's wifi module, we choose to perform port forwarding between Arduino USB port and remote webserver port. This is strongly deprecated.


## Specification

### Auduino transmits to *sock\_server*:

- id (bike-id) can only cantain alphanumeric chacracters. (i.e. [a-zA-Z0-9])
- uid is RFID, represented as a 8-digit hex number. 
- If no card is readed, simply return uid=00000000.
- In the source, the GPS location is generated in random due to debugging.

```
id=bike7122
lat=121.239156
lng=25.033570
x=0.79 
y=0.27 
z=-0.42 
uid=00000000
*
```

### *sock\_server* to web server(backend):
- uid is represented as a interger.
- gps[0], gps[1] = lng, lat

Send HTTP POST to `bike.csie.org/map/[BIKE_ID]/`.
The POSt data is in JSON format:
```json
{
  "gps": [25.25245333, 121.54130],
  "axis": [0.8, 3.2, 3.32],
  "uid": 0
}
```

## Dependency

- Website: Python3 web framework, Django.
- IoT Lock: Arduino equipped with accelerometer, GPS.
