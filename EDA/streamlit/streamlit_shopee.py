import streamlit as st
import plotly.graph_objects as go
import seaborn as sns
import pandas as pd
import plotly.express as px
from matplotlib.figure import Figure

import plot_func
import plotly.express as px



#----------------------------* Set up data frame *----------------------------#
df = pd.read_csv('./df_Shopee_EDA_5_seg.csv')
df = df.drop(columns='Unnamed: 0')

list_segment = ['Ultra_Low-end','Low_end','Mid_end','Mid_to_High_end','High_end','Premium']

ultra_low_end = df[df['segmentation'] == 'Ultra_Low-end']
low_end = df[df['segmentation'] == 'Low_end']
mid_end = df[df['segmentation'] == 'Mid_end']
mid_high = df[df['segmentation'] == 'Mid_to_High_end']
high_end = df[df['segmentation'] == 'High_end']
premium  = df[df['segmentation'] == 'Premium']

st.set_page_config(page_title='Final project ML30', layout='wide')
st.markdown('<h1 style="text-align:center;color:black;font-weight:bolder;font-size:60px;">Data analysis project<br>Cell phone market on Shopee E-commerce<br><br></h1>',unsafe_allow_html=True)

col_1, col_2, col_3 = st.columns([1,3.5,1])
with col_2:
    st.image('./Images/245986176_4908091866113927_6055801765751786170_n.png', use_column_width=False)

col_4, col_5, col_6 = st.columns([1,3.5,1])
with col_5:
    menu = ["Let's go","Problem and solution", "Exploratory data analysis", "Suggestion", "Improvement"]
    choice = st.selectbox(label = 'Welcome to my presentation, hope you enjoy', options = menu)

if choice == "Let's go":
    st.write('')
    
#----------------------------* Problem and solution *----------------------------#
elif choice == 'Problem and solution':
    col_7, col_8, col_9 = st.columns([1,3.5,1])
    with col_8:
        title_problem = 'What is the problem?'
        st.markdown(f"<h1 style='text-align: center; color: black;'>{title_problem}</h1>", unsafe_allow_html=True)

        st.image('./Images/digitalprogrammes-e-commerce-shopee-onboarding.png', width=1460)

        line_1 = "You're working in a consulting agency to help clients develop business."
        line_2 = "One of them wants to create a new business selling smartphones on Shopee e-commerce."
        line_3 = 'Take advantage data analysis help them!'
        st.markdown(f"<h1 style='text-align: left; color: black; font-weight:normal; font-size:30px'>{line_1}<br><br>{line_2}<br><br>{line_3}</h1>", unsafe_allow_html=True)
        
    #----------------------------------------------------#
    col_10, col_11, col_12 = st.columns([1,3.5,1])
    with col_11:
        title_solution = 'Design solution'
        st.markdown(f"<h1 style='text-align: center; color: black; '>{title_solution}</h1>", unsafe_allow_html=True)

        line_1 = "1. Figure out exactly what client want!"
        line_2 = "2. Collect data"
        line_3 = '3. Clean data'
        line_4 = '4. Explore data'
        line_5 = '5. Apply machine learning'
        st.markdown(f"<h1 style='text-align: left; color: black; font-weight:normal; font-size:20px'>{line_1}<br><br>{line_2}<br><br>{line_3}<br><br>{line_4}<br><br>{line_5}<br></h1>", unsafe_allow_html=True)
        
