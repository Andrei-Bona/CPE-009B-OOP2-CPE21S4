from FileReaderWriter import FileReaderWriter
import csv

class CSVFileReaderWriter(FileReaderWriter):
    def read(self, filepath):
        with open(filepath, newline = '') as csvfile:
            data = csv.reader(csvfile, delimiter = ',', quotechar = '|')

    def write(self, filepath, data):
        with open(filepath, 'w', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',', 
                                quotechar = '|', quoting = csv.QUOTE_MINIMAL)
            writer.writerow(data)


        