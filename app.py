from nest import nest

def test_spider():
    print('*** METRÔ ***')
    print(nest.metro_spider())
    print('*** CPTM ***')
    print(nest.cptm_spider())

if __name__ == '__main__': test_spider()
