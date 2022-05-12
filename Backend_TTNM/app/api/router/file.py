import random
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.db.repositories.image.get_images import get_all_images
from app.utils.read_file_xlxs import read
from fastapi.responses import FileResponse
import requests
import os


router = router = APIRouter(
    prefix="/file",
    tags=["File"],
    responses={404: {"description": "Not found"}}
)

@router.post("/")
async def read_excel(
    # user: dict = Depends(get_current_user),
    _in: UploadFile = File(None)
):
    respon = read(None, _in)
    return respon


@router.get(
    "/get-image",
)
def get_image(
    image_path: str
):
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type="image/jpeg")
    return HTTPException(
        status_code=404, detail="File not found!"
    )


# @router.get(
#     "/update-images",
# )
# def update_images():
#     images, session = get_all_images()
#     # for indx, image in enumerate(images):
#     #     # response = requests.get(url)
#     #     # file_extension = response.headers.get('Content-Type').split('/')[-1].lower()
#     #     # save_to = write_file(
#     #     #     image.id_image,
#     #     #     file_extension,
#     #     #     response.content
#     #     # )
#     #     if indx + 1 > 31:
#     #         ran_num = random.randint(1, 31)
#     #         image.path = f'images/{ran_num}.jpeg'
#     #         session.flush()
#     #         session.commit()
#     return images


def write_file(
    image_id,
    file_extension,
    data
) -> str:
    destination_dir = f'images'
    is_exist = os.path.exists(destination_dir)
    if not is_exist:
        os.makedirs(destination_dir)
    filename = f'{image_id}.{file_extension}'
    save_to = f'{destination_dir}/{filename}'
    with open(save_to, "wb") as f:
        f.write(data)
    return save_to
