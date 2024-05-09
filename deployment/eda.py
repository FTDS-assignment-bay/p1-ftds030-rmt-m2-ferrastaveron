import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def run():
   st.title('Exploratory Data Analysis')

   st.write('Pada halaman ini akan dipaparkan eksplorasi data board game yang didapatkan dari situs BoardGameGeek.')
   
   image = Image.open('boardgame.jpg')
   st.image(image)
   st.markdown('---')
   
   st.write('### Board Game dengan Rating Tertinggi')
   image2 = Image.open('erune.jpg')
   st.image(image2)
   st.write('Board Game dengan rating terbaik menurut dataset dari BoardGameGeek adalah Erune dengan rating hampir sempurna di 9.58.')
   st.markdown('---')

   st.write('### Board Game dengan Rating Terendah')
   image3 = Image.open('one.png')
   st.image(image3)
   st.write('Sedangkan untuk Board Game dengan rating terburuk dipegang oleh Oneupmanship yang rilis tahun 2013. Game tersebut hanya memiliki rating 1.05 dari total 67 orang pemain yang memberi rating.')
   st.write('Sekilas mirip dengan Monopoly tapi versi buatan orang goa.')
   st.markdown('---')

   st.write('### Board Game Tertua')
   image4 = Image.open('senet.jpg')
   st.image(image4)
   st.write('Board Game tertua dalam dataset berumur sekitar 5500 tahun dan pertama kali dirilis sekitar tahun 3500 sebelum masehi. Nama game tersebut adalah Senet yang berasal dari zaman Mesir kuno. Permainannya mirip seperti catur dan terdiri dari 8 sampai 10 pion untuk memainkannya.')
   st.markdown('---')

   st.write('### Board Game dengan Playtime Terlama')
   image5 = Image.open('north.jpg')
   st.image(image5)
   st.write('Board Game dengan playtime atau waktu bermain terlama dalam dataset tersebut bernama "The Campaign for North Africa: The Desert War". Tidak tanggung-tanggung, rata-rata waktu yang dibutuhkan untuk menyelesaikan permainannya mencapai 60000 menit atau setara dengan 41 hari. Mending perbanyak ibadah atau cari kerja kamu.')
   st.write('Sekilas sih tidak terlihat seperti board game ya, lebih seperti tabel periodik kimia.')
   st.markdown('---')

   st.write('### 5 Mekanik Paling Umum')
   image6 = Image.open('mech.png')
   st.image(image6)
   st.write('Dice Rolling atau permainan melempar dadu menjadi mekanik yang paling umum digunakan pada suatu permainan papan. Sementara auction atau lelang adalah mekanik yang paling jarang digunakan.')
   st.markdown('---')

   st.write('### Domain Paling Umum')
   image7 = Image.open('domain.png')
   st.image(image7)
   st.write('Domain atau tipe permainan papan yang paling sering muncul dalam data adalah Wargames atau peperangan, disusul dengan Strategy Games (permainan strategi) dan Family Games (permainan keluarga).')
   st.markdown('---')











if __name__ == '__main__':
   run()