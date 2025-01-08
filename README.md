<div align="center">

# ZTT Sticker
<figure>
        <img src="stickers/0.jpg" alt="missing image" style="width: 300px; height: auto;">
        <figcaption></figcaption>
    </figure>
</div>

## Usage

First, use `pip` to download the `opencv-python` package.

```bash
conda create ztt python=3.10
conda activate ztt
pip install -r requirements.txt
```

Then, run the following command to extract all the frames from target video, e.g.,
the following video:

```bash
python scripts/extract_frames.py videos/捏我脸.mp4
```

## TODO

- [ ] Integrate FaceRate.ai, an AI tool for evaluating facial attractiveness, to rank the extracted frames. This will involve using the FaceRate.ai API to analyze each frame and assign a score based on facial features.
