<div align="center">

# ZTT Sticker
<figure>
        <img src="gallery/0.jpg" alt="missing image" style="width: 300px; height: auto;">
        <figcaption></figcaption>
    </figure>
</div>

## Usage

First, use `pip` to download the `opencv-python` and `pillow` package.

```bash
conda create ztt python=3.10
conda activate ztt
pip install -r requirements.txt
```

Then, run the following command to extract all the frames from target video, e.g.,
the following video:

https://github.com/user-attachments/assets/7b1b2f0d-529b-4409-adcd-2d215c9fbe4c

```bash
python scripts/extract_frames.py videos/捏我脸.mp4
python scripts/create_gif.py output/捏我脸/捏我脸_{0173..0240}.png --fps 30
```

## Gallery

<div align="center" style="text-align: center;">

### Images
<table>
    <tr>
        <td>
            <img src="gallery/0.jpg" alt="Image 0" width="200"><br>
            <p>slight smile</p>
        </td>
        <td>
            <img src="gallery/2.png" alt="Image 2" width="200"><br>
            <p>slight smile</p>
        </td>
    </tr>
    <tr>
        <td>
            <img src="gallery/1.png" alt="Image 1" width="200"><br>
            <p>smirking</p>
        </td>
        <td>
            <img src="gallery/3.png" alt="Image 3" width="200"><br>
            <p>winking</p>
        </td>
    </tr>
</table>
</div>

<div align="center" style="text-align: center;">

### GIFs
<table>
    <tr>
        <td>
            <img src="gallery/捏我脸_0000-捏我脸_0085-30fps.gif" alt="GIF 0" width="200">
        </td>
        <td>
            <img src="gallery/捏我脸_0086-捏我脸_0143-10fps.gif" alt="GIF 1" width="200">
        </td>
    </tr>
    <tr>
        <td>
            <img src="gallery/捏我脸_0144-捏我脸_0172-10fps.gif" alt="GIF 2" width="200">
        </td>
        <td>
            <img src="gallery/捏我脸_0173-捏我脸_0240-20fps.gif" alt="GIF 3" width="200">
        </td>
    </tr>
</table>
</div>

## TODO

- [ ] Integrate FaceRate.ai, an AI tool for evaluating facial attractiveness, to rank the extracted frames. This will involve using the FaceRate.ai API to analyze each frame and assign a score based on facial features.
- [ ] Automatically identify the emoji that best matches the extracted frame’s portrait and insert it into the frame.

## Related Resources

- [louiejancevski/FacialEmotionDetector](https://github.com/louiejancevski/FacialEmotionDetector)
- [facerate.ai](https://facerate.ai/app)
- [kdhht2334/awesome-SOTA-FER](https://github.com/kdhht2334/awesome-SOTA-FER)
- [Facial Beauty Prediction](https://paperswithcode.com/task/facial-beauty-prediction)
- [SCUT-FBP5500-Database-Release](https://github.com/HCIILAB/SCUT-FBP5500-Database-Release)
- [Image Quality Assessment](https://paperswithcode.com/task/image-quality-assessment)
- [chaofengc/Awesome-Image-Quality-Assessment](https://github.com/chaofengc/Awesome-Image-Quality-Assessment)
- [nilaoda/N_m3u8DL-RE](https://github.com/nilaoda/N_m3u8DL-RE)
- [wbt5/real-url](https://github.com/wbt5/real-url)
