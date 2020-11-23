from flask import Flask, render_template, request
from cleaning_data import data_auto
from plots import distribution_district, distribution_build, distribution_renovation, distribution_structure, district, population, typebuild, typebuildtwo, grow, contime, subway,elevato
import folium
from data import distrik ,bstructure, btype, renovCon, subway2, elevator,conTime 
from prediction import prediction_data, feature_importances
# inisialisasi Flask
app = Flask(__name__)

# home 
@app.route('/')
def home():
    return render_template('home.html')

# tabel_data
@app.route('/data')
def data():
    data = data_auto()
    return render_template('table_data.html',data=data) 

# plots 
@app.route('/plots')
def plots():
    data = distribution_district()
    data2 = distribution_build() 
    data3 = distribution_renovation()
    data4 = distribution_structure()
    data5 = grow()
    data6 = contime()
    data7 = subway()
    data8 = elevato()
    return render_template('plots.html',data=data,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6,data7=data7,data8=data8)


@app.route('/rank')
def ranking():
    data = district()
    data2 = population()
    data3 = typebuild()
    data4 = typebuildtwo()
    return render_template('ranking.html',data=data,data2=data2,data3=data3,data4=data4)


@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        data = request.form
        data = data.to_dict()
        hasil = prediction_data(data)
        hasil2 = feature_importances(data)
        data['square'] = float(data['square'])
        data['livingRoom'] = int(data['livingRoom'])
        data['drawingRoom'] = int(data['drawingRoom'])
        data['kitchen'] = int(data['kitchen'])
        data['bathRoom'] = int(data['bathRoom'])
        data['floor'] = int(data['floor'])
        data['buildingType'] = str(data['buildingType'])
        data['constructionTime'] = int(data['constructionTime'])
        data['renovationCondition'] = str(data['renovationCondition'])
        data['buildingStructure'] = str(data['buildingStructure'])
        data['ladderRatio'] = float(data['ladderRatio'])
        data['elevator'] = str(data['elevator'])
        data['subway'] = str(data['subway'])
        data['district'] = str(data['district'])
        return render_template('result.html',hasil_prediction=hasil,feature=hasil2)
    return render_template('prediction.html',data_distrik = sorted(distrik), data_structure = sorted(bstructure),data_type=sorted(btype),datarenov=sorted(renovCon),data_subway=sorted(subway2),data_elevator=sorted(elevator),data_time=sorted(conTime))


