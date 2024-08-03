import os
import time
import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()


def clear_screen():
  os.system('clear')


def pause():
  pygame.mixer.pause()


pause()


def play():
  pygame.mixer.unpause()
  print("\n🎵 🎵 🎵 🎵 🎵 🎵 🎵 🎵 🎵 🎵 🎵 🎵 🎵")
  print("\nPlaying", songName, "from", artistName)
  print("\n▶️       ⏸️")
  print("\nPlay    Pause")
  while True:
    pressEnter = input().strip().lower()
    if pressEnter == "":
      pause()
      print("Song Paused. Press R to resume or E to exit")
    elif pressEnter == "r":
      play()
      print("\n🎵 🎵 🎵 🎵 🎵 🎵 🎵 🎵 🎵 🎵 🎵 🎵 🎵")
      print("\nPlaying")
      print("\n▶️       ⏸️")
      print("\nPlay    Pause")
    elif pressEnter == "e":
      print("\nReloading menu...")
      return
    else:
      print("Invalid input. Reloading menu...")
      return


def main():
  while True:
    time.sleep(1)
    clear_screen()
    print("🎵 MyPOD Music Player 🎵")
    print("\nPress 1 to Play   ▶️")
    print("\nPress 2 to Exit   🔚")
    print("\nPress anything else to see the menu again.")
    userInput = input("\nEnter your choice: ").strip()
    if userInput == "1":
      global songName
      songName = input("Pick the song: ")
      global artistName
      artistName = input("Pick the artist: ")
      play()
    elif userInput == "2":
      print("\nExiting... 🔚🔚🔚")
      break
    else:
      print("\nInvalid input. Please try again.")
      time.sleep(1)
      print("\nEntering menu...")
      continue


if __name__ == "__main__":
  main()

time.sleep(1)
clear_screen()
print("\nThanks for listening!")
