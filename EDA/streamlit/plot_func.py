from plotly.subplots import make_subplots
import streamlit as st
# from gotLibrary import GotLib
import plotly.express as px
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from matplotlib.figure import Figure
import plotly.express as px


#-------------------------------------Pie---------------------------------------------#
def pie_volume(data, name):
    title_overview = name
    st.markdown(f"<h1 style='text-align: center; color: black;'>{title_overview}</h1>", unsafe_allow_html=True)

    fig = px.pie(data,
        values= 'total_revenue',
        names='shop_name',)

    st.plotly_chart(fig, use_container_width=True)

def pie_revenue(data, name):
    title_overview = name
    st.markdown(f"<h1 style='text-align: center; color: black;'>{title_overview}</h1>", unsafe_allow_html=True)

    fig = px.pie(data,
        values= 'total_revenue',
        names='shop_name',)

    st.plotly_chart(fig, use_container_width=True)
   

#-------------------------------------month---------------------------------------------#
def top_10_month_volume(data, name):
    title_overview = name
    st.markdown(f"<h1 style='text-align: center; color: black;'>{title_overview}</h1>", unsafe_allow_html=True)
    data = data.groupby('company')['month_sales_volume'].sum().sort_values(ascending=False)[:10].reset_index()

    fig = px.bar(data,
        x='month_sales_volume',
        y='company',
        labels={'month_sales_volume':'Month sales volume', 'company': ''}
        )
    fig.update_traces(marker_color='#3366CC')
    st.plotly_chart(fig, use_container_width=True)

def top_10_month_revenue(data, name):
    title_overview = name
    st.markdown(f"<h1 style='text-align: center; color: black;'>{title_overview}</h1>", unsafe_allow_html=True)  
    data = data.groupby('company')['month_sales_volume', 'month_revenue'].sum().sort_values(by='month_sales_volume',ascending=False)[:10].reset_index()
    fig = px.bar(data,
        x='month_revenue',
        y= 'company',
        labels={'month_revenue': 'Month revenue', 'company' : ' '}
        )
    fig.update_traces(marker_color = '#109618')
    st.plotly_chart(fig, use_container_width=True) 

#-------------------------------------Sales---------------------------------------------#
def top_10_sales_volume(data, name):
    title_overview = name
    st.markdown(f"<h1 style='text-align: center; color: black;'>{title_overview}</h1>", unsafe_allow_html=True)
    data = data.groupby('company')['total_sales_volume'].sum().sort_values(ascending=False)[:10].reset_index()

    fig = px.bar(data,
        x='total_sales_volume',
        y='company',
        labels={'total_sales_volume':'Total sales volume', 'company': ''}
        )
    fig.update_traces(marker_color='#3366CC')
    st.plotly_chart(fig, use_container_width=True)

#-------------------------------------Revenue---------------------------------------------#
def top_10_revenue(data, name):
    title_overview = name
    st.markdown(f"<h1 style='text-align: center; color: black;'>{title_overview}</h1>", unsafe_allow_html=True)  
    data = data.groupby('company')['total_sales_volume', 'total_revenue'].sum().sort_values(by='total_sales_volume',ascending=False)[:10].reset_index()
    fig = px.bar(data,
        x='total_revenue',
        y= 'company',
        labels={'total_revenue': 'Total revenue', 'company' : ' '}
        )
    fig.update_traces(marker_color = '#109618')
    st.plotly_chart(fig, use_container_width=True) 
#-------------------------------Price--------------------------------------#
def price_box(data_1, data_2, data_3, data_4, data_5, data_6):

    fig = go.Figure()
    fig.add_trace(go.Box(y=data_1['price'], name = 'Ultra Low End'))  
    fig.add_trace(go.Box(y=data_2['price'],name = 'Low End'))
    fig.add_trace(go.Box(y=data_3['price'], name = 'Mid End'))
    fig.add_trace(go.Box(y=data_4['price'], name = 'Mid to High End'))
    fig.add_trace(go.Box(y=data_5['price'], name = 'High End')) 
    fig.add_trace(go.Box(y=data_6['price'], name = 'Premium'))

    fig.update_traces(boxpoints='all', jitter=0)
    fig.update_layout(autosize=False, width=500, height=800)
    st.plotly_chart(fig, use_container_width=True)


def price_scr(dataframe):
    fig = px.scatter(dataframe, x="price", y="sales_volume", color="segmentation", title='Scatter price and sales volume')
    fig.update_layout(autosize=False, width=500, height=500)    
    st.plotly_chart(fig, use_container_width=True)



