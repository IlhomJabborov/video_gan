import cv2
import numpy as np
import glob
from os.path import isfile, join
import subprocess
import os
import shutil

def make_folder():
    upload_folder = 'upload'
    result_folder = 'results'
    video_folder = 'videos'
    video_result_folder = 'results_videos'
    video_mp4_result_folder = 'results_mp4_videos'

    if os.path.isdir(upload_folder):
        print(upload_folder+" exists")
    else :
        os.mkdir(upload_folder)

    if os.path.isdir(video_folder):
        print(video_folder+" exists")
    else :
        os.mkdir(video_folder)

    if os.path.isdir(video_result_folder):
        print(video_result_folder+" exists")
    else :
        os.mkdir(video_result_folder)

    if os.path.isdir(video_mp4_result_folder):
        print(video_mp4_result_folder+" exists")
    else :
        os.mkdir(video_mp4_result_folder)

    if os.path.isdir(result_folder):
        print(result_folder+" exists")

    else :
        os.mkdir(result_folder)

def generate_video():

    directory = 'videos' #PATH_WITH_INPUT_VIDEOS
    zee = 0


    upload_folder = 'upload'
    result_folder = 'results/restored_imgs/'
    video_result_folder = 'results_videos/'
    video_mp4_result_folder = 'results_mp4_videos/'

    os.makedirs(upload_folder, exist_ok=True)
    os.makedirs(result_folder, exist_ok=True)
    os.makedirs(video_result_folder, exist_ok=True)
    os.makedirs(video_mp4_result_folder, exist_ok=True)


    for folder in [upload_folder, result_folder, video_result_folder, video_mp4_result_folder]:
        for f in os.listdir(folder):
            full_path = os.path.join(folder, f)
            if os.path.isfile(full_path):
                os.remove(full_path)  # Faylni o'chirish
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path)

    def convert_frames_to_video(pathIn, pathOut, fps):
        frame_array = []
        files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

        files.sort(key=lambda x: int(x[5:-4]))
        size2 = (0, 0)

        for i in range(len(files)):
            filename = pathIn + files[i]

            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width, height)
            size2 = size
            print(filename)

            frame_array.append(img)
        out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size2)
        for i in range(len(frame_array)):

            out.write(frame_array[i])
        out.release()

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        if os.path.isfile(f):
            print("PROCESSING :" + str(f) + "\n")

            cam = cv2.VideoCapture(str(f))


            audio_file = None
            try:
                audio_file = f.replace('.mp4', '.aac')
                subprocess.call(['ffmpeg', '-i', f, '-q:a', '0', '-map', 'a', audio_file], stderr=subprocess.DEVNULL)


                if not os.path.exists(audio_file) or os.path.getsize(audio_file) == 0:
                    audio_file = None
            except Exception:
                audio_file = None


            fps = cam.get(cv2.CAP_PROP_FPS)


            currentframe = 0

            while(True):

                ret, frame = cam.read()

                if ret:

                    name = 'upload/frame' + str(currentframe) + '.jpg'

                    cv2.imwrite(name, frame)

                    currentframe += 1
                    print(currentframe)
                else:
                    break


            cam.release()


            os.system("python3.10 inference_gfpgan.py -i upload -o results -v 1.2 -s 2 --bg_upsampler realesrgan")


            for f in os.listdir(upload_folder):
                os.remove(os.path.join(upload_folder, f))


            pathIn = 'results/restored_imgs/'
            zee = zee + 1
            fName = "video" + str(zee)
            filenameVid = f"{fName}.avi"
            pathOut = "results_videos/" + filenameVid
            convert_frames_to_video(pathIn, pathOut, fps)


            for f in os.listdir('results/restored_imgs'):
                os.remove(os.path.join('results/restored_imgs', f))


            src = 'results_videos/' + filenameVid
            dst = 'results_mp4_videos/' + fName + '.mp4'


            if audio_file and os.path.exists(audio_file):
                subprocess.call(['ffmpeg', '-i', src, '-i', audio_file, '-c:v', 'copy', '-c:a', 'aac', dst])

                os.remove(audio_file)
            else:

                subprocess.call(['ffmpeg', '-i', src, '-c', 'copy', dst])



            for f in os.listdir(video_result_folder):
                os.remove(os.path.join(video_result_folder, f))

# def remove_files():
#     # Crear directorios si no existen
#     upload_folder = 'upload'
#     result_folder = 'results/restored_imgs/'
#     video_result_folder = 'results_videos/'
#     video_mp4_result_folder = 'results_mp4_videos/'
#     video_folder = 'videos'

#     #elimina los frames del video anterior
#     for f in os.listdir(upload_folder):
#         os.remove(os.path.join(upload_folder, f))

#     #elimina los frames mejorados del video anterior
#     for f in os.listdir('results/restored_imgs'):
#         os.remove(os.path.join('results/restored_imgs', f))

#     #elimina todos los videos que subiste para mejorar la resolución
#     for f in os.listdir(video_folder):
#         os.remove(os.path.join(video_folder, f))

#     #limpia los archivos .avi anteriores
#     for f in os.listdir(video_result_folder):
#         os.remove(os.path.join(video_result_folder, f))

#     #limpia los archivos de resultado .mp4
#     for f in os.listdir(video_mp4_result_folder):
#         os.remove(os.path.join(video_mp4_result_folder, f))


print("Boshlandi ...")
make_folder()
print("Video Generatsiya ...")
generate_video()
print("Video tayyor ! [ results_mp4_videos ] faylida")

# a = int(input("1 yozing,fayllar o'chishi uchun."))
# if a == 1:
#     remove_files()
#     print("delete")
# else :
#     print("Fayllar o'chirilmadi !")