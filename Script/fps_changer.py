from moviepy.editor import VideoFileClip


if __name__ == "__main__":
    input_video_pth = r""
    output_video_pth = r""
    # must be consistent with the label studio fps
    fps = 25

    video_clip = VideoFileClip(input_video_pth)
    video_clip = video_clip.set_fps(fps)

    video_clip.write_videofile(output_video_pth, codec='libx264', audio_codec='aac')
    video_clip.close()