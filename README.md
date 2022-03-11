# plaintext_playlist_py

Library to parse [plaintext-playlist](https://github.com/seanbreckenridge/plaintext-playlist) files

Mostly for personal usage, making this installable as a library means I can use it across code/projects/scripts

Also includes some `ID3`/music scripts:

- [`bin/id3stuff`](bin/id3stuff) - a personal opinionated script to set ID3 metadata using `mutagen` -- prompts me to set the arist/album/album artist for groups of collections by scanning my music directory

## Installation

Requires `python3.10+`

To install with pip, run:

    pip install git+https://github.com/seanbreckenridge/plaintext-playlist

## Usage

`plaintext_playlist_py`

### Tests

```bash
git clone 'https://github.com/seanbreckenridge/plaintext_playlist_py'
cd ./plaintext_playlist_py
pip install '.[testing]'
flake8 ./plaintext_playlist_py
mypy ./plaintext_playlist_py
```
