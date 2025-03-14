import hashlib

from inspect_ai.tool import bash, ToolDef

def hash_string(string: str) -> str:
    hash_object = hashlib.sha256()
    hash_object.update(string.encode("utf-8"))
    hex_digest = hash_object.hexdigest()
    return hex_digest


if __name__ == "__main__":
    print(hash_string(ToolDef(bash).name))
