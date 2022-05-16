import streamlit as st
import pandas as pd
from core import yoga_centres

st.set_page_config(
    page_title="Lucid | Map",
    page_icon="../assets/logo.png",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("../../README.md").read(),
    },
)

st.title("Map")

# data = yoga_centres()
# df = pd.DataFrame(index=["lat", "lon"])
# path = data["resourceSets"]["resources"][0]
# for point in path:
#    try:
#        data = path[point]["coordinates"]
#        df.append(data)
#    except:
#        pass
# df = pd.read_json(data)

df = pd.read_json("data.json")
st.map(df)
