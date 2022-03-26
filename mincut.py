import math
import random
import graphviz
import copy
from py_linq import Enumerable
def minCut():
    with open(r"C:\Users\shiry\Downloads\mincut\temp\26.txt") as req_file:
        mincut_data = []
        for line in req_file:
            line = line.split()
            if line:
                line = [int(i) for i in line]
                mincut_data.append(line)
    print('Выберите граф от 1 до 20')
    choice = int(input())
    data_choice = []
    countNodes = mincut_data[0][0]
    iter = 0
    var = Enumerable(mincut_data).where(lambda x: len(x) != 2)
    var = list(var)
    lst = []
    temp = []
    for item in var:
        iter += 1
        if iter == countNodes:
            iter = 0
            temp.append(item)
            lst.append(copy.deepcopy(temp))
            temp.clear()
        else:
            temp.append(item)
    iter = 1
    for i in range(countNodes):
        k = 1
        temp = []
        temp.append(iter)
        for j in lst[choice-1][i]:
            if j == 1:
                temp.append(k)
            k+=1
        data_choice.append(temp)
        iter+=1
    edgelist = []
    nodelist = []
    for every_list in data_choice:
        nodelist.append(every_list[0])
        temp_list = []
        for temp in range(1, len(every_list)):
            temp_list = [every_list[0], every_list[temp]]
            flag = 0
            for ad in edgelist:
                if set(ad) == set(temp_list):
                    flag = 1
            if flag == 0:
                edgelist.append([every_list[0], every_list[temp]])
    d = graphviz.Graph('ER', filename='er.gv', engine='neato')
    for node in nodelist:
        d.node(str(node), color="red")
    eTemp = []
    for i in range(len(edgelist)):
        if edgelist[i][0] != edgelist[i][1]:
            eTemp.append(edgelist[i])
    #edgelist = copy.deepcopy(eTemp)
    EdgeDic = {}
    itr = 0
    for edge in edgelist:
        EdgeDic[itr] = edge
        itr+=1
        d.edge(str(edge[0]),str(edge[1]),str(itr))
    d.view()
    def karger_1(EdgeDic):
        count = 1000
        while count>2:
            keys = list(EdgeDic.keys())
            if len(keys) == 0:
                break
            keyI = random.choice(keys)
            r = EdgeDic[keyI]
            v1 = r[0]
            v2 = r[1]
            del EdgeDic[keyI]
            delList1 = []
            delList2 = []
            for kv in EdgeDic:
                if EdgeDic[kv][0] == v2:
                    delList1.append(kv)
                elif EdgeDic[kv][1] == v2:
                    delList2.append(kv)
            for item in delList1:
                temp = EdgeDic[item]
                temp[0] = v1
                EdgeDic[item] = temp
            for item in delList2:
                temp = EdgeDic[item]
                temp[1] = v1
                EdgeDic[item] = temp
            eDic = copy.deepcopy(EdgeDic)
            EdgeDic = {key: val for key, val in eDic.items() if val[0] != val[1]}
            nodes = []
            for kv in EdgeDic:
                for value in EdgeDic[kv]:
                    nodes.append(value)
            nodes = list(Enumerable(nodes).distinct())
            count = len(nodes)
        return EdgeDic

    def karger_stein(EdgeDic, n):
        count = 1000000
        e = {}
        while count>math.sqrt(n):
            keys = list(EdgeDic.keys())
            if len(keys) == 0:
                break
            keyI = random.choice(keys)
            r = EdgeDic[keyI]
            v1 = r[0]
            v2 = r[1]
            del EdgeDic[keyI]
            delList1 = []
            delList2 = []
            for kv in EdgeDic:
                if EdgeDic[kv][0] == v2:
                    delList1.append(kv)
                elif EdgeDic[kv][1] == v2:
                    delList2.append(kv)
            for item in delList1:
                temp = EdgeDic[item]
                temp[0] = v1
                EdgeDic[item] = temp
            for item in delList2:
                temp = EdgeDic[item]
                temp[1] = v1
                EdgeDic[item] = temp
            eDic = copy.deepcopy(EdgeDic)
            EdgeDic = {key: val for key, val in eDic.items() if val[0] != val[1]}
            nodes = []
            for kv in EdgeDic:
                for value in EdgeDic[kv]:
                    nodes.append(value)
            nodes = list(Enumerable(nodes).distinct())
            count = len(nodes)
            e = copy.deepcopy(EdgeDic)
        res = karger_1(e)
        return res

    def operation(n):
        i = 0
        count = 10000
        ans = []
        while i < n:
            i += 1
            e = copy.deepcopy(EdgeDic)
            b = karger_1(e)
            if len(b) < count:
                ans.clear()
                count = len(b)
                for item in b:
                    ans.append(item)
        return count,ans

    def operation_ks(n):
        i = 0
        count = 10000
        ans = []
        while i < n:
            i += 1
            e = copy.deepcopy(EdgeDic)
            b = karger_stein(e, countNodes)
            if len(b) < count:
                ans.clear()
                count = len(b)
                for item in b:
                    ans.append(item)
        return count,ans
    print("Алгоритм Каргера --- 1 || Алгоритм Каргера-Штейна --- 2")
    ch_type = int(input())
    if ch_type == 1:
        cnt, a = operation(10*len(nodelist)*len(nodelist))
    else:
        cnt, a = operation_ks(len(nodelist))
    print('Количество элементов в минимальном разрезе: '+str(cnt))
    for item in a:
        print(item+1)



