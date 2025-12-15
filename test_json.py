import json

x={
    "a": 1,
    "B": True,
    "abcd": "efgh",
}

with open("test_json", "w") as abcd:
    json.dump(x, abcd)