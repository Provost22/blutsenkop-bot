import streamlit as st
import random

st.set_page_config(page_title="Blutsenkop Bot", page_icon="🍺")

st.title("🤖 Den Blutsenkop Bot")
st.write("Typ iets tegen den Blutsenkop hieronder ⬇️")

zin = st.text_input("Wat wil je zeggen?", "")

if zin:
    zin_lc = zin.lower()

    if "afsluiten" in zin_lc or "stop" in zin_lc:
        st.write("Blutsenkop: Enfin, ik ga slapen. Veel succes met uw leven.")

    elif "bier" in zin_lc:
        st.write("Blutsenkop: Bier? Ik sta al aan de tapkraan jong.")

    elif "honger" in zin_lc:
        st.write("Blutsenkop: Da's uw eigen schuld, ge had mosselen moeten bestellen.")

    elif "moe" in zin_lc:
        st.write("Blutsenkop: Ik heb 4 dagen Rock Werchter overleefd, gij klaagt over moe?")

    else:
        uitspraken = [
            "Zeg maat, trakteer is iets of zwijg.",
            "Ik heb een kater, dus geen gezaag vandaag.",
            "Mijn hoofd bonkt harder dan een techno set om 6u 's morgens.",
            "Wa zegde? Ge zijt precies van de scouts."
        ]
        st.write("Blutsenkop: " + random.choice(uitspraken))
