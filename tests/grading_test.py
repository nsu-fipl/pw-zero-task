import hashlib

expected = '''f435c0997fd15c22554baf2856141cffef084be0d35af48eb72ba026b66a4a1b
94c7f92af0ea0b2ba78e722b3f08bd9d441d9a53dbe9965b0dd5cb1fa09216bb
c32f2b1a66f8a79deadb74f533f3075c60a629df343b89e8c4477d40fa960ba8
cdaf613756b3d7f18c78ec3e0b7b1442783c8da5f7d46b4046bdd7f5c95d4047
f435c0997fd15c22554baf2856141cffef084be0d35af48eb72ba026b66a4a1b
f98432d37591f2fc409dd49e64b690fdec641320bbf18e83d9b0892d914b3fe9
1878e420281704a4dd509b7e730b8ffe57e146fdbceee3d1fe1f9076fdddea2b
f435c0997fd15c22554baf2856141cffef084be0d35af48eb72ba026b66a4a1b
01daaaadd81e61d0c19a105d845cf91e1fefe09a20d90d935097bc27cdefa81a
f435c0997fd15c22554baf2856141cffef084be0d35af48eb72ba026b66a4a1b
f35b602729835181c0de990f0b6b1e152960ef0403e504c208cafa4a34f96a84
c32f2b1a66f8a79deadb74f533f3075c60a629df343b89e8c4477d40fa960ba8
3bd5d91bfe70a5b1fac5780f6a451a9fddb28a35787918fc15d88bc0d52096d1
182645a6314d5e8ba74d3e3f0b0ca54188d5a2a2dd82b3bd67bbeb5e000d62b9
b8ff72cc22dc047cf4e64ccdeaf7c239c1b8f65bb8cfee438591b3cf71bc9701
f435c0997fd15c22554baf2856141cffef084be0d35af48eb72ba026b66a4a1b
6479dd7fda04d097f59e12c0d8dc9cae4d45e0855d93b93f228e75b449a67951
c32f2b1a66f8a79deadb74f533f3075c60a629df343b89e8c4477d40fa960ba8
56fd311890b9d4f9f6d96f143cc4d43c2acfd8a2390edbc9e73ac081caab0a29
bcc16eea570e9d454d27c6a0b031c99f25ce6998f4030eb30f8ad6ac51999c0e
f435c0997fd15c22554baf2856141cffef084be0d35af48eb72ba026b66a4a1b
c8471010f1bc07ee6a7419b56c669b4cc583ddb6f1c6d4dbe1021665852628c5
f435c0997fd15c22554baf2856141cffef084be0d35af48eb72ba026b66a4a1b
c8471010f1bc07ee6a7419b56c669b4cc583ddb6f1c6d4dbe1021665852628c5
182645a6314d5e8ba74d3e3f0b0ca54188d5a2a2dd82b3bd67bbeb5e000d62b9
b8ff72cc22dc047cf4e64ccdeaf7c239c1b8f65bb8cfee438591b3cf71bc9701
936a62f07ab05eda42cc5fedfb449f3d1ca1ccacee0e1e9270becb593f60d8c3
c32f2b1a66f8a79deadb74f533f3075c60a629df343b89e8c4477d40fa960ba8
'''


def normalize(cmd):
    return " ".join(cmd.rstrip('\n').split())


def hex(cmd):
    return hashlib.sha256(cmd.encode('utf-8')).hexdigest()


def test_git():
    with open("commands.txt") as f:
        cmd = f.readline()
        print(cmd)
        assert cmd
        assert "clone" in cmd, f"Incorrect git clone line"

        hashes = expected.strip('\n').split('\n')
        for i, cmd in enumerate(f):
          assert i < len(hashes), f"Too many git commands, expected {len(hashes) + 1} commands"
          actual_hex = hex(normalize(cmd))
          expected_hex = hashes[i]
          assert actual_hex == expected_hex, f"Incorrect git command at line: {i + 1 + 1}"
        
        assert i == len(hashes) - 1, f"Too few git commands, expected {len(hashes) + 1} commands"
