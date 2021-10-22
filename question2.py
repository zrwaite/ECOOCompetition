line=input()
answer=""
last_char=""
for i in range(len(line)):
    char=line[i]
    if (char=="A" and last_char=="A") or (char!="A" and last_char!="A"): 
        answer+=" "
    last_char=char
    answer+=char
print(answer)