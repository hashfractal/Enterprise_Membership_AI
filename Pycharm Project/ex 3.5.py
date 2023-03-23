import re
def read(text):
    strlist = str.split(text.strip(), ":")
    ridename = strlist[0].strip()
    if len(strlist) == 1:
        return ridename, None, None
    else:
        ridelimit = str.split(strlist[1], "~")
        if len(ridelimit) == 1:
            cmmin = re.sub(r'[^0-9]', " ", ridelimit[0]).strip()
            if len(cmmin) == 0:
                cmmin = None
            return ridename, cmmin, None
        else:
            cmmin = re.sub(r'[^0-9]', " ", ridelimit[0]).strip()
            cmmax = re.sub(r'[^0-9]', " ", ridelimit[1]).strip()
        return ridename, cmmin, cmmax

ridename, cmmin, cmmax = read(input())
print(f"이름: {ridename}\n하한: {cmmin}\n상한: {cmmax}")