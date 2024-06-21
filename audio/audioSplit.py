import ffmpeg
#文件切割为左右声到
def split_stereo_channels(input_file, output_dir):
    """
    Splits the stereo audio file into separate left and right channel audio files.
    
    :param input_file: Path to the input stereo audio file (e.g., 'path/to/input.mp3').
    :param output_dir: Directory where the output files will be saved.
    :return: List of paths to the output left and right channel audio files.
    """
    # Define output file paths
    left_channel_file = f"{output_dir}/left_channel.mp3"
    right_channel_file = f"{output_dir}/right_channel.mp3"
    
    # Process left channel
    ffmpeg.input(input_file).output(left_channel_file, map_channel='0.0.0').run()

    # Process right channel
    ffmpeg.input(input_file).output(right_channel_file, map_channel='0.0.1').run()
    
    # Return the paths of the processed files
    return [left_channel_file, right_channel_file]

# Example usage:
input_path = '/home/pine/Desktop/audio/143822_057383693915_013588822626_m2gq059vdvkclkf03tdh.mp3'  # Specify your input file path
output_directory = '/home/pine/Desktop/audio/output'  # Specify your output directory
output_files = split_stereo_channels(input_path, output_directory)
print(output_files)
