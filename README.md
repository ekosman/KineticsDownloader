# Download DeepMind's Kinetics

Download all videos from DeepMind's [Kinetics dataset](https://deepmind.com/research/open-source/open-source-datasets/kinetics/).
Moreover, you can use this library to extract **frames** and **sound track** from videos, generate metadata for training
and pack all sound tracks into a single **tfrecords** file for faster reading.

## Requirements

* Python >= 3.4
* youtube-dl
* ffmpeg
* gzip

Required Python packages are listed in **requirements.txt**.

## Usage

**WARNING:** Before you start any download from YouTube, please be sure, that you have checked [YouTube Terms Of Service](https://www.youtube.com/static?template=terms) and you are compliant. Especially check section 5.H.

**Download all videos**:
```
python download.py --all
```

## Download structure

The training and validation videos are downloaded into their individual directories.
Furthermore, a directory is created for each class.

Example:

```
dataset/train/blowing_glass
dataset/valid/blowing_glass
```

Test videos are all downloaded into a single directory because their classes are not known.

Example:

```
dataset/test
```

### File names and video format

The videos are all download in mp4. If a video isn't available in mp4, it's downloaded in
 the next best format and converted into mp4. All videos are downloaded with sound.

Videos' file names correspond to their YouTube IDs. All spaces in directory names are replaced with
underscores (e.g. blowing glass => blowing_glass).

## References

* [[1] The Kinetics Human Action Video Dataset - W.Kay et al. (2017)](https://arxiv.org/abs/1705.06950)
