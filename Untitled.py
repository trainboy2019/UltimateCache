import requests
import os
import itertools
firstRun=True
bypass=False
def download_file(url):
    local_filename = url.split('/')[-1]
    #NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    if "Access Denied" in r.content:
        pass
    else:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    #f.flush() commented by recommendation from J.F.Sebastian
        return local_filename
alphabets=['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']
for i in itertools.product(alphabets, repeat = 50):
    bypass=False
    with open("masterList.txt","r+") as f:
        with open("url.txt", "a") as g:
            f.seek(0)
            g.seek(0)
            dataRaw=f.read()
            data=dataRaw.split("\n")
            if firstRun==True:
                for j in data:
                    if str(''.join(i))==j:
                        bypass=True
                    else:
                        pass
            
            if bypass!=True:
                try:
                    url="https://announcement-resource-cdn.fire-emblem-heroes.com/announce/"+str(''.join(i))
                    url=url.replace("\n","")
                    download_file(url)
                    print(url)
                    g.write(url)
                    g.write("\n")
                except:
                    pass
                f.write(''.join(i))
                f.write("\n")
            else:
                print("bypassed "+str(''.join(i)))

