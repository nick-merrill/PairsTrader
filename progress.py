import sys

class Progress:
    current = 0
    width = 75
    total = 100

    def __init__(self, total):
        self.total = total

    def refresh(self):
        num_hash = int(1. * self.current / self.total * self.width)
        num_space = self.width - num_hash
        sys.stdout.write('\r[{0}{1}] {2}%  '.format('#' * num_hash, ' ' * num_space, \
                         int(100.*self.current/self.total)))
        sys.stdout.flush()

    def update(self, current):
        self.current = current
        self.refresh()

