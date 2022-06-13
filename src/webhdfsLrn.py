from pywebhdfs.webhdfs import PyWebHdfsClient

hdfs = PyWebHdfsClient(host='localhost',port='50070', user_name='root')  # Use your own host/port/user_name config

fileData = hdfs.read_file("/geeks/newToHdfs.txt")
print(fileData)
#===============================================================================
# for item in file_statuses["FileStatus"]:
#     print(item["txt"])
#===============================================================================