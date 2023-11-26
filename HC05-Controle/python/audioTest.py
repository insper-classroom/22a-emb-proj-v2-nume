from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# Get current volume

currentVolumeDb = volume.GetMasterVolumeLevel()
volume.SetMasterVolumeLevel(-10.015, None)
# NOTE: -10.329694747924805 = 50% do vo

print(currentVolumeDb)

