import pyaudio
import wave
import soundfile as sf
from tacotron2_demo.core.models import TTSModel
import json
import sys
import os
from alfred.dl.tf.common import mute_tf
mute_tf()


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


if __name__ == "__main__":
    tts_model = TTSModel()

    ts = [
        '如果现在还不了，您可以想办法处理啊，您家人知道您的逾期情况吗？他们能不能帮您周转处理逾期账单？',
        '早上好呀，今天天气看起来蛮不错的，作为一个很厉害的人工智能，你想知道今天的天气预报吗',
        '哈哈哈哈，我的声音是不是很奇怪？是我主人把我训练出来的',
        '科学家都是非常严谨的，你真的不希望来一杯咖啡吗',
        '别熬夜了，少年，早点睡觉吧'
    ]

    for t in ts:
        mels, alignment_history, audios = tts_model.do_synthesis(t)
        sf.write('demo.wav', audios, 24000)
        print('start to play...')
        play('demo.wav')
