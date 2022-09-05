import math

def solution(test):
    def dfs(c, sx, sy, tx, ty):
        if (sx, sy) in seen:
            return False
        
        seen.add((sx, sy))
        
        if sx > tx or sy > ty: 
            return False
        
        n = sx + sy
        a = math.sqrt(n)
        if a * a == n:
            return False
        
        if sx == tx and sy == ty: 
            return True
        
        return dfs(c, sx+sy, sy, tx, ty) or dfs(c, sx, sy+sx, tx, ty) or dfs(c, sx+c, sy+c, tx, ty)
    
    seen = set()
    c, sx, sy, tx, ty = test[0], test[1], test[2], test[3], test[4]
    return dfs(c, sx+sy, sy, tx, ty) or dfs(c, sx, sy+sx, tx, ty) or dfs(c, sx+c, sy+c, tx, ty)
    
    


test = [1,1,4,7,6]
test2 = [1,4,3,6,4]
print(solution(test))
print(solution(test2))

