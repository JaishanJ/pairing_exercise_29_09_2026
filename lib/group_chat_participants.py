def group_chat_names(list_names):
    if list_names == []:
        return ""
    if len(list_names) <= 2:
        return " & ".join(list_names)
    return ", ".join(list_names[:-1]) + " & " + list_names[-1]