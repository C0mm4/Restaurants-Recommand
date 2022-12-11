import pandas as pd
import numpy as np
import requests

query = "한식"
url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
headers = {
    "Authorization": "KakaoAK 1168d5470dcbd5177abd32917433f470"
}
params = {"query": f"{query}",
            "size": f"{15}",
            }
places = list()
placeList = list()

logList = list()

step = 0.00001


for x in np.arange(129.08556, 126.30778, -step):
    for y in np.arange(33.48000, 38.39472, step):
        params['rect'] = "{},{},{},{}".format(x,y,x-step,y+step)
        for i in range(1,3):
            params['page'] = f"{i}"
            try:
                places = requests.get(url,params = params, headers = headers).json()['documents']
        
                for z in places:
                    placeList.append(list(z.values()))
            except KeyError:
                returnback = requests.get(url,params = params, headers = headers).json()
                
                if returnback['errorType'] == 'RequestThrottled':
                    print("Reached limit at {} {} {} {}".format(x,y,x-step, y+step))
                    logList.append("Limit at {} {} {} {}".format(x,y,x-step, y+step))

                if(len(places)):
                    places.pop()
                if(len(places)):
                    newplaces = np.array(placeList)
                
                    df = pd.DataFrame(newplaces, columns = ['adress', 'category', 'place name',
                                                            'place url', 'road adress name'
                                                            ,'x', 'y'])
                
                    df.to_csv('Places.csv', encoding = 'utf-8-sig')

                
                newlogs = np.array(logList)
                ldf = pd.DataFrame(logList, columns = ['logs'])
                ldf.to_csv('Logs.csv', mode ='a', encoding = 'utf-8-sig')

                exit(1)

        print('{} % 진행'.format((129.08556-x)/(129.08556-126.30778 + step) * 100 + (y-33.48000)/(38.39472-33.48000 + step) * 100))
    
    
newplaces = np.array(placeList)
newplaces = np.delete(newplaces, [1,2,4,5,6], axis=1)

df = pd.DataFrame(newplaces, columns = ['adress name', 'category', 'place name',
                                        'place url', 'road adress name',
                                        'x', 'y'])

df.to_csv('test6.csv', mode = 'a', encoding = 'utf-8-sig')
