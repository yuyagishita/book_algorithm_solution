s = '(()))('
st = list()
ps = list()

for i in range(len(s)):
    if s[i] == '(':
        st.append(i)
    else:
        if len(st) == 0:
            print('False')
            exit()
        t = st.pop()
        ps.append([t, i])

if len(st) == 0:
    print('True')
    print(sorted(ps))
else:
    print('False')
