exp = "34+12-*"

st = list()

for i in range(len(exp)):
    if exp[i].isdecimal():
        st.append(int(exp[i]))
    else:
        ans = 0
        b = st.pop()
        a = st.pop()
        if exp[i] == '+':
            st.append(int(a) + int(b))
        elif exp[i] == '-':
            st.append(int(a) - int(b))
        elif exp[i] == '*':
            st.append(int(a) * int(b))
        else:
            st.append(int(a) / int(b))
        print(st)

print(st.pop())
