import pandas as pd
import matplotlib.pyplot as plt 
import gradio as gr 


df = pd.read_csv('previsions_meteo.csv') 


   
   plt.figure(figsize=(10, 6)) 
   plt.plot(df_lieu['Date'], df_lieu['Temperature'], label='Température')
   plt.plot(df_lieu['Date'], df_lieu['Humidite'], label='Humidité')         
   plt.plot(df_lieu['Date'], df_lieu['Precipitations'], label='Précipitations')         
   plt.xlabel("Date")         plt.ylabel("Valeur")         
   plt.title(f"Prévisions météorologiques pour {lieu}")
   plt.legend()         
   plt.xticks(rotation=45)         
   plt.show() 
 
def previsions_meteo_interactives(lieu): 
    # Charger les données de prévision météorologique à l'aide de pandas     
    df = pd.read_csv('previsions_meteo.csv')  # Remplacez par le chemin réel de votre ensemble de données de prévision météorologique 