@app.route('/map')
def index():
    df = data_auto()

    dfA = df[df['district']=='A']
    dfB = df[df['district']=='B']
    dfC = df[df['district']=='C']
    dfD = df[df['district']=='D']
    dfE = df[df['district']=='E']
    dfF = df[df['district']=='F']
    dfG = df[df['district']=='G']
    dfH = df[df['district']=='H']
    dfI = df[df['district']=='I']
    dfJ = df[df['district']=='J']
    dfK = df[df['district']=='K']
    dfL = df[df['district']=='L']
    dfM = df[df['district']=='M']

    list_lat_long = []
    for index,value in dfA.iterrows():
        temp = [value['Lat'],value['Lng']]
        list_lat_long.append(temp)

    list_lat_longB = []
    for index,value in dfB.iterrows():
        temp = [value['Lat'],value['Lng']]
        list_lat_longB.append(temp)

    list_lat_longC = []
    for index,value in dfC.iterrows():
        temp = [value['Lat'],value['Lng']]
        list_lat_longC.append(temp)

    list_lat_longD = []
    for index,value in dfD.iterrows():
        temp = [value['Lat'],value['Lng']]
        list_lat_longD.append(temp)
        
    list_lat_longE = []
    for index,value in dfE.iterrows():
        temp = [value['Lat'],value['Lng']]
        list_lat_longE.append(temp)
        
    list_lat_longF = []
    for index,value in dfF.iterrows():
        temp = [value['Lat'],value['Lng']]
        list_lat_longF.append(temp)

    list_lat_longG = []
    for index,value in dfG.iterrows():
        temp = [value['Lat'],value['Lng']]
        list_lat_longG.append(temp)

    list_lat_longH = []
    for index,value in dfH.iterrows():
        temp = [value['Lat'],value['Lng']]
        list_lat_longH.append(temp)

    list_lat_longI = []
    for index,value in dfI.iterrows():
        temp = [value['Lat'],value['Lng']]
        list_lat_longI.append(temp)

    list_lat_longJ = []
    for index,value in dfJ.iterrows():
        temp = [value['Lat'],value['Lng']]
        list_lat_longJ.append(temp)

    list_lat_longK = []
    for index,value in dfK.iterrows():
        temp = [value['Lat'],value['Lng']]
        list_lat_longK.append(temp)

    list_lat_longL = []
    for index,value in dfL.iterrows():
        temp = [value['Lat'],value['Lng']]
        list_lat_longL.append(temp)

    list_lat_longM = []
    for index,value in dfM.iterrows():
        temp = [value['Lat'],value['Lng']]
        list_lat_longM.append(temp)


    mapp = folium.Map(
    location = [39.9042, 116.4074],
    zoom_start=12,
    )
    itr = 100
    for item in range(itr):
        folium.Marker(
            location = list_lat_long[item],
            popup = str(dfA['totalPrice'].values[item]) + '<hr></hr>' 
            + str(dfA['district'].values[item]) + '<hr></hr>' + str(dfA['Cid'].values[item]) + '<hr></hr>' + str(dfA['buildingType'].values[item]) + '<hr></hr>' + str(dfA['url'].values[item]),
            icon= folium.Icon(color='red',icon='home',prefix='fa')
        ).add_to(mapp)
        
    for item in range(itr):
        folium.Marker(
            location = list_lat_longB[item],
            popup = str(dfB['totalPrice'].values[item]) + '<hr></hr>' 
            + str(dfB['district'].values[item]) + '<hr></hr>' + str(dfB['Cid'].values[item]) + '<hr></hr>' + str(dfB['buildingType'].values[item]) + '<hr></hr>' + str(dfB['url'].values[item]) ,
            icon= folium.Icon(color='blue',icon='home',prefix='fa')
        ).add_to(mapp)

    for item in range(len(list_lat_longC)):
        folium.Marker(
            location = list_lat_longC[item],
            popup = str(dfC['totalPrice'].values[item]) + '<hr></hr>' 
            + str(dfC['district'].values[item]) + '<hr></hr>' + str(dfC['Cid'].values[item]) + '<hr></hr>' + str(dfC['buildingType'].values[item]) + '<hr></hr>' + str(dfC['url'].values[item]) ,
            icon= folium.Icon(color='green',icon='home',prefix='fa')
        ).add_to(mapp)

    for item in range(itr):
        folium.Marker(
            location = list_lat_longD[item],
            popup = str(dfD['totalPrice'].values[item]) + '<hr></hr>' 
            + str(dfD['district'].values[item]) + '<hr></hr>' + str(dfD['Cid'].values[item]) + '<hr></hr>' + str(dfD['buildingType'].values[item]) + '<hr></hr>' + str(dfD['url'].values[item]),
            icon= folium.Icon(color='purple',icon='home',prefix='fa')
        ).add_to(mapp)
        
    for item in range(itr):
        folium.Marker(
            location = list_lat_longE[item],
            popup = str(dfE['totalPrice'].values[item]) + '<hr></hr>' 
            + str(dfE['district'].values[item]) + '<hr></hr>' + str(dfE['Cid'].values[item]) + '<hr></hr>' + str(dfE['buildingType'].values[item]) + '<hr></hr>' + str(dfE['url'].values[item]),
            icon= folium.Icon(color='orange',icon='home',prefix='fa')
        ).add_to(mapp)

    for item in range(itr):
        folium.Marker(
            location = list_lat_longF[item],
            popup = str(dfF['totalPrice'].values[item]) + '<hr></hr>' 
            + str(dfF['district'].values[item]) + '<hr></hr>' + str(dfF['Cid'].values[item]) + '<hr></hr>' + str(dfF['buildingType'].values[item]) + '<hr></hr>' + str(dfF['url'].values[item]),
            icon= folium.Icon(color='beige',icon='home',prefix='fa')
        ).add_to(mapp)

    for item in range(itr):
        folium.Marker(
            location = list_lat_longG[item],
            popup = str(dfG['totalPrice'].values[item]) + '<hr></hr>' 
            + str(dfG['district'].values[item]) + '<hr></hr>' + str(dfG['Cid'].values[item]) + '<hr></hr>' + str(dfG['buildingType'].values[item]) +'<hr></hr>' + str(dfG['url'].values[item]),
            icon= folium.Icon(color='darkpurple',icon='home',prefix='fa')
        ).add_to(mapp)
        
    for item in range(itr):
        folium.Marker(
            location = list_lat_longH[item],
            popup = str(dfH['totalPrice'].values[item]) + '<hr></hr>' 
            + str(dfH['district'].values[item]) + '<hr></hr>' + str(dfH['Cid'].values[item]) + '<hr></hr>' + str(dfH['buildingType'].values[item]) + '<hr></hr>' + str(dfH['url'].values[item]) ,
            icon= folium.Icon(color='cadetblue',icon='home',prefix='fa')
        ).add_to(mapp)

    for item in range(itr):
        folium.Marker(
            location = list_lat_longI[item],
            popup = str(dfI['totalPrice'].values[item]) + '<hr></hr>' 
            + str(dfI['district'].values[item]) + '<hr></hr>' + str(dfI['Cid'].values[item]) + '<hr></hr>' + str(dfI['buildingType'].values[item]) + '<hr></hr>' + str(dfI['url'].values[item]),
            icon= folium.Icon(color='darkblue',icon='home',prefix='fa')
        ).add_to(mapp)

    for item in range(itr):
        folium.Marker(
            location = list_lat_longJ[item],
            popup = str(dfJ['totalPrice'].values[item]) + '<hr></hr>' 
            + str(dfJ['district'].values[item]) + '<hr></hr>' + str(dfJ['Cid'].values[item]) + '<hr></hr>' + str(dfJ['buildingType'].values[item]) + '<hr></hr>' + str(dfJ['url'].values[item]),
            icon= folium.Icon(color='gray',icon='home',prefix='fa')
        ).add_to(mapp)
        
    for item in range(itr):
        folium.Marker(
            location = list_lat_longK[item],
            popup = str(dfK['totalPrice'].values[item]) + '<hr></hr>' 
            + str(dfK['district'].values[item]) + '<hr></hr>' + str(dfK['Cid'].values[item]) + '<hr></hr>' + str(dfK['buildingType'].values[item]) + '<hr></hr>' + str(dfK['url'].values[item]) ,
            icon= folium.Icon(color='black',icon='home',prefix='fa')
        ).add_to(mapp)
        
    for item in range(itr):
        folium.Marker(
            location = list_lat_longL[item],
            popup = str(dfL['totalPrice'].values[item]) + '<hr></hr>' 
            + str(dfL['district'].values[item]) + '<hr></hr>' + str(dfL['Cid'].values[item]) + '<hr></hr>' + str(dfL['buildingType'].values[item]) + '<hr></hr>' + str(dfL['url'].values[item]) ,
            icon= folium.Icon(color='pink',icon='home',prefix='fa')
        ).add_to(mapp)

    for item in range(itr):
        folium.Marker(
            location = list_lat_longM[item],
            popup = str(dfM['totalPrice'].values[item]) + '<hr></hr>' 
            + str(dfM['district'].values[item]) + '<hr></hr>' + str(dfM['Cid'].values[item]) + '<hr></hr>' + str(dfM['buildingType'].values[item])+ '<hr></hr>' + str(dfM['url'].values[item]) ,
            icon= folium.Icon(color='white',icon='home',prefix='fa')
        ).add_to(mapp)
        return mapp._repr_html_()
    


    # list_lat_long = []
    # for index,value in df.iterrows():
    #     temp = [value['Lat'],value['Lng']]
    #     list_lat_long.append(temp)
    # x = len(list_lat_long)

    # map_crime = folium.Map(
    # location = [39.9042, 116.4074],
    # zoom_start=12,
    # )
    # for item in range(100):
    #     folium.Marker(
    #         location = list_lat_long[item],
    #         popup = str(df['totalPrice'].values[item]) + '<hr></hr>' 
    #         + str(df['Cid'].values[item]),
    #         icon= folium.Icon(color='red',icon='home',prefix='fa')
    #     ).add_to(map_crime)
    # return map_crime._repr_html_()


if __name__ == '__main__':
    app.run(debug=True,port=1111)



