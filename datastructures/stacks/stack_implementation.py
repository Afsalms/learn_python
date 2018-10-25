
class Mylist(list):
    def __getitem__(self, *args, **kwargs):
        raise Exception("Cannot access stack using index")

    def __setitem__(self, *args, **kwargs):
        raise Exception("Cannot change stack using index")

    def append(self, *args, **kwargs):
        if not  kwargs.get("from_stack"):
            raise Exception("Append not implemented")
        super(Mylist, self).append(args[0])

    def extend(self, *args, **kwargs):              
        raise Exception("Extend not implemented")


class Stack:       
    def __init__(self):                                   
        self.stack = Mylist()  

    def push(self,data):
        if data not in self.stack:         
            self.stack.append(data, from_stack=True)
            return True                          
        return False
    def pop(self):
        if len(self.stack)<=0:
            return ("Stack Empty!")
        return self.stack.pop()

    def size(self):
        return len(self.stack)


