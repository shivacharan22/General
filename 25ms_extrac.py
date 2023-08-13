
import wave
import contextlib
import os
from pydub import AudioSegment

output_dir = r"D:\mosiq_dect\data256_"
input_dir = r"D:\mosiq_dect\data_1.5"

for indf,folder in enumerate(os.listdir(input_dir)):
    for index,file in enumerate(os.listdir(os.path.join(input_dir, folder))):
            audio = AudioSegment.from_file(os.path.join(os.path.join(input_dir, folder), file))
            prev = 0
            if len(audio) == 0 or len(audio)!=2000:
                continue
            print(len(audio))
            if not os.path.exists(output_dir+"\\"+folder):
                os.makedirs(output_dir+"\\"+folder)
            for i in range(0,len(audio),256):             
                temp = audio[prev:i]
                prev = i
                temp.export(output_dir+"\\"+folder+"\\audio_"+str(i)+"_"+str(index)+"_"+str(indf)+".wav", format="wav")
                if file.endswith(".wav"):
                    audio = AudioSegment.from_file(os.path.join(os.path.join(input_dir, folder), file))
                    prev = 0
                    print(len(audio))
                    for i in range(0,len(audio),256):             
                        temp = audio[prev:i]
                        prev = i
                        temp.export(output_dir+"\\audio_"+str(i)+"_"+str(index)+"_"+indf+".wav", format="wav")
                elif file.endswith(".m4a"):
                    audio = AudioSegment.from_file(os.path.join(input_dir, file))
                    prev = 0
                    print(len(audio))
                    for i in range(0,len(audio),256):             
                        temp = audio[prev:i]
                        prev = i
                        temp.export(output_dir+"\\audio_"+str(i)+"_"+str(index)+"_"+indf+"m4a"+".wav", format="wav")
                elif file.endswith(".amr"):
                    audio = AudioSegment.from_file(os.path.join(input_dir, file))
                    prev = 0
                    print(len(audio))
                    for i in range(0,len(audio),256):             
                        temp = audio[prev:i]
                        prev = i
                        temp.export(output_dir+"\\audio_"+str(i)+"_"+str(index)+"_"+indf+"amr"+".wav", format="wav")
                elif file.endswith(".mp4"):
                    audio = AudioSegment.from_file(os.path.join(input_dir, file))
                    prev = 0
                    print(len(audio))
                    for i in range(0,len(audio),256):             
                        temp = audio[prev:i]
                        prev = i
                        temp.export(output_dir+"\\audio_"+str(i)+"_"+str(index)+"0_mp4"+".wav", format="wav")