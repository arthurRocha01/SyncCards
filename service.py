import os
from datetime import datetime
from anki_client import send_to_anki

class ServiceHandler:
    def extract_date(self, image: str) -> datetime:
        basename = os.path.splitext(image)[0]
        return datetime.strptime(basename, "%Y-%m-%d_%H-%M")

    def rename_images(self, image_pair: list[str]) -> list[str]:
        img1, img2 = image_pair
        date1, date2 = self.extract_date(img1), self.extract_date(img2)

        if date1 < date2:
            front, back = img1, img2
        else:
            front, back = img2, img1

        front_name, front_ext = os.path.splitext(front)
        back_name, back_ext = os.path.splitext(back)

        return [
            f"{front_name}_front{front_ext}",
            f"{back_name}_back{back_ext}",
        ]

    def process_file(self, image_pair: list[str]) -> None:
        renamed_pair = self.rename_images(image_pair)
        send_to_anki(renamed_pair)