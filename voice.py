import speech_recognition as sr
import pyttsx3

# Initialiser le moteur de synthèse vocale
moteur = pyttsx3.init()

# Initialiser le reconnaiseur vocal
reconnaiseur = sr.Recognizer()

# Fonction pour faire parler l'assistant vocal
def parler(texte):
    moteur.say(texte)
    moteur.runAndWait()

# Fonction pour écouter les commandes vocales
def ecouter():
    with sr.Microphone() as source:
        print("Dites quelque chose...")
        audio = reconnaiseur.listen(source)
        
        try:
            commande = reconnaiseur.recognize_google(audio, language="fr-FR")
            print("Vous avez dit :", commande)
        except:
            print("Je n'ai pas compris.")
            commande = ""
        
        return commande.lower()

# Boucle principale pour l'assistant vocal
while True:
    commande = ecouter()
    
    if "bonjour" in commande:
        parler("Bonjour, comment puis-je vous aider ?")
    
    elif "quelle heure est-il" in commande:
        import datetime
        maintenant = datetime.datetime.now()
        heure = maintenant.strftime("%H:%M")
        parler("Il est " + heure)
        
    elif "stop" in commande:
        parler("Au revoir !")
        break
        
    else:
        parler("Je n'ai pas compris.")
