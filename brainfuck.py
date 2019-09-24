import sys,os;M=[0]*30000;A=[]
p=k=x=0;S=open(sys.argv[1]).read()
while x<len(S):exec"""M[p]+=1
M[p]-=1 M[p]=ord(os.read(0,1)or"\\0")
os.write(1,chr(M[p])) p-=p>0 p+=1
k=A.append(x)if+M[p]else+1 x=A.pop()-1
k+=1 0 k-=1 0""".split()['+-,.<>[][+]+'
.find(S[x]+'+'*(k>0))];M[p]&=255;x+=1
