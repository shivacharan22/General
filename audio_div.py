import wave
import contextlib
import os

directory = r'D:\mosiq_dect\extra\extra'
output_dir = r'D:\mosiq_dect\data_1.5'
dic_list = ['Aedes aegypti','Aedes sierrensis','Anopheles atroparvus','Anopheles dirus','Anopheles farauti','Anopheles freeborni','Anopheles gambiae akron','Anopheles gambiae kisumu','Anopheles minimus','Anopheles quadriannulatus','Anopheles stephensi','Culex pipiens','Culex tarsalis']

for index, filename in enumerate(os.listdir(directory)):
    for file in os.listdir(os.path.join(directory, filename)):
        if os.path.isdir(os.path.join(os.path.join(directory, filename),file)):
            for fil in os.listdir(os.path.join(os.path.join(directory, filename),file)):
                if fil.endswith(".wav"):
                    with contextlib.closing(wave.open(os.path.join(os.path.join(os.path.join(directory, filename),file),fil),'r')) as f:
                        frames = f.getnframes()
                        rate = f.getframerate()
                        duration = frames / float(rate)
                        print(duration)
                        for i in range(int(duration/1.5)):
                            with wave.open('audio'+str(i)+'.wav','w') as f1:
                                f1.setparams(f.getparams())
                                f1.writeframes(f.readframes(int(rate*1.5)))
        elif file.endswith(".wav"):
            with contextlib.closing(wave.open(os.path.join(os.path.join(directory, filename),file),'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
                print(duration)
                for i in range(int(duration/1.5)):
                    with wave.open('audio'+str(i)+'.wav','w') as f1:
                        f1.setparams(f.getparams())
                        f1.writeframes(f.readframes(int(rate*1.5)))
