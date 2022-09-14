from InquirerPy import inquirer

from igm.conf import InquireRestart
from igm.env import env

_LAST_K = 0
_LAST_B = 0


def inquire_func():
    global _LAST_K, _LAST_B

    print('We are trying to create a project to fit a linear function of \'y = kx + b\' :)')
    k = float(env.K or inquirer.number(
        message="What's is the k value:",
        float_allowed=True,
        default=_LAST_K,
    ).execute())
    b = float(env.B or inquirer.number(
        message="What's is the b value:",
        float_allowed=True,
        default=_LAST_B,
    ).execute())

    if env.NON_CONFIRM:
        confirm = True
    else:
        confirm = inquirer.confirm(message=f"y = {k:.2f}x + {b:.2f}, confirm?").execute()

    if confirm:
        return dict(k=k, b=b)
    else:
        # save this time's fillings
        _LAST_K, _LAST_B = k, b
        raise InquireRestart('Not confirmed.')
