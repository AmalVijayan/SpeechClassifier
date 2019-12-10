#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Loading the saved model
import pickle
filename = 'News_Classifier.pkl'
model = pickle.load(open(filename, 'rb'))


# In[2]:


#Importing the speech recognition module
import speech_recognition as sr
#A random default value for prediction -- not among the classes we are predicting
prediction = 10

#Initializing the speech recognizer
r = sr.Recognizer()

#Declaring the listener source
with sr.Microphone() as source:
    print('-'*30)
    print('-'*30)
    print("\n\nHi !! Say something and I will try to understand what you are talking about !!\n")
    print('-'*30)
    print("\nListening :\n")
    print('-'*30)
    
    #Initializing the listener 
    audio = r.listen(source)
    
    #Collecting Speech and Classifying
    try:
        text = r.recognize_google(audio)
        print("\nYou said : {}".format(text))
        prediction, _ = model.predict([text.strip()])
        
    except:
        print("\nSorry could not recognize what you said")
    
    if int(prediction) == 0:
        print('\nYou spoke about POLITICS')
    elif int(prediction) == 1:
        print('\nYou spoke about TECHNOLOGY')
    elif int(prediction) == 2:
        print('\nYou spoke about Entertainment')
    elif int(prediction) == 3:
        print('\nYou spoke about Business')

