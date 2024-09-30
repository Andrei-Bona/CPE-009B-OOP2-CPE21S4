from FileReaderWriter import FileReaderWriter
from CSVFileReaderWriter import CSVFileReaderWriter
from JSONFileReaderWriter import JSONFileReaderWriter
from TextFileReaderWrite import TextFileReaderWrite

df = FileReaderWriter()
df.read()
df.write()

c = CSVFileReaderWriter()
c.read("sample.csv")
c.write(filepath = "sample2.csv", data = ["Hello", "World"])
print()

j = JSONFileReaderWriter()
j.read("sample.json")
j.write(data = ['foo', {'bar': ('baz', None, 1.0, 2)}], filepath = "sample2.json")
print()

t = TextFileReaderWrite()
t.read("sample.txt")
t.write(filepath = "sample2.txt", data = "CPE009B")
t.read("sample2.txt")