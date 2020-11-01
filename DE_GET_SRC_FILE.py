import requests
import shutil
import urllib.request



# get the file from source.
url =(" https://raw.githubusercontent.com/SteffiPeTaffy/machineLearningAZ/master/Machine%20Learni"
"ng%20A-Z%20Template%20Folder/Part%204%20-%20Clustering/Section%2025%20-"
"%20Hierarchical%20Clustering/Mall_Customers.csv")

req = requests.get(url)
url_content = req.content
csv_file = open('customer_data_3.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

# moving or copying  the file from current location to Target Location

source = r'C:\Users\sekar\customer_data_3.csv'
target = r'D:\SFE\customer_data_3.csv'
shutil.copy(source,target)

#here =os.path.dirname(os.path.realpath(__file__))
#filename = "customer_data_1.csv"
#filepath = os.path.join(here, filename)
#source1 =filepath
#target1 =r'D:\Python\customer_data_1.csv'
#shutil.move(source1,target1)
