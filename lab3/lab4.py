def OLSmethod(x, y, xy, x2):
    n = len(x)
    a = (n * sum(xy) - sum(x) * sum(x2)) / (n * sum(x2) - sum(x) ** 2)
    b = (sum - a * sum(x)) / n

    return [a, b]


def main():
    x = [i*2 for i in range(10)]
    y = [33, 32, 29, 24, 29, 19, 32, 23, 22, 25]
    xy = [x[i] * y[i] for i in range(len(x))]
    x2 = [x[i] * x[i] for i in range(len(x))]
    
    results = OLSmethod(x, y, xy, x2)
    print(results)
    
    
if __name__ == "__main__":
    main()