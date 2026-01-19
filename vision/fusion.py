class Fusion:

    def __init__(self, frame_width):
        self.frame_width = frame_width
        self.left_boundary = frame_width * 0.35
        self.right_boundary = frame_width * 0.65

    def get_position(self, bbox):
        """
        Returns one of: 'left', 'ahead', 'right'
        """

        # Defensive check
        if bbox is None or len(bbox) != 4:
            return None

        x1, _, x2, _ = bbox
        center_x = (x1 + x2) / 2

        if center_x < self.left_boundary:
            return "left"

        elif center_x <= self.right_boundary:
            return "ahead"

        else:
            return "right"
