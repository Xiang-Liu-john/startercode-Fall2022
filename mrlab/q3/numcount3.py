from mrjob.job import MRJob   # MRJob version

# Change the class name!!
class WordCount(MRJob):  #MRJob version
    def mapper(self, key, line):
        words = line.split()
        for w in words:
            yield (len(w), 1)

    def reducer(self, key, values):
        i = sum(values)
        if i > 1:
            yield (key, i)

if __name__ == '__main__':
    WordCount.run()   # MRJob version