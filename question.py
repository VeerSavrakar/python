class Rectangle:
    def __init__(self, length: int, width: int):
        self.length= length
        self.width= width
    
    def __iter__(self):
        yield{'legth': self.length}
        yield{'width': self.width}
        
    def __str__(self):
        return f"Length: {self.length} , Width: {self.width}"
        
rectangle= Rectangle(23,43)
print(rectangle)