class SceneDescriber:
    def __init__(self):
        pass

    def describe(self, detection):
        if not detection:
            return None

        label = detection["label"]
        pos = detection["position"]
        dist = detection["distance"]

        if dist == "very close" and pos == "ahead":
            return f"Warning. {label} very close ahead"

        if dist in ["very close", "close"]:
            if label in ["person", "car", "bike"]:
                return f"{label} approaching on your {pos}"
            if label in ["chair", "table", "bag", "bottle"] and dist == "very close":
                return f"Obstacle very close on your {pos}"

        if dist == "close" and pos == "ahead":
            return f"{label} ahead"

        return None


    def describe_object(self, detection):
   
        return self.describe(detection)
     
    def describe_navigation(self, action):
        mapping = {
            "move_left": "Move slightly left",
            "move_right": "Move slightly right",
            "move_forward": "Move forward",
            "move_backward": "Move backward",
            "stop": "Stop now"
        }

        return mapping.get(action, None)
