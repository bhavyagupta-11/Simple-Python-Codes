import os
#os is used to communicate in directories

#Each Website we crawl is a seperate directory
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project '+ directory)
        os.makedirs(directory)

#create_project_dir('Linkedin')

#Create queue for all the links found and a crawled list where the links alreaady crawled are stored so that they are not crawled again 
def create_data_files(project_name,base_url):
    queue=project_name+'/queue.txt'
    crawled=project_name+'/crawled.txt'
    #this created 2 files crawl and queue inside the directory
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

#Create a new File, it opens the file writes a data and closes it
def write_file(path,data):
    f=open(path,'w')  #w stands for write mode
    f.write(data)
    f.close()

#create_data_files('Linkedin','https://www.linkedin.com/')

#Add data onto existing file
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data +'\n')

#delete the contents of a file
def delete_content(path):
    with open(path,'w'):
        pass

#Read a file and convert each line into set items, this id done to avoid any repeted urls
def file_to_set(file):
    results=set()
    with open(file,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#iterate through the set each item will be a new line for the file
def set_to_file(links,file):
    delete_content(file)
    for link in sorted(links):
        append_to_file(file,link)

