# Subtitles-Delayer

A simple Python script which allows the user to delay an srt file after a certain timecode.

## Description

Why did I do this ? Why not simply use tools like ffmpeg/sed/...

Well, I was surprised to discover that ffmpeg doesn't allow you to delay subtitles after a certain timestamp in your srt file (like delay a subtitles file by 2 seconds after 5 min for instance), and all my attempts at using ffmpeg failed miserably.

Soooo, here is a script which allows me to do that !

## Getting Started

### Dependencies

* Python3.12 (may work with earlier versions of Python)

### Installing

* `git clone https://github.com/edaveau/Subtitles-Delayer.git`
* `cd Subtitles-Delayer`
* `python3 main.py`

### Executing program

Clone the repository and go to the folder `Subtitles-Delayer`, then run the following command from any CLI :
```python3
python3 main.py --filein somefolder/mysubtitle.srt --timestamp 3m50s --delay 5
```

The command above will delay all the subtitles after `3 minutes and 50 seconds` in your srt file `mysubtitle.srt` by `5` seconds.

The following formats for the parameter `timestamp` are accepted by the script:
* `01:02:03,123`
* `02:03:04.456`
* `3560`
* `3m20s`

## Version History

* 1.0.1
    * Added README.md
* 1.0
    * Fully functional release (simple CLI use, one file in one file out)
* 0.1
    * Initial Release (_no write to output_)

## License

This project is licensed under the GPLv3.0 License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [Simple README](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [MarredCheese on StackOverflow](https://stackoverflow.com/a/42320260)
