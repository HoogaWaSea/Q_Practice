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
    dic = {}
    curKey = 0
    curVal = 0
    
    for i in range(len(queryType)):
        print(dic)

        if queryType[i] == "insert":
            key, val = query[i][0], query[i][1]
            dic[key-curKey] = val - curVal
            
        elif queryType[i] == "addToValue":
            k = query[i][0]
            curVal += k
            
        elif queryType[i] == "addToKey":
            k = query[i][0]
            curKey += k
            
        else:
            k = query[i][0]
            k -= curKey
            val = dic[k] + curVal
            ans = ans + val
            print(ans)
            
    return ans

queryType1 = ["insert", "insert", "addToValue", "addToKey", "get"]
query1 = [[1,2], [2,3],[2],[1],[3]]


queryType2 = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"]
query2 = [[1,2], [2], [1],[2,3],[1],[-1],[3]]

solution(queryType1, query1)
solution(queryType2, query2)


