
d = {'(':1,')':-1}

def check(p):
    ch = []
    ch.append(p[0])
    for i in range(1,len(p)):
        if p[i] == ')' and ch[-1] =='(':
            ch.pop()
        else:
            ch.append(p[i])
    if len(ch)==0:
        return True
    else:
        return False
    
def split(p):
    u,v = '',''
    ch = 0
    for i in range(len(p)):
        u += p[i]
        ch += d[p[i]]
        if ch==0:
            break           
    if i < len(p)-1:
        v = p[i+1:]

    return u,v

def reverse(p):
    return ''.join([')' if j == '(' else '(' for j in p])
    

def recursive(p):
    if p =='':
        return ''
    u,v = split(p)
    if check(u):
        return u + recursive(v)
    else:
        return '(' + recursive(v) + ')' + reverse(u[1:-1])
    
def solution(p):
    if check(p):
        answer = p
    else:
        answer = recursive(p)
    return answer
