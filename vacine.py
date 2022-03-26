import random
import graphviz

def VisGraph(p1, p2, t1, t2, gr, n, t):
    """Визуализация задачи о нахождении минимального времени производстве продукта

    :param p1: список, содержащий информацию о времени производства каждого этапа на заводе1
    :param p2: список, содержащий информацию о времени производства каждого этапа на заводе2
    :param t1: список, содержащий информацию о времени перевозки продукта с завода1 на завод2
    :param t2: список, содержащий информацию о времени перевозки продукта с завода2 на завод1
    :param gr: список, содержащий информацию о передвижениях продукта между заводами
    :param n: количество этапов производства
    :param t: наименьшее время производства товара
    """
    d = graphviz.Digraph(filename='rank_same.gv')

    with d.subgraph(name='c1') as s:
        s.attr(style='filled', color='lightgrey')
        s.node_attr.update(style='filled', color='grey')
        for i in range(n):
            s.node('t1/' + str(i + 1) + '=' + str(p1[i]))

    with d.subgraph(name='c2') as s:
        s.attr(style='filled', color='blue')
        s.node_attr.update(style='filled', color='grey')
        for i in range(0, n):
            s.node('t2/' + str(i + 1) + '=' + str(p2[i]))

    for i in range(0, n - 1):
        d.edge('t1/' + str(i + 1) + '=' + str(p1[i]), 't1/' + str(i + 2) + '=' + str(p1[i + 1]))
        d.edge('t2/' + str(i + 1) + '=' + str(p2[i]), 't2/' + str(i + 2) + '=' + str(p2[i + 1]))
        d.edge('t1/' + str(i + 1) + '=' + str(p1[i]), 't2/' + str(i + 2) + '=' + str(p2[i + 1]), label=str(t1[i]))
        d.edge('t2/' + str(i + 1) + '=' + str(p2[i]), 't1/' + str(i + 2) + '=' + str(p1[i + 1]), label=str(t2[i]))
    for x in range(0,n):
        if gr[x] == 1:
            d.node('t'+str(gr[x])+'/' + str(x + 1) + '=' + str(p1[x]), color="red")
        else:
            d.node('t' + str(gr[x]) + '/' + str(x + 1) + '=' + str(p2[x]), color="red")
    d.node('S*='+str(t))
    s1 = 0
    s2 = 0
    for i in range(0,n):
        s1+=p1[i]
        s2+=p2[i]
    d.node('S1='+str(s1))
    d.node('S2='+str(s2))
    d.view()

def MinTime(n):
    """Нахождение минимального времени производства продукта на двух заводах(конвейерах)

    n - количество этапов производства
    """
    p1 = [random.randint(1, 10) for i in range(n)]
    p2 = [random.randint(1, 10) for i in range(n)]
    t1 = [random.randint(1, 5) for i in range(n - 1)]
    t2 = [random.randint(1, 5) for i in range(n - 1)]
    # p1 = [2, 4, 2, 4, 2, 4]
    # p2 = [4, 2, 4, 2, 4, 2]
    # t1 = [1, 1, 1, 1, 1]
    # t2 = [1, 1, 1, 1, 1]
    f1 = list(range(0, n))
    f2 = list(range(0, n))
    f1[0] = p1[0]
    f2[0] = p2[0]
    l1 = list(range(0, n))
    l2 = list(range(0, n))
    way = list(range(0, n))
    for j in range(1, n):
        if f1[j - 1] + p1[j] <= f2[j - 1] + t2[j - 1] + p1[j]:
            f1[j] = f1[j - 1] + p1[j]
            l1[j - 1] = 1
        else:
            f1[j] = f2[j - 1] + t2[j - 1] + p1[j]
            l1[j - 1] = 2
        if f2[j - 1] + p2[j] <= f1[j - 1] + t1[j - 1] + p2[j]:
            f2[j] = f2[j - 1] + p2[j]
            l2[j - 1] = 2
        else:
            f2[j] = f1[j - 1] + t1[j - 1] + p2[j]
            l2[j - 1] = 1
    if f1[n - 1] <= f2[n - 1]:
        f = f1[n - 1]
        way[n - 1] = 1
    else:
        f = f2[n - 1]
        way[n - 1] = 2
    for j in range(n - 1, 0, -1):
        if way[j] == 1:
            way[j - 1] = l1[j - 1]
        else:
            way[j - 1] = l2[j - 1]
    VisGraph(p1, p2, t1, t2, way, n, f)
