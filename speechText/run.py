import speech_recognition as sr 
mic_name = "HDA Intel PCH: ALC3246 Analog (hw:0,0)"

class Run():

    def main():
        sample_rate = 48000
        #Chunk is like a buffer. It stores 2048 samples (bytes of data) 
        #here. 
        #it is advisable to use powers of 2 such as 1024 or 2048 
        chunk_size = 2048
        #Initialize the recognizer 
        r = sr.Recognizer() 

        #generate a list of all audio cards/microphones 
        mic_list = sr.Microphone.list_microphone_names() 
        print(mic_list)


        #the following loop aims to set the device ID of the mic that 
        #we specifically want to use to avoid ambiguity. 
        for i, microphone_name in enumerate(mic_list): 
            if microphone_name == mic_name: 
                device_id = i
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source: 
        #wait for a second to let the recognizer adjust the 
        #energy threshold based on the surrounding noise level
            r.adjust_for_ambient_noise(source) 
            print ("Wait for a minute and - Say Something")
            #listens for the user's input 
            audio = r.listen(source) 
                
            try: 
                text = r.recognize_google(audio) 
                print ("you said: " + text )
            
            #error occurs when google could not understand what was said 
            
            except sr.UnknownValueError: 
                text = "Google Speech Recognition could not understand audio"
                print(text) 
            
            except sr.RequestError as e: 
                text = "Could not request results from Google Speech Recognition service; {0}".format(e)
                print(text)
            
            return text



'''
        recorder = Recorder("speech.wav")#
        print(recorder)

        print("Please say something nice into the microphone\n")
        recorder.record_to_file()

        print("Transcribing audio....\n")
        result = transcribe_audio('speech.wav')
        print(result)
        text = result["results"][0]["alternatives"][0]["transcript"]
        print(text)
        return text
'''

    # if __name__ == '__main__':
    #     dotenv_path = join(dirname(__file__), '.env')
    #     load_dotenv(dotenv_path)
    #     try:
    #         main()
    #     except:
    #         print("IOError detected, restarting...")
    #         main()


