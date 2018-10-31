fin = open("schedule.json", "r", encoding="UTF-8")
fout = open("Schedule2.proto", "w", encoding="UTF-8")

def parseJSON(arr):
    text = ""
    for i in range(len(arr)):
        text += arr[i].rstrip().lstrip()
    return JSONdecodeDict(text)


def JSONdecodeDict(text):
    dict = {}
    splitedText = dictTextSpliter(text)
    for key in splitedText.keys():
        if splitedText[key][0] == '{':
            dict[key] = JSONdecodeDict(splitedText[key][1:-1])
        elif splitedText[key][0] == '[':
            dict[key] = JSONdecodeArray(splitedText[key][1:-1])
        elif splitedText[key][0] == '"' or splitedText[key][0] == "'":
            dict[key] = splitedText[key][1:-1]
        else:
            dict[key] = splitedText[key]
    return dict


def JSONdecodeArray(text):
    array = []
    splitedText = arrayTextSpliter(text)
    print(splitedText)
    for obj in splitedText:
        if obj[0] == '{':
            array.append(JSONdecodeDict(obj[1:-1]))
        elif obj[0] == '[':
            array.append(JSONdecodeArray(obj[1:-1]))
        elif obj[0] == '"' or obj[0] == "'":
            array.append(obj[1:-1])
        else:
            array.append(obj)
    return array


def arrayTextSpliter(text):
    array = []
    cnt = 0
    indexLast = 0
    value = ""
    for i in range(len(text)):
        c = text[i]
        if c == '{' or c == '[':
            cnt += 1
        if c == '}' or c == ']':
            cnt -= 1
        if c == ',' and cnt == 0:
            value = text[indexLast:i].rstrip().lstrip()
            indexLast = i + 1
            array.append(value)
            value = ""
    if cnt == 0:
        value = text[indexLast::].rstrip().lstrip()
        array.append(value)
    return array


def dictTextSpliter(text):
    dict = {}
    cnt = 0
    indexLast = 0
    indexLast = 0
    name = ""
    value = ""
    for i in range(len(text)):
        c = text[i]
        if c == ":" and cnt == 0:
            name = text[indexLast:i].rstrip().lstrip()[1:-1]
            indexLast = i + 1
        if c == '{' or c == '[':
            cnt += 1
        if c == '}' or c == ']':
            cnt -= 1
        if c == ',' and cnt == 0:
            value = text[indexLast:i].rstrip().lstrip()
            indexLast = i + 1
            dict[name] = value
            name = ""
            value = ""
    if cnt == 0:
        value = text[indexLast::].rstrip().lstrip()
        dict[name] = value
    return dict


def PROTOBUFencode(dict):
    return


text = fin.readlines()
shedule = parseJSON(text)
print(shedule)

fin.close()
fout.close()