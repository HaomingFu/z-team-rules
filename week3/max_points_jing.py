points = [(0,0),(1,1),(1,-1)]

def maxPoints(points):
    if not points<=2:
        return len(points)
    count = collections.defaultdict(int)
    vertical = 0
    for i in xrange(len(points)):
        for j in xrange(i+1, len(points)):
            if(points[i].x == points[j].x):
                if(points[i].y == points[j].y):
                    continue;
                else:
                    vertical += 1
                    print vertical
            else:
                k = (points[i].y-points[j].y)/float(points[i].x - points[j].x)
                count[k] += 1
                print k, count[k]
    return max(vertical, max(count.values()))

print maxPoints(points)
