import streamlit as st
import plotly.graph_objects as go
import seaborn as sns
import pandas as pd
import plotly.express as px
from matplotlib.figure import Figure

import function_support
import plotly.express as px



#----------------------------* Set up data frame *----------------------------#
df = pd.read_csv('./df_Shopee_EDA_5_seg.csv')
df = df.drop(columns='Unnamed: 0')

list_segment = ['Ultra_Low_end','Low_end','Mid_end','Mid_to_High_end','High_end','Premium']

ultra_low_end = df[df['segmentation'] == 'Ultra_Low_end']
low_end = df[df['segmentation'] == 'Low_end']
mid_end = df[df['segmentation'] == 'Mid_end']
mid_high = df[df['segmentation'] == 'Mid_to_High_end']
high_end = df[df['segmentation'] == 'High_end']
premium  = df[df['segmentation'] == 'Premium']

st.set_page_config(page_title='Final project ML30', layout='wide')




menu = ["Let's go","Problem and solution", "Exploratory data analysis", "Suggestion", "Improvement"]
choice = st.sidebar.selectbox(label = 'Welcome to my presentation, hope you enjoy', options = menu)

if choice == "Let's go":
    st.markdown('<h1 style="text-align:center;color:black;font-weight:bolder;font-size:40px;"> Analysis of cell phone market<br>Shopee E-commerce<br></h1>',unsafe_allow_html=True)
    col_1, col_2, col_3 = st.columns([1,3.5,1])
    with col_2:
        st.image('./Images/245986176_4908091866113927_6055801765751786170_n.png', use_column_width=False)
 
#----------------------------* Problem and solution *----------------------------#
elif choice == 'Problem and solution':
    title_problem = 'What is the problem?'
    st.markdown(f"<h1 style='text-align: center; color: black;'>{title_problem}</h1>", unsafe_allow_html=True)

    col_7, col_8, col_9 = st.columns([1,3.5,1])
    with col_8:
        st.image('./Images/digitalprogrammes-e-commerce-shopee-onboarding.png', width=1460)

    col_30, col_31, col_33 = st.columns([1,3,1])
    with col_31:
        line_1 = "You're working in a consulting agency to help clients develop business."
        line_2 = "One of them wants to create a new business selling smartphones on Shopee e-commerce."
        line_3 = 'Take advantage data analysis help them!'
        st.markdown(f"<h1 style='text-align: left; color: black; font-weight:normal; font-size:25px'>{line_1}<br><br>{line_2}<br><br>{line_3}</h1>", unsafe_allow_html=True)
        
    #----------------------------------------------------#
    title_solution = 'Solution'
    st.markdown(f"<h1 style='text-align: center; color: black; '>{title_solution}</h1>", unsafe_allow_html=True)
    col_10, col_11, col_12 = st.columns([1,3,1])

    with col_11:
        line_1 = "1. Figure out exactly what client want!"
        line_2 = "2. Collect data"
        line_3 = '3. Clean data'
        line_4 = '4. Explore data'
        line_5 = '5. Apply machine learning'
        st.markdown(f"<h1 style='text-align: left; color: black; font-weight:normal; font-size:25px'>{line_1}<br><br>{line_2}<br><br>{line_3}<br><br>{line_4}<br><br>{line_5}<br></h1>", unsafe_allow_html=True)
        
#----------------------------***----------------------------#
                #############################
                ########### Detail###########
                #############################xxx
#----------------------------***----------------------------#


elif choice == 'Exploratory data analysis':

#----------------------------* Final data *----------------------------#  
        st.markdown('<h1 style="text-align:center;color:black;font-weight:bolder;font-size:40px;"> Final data<br><br></h1>',unsafe_allow_html=True)
        col_13, col_14, col_15 = st.columns([1,3.5,1])
        with col_14:
            st.dataframe(df)

#----------------------------* Segmentation *----------------------------#  
            title_seg = 'Segmentation'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:bolder; font-size:40px;'><br>{title_seg}</h1>", unsafe_allow_html=True)
   
            line_7 = "References:"
            line_8 = "- IDC forecast worldwide smartphone growth (Sep - 2020)"
            line_9 = '- Pricing segment from the biggest retatiler cell phone TGDD'
            line_10 = 'Base on these references, define segment on our dataset:'

            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:bold; font-size:25px'>{line_7}</h1>", unsafe_allow_html=True)

            st.markdown(f'''<h1 style='text-align: left; color: black; font-weight:normal; font-size:25px'>
                        {line_8} (<a href='https://www.idc.com/getdoc.jsp?containerId=prUS46865120'>link</a>)<br><br>
                        {line_9} (<a href='https://www.thegioididong.com/dtdd'>link</a>)<br></h1>''',
                        unsafe_allow_html=True)


            st.markdown(f"<p style='text-align: left; color: black; font-weight:bold; font-size:25px'>{line_10}</p>", unsafe_allow_html=True)
            st.image('./Images/segment_2.png')

