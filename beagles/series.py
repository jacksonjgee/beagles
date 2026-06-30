class Series: 
    def __init__(self, data: list, name: str | None = None):
        self.data = list(data)
        self.name = name
    
    def __len__(self):
        return len(self.data)
    
    def __repr__(self):
        return f"Series {self.data}, name = {self.name}"
    
    def head(self, n = 5):
        return self.data[:n]
    
    def sum(self):
        return sum(self.data)
    
    def avg(self):
        return self.sum() / len(self.data)