#----------------------------* Design solution *----------------------------#
        # define_question = st.checkbox('1. Define question')
        # collect_data    = st.checkbox('2. Collect data')
        # clean_data    = st.checkbox('3. Clean data')
        # explore_data    = st.checkbox('4. Explore data')
        # apply_ML    = st.checkbox('5. Apply machine learning')

    # if define_question: 
    #     title_overview = 'Figure out exactly what client want?'
    #     st.markdown(f"<h1 style='text-align: center; color: black;'>{title_overview}</h1>", unsafe_allow_html=True)
    #     st.markdown("""
    #     ### 
    #             1. Explore Segmentation
    #             2. Features affect shop's prestige
    #     """)
    #     st.image('./Images/what-is-shopee-business-model-new-initatives-in-2021-768x402.jpeg')

    # elif collect_data:
    #     title_collect = 'Scrape data'
    #     st.markdown(f"<h1 style='text-align: center; color: black;'>{title_collect}</h1>", unsafe_allow_html=True)
    #     st.markdown("""
    #     Crawl data on Shopee website in mobile phone category, sort by monthly sales volume
    #     * **Python libraries:** Selenium
    #     * **Data source:** [shoppee.vn/Điện-thoại-cat & sortBy=sales](https://shopee.vn/%C4%90i%E1%BB%87n-tho%E1%BA%A1i-cat.11036030.11036031?page=0&sortBy=sales).
    #     """)
    #     st.image('./Images/Screen Shot 2021-10-20 at 19.53.35.png')

    # elif clean_data:
    #     title_clean = 'Clean data set'
    #     st.markdown(f"<h1 style='text-align: center; color: black;'>{title_clean}</h1>", unsafe_allow_html=True)
    #     st.markdown("""
    #     ### **Python libraries:** Pandas, Numpy
    #     ### Steps to clean data:
    #                 Step 1: Overview data and remove unneeded columns
    #                 Step 2: Working with missing values
    #                 Step 3: Check and change datatype
    #                 Step 4: Handle duplicated data
    #                 Step 5: Handel mislabeled and corrupted data
    #     """)
    #     st.image('./Images/data-cleaning.png')

    # elif explore_data:
    #     title_explore = 'Exploratory data analysis'
    #     st.markdown(f"<h1 style='text-align: center; color: black;'>{title_explore}</h1>", unsafe_allow_html=True)
    #     st.markdown("""
    #     ### **Python libraries:** Pandas, Matplotlib, Seaborn, Scikit-learn
    #     ### Step EDA:
    #                 Step 1: Feature engineering
    #                 Step 2: Segmentation and EDA
    #                 Step 3: Summary information
    #     """)
    #     st.image('./Images/Screen-Shot-2018-11-23-at-10.23.17-am.png')

    # elif apply_ML:
    #     title_ML = 'Apply machine learning model'
    #     st.markdown(f"<h1 style='text-align: center; color: black;'>{title_ML}</h1>", unsafe_allow_html=True)
    #     st.markdown("""
    #     ### **Python libraries:** Pandas, Matplotlib, Seaborn, Scikit-learn
    #     ### Step EDA:
    #                 Step 1: Define problem: Classification or regression
    #                 Step 2: List model can solve and trial to error
    #                 Step 3: Fine tuning best model
    #                 Step 4: Deploy
    #     """)

#----------------------------***----------------------------#
                #############################
                ########### Detail###########
                #############################
#----------------------------***----------------------------#


elif choice == 'Exploratory data analysis':

#----------------------------* Feature engineering *----------------------------#  
        title_overview = 'Feature engineering'
        st.markdown(f"<h1 style='text-align: center; color: black;'>{title_overview}</h1>", unsafe_allow_html=True)
        col_13, col_14, col_15 = st.columns([1,3.5,1])
        with col_14:
            st.header("Final dataset")
            line_6 = 'Calcualate new feature: Month revenue, total revenue and segmentation'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:20px'>{line_6}<br></h1>", unsafe_allow_html=True)
            st.dataframe(df)

#----------------------------* Segmentation *----------------------------#  
            title_seg = 'Segmentation'
            st.markdown(f"<h1 style='text-align: center; color: black;'>{title_seg}</h1>", unsafe_allow_html=True)
   
            line_7 = "How to split 5 segments:"
            line_8 = "- IDC forecast worldwide smartphone growth (Sep - 2020)"
            line_9 = '- Pricing segment from the biggest retatiler cell phone TGDD'
            line_10 = '- Actual data situation'

            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:bold; font-size:20px'>{line_7}</h1>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:normal; font-size:20px'>{line_8}<br><br>{line_9}<br><br>{line_10}<br></h1>", unsafe_allow_html=True)
        
        col_16, col_17, col_18 = st.columns([1,2,1])
        with col_17:
                st.image('./Images/Segmentation/IDC.png', width=1000)
                st.write("IDC Forecast: [link](https://www.idc.com/getdoc.jsp?containerId=prUS46865120)")
                st.write("Retailer TGDD: [link](https://www.thegioididong.com/dtdd)")

#----------------------------* Take a look segment *----------------------------# 
        col_19, col_20, col_21 = st.columns([1,2,1])
        with col_20:
            line_11 = 'Take a look single segment and every product represent is the highest sale volume in this month'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:26px'>{line_11}</h1>", unsafe_allow_html=True)

        col_22, col_23, col_24,col_25,col_26,col_27, col_28 = st.columns([1,1,1,1,1,1,1])
        with col_23:
                    line_12 = 'Ultra low end'
                    line_13 = 'Under 2.000.000 VND'

                    st.markdown(f"<h1 style='text-align: center; color: black; font-weight:bold; font-size:30px'>{line_12}</h1>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{line_13}<br></h1>", unsafe_allow_html=True)
                    st.image('./Images/Segmentation/1. ultra_low_end.jpg', use_column_width=True)

        with col_24:
                    line_14 = 'Low end'
                    line_15 = '2.000.000 - 4.000.000 VND'

                    st.markdown(f"<h1 style='text-align: center; color: black; font-weight:bold; font-size:30px'>{line_14}</h1>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{line_15}<br></h1>", unsafe_allow_html=True)
                    
                    st.image('./Images/Segmentation/2. low_end.jpg', use_column_width=True)

        with col_25:
                line_16 = 'Mid end'
                line_17 = '4.000.000 - 7.000.000 VND'

                st.markdown(f"<h1 style='text-align: center; color: black; font-weight:bold; font-size:30px'>{line_16}</h1>", unsafe_allow_html=True)
                st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{line_17}<br></h1>", unsafe_allow_html=True)

                st.image('./Images/Segmentation/3. mid_end.jpg')

        with col_26:
                line_18 = 'Mid to High end'
                line_19 = '7.000.000 - 13.000.000 VND'

                st.markdown(f"<h1 style='text-align: center; color: black; font-weight:bold; font-size:30px'>{line_18}</h1>", unsafe_allow_html=True)
                st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{line_19}<br></h1>", unsafe_allow_html=True)

                st.image('./Images/Segmentation/4. mid_high.jpg')

        with col_27:
                line_20 = 'High end'
                line_21 = 'Over 13.000.000 VND'

                st.markdown(f"<h1 style='text-align: center; color: black; font-weight:bold; font-size:30px'>{line_20}</h1>", unsafe_allow_html=True)
                st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{line_21}<br></h1>", unsafe_allow_html=True)
                st.image('./Images/Segmentation/5. high_end.jpg')

