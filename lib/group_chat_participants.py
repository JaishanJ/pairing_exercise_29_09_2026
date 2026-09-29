def group_chat_names(list_names):
    if list_names == []:
        return ""
    elif len(list_names) == 1:
        return list_names[0]
    elif len(list_names) == 2:
        return f"{list_names[0]} & {list_names[1]}"
    else:
        except_last = ", ".join(list_names[:-1])
        return f"{except_last} & {list_names[-1]}"