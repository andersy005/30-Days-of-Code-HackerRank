def number_needed(a, b):
    for ch in a:
        if ch in b:
            a = a.replace(ch, '', 1)
            b = b.replace(ch, '', 1)
            
    for ch in b:
        if ch in a:
            a = a.replace(ch,'',1)
            b = b.replace(ch,'',1)
            
    return len(a) + len(b)

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
