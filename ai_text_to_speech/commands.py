def check_exit_command(text: str) -> bool:
"""Check if user wants to exit"""
return text.strip().lower() in ['exit', 'quit', 'bye', 'close']
