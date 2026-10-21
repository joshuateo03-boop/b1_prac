class controller:
    def __init__(self):
        self.K_P = 0.15
        self.K_D = 0.6
        self.previous_error = 0.0

    def compute_control(self, observation, reference) -> float:
        current_error = reference - observation
        difference = (current_error - self.previous_error)
        control_signal = self.K_P * current_error + self.K_D * difference
        self.previous_error = current_error
        return control_signal
    