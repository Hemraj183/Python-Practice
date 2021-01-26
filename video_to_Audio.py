import imageio
import moviepy.editor


print("Processing..............")

video = moviepy.editor.VideoFileClip('Test1.mkv')
audio = video.audio

audio.write_audiofile('sample.mp3')
print("Converted Sucessfully")
