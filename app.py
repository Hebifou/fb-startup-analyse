
import streamlit as st
import pandas as pd

# Dummy-Daten
haendler_data = pd.DataFrame({
    "Name": ["Bar 17°", "Hanse Delikat", "Markthalle Neun", "Kaffeeklappe"],
    "Kategorie": ["Bar", "Feinkostladen", "Markthalle", "Café"],
    "Stadtteil": ["Schanze", "Eppendorf", "Altona", "St. Pauli"],
    "Zielgruppen-Fit": ["hoch", "mittel", "hoch", "hoch"]
})

influencer_data = pd.DataFrame({
    "Name": ["@foodlovehh", "@gastrohamburg", "@plantbasedpaula", "@hamburgdrinks"],
    "Plattform": ["Instagram", "TikTok", "Instagram", "YouTube"],
    "Follower": [12000, 8500, 10200, 7500],
    "Thema": ["Foodspots", "Gastro-Kritik", "Vegane Snacks", "Drinks & Bars"]
})

medien_data = pd.DataFrame({
    "Medium": ["Mit Vergnügen Hamburg", "Geheimtipp Hamburg", "Hamburg Kulinarisch", "Hinz&Kunzt"],
    "Typ": ["Blog", "Online-Magazin", "Blog", "Stadtmagazin"],
    "Fokus": ["Lifestyle & Food", "Szene & Genuss", "Kulinarik", "Stadtleben"],
    "Kontakt": ["mitvergnuegen.com", "geheimtipphamburg.de", "hamburgkulinarisch.de", "hinzundkunzt.de"]
})

partner_data = pd.DataFrame({
    "Partner": ["Küchenfreunde Hamburg", "Drink Syndikat", "Feierabend Markt", "Brew & Bite"],
    "Typ": ["Eventlocation", "Spirituosenmarke", "Eventreihe", "Café-Kette"],
    "Kooperationsidee": ["Pop-up Dinners", "Co-Branding Drinks", "Standplatz", "Testverkauf"],
    "Relevanz": ["hoch", "hoch", "mittel", "hoch"]
})

empfehlung_text = (
    "Empfehlung: Kooperation mit 'Bar 17°' + Influencer-Kampagne mit @foodlovehh + PR via 'Geheimtipp Hamburg'."
)

st.set_page_config(page_title="F&B Analyse Hamburg")
st.title("📊 Lokale Marketinganalyse für F&B-Startups – Hamburg")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📍 Partner & Händler", "📲 Influencer", "📰 Medien", "🤝 Kooperationen", "✅ Empfehlung"
])

with tab1:
    st.subheader("Lokale Händler & Orte")
    st.dataframe(haendler_data)

with tab2:
    st.subheader("Influencer-Vorschläge")
    st.dataframe(influencer_data)

with tab3:
    st.subheader("Relevante Medien")
    st.dataframe(medien_data)

with tab4:
    st.subheader("Potenzielle Kooperationspartner")
    st.dataframe(partner_data)

with tab5:
    st.subheader("Empfohlene Maßnahme")
    st.write(empfehlung_text)
