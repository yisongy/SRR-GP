import os
def getLabel():
    distribution = str(os.getcwd())[-7:]
    a = open("result_" + str(distribution))
    b = open("result_" + str(distribution)[0:3])
    c = open("result_" + str(distribution)[4:7])

    Label0 = []
    for line in a:
        Label0 = line

    LabelA = []
    for line in b:
        LabelA = line

    LabelB = []
    for line in c:
        LabelB = line

    return Label0, LabelA, LabelB

def getfailedAndsucc(Label0):
    failed = []
    sign = 0
    for i in Label0:
        sign += 1
        if i == '1':
            failed.append(sign)

    succ = []
    sign = 0
    for i in Label0:
        sign += 1
        if i == '0':
            succ.append(sign)
    return failed, succ
