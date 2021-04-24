from pipe import pipe

def number_pipes():
    pipped_message=pipe(message=message)
    assert pipped_message.count("|")==4
    assert len(message)==len(message)