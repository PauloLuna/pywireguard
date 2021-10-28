from base64 import b64decode

from ..peer import Peer


class UserspacePeer(Peer):
    def serialize(self):
        result = f"public_key={b64decode(self.public_key).hex()}"
        if self.preshared_key is not None:
            result += f"\npreshared_key={b64decode(self.preshared_key).hex()}"
        if self.endpoint is not None:
            result += f"\nendpoint={self.endpoint}"
        if self.allowed_ips is not None:
            result += "\n" + "\n".join([f"allowed_ip={ip}" for ip in self.allowed_ips])
        return result