#-------------------------------Monthly event--------------------------------------#
def monthly_event_scr(dataframe):
    fig = px.scatter(dataframe, x="monthly_event", y="sales_volume", color="segmentation")
    fig.update_layout(autosize=False, width=500, height=500)    
    st.plotly_chart(fig, use_container_width=True)

#-------------------------------Favorite--------------------------------------#
def favorite_scr(dataframe):
    fig = px.scatter(dataframe, x="favorite_product", y="sales_volume", color="segmentation")
    fig.update_layout(autosize=False, width=500, height=500)      
    st.plotly_chart(fig, use_container_width=True)

#-------------------------------Top 10 most discount--------------------------------------#
def dis_box(data_1, data_2, data_3, data_4, data_5, data_6):

    fig = go.Figure()
    fig.add_trace(go.Box(y=data_1['discount'],name = 'Ultra Low End'))  
    fig.add_trace(go.Box(y=data_2['discount'],name = 'Low End'))
    fig.add_trace(go.Box(y=data_3['discount'], name = 'Mid End'))
    fig.add_trace(go.Box(y=data_4['discount'], name = 'Mid to High End'))
    fig.add_trace(go.Box(y=data_5['discount'], name = 'High End')) 
    fig.add_trace(go.Box(y=data_6['discount'], name = 'Premium'))

    fig.update_traces(boxpoints='all', jitter=0)
    fig.update_layout(autosize=False, width=500, height=500)
    st.plotly_chart(fig, use_container_width=True)

def discount_scr(dataframe):
    fig = px.scatter(dataframe, x="discount", y="sales_volume", color="segmentation")
    fig.update_layout(autosize=False, width=500, height=500)     
    st.plotly_chart(fig, use_container_width=True)


#-------------------------------Shopee mall--------------------------------------#
def shopee_mall_scr(dataframe):
    fig = px.scatter(dataframe, x="shopee_mall", y="sales_volume", color="segmentation")
    fig.update_layout(autosize=False, width=500, height=500)     
    st.plotly_chart(fig, use_container_width=True)

#---------------------------Guaranteed by Shopee---------------------------------#
def guaranteed_scr(dataframe):
    fig = px.scatter(dataframe, x="shopee_guaranteed", y="sales_volume", color="segmentation")   
    st.plotly_chart(fig, use_container_width=True)


#---------------------------Response rate---------------------------------#
def res_rate_scr(dataframe):
    fig = px.scatter(dataframe, x="response_rate", y="sales_volume", color="segmentation")
    fig.update_layout(autosize=False, width=500, height=500)       
    st.plotly_chart(fig, use_container_width=True)

#---------------------------Rating count product---------------------------------#
def rate_count_pro_scr(dataframe):
    fig = px.scatter(dataframe, x="rating_count_product", y="sales_volume", color="segmentation")
    fig.update_layout(autosize=False, width=500, height=500)    
    st.plotly_chart(fig, use_container_width=True)

#---------------------------Time response---------------------------------#
def time_res(dataframe):
    fig = px.scatter(dataframe, x="time_response", y="sales_volume", color="segmentation")
    fig.update_layout(autosize=False, width=500, height=500)    
    st.plotly_chart(fig, use_container_width=True)

#---------------------------Experience---------------------------------#
def ex_scr(dataframe):
    fig = px.scatter(dataframe, x="experience", y="sales_volume", color="segmentation")
    fig.update_layout(autosize=False, width=500, height=500)    
    st.plotly_chart(fig, use_container_width=True)

#---------------------------Follower---------------------------------#
def follower_scr(dataframe):
    fig = px.scatter(dataframe, x="follower", y="sales_volume", color="segmentation")
    fig.update_layout(autosize=False, width=500, height=500)    
    st.plotly_chart(fig, use_container_width=True)

def month_follower_scr(dataframe):
    fig = px.scatter(dataframe, x="follower", y="monthly_sales_volume", color="segmentation")
    fig.update_layout(autosize=False, width=500, height=500)    
    st.plotly_chart(fig, use_container_width=True)

#---------------------------Special shop---------------------------------#
def special_scr(dataframe):
    fig = px.scatter(dataframe, x="special_shop", y="sales_volume", color="segmentation")
    fig.update_layout(autosize=False, width=500, height=500)    
    st.plotly_chart(fig, use_container_width=True)

#---------------------------Rating product---------------------------------#
def rating_pro(dataframe):
    fig = px.scatter(dataframe, x="rating_product", y="sales_volume", color="segmentation")
    fig.update_layout(autosize=False, width=500, height=500)    
    st.plotly_chart(fig, use_container_width=True)


#---------------------------Replace---------------------------------#
def replace(series):
    if series == 0:
        return 'No'
    elif series == 1:
        return 'Yes'