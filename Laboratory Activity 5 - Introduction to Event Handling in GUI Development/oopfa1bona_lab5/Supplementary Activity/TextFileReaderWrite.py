class TextFileReaderWrite():
    def read(self, filepath):
        with open(filepath, "r") as read_file:
            print(read_file.read())

    def write(self, filepath, data ):
        with open(filepath, "w") as write_file:
            write_file.write(data)

    def append(self, filepath, data):
        with open(filepath, "a") as append_file:
            file.write(data)
