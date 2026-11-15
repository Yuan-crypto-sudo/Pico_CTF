import base64
from urllib.parse import unquote

expected = ("JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
            "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
            "JTM0JTVmJTMzJTYzJTYzJTM4JTYxJTM5JTY0JTM2")

bas64 = base64.b64decode(expected)


urldecode = unquote(bas64)

print("academy{" + urldecode + "}")