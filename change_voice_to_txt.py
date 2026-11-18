import speech_recognition as sr
import os
r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=0.3)
    while True:
        try:
            print("Listening...")
            audio = r.listen(source,timeout=10)
            text = r.recognize_google(audio,language="fa-IR",)

            print (f"You said: {text}")
            if os.path.exists("change_voice_to_text.txt"):
                with open("change_voice_to_text.txt","a") as edit_file:
                    edit_file.write(f"{str(text)}\n")
            else:
                with open("change_voice_to_text.txt","w") as file:
                    file.write(f"{str(text)}\n")
                

            if"خروج" in text:
                print("Exiting program...")
                break
    
        except sr.WaitTimeoutError:
            print("time out !!!!")
            break

        
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            break
            
        except sr.UnknownValueError:
            print("Could not understand audio")
            break

        except KeyboardInterrupt:
            print("Program terminated by user")
            break