import generate_data
import os
import uuid

filename = 'py-script-generated'
REPEAT = 100

for i in range(REPEAT):
    unique_filename = filename+str(uuid.uuid4())
    generate_data.main(unique_filename)
    os.system('gsutil cp '+unique_filename+'.json gs://stephwangstarter-files-source-1574201370 2>&1 > /dev/null')
    os.remove(unique_filename+'.json')
    print("file: "+ unique_filename + " iteration: " + str(i+1))