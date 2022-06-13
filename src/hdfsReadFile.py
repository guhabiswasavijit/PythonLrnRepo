from hdfs import InsecureClient
client_hdfs = InsecureClient('http://127.0.0.1:8083', user='root')

#===============================================================================
# with client_hdfs.read('geeks/newToHdfs.txt') as reader:
#     content = reader.read()
#     print(content)
#===============================================================================

client_hdfs.write("/test.txt", "I'm new to hdfs")