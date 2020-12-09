import librosa
import scipy
from scipy.io import wavfile as wf
import wave
import pyaudio
import numpy as np
import os
# from librosa.output import write_wav
import soundfile as sf

y, sr = librosa.load(
    '/media/jintian/samsung/source/ai/swarm/exp/TensorFlowTTS_chinese/generate_tts_data/aliyu_语速-300_采样8k.wav')
print(y)
print(sr)

# wf.write('aa.wav', sr, y)
sf.write('aaa.wav', y, sr)
# write_wav('aaa.wav', y, sr)


def wav2pcm(wavfile, pcmfile, data_type=np.int16):
    f = open(wavfile, "rb")
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype= data_type)
    data.tofile(pcmfile)

def play(f):
    chunk = 1024
    wf = wave.open(f, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                    rate=wf.getframerate(), output=True)
    data = wf.readframes(chunk)  # 读取数据
    while data != b'':  # 播放
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()  # 停止数据流
    stream.close()
    p.terminate()  


play('aaa.wav', False)
