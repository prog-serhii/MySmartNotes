import io

from fastapi import APIRouter, UploadFile, File


router = APIRouter()


@router.post('/text_ocr/')
async def text_ocr(file: UploadFile = File(...)):
    # UPLOAD_DIR.mkdir(exist_ok=True)
    bytes_str = io.BytesIO(await file.read())
    try:
        img = Image.open(bytes_str)
    except:
        raise HTTPException(detail='Invalid image', status_code=400)
    preds = pytesseract.image_to_string(img)

    return {'result': preds}
