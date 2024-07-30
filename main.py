import requests
from youtube_transcript_api import YouTubeTranscriptApi
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Assurez-vous d'avoir téléchargé les ressources NLTK nécessaires
nltk.download('punkt')
nltk.download('stopwords')

# Fonction pour obtenir la transcription de la vidéo
def get_transcript(video_id, language='fr'):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        return ' '.join([t['text'] for t in transcript])
    except Exception as e:
        print(f"Erreur lors de l'obtention de la transcription : {e}")
        return None

# Fonction d'analyse de contenu
def analyze_content(transcript):
    # Simuler une analyse simple
    words = word_tokenize(transcript)
    stop_words = set(stopwords.words('french'))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Calculer un pourcentage d'authenticité basé sur le nombre de mots filtrés
    authenticity_percentage = min(100, len(filtered_words) / 100) * 100  # Normalisation pour obtenir un pourcentage
    return round(authenticity_percentage, 2)

# Fonction principale
def main(video_url):
    video_id = video_url.split('v=')[1]
    transcript = get_transcript(video_id, language='fr')  # Demander la transcription en français
    
    if transcript:
        authenticity_percentage = analyze_content(transcript)
        print(f'Pourcentage d\'authenticité : {authenticity_percentage}%')
    else:
        print("Impossible d'analyser la vidéo.")

# Exemple d'utilisation
if __name__ == "__main__":
    video_url = input("Entrez le lien de la vidéo YouTube : ")
    main(video_url)