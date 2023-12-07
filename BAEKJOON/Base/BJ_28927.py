a,b,c = map(int,input().split())
d,e,f = map(int,input().split())
g=(a*3)+(b*20)+(c*120)
h=(d*3)+(e*20)+(f*120)

if(g>h):
    print("Max")
elif(g<h):
    print("Mel")
else:
    print("Draw")