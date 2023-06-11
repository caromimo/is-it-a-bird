# getting bird and forest images

# import libraries
from fastbook import search_images_ddg
from fastai.vision.all import (
    Path,
    download_images,
    resize_images,
    verify_images,
    get_image_files,
)
from time import sleep


def search_images(term, max_images=30):
    print(f"Searching for '{term}'")
    return search_images_ddg(term, max_images)


searches = "forest", "bird"
path = Path("bird_or_not")

for o in searches:
    dest = path / o
    dest.mkdir(exist_ok=True, parents=True)
    download_images(dest, urls=search_images(f"{o} photo"))
    sleep(10)  # Pause between searches to avoid over-loading server
    download_images(dest, urls=search_images(f"{o} sun photo"))
    sleep(10)
    download_images(dest, urls=search_images(f"{o} shade photo"))
    sleep(10)
    resize_images(path / o, max_size=400, dest=path / o)

failed = verify_images(get_image_files(path))
failed.map(Path.unlink)
print(f"We removed {len(failed)} photos.")
