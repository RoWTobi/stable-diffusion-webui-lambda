import os
import shutil

os.system(f"git lfs install")
os.system(f"git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui /home/demo/source/stable-diffusion-webui")

# Config Datei
shutil.move("ui-config.json", "/home/demo/source/stable-diffusion-webui/ui-config.json")

os.chdir(f"/home/demo/source/stable-diffusion-webui")

# Addons
os.system(f"git clone https://github.com/Mikubill/sd-webui-controlnet /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet")
os.system(f"git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete /home/demo/source/stable-diffusion-webui/extensions/a1111-sd-webui-tagcomplete")

os.system(f"git clone https://github.com/catppuccin/stable-diffusion-webui /home/demo/source/stable-diffusion-webui/extensions/stable-diffusion-webui-catppuccin")

os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://civitai.com/api/download/models/11745 -d /home/demo/source/stable-diffusion-webui/models/Stable-diffusion -o chilloutmix_NiPrunedFp32Fix.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://civitai.com/api/download/models/31284 -d /home/demo/source/stable-diffusion-webui/models/Lora -o koreanDollLikeness.safetensors")

os.system(f"python launch.py --port 8266 --listen --cors-allow-origins=* --xformers --enable-insecure-extension-access --theme dark --gradio-queue --disable-safe-unpickle")
