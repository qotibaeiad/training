def Common_Prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for st in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(st) and prefix[i] == st[i]:
            i += 1
        if i < len(prefix):
            prefix = prefix[:i]
        if not prefix:
            return ""

    return prefix
example3 = Common_Prefix(["eiv","eiade", "eiad"])
print(example3)
