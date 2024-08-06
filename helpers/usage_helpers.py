def remove_space_from_code_snippet(code):
    return ",\n".join([c.strip() for c in code.split(",")])