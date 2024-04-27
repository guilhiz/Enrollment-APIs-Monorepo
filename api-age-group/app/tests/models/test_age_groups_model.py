import pytest
from pydantic import ValidationError
from app.models.age_group import AgeGroup


def test_age_group_models():
    age_group = AgeGroup(id=3, min_age=25, max_age=75)
    assert age_group.dict() == {"id": 3, "min_age": 25, "max_age": 75}


def test_age_group_invalid_min_age():
    with pytest.raises(ValidationError):
        AgeGroup(id=4, min_age=-1, max_age=50)

    with pytest.raises(ValidationError):
        AgeGroup(id=5, min_age=0, max_age=50)


def test_age_group_invalid_max_age():
    with pytest.raises(ValidationError):
        AgeGroup(id=6, min_age=10, max_age=121)

    with pytest.raises(ValidationError):
        AgeGroup(id=7, min_age=10, max_age=1)
