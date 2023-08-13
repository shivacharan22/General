
import wave
import contextlib
import os
from pydub import AudioSegment

output_dir = r"D:\mosiq_dect\data_1.5\Anopheles quadrimaculatus"
input_dir = r"D:\mosiq_dect\extra\extra\Anopheles quadrimaculatus\Auburn_Xperia"


for index,file in enumerate(os.listdir(input_dir)):
    if file.endswith(".wav"):
        with contextlib.closing(wave.open(os.path.join(input_dir, file),'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
                print(duration)
                if duration>2.0:
                    for i in range(int(duration/2.0)):
                        with wave.open(output_dir+'\\audio'+str(i)+"_"+str(index)+'0'+'.wav','w') as f1:
                            f1.setparams(f.getparams())
                            f1.writeframes(f.readframes(int(rate*2.0)))
                else:
                    print("less")
                    with wave.open(output_dir+'\\audio'+"_"+str(index)+'0'+'.wav','w') as f1:
                            f1.setparams(f.getparams())
                            f1.writeframes(f.readframes(int(rate*duration)))
                            print("created")
    elif file.endswith(".m4a"):
        audio = AudioSegment.from_file(os.path.join(input_dir, file))
        prev = 0
        print(len(audio))
        for i in range(0,len(audio),2000):             
             temp = audio[prev:i]
             prev = i
             temp.export(output_dir+"\\audio_"+str(i)+"_"+str(index)+"1_m4a"+".wav", format="wav")
    elif file.endswith(".amr"):
        audio = AudioSegment.from_file(os.path.join(input_dir, file))
        prev = 0
        print(len(audio))
        for i in range(0,len(audio),2000):             
             temp = audio[prev:i]
             prev = i
             temp.export(output_dir+"\\audio_"+str(i)+"_"+str(index)+"0_amr"+".wav", format="wav")
    elif file.endswith(".mp4"):
        audio = AudioSegment.from_file(os.path.join(input_dir, file))
        prev = 0
        print(len(audio))
        for i in range(0,len(audio),2000):             
             temp = audio[prev:i]
             prev = i
             temp.export(output_dir+"\\audio_"+str(i)+"_"+str(index)+"0_mp4"+".wav", format="wav")