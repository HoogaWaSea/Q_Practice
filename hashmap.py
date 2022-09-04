# def addToValue(hmap,k):
#     for key,val in hmap.items():
#         hmap[key]+=k
#     return hmap

# def addToKey(hmap,k):
#     newHmap={}
#     for key,val in hmap.items():
#         newKey = key+k
#     newHmap[newKey]=val
#     return newHmap

def solution(queryType, query):
    ans = 0
    hmap = {}
    ck = 0
    cv = 0
    for i in range(len(queryType)):
        cmd = queryType[i]
        quer = query[i]
        if cmd == "insert":
            key,val = quer[0],quer[1]
            hmap[key-ck]=val-cv
        elif cmd == "addToValue":
            k = quer[0]
            cv+=k
        elif cmd == "addToKey":
            k = quer[0]
            ck+=k
        else:
            k = quer[0]
            k-=ck
            val = hmap[k] + cv
            ans = ans + val
    return ans

queryType1 = ["insert", "insert", "addToValue", "addToKey", "get"]
querry1 = [[1,2], [2,3],[2],[1],[3]]


queryType2 = ["insert", "addToValue", "get",  "insert", "addToKey", "addToValue", "get"]
querry2 = [[1,2], [2], [1],[2,3],[1],[-1],[3]]


