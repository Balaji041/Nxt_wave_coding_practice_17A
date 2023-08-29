S=input()
S_est=ord(S[0])
for i in range(1,len(S)):
    if S_est > ord(S[i]):
        S_est=ord(S[i])
print(chr(S_est))
"""
input:edit
output:d
"""
