class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    image = str(body.get("image", ""))
    if image.endswith(":latest") or image == "latest":
        failed.append("image_tag_latest")

    if not body.get("champion"): failed.append("champion")\n    if not body.get("eval_passed"): failed.append("eval")\n    if not body.get("digest"): failed.append("digest")
    return {"passed": not failed, "failed": failed, "applied": False}
