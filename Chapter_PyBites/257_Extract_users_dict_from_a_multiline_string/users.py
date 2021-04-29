pw = """
postfix:x:108:112::/var/spool/postfix:/bin/false
ssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash
artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash
"""


def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    dic = {}
    for s in passwd.splitlines()[1:]:
        fields = line.split(':')
        user = s.split(":")[0]
        name = 'unknown' if not fields[4] else re.sub('\,+', ' ', fields[4].rstrip(','))
        dic[user] = name
    return dic 