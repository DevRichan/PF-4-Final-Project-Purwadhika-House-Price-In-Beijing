import plotly 
import plotly.graph_objects as go 
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import json
from cleaning_data import data_auto
import folium

# def bar():
#     df = data_tsa()
#     x = pd.DataFrame(df.groupby(['Claim Type','Claim Site']).count()['Item'])
#     x.reset_index(inplace=True)
#     fig = px.bar(x, x="Claim Type", y="Item", color="Claim Site", title="Claim Type Count by Claim Site")
#     fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     return fig_json

def grow():
    df = data_auto()
    df['trade_year'] = df['tradeTime'].astype(str).str[0:4]
    df_year=df.groupby('trade_year').totalPrice.mean()
    fig = px.line(df_year, x=df_year.index, y=df_year.values)
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json



def distribution_district():
    df = data_auto()
    fig = px.box(df, x="district", y="totalPrice",color='district')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def distribution_build():
    df = data_auto()
    fig = px.box(df, x="buildingType", y="totalPrice",color='buildingType')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
    
def distribution_renovation():
    df = data_auto()
    fig = px.box(df, x='renovationCondition', y="totalPrice",color='renovationCondition')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def distribution_structure():
    df = data_auto()
    fig = px.box(df, x='buildingStructure', y="totalPrice",color='buildingStructure')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def district():
    df = data_auto()
    c_district = []
    jml_cid = []
    for i in df['district'].unique():
        c_district.append(i)
        jml_cid.append(len(df[df['district'] == i]['Cid'].unique()))
    dfdist = pd.DataFrame({
        'district':c_district,
        'nofRegions': jml_cid
    })
    #sort
    dfdist.sort_values(by=['nofRegions'],inplace=True)
    #graph
    fig = px.bar(dfdist, x='district', y='nofRegions', height=400,color = 'district')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def population():
    df = data_auto()
    uniqueA = []
    uniqueB = []
    uniqueC = []
    uniqueD = []
    uniqueE = []
    uniqueF = []
    uniqueG = []
    uniqueH = []
    uniqueI = []
    uniqueJ = []
    uniqueK = []
    uniqueL = []
    uniqueM = []

    for a in df[df['district'] == 'A']['Cid'].unique():
        uniqueA.append(a)
    for b in df[df['district'] == 'B']['Cid'].unique():
        uniqueB.append(b)
    for c in df[df['district'] == 'C']['Cid'].unique():
        uniqueC.append(c)
    for d in df[df['district'] == 'D']['Cid'].unique():
        uniqueD.append(d) 
    for e in df[df['district'] == 'E']['Cid'].unique():
        uniqueE.append(e)
    for f in df[df['district'] == 'F']['Cid'].unique():
        uniqueF.append(f)
    for g in df[df['district'] == 'G']['Cid'].unique():
        uniqueG.append(g)
    for h in df[df['district'] == 'H']['Cid'].unique():
        uniqueH.append(h)
    for i in df[df['district'] == 'I']['Cid'].unique():
        uniqueI.append(i)
    for j in df[df['district'] == 'J']['Cid'].unique():
        uniqueJ.append(j)
    for k in df[df['district'] == 'K']['Cid'].unique():
        uniqueK.append(k)
    for l in df[df['district'] == 'L']['Cid'].unique():
        uniqueL.append(l)
    for m in df[df['district'] == 'M']['Cid'].unique():
        uniqueM.append(m)

    populasiA = []
    populasiB = []
    populasiC = []
    populasiD = []
    populasiE = []
    populasiF = []
    populasiG = []
    populasiH = []
    populasiI = []
    populasiJ = []
    populasiK = []
    populasiL = []
    populasiM = []


    for a in uniqueA:
        x = df[df['Cid']==a]['communityAverage'].values[:1][0]
        populasiA.append(x)
        
    for b in uniqueB:
        x = df[df['Cid']==b]['communityAverage'].values[:1][0]
        populasiB.append(x)
        
    for c in uniqueC:
        x = df[df['Cid']==c]['communityAverage'].values[:1][0]
        populasiC.append(x)
        
    for d in uniqueD:
        x = df[df['Cid']==d]['communityAverage'].values[:1][0]
        populasiD.append(x)

    for e in uniqueE:
        x = df[df['Cid']==e]['communityAverage'].values[:1][0]
        populasiE.append(x)
        
    for f in uniqueF:
        x = df[df['Cid']==f]['communityAverage'].values[:1][0]
        populasiF.append(x)
        
    for g in uniqueG:
        x = df[df['Cid']==g]['communityAverage'].values[:1][0]
        populasiG.append(x)
        
    for h in uniqueH:
        x = df[df['Cid']==h]['communityAverage'].values[:1][0]
        populasiH.append(x)
        
    for i in uniqueI:
        x = df[df['Cid']==i]['communityAverage'].values[:1][0]
        populasiI.append(x)
        
    for j in uniqueJ:
        x = df[df['Cid']==j]['communityAverage'].values[:1][0]
        populasiJ.append(x)
        
    for k in uniqueK:
        x = df[df['Cid']==k]['communityAverage'].values[:1][0]
        populasiK.append(x)
        
    for l in uniqueL:
        x = df[df['Cid']==l]['communityAverage'].values[:1][0]
        populasiL.append(x)
        
    for m in uniqueM:
        x = df[df['Cid']==m]['communityAverage'].values[:1][0]
        populasiM.append(x)

    totpopulasiA = 0
    totpopulasiB = 0
    totpopulasiC = 0
    totpopulasiD = 0
    totpopulasiE = 0
    totpopulasiF = 0
    totpopulasiG = 0
    totpopulasiH = 0
    totpopulasiI = 0
    totpopulasiJ = 0
    totpopulasiK = 0
    totpopulasiL = 0
    totpopulasiM = 0

    for i in populasiA:
        totpopulasiA = totpopulasiA + i
        
    for i in populasiB:
        totpopulasiB = totpopulasiB + i

    for i in populasiC:
        totpopulasiC = totpopulasiC + i

    for i in populasiD:
        totpopulasiD = totpopulasiD + i
        
    for i in populasiE:
        totpopulasiE = totpopulasiE + i
        
    for i in populasiF:
        totpopulasiF = totpopulasiF + i
        
    for i in populasiG:
        totpopulasiG = totpopulasiG + i
        
    for i in populasiH:
        totpopulasiH = totpopulasiH + i
        
    for i in populasiI:
        totpopulasiI = totpopulasiI + i
        
    for i in populasiJ:
        totpopulasiJ = totpopulasiJ + i
        
    for i in populasiK:
        totpopulasiK = totpopulasiK + i
        
    for i in populasiL:
        totpopulasiL = totpopulasiL + i
        
    for i in populasiM:
        totpopulasiM = totpopulasiM + i

    populasii = pd.DataFrame({
        'distrik' : ['A','B','C','D','E','F','G','H','I','J','K','L','M'],
        'totpopulasi' : [totpopulasiA,totpopulasiB,totpopulasiC,totpopulasiD,totpopulasiE,totpopulasiF,totpopulasiG,totpopulasiH,
        totpopulasiI,totpopulasiJ,totpopulasiK,totpopulasiL,totpopulasiM]
    })
    populasii.sort_values(by=['totpopulasi'],inplace=True)
    fig = px.bar(populasii, x='distrik', y='totpopulasi', height=400,title='Populasi per Distrik',color='distrik')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def typebuild():
    #jumlah bangunan per district
    df = data_auto()
    diistrict=[]
    jml_diistrict=[]
    for i in df['district'].unique():
        diistrict.append(i)
        jml_diistrict.append(len(df[df['district'] == i]['buildingType']))
    btdis = pd.DataFrame({
        'district':diistrict,
        'nofBuilding':jml_diistrict
    })
    btdis.sort_values(by='nofBuilding',inplace=True)
    fig = px.bar(btdis, x='district', y='nofBuilding', height=400,color='district')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json


