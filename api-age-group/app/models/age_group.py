from pydantic import BaseModel, Field, validator


class AgeGroup(BaseModel):
    id: int
    min_age: int = Field(gt=0, le=120)
    max_age: int = Field(le=120, gt=1)

    @validator("max_age")
    def check_ages(cls, v, values, **kwargs):
        if "min_age" in values and v <= values["min_age"]:
            raise ValueError("max_age must be greater than min_age")
        return v
