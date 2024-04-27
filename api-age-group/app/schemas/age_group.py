def convert_age_group(age_group):
    return {"id": str(age_group["_id"]), "min_age": age_group["min_age"], "max_age": age_group["max_age"]}


def convert_age_groups(age_groups):
    return [convert_age_group(age_group) for age_group in age_groups]
