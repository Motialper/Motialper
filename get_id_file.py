import json
from urllib.request import urlopen
import csv



def get_id():
    with urlopen( "https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty") as data:
        stories = json.loads(data.read())
    return stories



def get_job_id(stories):
    id_jobs_arr = []
    for id_all in stories :
        with  urlopen(f" https://hacker-news.firebaseio.com/v0/item/{id_all}.json?print=pretty") as  get_job_id: 
         id_job = json.loads(get_job_id.read())
         clean_job =  id_job.pop('job', None ), id_job.pop('title', None ), id_job.pop('url', None ),
         id_jobs_arr.append(clean_job)
    return id_jobs_arr 



def file_to_csv(file_name, data):
    with open(file_name, 'w+') as file_id:
     writer = csv.writer(file_id)
     for row_list in data:
        writer.writerows(row_list)    
    return    


def main():
    name_file = input('enter name file:')
    gid = get_id()
    #print(gid)
    data_id = get_job_id(gid)
    #print(jid)
    file_to_csv(name_file, data_id)
    print("complet\n")
if __name__ == "__main__":
    main()
         
        






