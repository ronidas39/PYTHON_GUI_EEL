import eel
import requests
import json
import matplotlib.pyplot as plt
import pandas as pd

eel.init("HTMLS")
@eel.expose
def get_data(cname):
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "7d18fd6581msh81a4886d454a322p1e64c5jsn2c784c87b0cf"
    }

    response = requests.request("GET", url, headers=headers)
    data=response.text
    data=json.loads(data)
    for i in range(len(data['response'])):
        x=data['response'][i]['country']
        if(x.lower()==cname.lower()):
            total=data['response'][i]['cases']['total']
            active=data['response'][i]['cases']['active']
            recovered=data['response'][i]['cases']['recovered']
            critical=data['response'][i]['cases']['critical']
            new=data['response'][i]['cases']['new']
            try:
             new=int(new.replace('+',''))
            except:
             new=0
            total_deaths=data['response'][i]['deaths']['total']
            try:
             new_deaths=data['response'][i]['deaths']['new']
             new_deaths=int(new_deaths.replace('+',''))
            except:
                new_deaths=0
            data={}
            data.update({'Total Cases':(total)})
            data.update({'Active Cases':(active)})
            data.update({'Recovered Cases':(recovered)})
            data.update({'Critical Cases':(critical)})
            data.update({'New Cases':(new)})
            data.update({'Total Deaths':(total_deaths)})
            data.update({'New Deaths':(new_deaths)})
            print(data)
            df=pd.DataFrame.from_dict(data,orient='index',columns=['ALL CATEGORIRES'])
            fig=plt.figure(figsize=(20,10))
            plt.style.use('dark_background')
            df['ALL CATEGORIRES'].plot(kind='bar',color=['red','blue','yellow','orange','white','green','purple'],fontsize=40)
            plt.xlabel('All CATEGORIES',fontsize=50,color='red',fontweight='bold')
            plt.grid(b=True,which='both',color='white',linestyle='-')
            plt.title('Live Data of Corona Virus For: '+cname.upper(),color='blue',fontsize=80)
            plt.savefig('C:\\Users\\ronidas\\Desktop\\PYTHON_GUI_EEL\\HTMLS\\'+cname+'.png',bbox_inches='tight')




            return (data)





    return ('country not found')

eel.start("coronaapp.html",size=(1024,950))