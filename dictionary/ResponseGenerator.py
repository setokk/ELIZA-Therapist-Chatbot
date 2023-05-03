
class ResponseGenerator:
    
    def __init__(self, responseTemplate, reObject, groupIndexes) -> None:
        # Response string with any number of '{}' for formatting
        self.responseTemplate = responseTemplate 
        
        # The re object we got from the re.compile method
        self.reObject = reObject
        
        # The group indexes to replace the '{}' from the response template string
        self.groupIndexes = groupIndexes
        
        # The matched object
        self.matchedObject = None
    
    def generateResponse(self):
        groups = []
        for index in self.groupIndexes:
            groups.append(self.matchedObject.group(index).lower())
        
        # We have the groups, now we can replace
        res = self.responseTemplate.format(*groups)
        
        # Reset to None
        self.matchedObject = None
        
        return res
    
    def matches(self, message):
        self.matchedObject = self.reObject.search(message)
        return (not self.matchedObject is None)