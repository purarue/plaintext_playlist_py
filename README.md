# plaintext_playlist_py

Library to parse [plaintext-playlist](https://github.com/seanbreckenridge/plaintext-playlist) files

Mostly for personal usage, making this installable as a library means I can use it across code

Also includes some `ID3`/music scripts:

- [`bin`](bin/id3stuff) - a personal opinionated script to set ID3 metadata

## Installation

Requires `python3.7+`

To install with pip, run:

    pip install plaintext_playlist_py

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