#----------------------------* Discover each segment *----------------------------# 

        title_EDA = 'Ultra low end'
        st.markdown(f"<h1 style='text-align: center; color: black;'><br><br><br>{title_EDA}</h1>", unsafe_allow_html=True)
            
#----------------------------* Ultra low end *----------------------------#                 
       
        col1, col2 = st.columns(2)
                # Top 10 sale volume
        with col1:
                    ultra_low_volume_plot = plot_func.top_10_sales_volume(ultra_low_end, 'Top 10 total sales volume')
                # Top 10 revenue
        with col2:
                    low_volume_plot = plot_func.top_10_revenue(ultra_low_end, 'Top 10 total revenue')

        # Logo top 5 highest revenue
        shop_1, shop_2, shop_3 = st.columns([1,1,1])
        with shop_2:
            top_shop = "Top 5 Ultra low end by Revenue"
            st.markdown(f"<h1 style='text-align: center; color: black;'><br>{top_shop}<br><br></h1>", unsafe_allow_html=True)

        logo_1, logo_2, logo_3, logo_4, logo_5, logo_6, logo__7 = st.columns([1,1,1,1,1,1,1])
        with logo_2:
            st.image('./Images/logo_ultra/ultra_top1.jpg', width=300)
            baochau = 'smartphone_baochau'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{baochau}</h1>", unsafe_allow_html=True)
        
        with logo_3:
            st.image('./Images/logo_ultra/ultra_top2.jpg', width=300)
            Baongoc = 'Baongocstore2016'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{Baongoc}</h1>", unsafe_allow_html=True)
        
        with logo_4:
            st.image('./Images/logo_ultra/ultra_top3.jpg', width=300)
            tuanhung_1 = 'Hệ thống Tuân Hưng Yên Chính'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{tuanhung_1}</h1>", unsafe_allow_html=True)
        with logo_5:
            st.image('./Images/logo_ultra/ultra_top4.jpg', width=300)
            tuanhung_2 = 'Tuân Hưng Yên'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{tuanhung_2}</h1>", unsafe_allow_html=True)
        
        with logo_6:
            st.image('./Images/logo_ultra/ultra_top5.jpg', width=300)
            tuanduong = 'Tuấn Dương Mobile'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{tuanduong}</h1>", unsafe_allow_html=True)

        tabel_1, tabel_2, tabel_3 = st.columns([1,1,1])
        with tabel_2:
            phones_ultra = 'Four highest selling phones in top 10'
            st.markdown(f"<h1 style='text-align: center; color: black;'><br>{phones_ultra}<br><br></h1>", unsafe_allow_html=True)

        phone_1, phone_2, phone_3,phone_4,phone_5,phone_6 = st.columns([1,1,1,1,1,1])
        with phone_2:
                    st.image('./Images/Types_phone/Toy_phone.jpg', use_column_width=True)

        with phone_3:
                    st.image('./Images/Types_phone/Classic.jpg', use_column_width=True)

        with phone_4:
                st.image('./Images/Types_phone/Old model.jpg')

        with phone_5:
                st.image('./Images/Types_phone/Feature.jpg')
        

        sun_1, sum_2, sum_3 = st.columns([1,1,1])
        with sum_2:
            sum_2 = 'Summary ultra low end segment:'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Bold;'><br>{sum_2}</h1>", unsafe_allow_html=True)

        sun_4, sum_5, sum_6 = st.columns([1,1,1])
        with sum_5:    
            sum_5 = '1. No big brand, just small store'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:20px'>{sum_5}</h1>", unsafe_allow_html=True)

        sun_7, sum_8, sum_9 = st.columns([1,1,1])
        with sum_8:    
            sum_8 = '2. Main product around: Feature phone, classic phone, old smartphone'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:20px'>{sum_8}</h1>", unsafe_allow_html=True)

        sun_10, sum_11, sum_12 = st.columns([1,1,1])
        with sum_11:    
            sum_11 = '3. '
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:20px'>{sum_11}</h1>", unsafe_allow_html=True)