#----------------------------* Highlight products of each segment by highest sale *----------------------------# 
        col_19, col_20, col_21 = st.columns([1,2,1])
        with col_20:
            line_11 = 'Highlight products of each segment by highest sale'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:Bold; font-size:30px'><br>{line_11}<br></h1>", unsafe_allow_html=True)

        col_22, col_23, col_24,col_25,col_26,col_27, col_28 = st.columns([1,1,1,1,1,1,1])
        with col_23:
                    line_12 = 'Ultra low end'
                    line_13 = 'Under 2.000.000 VND'

                    st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:30px'>{line_12}</h1>", unsafe_allow_html=True)
                    st.markdown(f"<p style='text-align: center; color: black; font-weight:normal; font-size:20px'>{line_13}<br></p>", unsafe_allow_html=True)
                    st.image('./Images/Segmentation/1. ultra_low_end.jpg', use_column_width=True)

        with col_24:
                    line_14 = 'Low end'
                    line_15 = '2.000.000 - 4.000.000 VND'

                    st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:30px'>{line_14}</h1>", unsafe_allow_html=True)
                    st.markdown(f"<p style='text-align: center; color: black; font-weight:normal; font-size:20px'>{line_15}<br></p>", unsafe_allow_html=True)
                    
                    st.image('./Images/Segmentation/2. low_end.jpg', use_column_width=True)

        with col_25:
                line_16 = 'Mid end'
                line_17 = '4.000.000 - 7.000.000 VND'

                st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:30px'>{line_16}</h1>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align: center; color: black; font-weight:normal; font-size:20px'>{line_17}<br></p>", unsafe_allow_html=True)

                st.image('./Images/Segmentation/3. mid_end.jpg',use_column_width=True)

        with col_26:
                line_18 = 'Mid to High end'
                line_19 = '7.000.000 - 13.000.000 VND'

                st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:30px'>{line_18}</h1>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align: center; color: black; font-weight:normal; font-size:20px'>{line_19}<br></p>", unsafe_allow_html=True)

                st.image('./Images/Segmentation/4. mid_high.jpg',use_column_width=True)

        with col_27:
                line_20 = 'High end'
                line_21 = 'Over 13.000.000 VND'

                st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:30px'>{line_20}</h1>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align: center; color: black; font-weight:normal; font-size:20px'>{line_21}<br></p>", unsafe_allow_html=True)
                st.image('./Images/Segmentation/5. high_end.jpg', use_column_width=True)

#----------------------------* Discover each segment *----------------------------# 

#----------------------------* Ultra low end *----------------------------#  
        title_EDA = 'Ultra low end'
        st.markdown(f"<h1 style='text-align: center; color: black; font-weight:bold; font-size:40px'><br><br><br>{title_EDA}</h1>", unsafe_allow_html=True)
       
        col1, col2 = st.columns(2)
                # Top 10 sale volume
        with col1:
                    ultra_low_volume_plot = function_support.top_10_sales_volume(ultra_low_end, 'Top 10 total sales volume')
                # Top 10 revenue
        with col2:
                    low_volume_plot = function_support.top_10_revenue(ultra_low_end, 'Top 10 total revenue')

        # Logo top 5 highest revenue
        shop_1, shop_2, shop_3 = st.columns([1,1,1])
        with shop_2:
            top_shop = "Top 5 shops by highest revenue"
            st.markdown(f"<p style='text-align: center; color: black;font-weight:normal; font-size:25px'>{top_shop}</p>", unsafe_allow_html=True)

        logo_1, logo_2, logo_3, logo_4, logo_5, logo_6, logo__7 = st.columns([1,1,1,1,1,1,1])
        with logo_2:
            st.image('./Images/logo_ultra/ultra_top1.jpg', width=250)
        
        with logo_3:
            st.image('./Images/logo_ultra/ultra_top2.jpg', width=250)
        
        with logo_4:
            st.image('./Images/logo_ultra/ultra_top3.jpg', width=250)

        with logo_5:
            st.image('./Images/logo_ultra/ultra_top4.jpg', width=250)

        with logo_6:
            st.image('./Images/logo_ultra/ultra_top5.jpg', width=250)


        tabel_1, tabel_2, tabel_3 = st.columns([1,1,1])
        with tabel_2:
            phones_ultra = 'Top 4 products by highest selling'
            st.markdown(f"<p style='text-align: center; color: black;font-weight:normal; font-size:25px'><br>{phones_ultra}</p>", unsafe_allow_html=True)

        phone_1, phone_2, phone_3,phone_4,phone_5,phone_6 = st.columns([1,1,1,1,1,1])
        with phone_2:
                    st.image('./Images/Types_phone/Toy_phone.jpg',  width=280)

        with phone_3:
                    st.image('./Images/Types_phone/Feature.jpg',  width=280)

        with phone_4:
                st.image('./Images/Types_phone/Old model.jpg', width=280)

        with phone_5:
                    st.image('./Images/Types_phone/Classic.jpg',  width=280)               
        

        sun_1, sum_2, sum_3 = st.columns([1,1,1])
        with sum_2:
            sum_2 = 'Summary:'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Bold; font-size:25px'><br>{sum_2}</h1>", unsafe_allow_html=True)

        sun_4, sum_5, sum_6 = st.columns([1,1,1])
        with sum_5:    
            sum_5 = '1. No big brand, just small store'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:20px'>{sum_5}</h1>", unsafe_allow_html=True)

        sun_7, sum_8, sum_9 = st.columns([1,1,1])
        with sum_8:    
            sum_8 = '2. Main product around: Feature phone, classic phone, smartphone old model and used'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:20px'>{sum_8}</h1>", unsafe_allow_html=True)

