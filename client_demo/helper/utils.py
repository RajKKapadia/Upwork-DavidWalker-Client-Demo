def generate_chat_history(chat_history: list) -> list:
    formated_history = []
    for i in range(0, len(chat_history), 2):
        formated_history.append(
            (
                chat_history[i],
                chat_history[i+1]
            )
        )
    return chat_history
