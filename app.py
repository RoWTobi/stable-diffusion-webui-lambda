import os
import shutil
import threading

def run_command(command):
    os.system(command)

os.system(f"git lfs install")
os.system(f"git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui /home/demo/source/stable-diffusion-webui")

shutil.move("ui-config.json", "/home/demo/source/stable-diffusion-webui/ui-config.json")

os.chdir(f"/home/demo/source/stable-diffusion-webui")

os.system(f"git clone https://github.com/Mikubill/sd-webui-controlnet /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet")
os.system(f"git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete /home/demo/source/stable-diffusion-webui/extensions/a1111-sd-webui-tagcomplete")

os.system(f"git clone https://github.com/catppuccin/stable-diffusion-webui /home/demo/source/stable-diffusion-webui/extensions/stable-diffusion-webui-catppuccin")

threads = []

# Models
models_commands = [
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://civitai.com/api/download/models/11745 -d /home/demo/source/stable-diffusion-webui/models/Stable-diffusion -o chilloutmix_NiPrunedFp32Fix.safetensors",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://civitai.com/api/download/models/31284 -d /home/demo/source/stable-diffusion-webui/models/Lora -o koreanDollLikeness.safetensors"
]

for command in models_commands:
    thread = threading.Thread(target=run_command, args=(command,))
    thread.start()
    threads.append(thread)

# ControllNet
controlnet_commands = [
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_canny_fp16.safetensors",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_canny_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_canny_fp16.yaml",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_softedge_fp16.safetensors",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_softedge_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_softedge_fp16.yaml",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose_fp16.safetensors -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_openpose_fp16.safetensors",
    "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_openpose_fp16.yaml -d /home/demo/source/stable-diffusion-webui/extensions/sd-webui-controlnet/models -o control_v11p_sd15_openpose_fp16.yaml"
]

for command in controlnet_commands:
    thread = threading.Thread(target=run_command, args=(command,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

os.system(f"python launch.py --port 8266 --listen --cors-allow-origins=* --xformers --enable-insecure-extension-access --theme dark --gradio-queue --disable-safe-unpickle")
