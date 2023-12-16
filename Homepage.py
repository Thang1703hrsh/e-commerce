import altair as alt
import streamlit as st
import requests
import pandas as pd
import base64
import datetime
from st_pages import Page, show_pages, add_page_title

st.set_page_config(
    page_title='E-commerce Sales Analysis',
    page_icon="chart_with_upwards_trend",
    layout='wide',
)
# st.title('Explore Sales Data')


def get_image_base64(image_path):
    with open(image_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')


image_base64 = get_image_base64('Devops-ecom.gif')
st.markdown(f"""
    <div style='border-radius: 100px; overflow: hidden;'>
        <img src='data:image/gif;base64,{image_base64}' width='100%' height='60%'/>
    </div>
    """, unsafe_allow_html=True)


st.markdown(
    """
<style>
.css-1aumxhk {
    background-color: #D4AF37;
}
</style>
""",
    unsafe_allow_html=True,
)


# # Specify what pages should be shown in the sidebar, and what their titles 
# # and icons should be
show_pages(
    [
        Page("Homepage.py", "Homepage", "🏠"),
        Page("pages/Customer.py", "Customer Analyst", ":customs:"),
        Page("pages/Product.py", "Product Analyst", ":shopping_trolley:"),
        Page("pages/Transaction.py", "Transaction Analyst", ":inbox_tray:"),
        Page("pages/Product_Link.py", "Product Link Algorithm", ":linked_paperclips:"),
        Page("pages/Revenue_Forecast.py", "Revenue Forecast Predict", ":chart_with_upwards_trend:"),
        Page("pages/Cluster_Customers.py", "Cluster Customers", ":customs:"),
    ]
)

