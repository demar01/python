from driving import allowed_driving

def allowed_driving_old(capfd):
    allowed_driving('Miel', 2)
    output = capfd.readouterr()[0].strip()
    assert out == "Miel is not allowed to drive"



def allowed_driving_old(capfd):
    allowed_driving('Tim', 27)
    output = capfd.readouterr()[0].strip()
    assert out == "Tim is allowed to drive"
