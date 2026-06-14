import random

class MarkovChain:
    def __init__(self, order=1):
        self.order = order
        self.model = {}

    def train(self, text):
        words = text.split()
        if len(words) < self.order + 1:
            return

        for i in range(len(words) - self.order):
            state = tuple(words[i:i + self.order])
            next_word = words[i + self.order]
            if state not in self.model:
                self.model[state] = []
            self.model[state].append(next_word)

    def generate(self, length=50):
        if not self.model:
            return ""

        # Start with a capitalized state if possible, otherwise random
        capitalized_states = [state for state in self.model.keys() if state[0][0].isupper()]
        if capitalized_states:
            current_state = random.choice(capitalized_states)
        else:
            current_state = random.choice(list(self.model.keys()))
        output = list(current_state)

        count = self.order
        while True:
            if current_state in self.model:
                next_word = random.choice(self.model[current_state])
                output.append(next_word)
                current_state = tuple(output[-self.order:])
                count += 1
                
                if count >= length and next_word[-1] in '.!?':
                    break
                
                if count >= length + 100:
                    break
            else:
                break

        return " ".join(output)
