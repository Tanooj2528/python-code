import pathlib 
import os 
import pygame 

inputdirectory = "C:\Users\tanoo\Downloads"

initial_count = 0 
for path in pathlib.Path = ("C:\Users\tanoo\Downloads") :
    if path.is_file() :
        initial_count += 1
        
print("There are", initial_count, "audio files\n")

list = os.listdir("C:\Users\tanoo\Downloads")
print(list)

song = input("\nEnter The Song File You Wish To Play: ")
file = os.path.join(inputdirectory, song)

pygame.init()
pygame.mixer.music.load(file)

while True :
    n = input("Type Play or Stop to start or stop the song. \n type exit to stop the music")
    if n == "play" :
        pygame.mixer.music.play()
    elif n == "stop" :
        pygame.mixer.music.pause()
    elif n == "exit" :
        pygame.mixer.music.exit()
        
