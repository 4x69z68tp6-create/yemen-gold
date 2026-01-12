import streamlit as st
import requests

def get_gold_price():
    try:
        url = "https://data-asg.goldprice.org/dbXRates/USD"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        data = response.json()
        price_per_ounce = data['items'][0]['xauPrice']
        return price_per_ounce / 31.1035
    except:
        return None

st.set_page_config(page_title="بورصة الذهب - اليمن", page_icon="💰")
st.title("💰 حاسبة أسعار الذهب في اليمن")

region = st.radio("اختر المنطقة (لتحديد سعر الصرف):", ("صنعاء (535)", "عدن (1620)", "إدخال يدوي"))

if region == "صنعاء (535)":
    exchange_rate = 535
elif region == "عدن (1620)":
    exchange_rate = 1620
else:
    exchange_rate = st.number_input("أدخل سعر الصرف:", value=600)

if st.button('احسب الآن'):
    gold_24_usd = get_gold_price()
    if gold_24_usd:
        price_24_yer = gold_24_usd * exchange_rate
        price_21_yer = (price_24_yer * 21) / 24
        
        st.metric("سعر عيار 24 (ريال)", f"{int(price_24_yer):,}")
        st.metric("سعر عيار 21 (ريال)", f"{int(price_21_yer):,}")
    else:
        st.error("خطأ في الاتصال بالإنترنت")
