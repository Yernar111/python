import json

print("Interface status")
print("="*80)
print(f"{'DN':<50} {'Description':<20}  {'Speed':<10} {'MTU'}")
print(f"{'-'*50} {'-'*20} {'-'*8} {'-'*8}")

with open("json-sample.json", "r") as abcd:
    u=json.load(abcd)
    a=u["imdata"]
    for i in range(len(a)):
        b=a[i]["l1PhysIf"]["attributes"]["dn"]
        c=a[i]["l1PhysIf"]["attributes"]["descr"]
        d=a[i]["l1PhysIf"]["attributes"]["speed"]
        e=a[i]["l1PhysIf"]["attributes"]["mtu"]
        print(f"{b:<50} {c:<20} {d:<10} {e}")