#----------------------------* Low end *----------------------------#

        title_low = 'Low end'
        st.markdown(f"<h1 style='text-align: center; color: black;'><br><br><br>{title_low}</h1>", unsafe_allow_html=True)
        # elif segement == "Low end":
        low_1, low_2 = st.columns(2)
                # Top 10 sale volume
        with low_1:
                    ultra_low_volume_plot = plot_func.top_10_sales_volume(low_end, 'Top 10 total sales volume')
                # Top 10 revenue
        with low_2:
                    low_volume_plot = plot_func.top_10_revenue(low_end, 'Top 10 total revenue')

#----------------------------* Mid end *----------------------------# 

        title_mid = 'Mid end'
        st.markdown(f"<h1 style='text-align: center; color: black;'><br>{title_mid}</h1>", unsafe_allow_html=True)

        mid_1, mid_2 = st.columns(2)
                # Top 10 sale volume
        with mid_1:
                    ultra_low_volume_plot = plot_func.top_10_sales_volume(mid_end, 'Top 10 total sales volume')
                # Top 10 revenue
        with mid_2:
                    low_volume_plot = plot_func.top_10_revenue(mid_end, 'Top 10 total revenue')

#----------------------------* Mid to High end *----------------------------# 
        title_mid = 'Mid to High end'
        st.markdown(f"<h1 style='text-align: center; color: black;'><br>{title_mid}</h1>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
                # Top 10 sale volume
        with col1:
                    mid_high_remove = mid_high[mid_high['shop_name'] != 'apple_flagship_store']
                    plot_func.top_10_sales_volume(mid_high_remove, 'Top 10 total sales volume')
                # Top 10 revenue
        with col2:
                    plot_func.top_10_revenue(mid_high_remove, 'Top 10 total revenue')
                    

    #----------------------------* Logo low end *----------------------------#    
        shop_1, shop_2, shop_3 = st.columns([1,1,1])
        with shop_2:
            top_shop = "Top 5 Low end by Revenue"
            st.markdown(f"<h1 style='text-align: center; color: black;'>{top_shop}</h1>", unsafe_allow_html=True)

        logo_1, logo_2, logo_3, logo_4, logo_5, logo_6, logo__7 = st.columns([1,1,1,1,1,1,1])
        with logo_2:
            st.image('./Images/Logo_low_end/low_end_top1.jpg', width=300)
            baochau = 'smartphone_baochau'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{baochau}</h1>", unsafe_allow_html=True)
        
        with logo_3:
            st.image('./Images/Logo_low_end/low_end_top2.jpg', width=300)
            vivo = 'Vivo official store'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{vivo}</h1>", unsafe_allow_html=True)
        
        with logo_4:
            st.image('./Images/Logo_low_end/low_end_top3.jpg', width=300)
            ss = 'Samsung official store'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{ss}</h1>", unsafe_allow_html=True)
        
        with logo_5:
            st.image('./Images/Logo_low_end/low_end_top4.jpg', width=300)
            xiaomi = 'Xiaomi authorized store'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{xiaomi}</h1>", unsafe_allow_html=True)
        
        with logo_6:
            st.image('./Images/Logo_low_end/low_end_top5.jpg', width=300)
            oppo = 'OPPO authorized store VN'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{oppo}</h1>", unsafe_allow_html=True)

    #----------------------------* Logo Mid end *----------------------------#            
        # Logo top 5 highest revenue
        shop_1, shop_2, shop_3 = st.columns([1,1,1])
        with shop_2:
            top_shop = "Top 5 Mid end by Revenue"
            st.markdown(f"<h1 style='text-align: center; color: black;'>{top_shop}</h1>", unsafe_allow_html=True)

        logo_1, logo_2, logo_3, logo_4, logo_5, logo_6, logo__7 = st.columns([1,1,1,1,1,1,1])
        with logo_2:
            st.image('./Images/logo_mid_end/mid_end_top1.jpg', width=300)
            
            xiaomi = 'Xiaomi authorized store'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{xiaomi}</h1>", unsafe_allow_html=True)
        
        with logo_3:
            st.image('./Images/logo_mid_end/mid_end_top2.jpg', width=300)
            baochau = 'smartphone_baochau'
            
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{baochau}</h1>", unsafe_allow_html=True)
        
        with logo_4:
            st.image('./Images/logo_mid_end/mid_end_top3.jpg', width=300)
            ss = 'Samsung official store'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{ss}</h1>", unsafe_allow_html=True)
        
        with logo_5:
            st.image('./Images/logo_mid_end/mid_end_top4.jpg', width=300)
            tg_mi = 'Thegioimi_Mistore'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{tg_mi}</h1>", unsafe_allow_html=True)
        
        with logo_6:
            st.image('./Images/logo_mid_end/mid_end_top5.jpg', width=300)
            mimedia = 'mimedia'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{mimedia}</h1>", unsafe_allow_html=True)

    #----------------------------* Logo Mid to High end *----------------------------#            
        # Logo top 5 highest revenue
        shop_1, shop_2, shop_3 = st.columns([1,1,1])
        with shop_2:
            top_shop = "Top 5 Mid to High end by Revenue"
            st.markdown(f"<h1 style='text-align: center; color: black;'>{top_shop}</h1>", unsafe_allow_html=True)

        logo_1, logo_2, logo_3, logo_4, logo_5, logo_6, logo__7 = st.columns([1,1,1,1,1,1,1])
        with logo_2:
            st.image('./Images/Mid to high end/mid_high_top1.jpg', width=300)
            ss = 'Samsung official store'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{ss}</h1>", unsafe_allow_html=True)
            
        
        with logo_3:
            st.image('./Images/Mid to high end/mid_high_top2.jpg', width=300)
            xiaomi = 'Xiaomi authorized store'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{xiaomi}</h1>", unsafe_allow_html=True)
            
        
        with logo_4:
            st.image('./Images/Mid to high end/mid_high_top3.jpg', width=300)
            tg_mi = 'Thegioimi_Mistore'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{tg_mi}</h1>", unsafe_allow_html=True)
        
        with logo_5:
            st.image('./Images/Mid to high end/mid_high_top4.jpg', width=300)
            dunk = 'Shopdunk'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{dunk}</h1>", unsafe_allow_html=True)
            
        
        with logo_6:
            st.image('./Images/Mid to high end/mid_high_top5.jpg', width=300)
            thuychi = 'Điện Tử Thuỳ Chi'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{thuychi}</h1>", unsafe_allow_html=True)

#----------------------------* summary low end + mid end  *----------------------------# 
        sun_1, sum_2, sum_3 = st.columns([1,1,1])
        with sum_2:
            sum_2 = 'Summary Low end, Mid end, Mid to High end segment:'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Bold;'><br>{sum_2}</h1>", unsafe_allow_html=True)

        sun_4, sum_5, sum_6 = st.columns([1,1,1])
        with sum_5:    
            sum_5 = '1. Belong to big brand, especially mid end owned by Xiaomi brand'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:20px'>{sum_5}</h1>", unsafe_allow_html=True)

        sun_7, sum_8, sum_9 = st.columns([1,1,1])
        with sum_8:    
            sum_8 = '2. smartphone_baochau had ineffective bussiness dispite participateing in the total. Last month, smartphone_baochau had month volume below 1% compare to the whole industry, '
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:20px'>{sum_8}</h1>", unsafe_allow_html=True)

        # Top 10 month sales volume and revenue
        title_mid = 'Month of Low end'
        st.markdown(f"<h1 style='text-align: center; color: black;'><br>{title_mid}</h1>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
                plot_func.top_10_month_revenue(low_end, 'Month revenue')
 
        with col2:
            plot_func.top_10_month_volume(low_end, 'Month volume')

#----------------------------* Assumption remove apple flagship store *----------------------------# 
        title_mid = 'Assumption outlier'
        st.markdown(f"<h1 style='text-align: center; color: black;'><br>{title_mid}</h1>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
                # Top 10 sale volume
        with col1:
                    pie_mid_high = pd.read_csv('./pie_mid_high.csv')
                    plot_func.pie_revenue(pie_mid_high, 'Revenue Mid to High end')
                # Top 10 revenue
        with col2:
                    pie_high = pd.read_csv('./pie_high.csv')
                    plot_func.pie_revenue(pie_high, 'Revenue High end')

        sun_4, sum_5, sum_6 = st.columns([1,1,1])
        with sum_5:    
            sum_5 = 'Remove Apple flagship store in Mid to High end and High end because they accoybted for more than 90%'
            st.markdown(f"<h1 style='text-align: left; color: black; font-weight:Normal; font-size:20px'>{sum_5}</h1>", unsafe_allow_html=True)

#----------------------------* High end *----------------------------#
        title_mid = 'High end'
        st.markdown(f"<h1 style='text-align: center; color: black;'><br>{title_mid}</h1>", unsafe_allow_html=True)
        # elif segement == "High end":
        col1, col2 = st.columns(2)
        # Top 10 sale volume
        with col1:  
                    high_end_remove = high_end[high_end['shop_name'] != 'apple_flagship_store']
                    plot_func.top_10_sales_volume(high_end_remove, 'Top 10 total sales volume')
        # Top 10 revenue
        with col2:
                    plot_func.top_10_revenue(high_end_remove, 'Top 10 total revenue')

   #----------------------------* Official store *----------------------------#            
        shop_1, shop_2, shop_3 = st.columns([1,1,1])
        with shop_2:
            top_shop = "Official brand shop"
            st.markdown(f"<h1 style='text-align: center; color: black;'>{top_shop}</h1>", unsafe_allow_html=True)

        logo_1, logo_2, logo_3, logo_4, logo_5, logo_6, logo_7 = st.columns([1,1,1,1,1,1,1])
        with logo_2:
            st.image('./Images/High_end/high_apple.jpg', width=300)
            apple = 'Apple Flagship Store'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{apple}</h1>", unsafe_allow_html=True)
        

        with logo_3:
            st.image('./Images/High_end/high_top1.jpg', width=300)
            dunk = 'Shopdunk'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{dunk}</h1>", unsafe_allow_html=True)
        
        with logo_4:
            st.image('./Images/Mid to high end/mid_high_top1.jpg', width=300)
            ss = 'Samsung official store'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{ss}</h1>", unsafe_allow_html=True)
            
        
        with logo_5:
            st.image('./Images/High_end/high_top6.jpg', width=300)
            huawei = 'Huawei Flahship store'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{huawei}</h1>", unsafe_allow_html=True)
            
        
        with logo_6:
            st.image('./Images/High_end/high_top7.jpg', width=300)
            oppo = 'OPPO authorized store VN'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{oppo}</h1>", unsafe_allow_html=True)

   #----------------------------* Portable phone *----------------------------#            
        shop_1, shop_2, shop_3 = st.columns([1,1,1])
        with shop_2:
            top_shop = "Portable phone"
            st.markdown(f"<h1 style='text-align: center; color: black;'>{top_shop}</h1>", unsafe_allow_html=True)

        logo_1, logo_2, logo_3, logo_4, logo_5, logo_6, logo_7 = st.columns([1,1,1,1,1,1,1])
        with logo_3:
            st.image('./Images/High_end/high_top2.jpg', width=300)
            bichngoc = 'Bichngocmobile'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{bichngoc}</h1>", unsafe_allow_html=True)
        

        with logo_4:
            st.image('./Images/High_end/high_top4.jpg', width=300)
            digi = 'Digiphone'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{digi}</h1>", unsafe_allow_html=True)
        
        with logo_5:
            st.image('./Images/High_end/high_top5.jpg', width=300)
            vk = 'Vk Mobile Shop'
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:normal; font-size:20px'>{vk}</h1>", unsafe_allow_html=True)
            
        sun_4, sum_5, sum_6 = st.columns([1,1,1])
        with sum_5:    
            sum_5 = 'High-end segment split, 2 groups: portable and official store '
            st.markdown(f"<h1 style='text-align: center; color: black; font-weight:Bold; font-size:25px'>{sum_5}</h1>", unsafe_allow_html=True)

elif choice == 'Suggestion':
    suggestion = 'Recommendations to build a better shop'
    st.markdown(f"<h1 style='text-align: center; color: black;'><br>{suggestion}</h1>", unsafe_allow_html=True)
        
#----------------------------* Premium *----------------------------# 
        # # elif segement == "Premium":
        # col1, col2 = st.columns(2)
        #         # Top 10 sale volume
        # with col1:
        #             ultra_low_volume_plot = plot_func.top_10_sales_volume(premium, 'Premium')
        #         # Top 10 revenue
        # with col2:
        #             low_volume_plot = plot_func.top_10_revenue(premium, 'Premium')


#----------------------------* EDA *----------------------------#  
#         title_EDA = 'Discover each segment'
#         st.markdown(f"<h1 style='text-align: center; color: black;'>{title_EDA}</h1>", unsafe_allow_html=True)
        
#         # Set select feature
#         features = st.selectbox("Select segment", (
#         "List segmentations",
#         "Ultra low end",
#         "Low end",
#         "Mid end",
#         "Mid to High end",
#         "High end",
#         "Premium"
#         ))
        
#         if features == "List segmentations":
#             st.write("IDC Forecast: [link](https://www.idc.com/getdoc.jsp?containerId=prUS46865120)")
#             st.write("Retailer TGDD: [link](https://www.thegioididong.com/dtdd)")

#         # Plot feature
        
#         elif features == 'Ultra low end':
#             col1, col2 = st.columns(2)
#             # Top 10 sale volume
#             with col1:
#                 ultra_low_volume_plot = plot_func.top_10_sales_volume(ultra_low_end, 'Ultra low end')
#             # Top 10 revenue
#             with col2:
#                 low_volume_plot = plot_func.top_10_sales_volume(low_end, 'Low end')

#             col3, col4 = st.columns(2)
#             with col1:
#                 mid_end_plot = plot_func.top_10_sales_volume(mid_end, 'Mid end')
#             with col2:
#                 mid_high_plot = plot_func.top_10_sales_volume(mid_high, 'Mid to High')     

#             col5, col6 = st.columns(2)
#             with col1:
#                 high_plot = plot_func.top_10_sales_volume(high_end, 'High end')
#             with col2:
#                 premium_plot = plot_func.top_10_sales_volume(premium, 'Premium')          
            
#             title_overview = '''Mobile phone market in Shopee e-commerce split 3 segment:'''
#             st.markdown(f"<h1 style='text-align: center; color: black; font-size: 30px;'>{title_overview}</h1>", unsafe_allow_html=True)
            
#             title_overview = '''1. Big segment from low to near high end with the biggest brand: Samsung, OPPO, Xiaomi, Vivo, some small store'''
#             st.markdown(f"<h1 style='text-align: center; color: black; font-size: 25px;'>{title_overview}</h1>", unsafe_allow_html=True)    
            
#             title_overview = '''2. High end and premium, all phone is flagship and expensive. They are hand goods or genuine distribution '''
#             st.markdown(f"<h1 style='text-align: center; color: black; font-size: 25px;'>{title_overview}</h1>", unsafe_allow_html=True)

#             title_overview = '''3. Feature phone for old model, classical model, toy phone'''
#             st.markdown(f"<h1 style='text-align: center; color: black; font-size: 25px;'>{title_overview}</h1>", unsafe_allow_html=True)    
         
#         # 2. Top 10 sales volume
#         elif features == 'Top 10 revenue':

#             col1, col2 = st.columns(2)
#             with col1:
#                 ultra_low_volume_plot = plot_func.top_10_revenue(ultra_low_end, 'Ultra low end')
#             with col2:
#                 low_volume_plot = plot_func.top_10_revenue(low_end, 'Low end')

#             col3, col4 = st.columns(2)
#             with col1:
#                 mid_end_plot = plot_func.top_10_revenue(mid_end, 'Mid end')
#             with col2:
#                 mid_high_plot = plot_func.top_10_revenue(mid_high, 'Mid to High')     

#             col5, col6 = st.columns(2)
#             with col1:
#                 high_plot = plot_func.top_10_revenue(high_end, 'High end')
#             with col2:
#                 premium_plot = plot_func.top_10_revenue(premium, 'Premium')          
            
#             title_overview = '''Pattern same top 10 sales volume'''
#             st.markdown(f"<h1 style='text-align: center; color: black; font-size: 40px;'>{title_overview}</h1>", unsafe_allow_html=True)
            
#         # 3. Price
#         elif features == 'Price':
#             price_box = plot_func.price_box(ultra_low_end,low_end, mid_end, mid_high, high_end, premium)
#             price_scr = plot_func.price_scr(df)


#             title_overview = '''Customer in ultra low end and low end sensitive with price'''
#             st.markdown(f"<h1 style='text-align: center; color: black; font-size: 30px;'>{title_overview}</h1>", unsafe_allow_html=True)

#         # 4 Monthly event
#         elif features == 'Monthly event':
#             event_scr = plot_func.monthly_event_scr(df)            

#         # 5 Monthly event
#         elif features == 'Favorite product':
#             favor_scr = plot_func.favorite_scr(df)

#         # 6 Discount
#         elif features == 'Discount':
#             disc_scr = plot_func.discount_scr(df)
#             disc_box = plot_func.dis_box(ultra_low_end,low_end, mid_end, mid_high, high_end, premium)
        
#         # 7 Shopee mall
#         elif features == 'Shopee Mall':
#             mall_scr = plot_func.shopee_mall_scr(df)

#         # 8 Shopee mall
#         elif features == 'Guaranteed by Shopee':
#             guar_scr = plot_func.guaranteed_scr(df)
        
#         # 9 Respone rate
#         elif features == 'Response rate':
#             re_ra_scr = plot_func.res_rate_scr(df)

#         # 10 Time response
#         elif features == 'Time response':
#             time_res_scr = plot_func.time_res(df)

#         # 11 Experience
#         elif features == 'Experience':
#             exper_scr = plot_func.ex_scr(df)

#         # 12 Follower
#         elif features == 'Followers':
#             follow_scr = plot_func.follower_scr(df)
#             month_follow_scr = plot_func.month_follower_scr(df)

#         # 12 Follower
#         elif features == 'Special shop':
#             spe_scr = plot_func.special_scr(df)

#         # 13 Rating count product
#         elif features == 'Rating count product':
#             ra_co_pro_scr = plot_func.rate_count_pro_scr(df)
        
#         # 14 Rating product
#         elif features == 'Rating product':
#             rating_pro_scr = plot_func.rating_pro(df)

# elif choice == 'Conclusion':

#         title_shop = 'Key feature for shop'
#         st.markdown(f"<h1 style='text-align: center; color: black;'>{title_shop}</h1>", unsafe_allow_html=True)
#         st.markdown("""
#         ### What is making a shop successful?:
#         """)

#         # First
#         st.write('1. Keep response rate above 75%')
#         re_ra_scr = plot_func.res_rate_scr(df)

#         # Second
#         st.write('2. Thinking more about followers to feed their loyalty')
#         month_follow_scr = plot_func.month_follower_scr(df)

#         # Third
#         st.write('3. Maintain monthly event with Shopee, more 70% shop keep that')
#         ratio_month_event = df.groupby('monthly_event')['shop_name'].count().reset_index()
#         ratio_month_event['monthly_event'] = ratio_month_event['monthly_event'].apply(plot_func.replace)

#         fig = px.pie(ratio_month_event, values='shop_name', names='monthly_event', title='Ratio monthly event')
#         fig.update_layout(autosize=False, width=500, height=500)    
#         st.plotly_chart(fig, use_container_width=True)

#         # Fourth
#         st.write('4. Shopee mall from mid to above segment and favorite shop for ultra low and low end segment')
       
#         # fifth
#         st.write('5. Discount is a cultural on e-commerce, especially low segment')
#         disc_scr = plot_func.discount_scr(df)
#         # Six
#         st.write('6. In any case, the rating of product is very important, make sure always above 4 star. Keep in mind')
#         rating_pro_scr = plot_func.rating_pro(df)

#         title_shop = 'where is segment potential to join?'
#         st.markdown(f"<h1 style='text-align: center; color: black;'>{title_shop}</h1>", unsafe_allow_html=True)
#         st.markdown("""
#         ### Option 1: 
#         ### High end and premium - Business base on price and feeling of safe
#         - Product: Android high end or iPhone
#         - The strategic product you should to sell is iPhone hand goods
#         - Your competitor is Apple flagship store and shopdunk
#         - All you need to create an attractive price to contact customers, because in this segment whole customer want to make sure their iPhone can be warranty in VN or another solution suggested by you.
#         """)
#         st.image('./Images/Screen Shot 2021-10-21 at 09.06.50.png')
#         st.image('./Images/Screen Shot 2021-10-21 at 09.06.01.png')

#         st.markdown("""

#         ### Option 2:
#         ### Ultra low end and low end - Business base on interest, pleasure or basic demand
#         - Product: feature phone, old model, classical model, toy phone.
#         - Selecting products depends on your understanding martket, let choose really special phones
#         - Your business match Shopee's keywords, take advantage to explore customer
#         """)
#         st.image('./Images/Screen Shot 2021-10-21 at 09.02.28.png')
#         st.image('./Images/Screen Shot 2021-10-21 at 09.02.37.png')
#         st.image('./Images/Screen Shot 2021-10-21 at 09.11.00.png')

# #----------------------------* Modeling *----------------------------#

# elif choice == 'Modelling':
#         title_overview = 'Some point to better'
        
#         st.markdown("""
#         ### Machine learning solve regression problem
#         """)
#         st.write('Input: Numerical features in dataset')
#         st.write('Output: Number - Answer: How long to build shop?')
#         st.write('Model used: Linear Regression, SVM, Random forest')
#         st.write('Reuslt: Model cannot improve in root mean square error: 15,9' )

# #----------------------------* Improvement *----------------------------#

# elif choice == 'Improvement':
#         title_overview = 'Some point to better'
#         st.markdown(f"<h1 style='text-align: center; color: black;'>{title_overview}</h1>", unsafe_allow_html=True)
#         st.write('1. In dataset, more feature relavant conversion rate: reach, view, engagement,.. in shop feed on Shopee app')
#         st.write('2. Explore insight with unsupervised learning')

#         st.write('3. Apply deep learning model to predict where is the phone can buy in ultra low end and low end')
#         title_problem = 'Thank you!'
#         st.markdown(f"<h1 style='text-align: center; color: black;'>{title_problem}</h1>", unsafe_allow_html=True)
#----------------------------* Scape data *----------------------------#
# elif choice == 'Scape data':
#         title_overview = 'Result of crawling data'
#         st.markdown(f"<h1 style='text-align: center; color: black;'>{title_overview}</h1>", unsafe_allow_html=True)

#          #-----------------Show data set------------------------#
#         first_df = pd.read_csv('./shopee_phone.csv')
#         first_df = first_df.drop(columns='Unnamed: 0')
#         st.title("First time: Overall data")
#         st.markdown(""" 
#                 - Through **100 pages** mobile phone category and sort by monthly sales
#                 - Got **5760** products but only **2078** products have monthly sales at least once
#                 - Crawl more detail 1679 and use it that to EDA""")
#         st.write(first_df)

#         #-----------------Show data set------------------------#
#         first_df = pd.read_csv('./final_data.csv')
#         first_df = first_df.drop(columns=['Unnamed: 0', 'name_product'])
#         st.title("Second time: Detailed data")
#         st.markdown(""" 
#                     Detailed dataset 1679 products use to EDA
#                     """)
#         st.write(first_df)  

#----------------------------* Clean data *----------------------------#
# elif choice == 'Clean data':
#         title_overview = 'Overview Solution'
#         st.markdown(f"<h1 style='text-align: center; color: black;'>{title_overview}</h1>", unsafe_allow_html=True)
#         st.markdown("""
#         ### Step 1: Overview data and remove unneeded columns
#                 - Before: data have 43 feature
#                 - After: data only 28 features
#                 - Reason: Duplicate and useless feature

#         ### Step 2: Working with missing values
#         1. Check and fill missing values
#         2. Identify categorical and numerical features

#                 a. Numerical features: Strip unwanted characteristics, calculated
#                     Example feature: rating, price,...

#                 b. Categorical features: 
#                     -  Name: strip, replace, and remove not mobile phones
#                             Exmple name removed: Ốp lưng, tai nghe, miếng dán,...

#                     - Another features: One hot endcoding
#                             Example: Shopee mall, monthly event

#         ### Step 3: Check and change datatype
#                 - Ensure every single feature correct data type

#         ### Step 4: Handle duplicated data
#                 - No duplicate

#         ### Step 5: Handel mislabeled and corrupted data
#                 -  Remove mislabeled in name column above
#         """)

#----------------------------* Exploratory data analysis *-----