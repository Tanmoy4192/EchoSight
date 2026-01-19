class decisionEngine:
    def selection(self, detections):
        if detections == None:
            return None #return nothing if detections list is empty
        
        canditates = []
        very_close = []
        close = []
        for detection in detections:
            if detection["distance"] == "very close":
                very_close.append(detection) #keep those detection which is very close
            elif detection["distance"] == "close":
                close.append(detection) # keep those detection which is close 
        
        if very_close:
            canditates = very_close # assign the list into canditates
        elif close:
            canditates = close

        ahead = []

        for detection in canditates:
            if detection["position"] == "ahead": # keep those which is close and ahead 
                ahead.append(detection)
        
        if ahead:
            canditates = ahead
        #set priority 
        for detection in canditates:
            if detection['label'] == "vehicle": # vehicle vey close ahead has heighest emergency < person < obstricle 
                return detection
        for detection in canditates:
            if detection["label"] == "person":
                return detection
        
        return canditates[0] if canditates else None