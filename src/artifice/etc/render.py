def terminal_output(*args):
    import sys
    print(*args, file=sys.stderr)
    sys.exit(0)