#----------------------------* Low end *----------------------------#

        title_low = 'Low end'
        st.markdown(f"<h1 style='text-align: center; color: black;'><br><br>{title_low}</h1>", unsafe_allow_html=True)

        low_1, low_2 = st.columns(2)
                # Top 10 sale volume
        with low_1:
                    ultra_low_volume_plot = function_support.top_10_sales_volume(low_end, 'Top 10 total sales volume')
                # Top 10 revenue
        with low_2:
                    low_volume_plot = function_support.top_10_revenue(low_end, 'Top 10 total revenue')

#----------------------------* Mid end *----------------------------# 

        title_mid = 'Mid end'
        st.markdown(f"<h1 style='text-align: center; color: black;'>{title_mid}</h1>", unsafe_allow_html=True)

        mid_1, mid_2 = st.columns(2)
                # Top 10 sale volume
        with mid_1:
                    ultra_low_volume_plot = function_support.top_10_sales_volume(mid_end, 'Top 10 total sales volume')
                # Top 10 revenue
        with mid_2:
                    low_volume_plot = function_support.top_10_revenue(mid_end, 'Top 10 total revenue')

#----------------------------* Mid to High end *----------------------------# 
        title_mid = 'Mid to High end'
        st.markdown(f"<h1 style='text-align: center; color: black;'>{title_mid}</h1>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
                # Top 10 sale volume
        with col1:
                    mid_high_remove = mid_high[mid_high['shop_name'] != 'apple_flagship_store']
                    function_support.top_10_sales_volume(mid_high_remove, 'Top 10 total sales volume')
                # Top 10 revenue
        with col2:
                    function_support.top_10_revenue(mid_high_remove, 'Top 10 total revenue')
                    

    #----------------------------* Logo low end *----------------------------#    
        shop_1, shop_2, shop_3 = st.columns([1,1,1])
        with shop_2:
            top_shop = "Top 5 Low end by Revenue"
            st.markdown(f"<p style='text-align: center; color: black;font-weight:normal; font-size:25px'><br>{top_shop}</p>", unsafe_allow_html=True)

        logo_1, logo_2, logo_3, logo_4, logo_5, logo_6, logo__7 = st.columns([1,1,1,1,1,1,1])
        with logo_2:
            st.image('./Images/Logo_low_end/low_end_top1.jpg', width=250)
        
        with logo_3:
            st.image('./Images/Logo_low_end/low_end_top2.jpg', width=250)

        
        with logo_4:
            st.image('./Images/Logo_low_end/low_end_top3.jpg', width=250)

        
        with logo_5:
            st.image('./Images/Logo_low_end/low_end_top4.jpg', width=250)

        
        with logo_6:
            st.image('./Images/Logo_low_end/low_end_top5.jpg', width=250)


    #----------------------------* Logo Mid end *----------------------------#            
        # Logo top 5 highest revenue
        shop_1, shop_2, shop_3 = st.columns([1,1,1])
        with shop_2:
            top_shop = "Top 5 Mid end by Revenue"
            st.markdown(f"<p style='text-align: center; color: black;font-weight:normal; font-size:25px'><br>{top_shop}</p>", unsafe_allow_html=True)

        logo_1, logo_2, logo_3, logo_4, logo_5, logo_6, logo__7 = st.columns([1,1,1,1,1,1,1])
        with logo_2:
            st.image('./Images/logo_mid_end/mid_end_top1.jpg', width=250)
            
        with logo_3:
            st.image('./Images/logo_mid_end/mid_end_top2.jpg', width=250)
        
        with logo_4:
            st.image('./Images/logo_mid_end/mid_end_top3.jpg', width=250)
        
        with logo_5:
            st.image('./Images/logo_mid_end/mid_end_top4.jpg', width=250)

        with logo_6:
            st.image('./Images/logo_mid_end/mid_end_top5.jpg', width=250)

    #----------------------------* Logo Mid to High end *----------------------------#            
        # Logo top 5 highest revenue
        shop_1, shop_2, shop_3 = st.columns([1,1,1])
        with shop_2:
            top_shop = "Top 5 Mid to High end by Revenue"
            st.markdown(f"<p style='text-align: center; color: black;font-weight:normal; font-size:25px'><br>{top_shop}</p>", unsafe_allow_html=True)

        logo_1, logo_2, logo_3, logo_4, logo_5, logo_6, logo__7 = st.columns([1,1,1,1,1,1,1])
        with logo_2:
            st.image('./Images/Mid to high end/mid_high_top1.jpg', width=250)
            
        with logo_3:
            st.image('./Images/Mid to high end/mid_high_top2.jpg', width=250)

        
        with logo_4:
            st.image('./Images/Mid to high end/mid_high_top3.jpg', width=250)

        
        with logo_5:
            st.image('./Images/Mid to high end/mid_high_top4.jpg', width=250)
            
        with logo_6:
            st.image('./Images/Mid to high end/mid_high_top5.jpg', width=250)

#----------------------------* summary low end + mid end + mid to high end  *----------------------------# 
        sun_1, sum_2, sum_3 = st.columns([1,1,1])
        with sum_2:
            sum_2 = 'Summary:'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Bold; font-size:25px'><br><br>{sum_2}</h1>", unsafe_allow_html=True)

        sun_4, sum_5, sum_6 = st.columns([1,1,1])
        with sum_5:    
            sum_5 = 'Low end, mid end and mid to high end attract a lot of big brands'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:20px'>{sum_5}</h1>", unsafe_allow_html=True)

#----------------------------* High end *----------------------------#
        title_mid = 'High end'
        st.markdown(f"<h1 style='text-align: center; color: black;'><br>{title_mid}</h1>", unsafe_allow_html=True)
        # elif segement == "High end":
        col, col1, col2 = st.columns([1,1.5,1.5])
        with col:
                    pie_high = pd.read_csv('./pie_high.csv')
                    function_support.pie_revenue(pie_high, 'Revenue High end')
        # Top 10 sale volume
        with col1:  
                    high_end_remove = high_end[high_end['shop_name'] != 'apple_flagship_store']
                    function_support.top_10_sales_volume(high_end_remove, 'Top 10 total sales volume')
        # Top 10 revenue
        with col2:
                    function_support.top_10_revenue(high_end_remove, 'Top 10 total revenue')

   #----------------------------* Official store *----------------------------#            
        shop_1, shop_2, shop_3 = st.columns([1,1,1])
        with shop_2:
            top_shop = "Flagship Store"
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:25px'>{top_shop}</h1>", unsafe_allow_html=True)

        logo_1, logo_2, logo_3, logo_4, logo_5, logo_6, logo_7 = st.columns([1,1,1,1,1,1,1])
        with logo_2:
            st.image('./Images/High_end/high_apple.jpg', width=250)

        with logo_3:
            st.image('./Images/High_end/high_top1.jpg', width=250)
        
        with logo_4:
            st.image('./Images/Mid to high end/mid_high_top1.jpg', width=250)
     
        with logo_5:
            st.image('./Images/High_end/high_top6.jpg', width=250)

        with logo_6:
            st.image('./Images/High_end/high_top7.jpg', width=250)

   #----------------------------* hand carried phone *----------------------------#            
        shop_1, shop_2, shop_3 = st.columns([1,1,1])
        with shop_2:
            top_shop = "Hand-carried phones"
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:25px'>{top_shop}</h1>", unsafe_allow_html=True)

        logo_1, logo_2, logo_3, logo_4, logo_5, logo_6, logo_7 = st.columns([1,1,1,1,1,1,1])
        with logo_3:
            st.image('./Images/High_end/high_top2.jpg', width=250)
        

        with logo_4:
            st.image('./Images/High_end/high_top4.jpg', width=250)
        
        with logo_5:
            st.image('./Images/High_end/high_top5.jpg', width=250)
        
        sun_1, sum_2, sum_3 = st.columns([1,1,1])
        with sum_2:
            sum_2 = 'Summary:'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Bold; font-size:25px'><br><br>{sum_2}</h1>", unsafe_allow_html=True)

        sun_4, sum_5, sum_6 = st.columns([1,1,1])
        with sum_5:    
            sum_5 = 'High-end segment split up 2 groups: hand-carried phones and flaggship store '
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:20px'>{sum_5}</h1>", unsafe_allow_html=True)

elif choice == 'Suggestion':
#----------------------------* List indicators *----------------------------#  
    title_seg = 'Consider indicators to build shop'
    st.markdown(f"<h1 style='text-align: center; color: black; font-weight:bolder; font-size:40px;'><br>{title_seg}<br><br></h1>", unsafe_allow_html=True)

#----------------------------* Discount and follower *----------------------------#  
    dis = 'Discount and follower'
    quote = 'No correlation between discount, follower and total sales volume'
    st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:35px'>{dis}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:25px'>{quote}</h1>", unsafe_allow_html=True)

    dis_1, dis_2, dis_3, dis_4  = st.columns([0.4,1.2,1,0.5])
    with dis_2:
            dis_tab = pd.DataFrame(df[['total_sales_volume', 'month_sales_volume', 'discount', 'follower']])
            function_support.dis_scr(dis_tab)
    with dis_3:
            dis_tab = pd.DataFrame(df[['total_sales_volume', 'month_sales_volume', 'discount', 'follower']])
            function_support.follower(dis_tab)

#----------------------------* Shopee_mall + Favorite shop + Monthly event *----------------------------#  
    dis = 'Shopee mall and Favorite shop'
    quote1 = "These shops are in Shopee mall or favorite shop fewer than normal shop but they make business better"
    quote = "Fewer shops are in Shopee mall or favorite shop but they make better sales than those that aren't"
    st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:35px'><br><br><br><br>{dis}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:25px'>{quote}</h1>", unsafe_allow_html=True)
    
    dis_111, dis_222, dis_333, diss_444   = st.columns([0.5,1,1,0.5])
    with dis_222:
            function_support.shopee_mall(df)
            st.image('./Images/median_shopee_mall.png', use_column_width=True)

    with dis_333:

            function_support.favorite(df)
            st.image('./Images/Median_favorite_shop.png', use_column_width=True)

#----------------------------* summary *----------------------------#  
    sum_1, sum_2, sum_3 = st.columns([0.3,1,1])
    with sum_2:
            sum_2 = 'According to data:'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Bold; font-size:30px'>{sum_2}</h1>", unsafe_allow_html=True)

    sun_4, sum_5, sum_6 = st.columns([0.4,1,1])
    with sum_5:    
            sum_5 = '1. Not effective yet: Discount, follower'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:25px'>{sum_5}</h1>", unsafe_allow_html=True)

    sun_7, sum_8, sum_9 = st.columns([0.4,1,1])
    with sum_8:    
            sum_8 = '2. Effective: Shopee mall, favorite shop'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:25px'>{sum_8}</h1>", unsafe_allow_html=True)


elif choice == 'Improvement':

    title_seg = 'Improve project'
    title_seg_2 = 'Apply machine learning'
    st.markdown(f"<h1 style='text-align: center; color: black; font-weight:bolder; font-size:40px;'><br>{title_seg}<br>{title_seg_2}</h1>", unsafe_allow_html=True)
    col_1, col_2, col_3 = st.columns([1,3.5,1])
    with col_2:
        st.image('./Images/what-is-shopee-business-model-new-initatives-in-2021-768x402.jpeg', width=1455)

    sun_1, sum_2, sum_3 = st.columns([1,1,1])
    with sum_2:
            sum_2 = 'Problem: How long to build a shop successfully? '
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Bold; font-size:30px'><br>{sum_2}</h1>", unsafe_allow_html=True)

    sun_4, sum_5, sum_6 = st.columns([1,1,1])
    with sum_5:    
            sum_5 = '1. Input: Important features'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:25px'>{sum_5}</h1>", unsafe_allow_html=True)

    sun_7, sum_8, sum_9 = st.columns([1,1,1])
    with sum_8:    
            sum_8 = '2. Output: Number of months'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:25px'>{sum_8}</h1>", unsafe_allow_html=True)

    title_seg = 'Thanks for your attention'
    st.markdown(f"<h1 style='text-align: center; color: black; font-weight:bolder; font-size:40px;'><br>{title_seg}</h1>", unsafe_allow_html=True)


