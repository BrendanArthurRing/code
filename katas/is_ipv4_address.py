def isIPv4Address(s):
    try:
        ip_arr = [int(i) for i in s.split('.')]
        if len(ip_arr) == 4:
            for i in ip_arr:
                if i > 255:
                    return False
            return True
        return False
    except:
        return False


# The best solution was

def isIPv4Address(s):
    p = s.split('.')

    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)
