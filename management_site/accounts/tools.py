def hide_email(email: str) -> str:
    _email = email.split('@')
    _email[0] = (_email[0][:5] if len(_email[0]) > 6 else _email[0][:len(_email[0]) // 2]) + '*' * 2
    _email[1] = '*' * 2 + (_email[1][-7:] if len(_email[1]) > 7 else _email[1][-1 * len(_email[1]) // 2:])
    return _email[0] + _email[1]
