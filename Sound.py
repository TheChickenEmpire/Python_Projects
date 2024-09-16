from word2number import w2n
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
import numpy as np
from comtypes import CLSCTX_ALL
def setsound(desired_vol):
        desired_vol = w2n.word_to_num(desired_vol)
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        vol_range = volume.GetVolumeRange()
        min_vol = vol_range[0]
        max_vol = vol_range[1]
        desired_vol_db = np.interp(desired_vol, [0, 100], [min_vol, max_vol])
        volume.SetMasterVolumeLevelScalar(desired_vol / 100, None)
        curr_vol = int(volume.GetMasterVolumeLevelScalar() * 100)
while True:
    setsound(input('Volume:\n'))