#Local URL: http://localhost:8501 Network URL: http://192.168.1.2:8501
#pagina: https://share.streamlit.io/andersonstiwardgonzalez/aaaaaaaaaaaaaaaaaaaa/main/app.py
import streamlit as st
st.set_page_config(page_title="B-phages", page_icon=":dna:", layout="wide")
st.title("¡Hola! Somos B-phages :wave:")
st.subheader("Somos una empresa comprometida con tu salud")
st.write("Queremos darte el mejor de los tratamientos contra las infecciones por bacterias multiresistentes")
st.write("Somos los mejores, somos una retrochimba")
st.write("[Aprende más de como ser cool --->](https://www.youtube.com/watch?v=VqgUkExPvLY)")
st.audio("y2mate.com - Bad Bunny  Tu No Metes Cabra Video Oficial.mp3")
st.image("jajaja.jpeg")
with st.container():
  st.write("---")
  st.title("Equipo de trabajo")
  left_column, right_column = st.columns(2)
  with left_column:
    st.write("[Ana Maria Ruiz León](https://co.linkedin.com/)")
    with right_column:
      st.image("aaaaana.jpg")
      st.image("homer.gif")
      with left_column:
        st.write("melooo")
        with st.container():
          st.tittle("Mision")

  
