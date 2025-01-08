import cv2
import os
import argparse

def extract_frames(video_path, output_dir, frame_prefix="frame"):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Unable to open video file {video_path}")
        return

    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Exit loop when video ends

        # Save each frame as an image
        frame_path = os.path.join(output_dir, f"{frame_prefix}_{frame_number:04d}.png")
        cv2.imwrite(frame_path, frame)
        frame_number += 1

    cap.release()
    print(f"Extracted {frame_number} frames to '{output_dir}'")

if __name__ == "__main__":
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Extract frames from an MP4 video.")
    parser.add_argument("video_path", help="Path to the input MP4 video file")
    parser.add_argument("--output_dir", help="Directory to save the extracted frames")
    parser.add_argument("--frame_prefix", help="Prefix for the frame filenames (default: 'frame')")

    args = parser.parse_args()

    video_filename = args.video_path.split("/")[-1].split(".")[0]

    if args.output_dir is None:
        # Use the `$pwd/output/video_filename` as the default output directory
        output_dir = os.path.join(os.getcwd(), "output", video_filename)
    else:
        output_dir = args.output_dir

    if args.frame_prefix is None:
        # Use the video filename as the default prefix
        frame_prefix = args.video_path.split("/")[-1].split(".")[0]
    else:
        frame_prefix = args.frame_prefix

    # Extract frames
    extract_frames(args.video_path, output_dir, frame_prefix)
