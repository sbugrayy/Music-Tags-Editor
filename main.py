import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TALB, TPE1, TPE2, TIT2
from mutagen.wavpack import WavPack
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
from mutagen.mp4 import MP4
from mutagen.apev2 import APEv2
from mutagen.asf import ASF
from mutagen.mp3 import MP3
from mutagen.wave import WAVE

folder_path = r"C:\Users\bugra\Desktop\Muziklerim"

default_album = "Electro"
default_album_artist = "Subnine"
default_contributing_artists = "Subnine"

special_album_speed = "Speed Electro"
special_album_speed_artist = "Subnine"
special_contributing_artists_speed = "Subnine"

special_album_cat = "Çat"
special_album_cat_artist = "Subnine"
special_contributing_artists_cat = "Subnine"


def update_tags(file_path):
    """
    Updates the tags of the specified audio file.
    Uses the appropriate tagging method based on file extension.
    """
    file_name = os.path.basename(file_path)
    file_name_without_ext = os.path.splitext(file_name)[0]
    extension = os.path.splitext(file_name)[1].lower()
    new_title = file_name_without_ext

    print(f"Processing '{file_name}'...")

    current_album = default_album
    current_album_artist = default_album_artist
    current_contributing_artists = default_contributing_artists

    if "çat" in new_title.lower():
        print(f"  'Çat' found in '{new_title}'. Assigning to '{special_album_cat}' album.")
        current_album = special_album_cat
        current_album_artist = special_album_cat_artist
        current_contributing_artists = special_contributing_artists_cat
    elif "slowed" in new_title.lower() or "speed up" in new_title.lower():
        print(f"  'slowed' or 'speed up' found in '{new_title}'. Assigning to '{special_album_speed}' album.")
        current_album = special_album_speed
        current_album_artist = special_album_speed_artist
        current_contributing_artists = special_contributing_artists_speed


    try:
        audio = None
        if extension == '.mp3':
            audio = ID3(file_path)
        elif extension == '.wav':
            try:
                audio = EasyID3(file_path)
            except Exception:
                from mutagen.wave import WAVE
                audio = WAVE(file_path)
        elif extension == '.flac':
            audio = FLAC(file_path)
        elif extension == '.ogg':
            audio = OggVorbis(file_path)
        elif extension == '.m4a' or extension == '.mp4':
            audio = MP4(file_path)
        elif extension == '.wma':
            audio = ASF(file_path)
        elif extension == '.wv':
            audio = WavPack(file_path)
        elif extension == '.ape':
            audio = APEv2(file_path)
        else:
            print(f"  ERROR: Unsupported file type for '{file_name}'.")
            return

        if audio is None:
            print(f"  Could not load or create tag data for '{file_name}'.")
            return

    except Exception as e:
        print(f"  An error occurred while opening '{file_name}' or creating tags: {e}")
        return

    try:
        if extension == '.mp3':
            audio['TIT2'] = TIT2(encoding=3, text=new_title)
            audio['TALB'] = TALB(encoding=3, text=current_album)
            audio['TPE2'] = TPE2(encoding=3, text=current_album_artist)
            audio['TPE1'] = TPE1(encoding=3, text=current_contributing_artists)
        elif extension in ['.wav', '.flac', '.ogg', '.m4a', '.wma', '.wv', '.ape']:
            # Use general keys for WAV and other formats
            audio['title'] = new_title
            audio['album'] = current_album
            audio['albumartist'] = current_album_artist
            audio['artist'] = current_contributing_artists
        else:
            print(f"  ERROR: Cannot update tags for '{file_name}' (unknown format).")
            return

        audio.save(file_path)
        print(f"✔️ '{file_name}' updated. (Title: '{new_title}', Album: '{current_album}')")

    except Exception as e:
        print(f"  An error occurred while saving tags for '{file_name}': {e}")


def main_function():
    # Processes all supported audio files in the specified folder.
    if not os.path.isdir(folder_path):
        print(f"ERROR: '{folder_path}' is not a valid folder. Please check the path in the script.")
        return

    print(f"Scanning folder: {folder_path}")
    print("---")

    file_count = 0
    supported_extensions = ['.mp3', '.wav', '.flac', '.ogg', '.m4a', '.mp4', '.wma', '.wv', '.ape']

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        extension = os.path.splitext(file_name)[1].lower()

        if extension in supported_extensions:
            update_tags(file_path)
            file_count += 1

    print("---")
    if file_count == 0:
        print("No supported audio files found in the specified folder.")
    else:
        print(f"Process completed. Total {file_count} files updated.")


if __name__ == "__main__":
    main_function()