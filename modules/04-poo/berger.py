from ma_classe import Dog

class Berger(Dog):
    def speak(self, sound="Waaf"):
        return super().speak(sound)


milou = Berger("Milou", 1)
print(milou)
print(milou.speak("Waaf Waaf"))