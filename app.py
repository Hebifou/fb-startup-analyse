import streamlit as st
import pandas as pd

# Dummy-Daten vorbereiten
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

# App-Layout
st.set_page_config(page_title="F&B Analyse Hamburg")
st.title("Lokale Marketinganalyse für F&B-Startups – Hamburg")
st.markdown(
    "#### Wir helfen Food & Beverage Startups dabei, "
    "datengestützte Marketingstrategien mit lokalen Partnern, "
    "relevanten Medien und passenden Influencern schnell und effizient zu entwickeln."
)
st.markdown("---")  # fügt eine horizontale Linie als optische Trennung ein


# Navigation
tabs = st.tabs([
    "Use Case", 
    "Partner & Händler", 
    "Influencer", 
    "Medien", 
    "Kooperationen", 
    "Empfehlung"
])

# Use Case
with tabs[0]:
    st.subheader("Individueller Marketing-Use-Case")
    produkt = st.selectbox("Produktart wählen:", ["Rum", "Kaffee", "Veganes Eis"])
    zielgruppe = st.selectbox("Zielgruppe:", ["jung & urban", "nachhaltig & bewusst", "genussorientiert"])
    budget = st.selectbox("Marketingbudget:", ["niedrig", "mittel", "hoch"])

    if st.button("Analyse starten"):
        st.markdown("### Ergebnis")
        if produkt == "Rum" and zielgruppe == "jung & urban":
            st.write("Empfehlung: Präsenz in Bars wie Bar 17° und Co-Branding mit Drink Syndikat. "
                     "Social-Media-Kampagne mit @hamburgdrinks (YouTube) oder @gastrohamburg (TikTok). "
                     "Eventplatzierung im Feierabend Markt für Tastings.")
        elif produkt == "Kaffee" and zielgruppe == "nachhaltig & bewusst":
            st.write("Empfehlung: Kooperation mit Kaffeeklappe (St. Pauli), Influencer-Kampagne mit @plantbasedpaula. "
                     "PR über Hamburg Kulinarisch. Testverkauf bei Brew & Bite.")
        elif produkt == "Veganes Eis":
            st.write("Empfehlung: PR mit Geheimtipp Hamburg, Influencer @foodlovehh, Produktplatzierung in Markthalle Neun.")
        else:
            st.write("Es konnte keine eindeutige Empfehlung generiert werden.")

# Händler
with tabs[1]:
    st.subheader("Lokale Händler & Orte")
    st.dataframe(haendler_data)

# Influencer
with tabs[2]:
    st.subheader("Influencer-Vorschläge")
    st.dataframe(influencer_data)

# Medien
with tabs[3]:
    st.subheader("Relevante Medien")
    st.dataframe(medien_data)

# Kooperationen
with tabs[4]:
    st.subheader("Potenzielle Kooperationspartner")
    st.dataframe(partner_data)

# Empfehlung (statisch)
with tabs[5]:
    st.subheader("Empfohlene Maßnahme")
    st.write("Empfehlung: Kooperation mit 'Bar 17°' + Influencer-Kampagne mit @foodlovehh + PR via 'Geheimtipp Hamburg'.")
