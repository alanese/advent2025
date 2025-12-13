from typing import Any
import json

def get_value_p1(thing: Any) -> int:
    if isinstance(thing, int):
        return thing
    elif isinstance(thing, list) or isinstance(thing, tuple):
        return sum([get_value_p1(entry) for entry in thing])
    elif isinstance(thing, dict):
        return sum([get_value_p1(k) + get_value_p1(v) for k,v in thing.items()])
    else:
        return 0
    
with open("input-12.txt") as f:
    data = json.loads(f.read())

print(get_value_p1(data))

#----------------------------
def get_value_p2(thing: Any) -> int:
    if isinstance(thing, int):
        return thing
    elif isinstance(thing, list) or isinstance(thing, tuple):
            return sum([get_value_p2(entry) for entry in thing])        
    elif isinstance(thing, dict):
        if "red" in thing.values():
            return 0
        else:
            return sum([get_value_p2(k) + get_value_p2(v) for k,v in thing.items()])
    else:
        return 0
    
print(get_value_p2(data))