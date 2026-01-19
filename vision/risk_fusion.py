class RiskFusion:
    def __init__(self):
        # Tunable weights
        self.distance_weight = {
            "very close": 3,
            "close": 1,
            "far": 0
        }

        self.position_weight = {
            "ahead": 2,
            "left": 1,
            "right": 1
        }

    def compute_risk(self, detection):
        """
        Returns risk score for a single detection.
        """

        pos = detection.get("position")
        dist = detection.get("distance")

        if pos not in self.position_weight:
            return 0

        if dist not in self.distance_weight:
            return 0

        # Risk = distance urgency × positional importance
        return self.distance_weight[dist] * self.position_weight[pos]
