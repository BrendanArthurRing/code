import textwrap

feedback_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "


def format_feedback(feedback, size):
    return textwrap.wrap(text=feedback, width=size)


format_feedback(feedback_text, 12)
