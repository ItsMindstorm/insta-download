# Prelude

This script can be used to grab all liked pictures from your instagram account

## Installation

The script requires a few things:

- Python
- Instaloader (only images)
  - `pip install instaloader`
  - `pipx install instaloader`
- yt-dlp (for videos)
  - `pip install yt-dlp`
  - `pipx install yt-dlp`

## Caveats

Both scripts send a moderate amount of requests to instagram, meaning that after a while, you will get rate limited which looks like this:

### Images

```sh
Error 401
```

### Videos

```sh
You might be rate limited
```

To circumvent this, you have to login into instagram trough whichever tool you choose, please check the tools documentation on how to do that

## How to use it to get liked pictures

1. Take out your data in JSON from instagram
2. Put the `liked_posts.json` file into this folder
3. Then refactor the json file by removing the `https://instagram.com/p/` and the ending `/` of each href tag
   - This can be done easily with neovim by using the `:%s` command
   - Unfortunately you will have to do this on your own
4. Finally run the `images.py` script with `python images.py` or `python3 images.py`

## How to use it to get all liked videos

1. Take out your data again and put the `liked_posts.json` into this folder
2. No need to refactor this time, however, you should run the `video.py` script with `python video.py` or `python3 video.py`

# Acknowledgements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for their absolutely bombastic and powerful tool for downloading videos
- [Instaloader](https://github.com/instaloader/instaloader) for providing a way to actually get the pictures from instagram in a programmatic way
