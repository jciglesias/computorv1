def parsing(monomes: list):
    ret = 0
    try :
        int(monomes[0])
    except :
        print("try int")
        return 1
    if monomes[1] != '*' or monomes[1] != '-' or monomes[1] != "+" or monomes[1] != "/" :
        return 1
    if monomes[2][0] != "X" or monomes[2][1] != "^":
        return 1
    try :
        ret = parsing(monomes[4::])
    except :
        print(ret)
        pass
    return ret

def solve(args: str):
    print("solve\n", args)