# def get_profile(*, name='julian', profession='programmer'):
#     return f"{name} is a {profession}"

kwargs = {"name": "julian", "profession": "programer"}

def get_profile(**kwargs):
    return f"{kwargs.get('name', 'julian')} is a {kwargs.get('profession', 'programmer')}"
