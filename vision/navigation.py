from vision.risk_fusion import RiskFusion

class NavigationEngine:

    def __init__(self):
        self.risk_fusion = RiskFusion()

    def decide(self, detections):
        if not detections:
            return None

        risk = {"left": 0, "ahead": 0, "right": 0}

        for det in detections:
            pos = det.get("position")
            if pos not in risk:
                continue

            risk_value = self.risk_fusion.compute_risk(det)
            risk[pos] += risk_value

        # Decision logic
        if risk["ahead"] >= 4:
            if risk["left"] < risk["right"]:
                return "move_left"
            elif risk["right"] < risk["left"]:
                return "move_right"
            else:
                return "stop"

        return None
