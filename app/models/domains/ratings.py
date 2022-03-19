from fastapi import HTTPException
from pydantic import BaseModel, validator


class StartNumber(BaseModel):
    star_number: float = 0

    @validator("star_number", pre=True)
    def check_str(cls, x):
        float_x = float(x)
        if (float_x > 5 or
                float_x < 0):
            raise HTTPException(
                status_code=400,
                detail='Start number must be smaller than 5 and greater than 1'
            )
        return x