def typebuildtwo():
    df = data_auto()
    for dst in df['district'].unique():
        fig = px.pie(df, values=df[df['district'] == dst]['buildingType'].value_counts().values, names=df[df['district'] == dst]['buildingType'].value_counts().index, color_discrete_sequence=px.colors.sequential.RdBu,title=dst)
        fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return fig_json

def contime():
    df = data_auto()
    fig = px.box(df, x='constructionTime', y="totalPrice",color='constructionTime')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json



def subway():
    df = data_auto()
    fig = px.box(df, x='subway', y="totalPrice",color='subway')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json


def elevato():
    df = data_auto()
    fig = px.box(df, x='elevator', y="totalPrice",color='elevator')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
# def map_folium():
#     df = data_auto()
#     list_lat_long = []
#     for index,value in df.iterrows():
#         temp = [value['Lat'],value['Lng']]
#         list_lat_long.append(temp)
#     x = len(list_lat_long)
#     map_crime = folium.Map(
#     location = [39.9042, 116.4074],
#     zoom_start=12,
#     )
#     for item in range(100):
#         folium.Marker(
#             location = list_lat_long[item],
#             popup = str(df['totalPrice'].values[item]) + '<hr></hr>' 
#             + str(df['Cid'].values[item]),
#             icon= folium.Icon(color='red',icon='home',prefix='fa')
#         ).add_to(map_crime)

#     return map_crime._repr_html_()
# def map_beijing():
#     df = data_auto()
#     fig = px.density_mapbox(df, lat='Lat', lon='Lng', z='totalPrice', radius=10,
#                         center=dict(lat=0, lon=180), zoom=0,
#                         mapbox_style='open-street-map')
#     fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     return fig_json

