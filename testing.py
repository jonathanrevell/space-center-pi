import time

def testBargraphs(series, names):
    for name in names:
        print("\nTesting bargraph " + name, end = '')
        _dict = {}
        _dict[name] = 1
        while(_dict[name] < 10):
            series.update(_dict)
            _dict[name] += 1
            time.sleep(1)
            print('.', end = '')