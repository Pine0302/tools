import ffmpeg
import os
import logging

def split_stereo_channels(input_file, output_dir, left_file, right_file):
    """
    Splits the stereo audio file into separate left and right channel audio files.
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        left_channel_file = os.path.join(output_dir, left_file)
        right_channel_file = os.path.join(output_dir, right_file)
        ffmpeg.input(input_file).output(left_channel_file, map_channel='0.0.0', y=None).run()
        ffmpeg.input(input_file).output(right_channel_file, map_channel='0.0.1', y=None).run()
        return [left_channel_file, right_channel_file]
    except Exception as e:
        logging.error(f"Error processing file {input_file}: {e}")
        return []

def convert_mp3_to_wav(input_file, output_file):
    """
    Converts an MP3 file to a WAV file.
    """
    try:
        # 转换格式
        ffmpeg.input(input_file).output(output_file, format='wav', y=None).run()
        return output_file
    except Exception as e:
        logging.error(f"Error converting {input_file} to WAV: {e}")
        return None
