class StateMachine:
    def __init__(self):
        self.types = {}
        self.initial_state = None
        self.final_state = []
        self.tokens = []
    def add_state(self, name, types_array, end=0):
        name = name.upper()
        self.types[name] = types_array
        if end:
            self.final_state.append(name)
    def set_start(self, name):
        self.initial_state = name.upper()
    def run(self, text):
        try:
            current_state = self.types[self.initial_state]
        except:
            raise "A error happened"
        if not self.final_state:
            raise "No final state"
        for key, value in self.types.items():
          (state, text) = self.types[key](text)
          if state in self.final_state:
            self.tokens.append((state, text))
            break
