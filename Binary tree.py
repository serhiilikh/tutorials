class Node:
    """represents node of a bintree with add, find and remove methods"""
    def __init__(self, val=None):
        """constructor including one key parameter"""
        self.parent = None
        self.left = None
        self.right = None
        self.val = val

    def add(self, val):
        """adds node down to the selected node"""
        if self.val> val:
            if self.left:
                self.left.add(val)
            else:
                tmp = Node(val)
                self.left = tmp
                tmp.parent = self
                print("new node added, value {0}, parent value {1}".format(tmp.val, self.val))
        else:
            if self.right:
                self.right.add(val)
            else:
                tmp = Node(val)
                self.right = tmp
                tmp.parent = self
                print("new node added, value {0}, parent value {1}".format(tmp.val, self.val))

    def find(self, val):
        """finds node. doesnt return node anyway"""
        if val == self.val:
            print("found it, its parent is {}".format(self.parent.val))
        elif val > self.val and self.right:
            self.right.find(val)
        elif val < self.val and self.left:
            self.left.find(val)
        else:
            print("sorry, found nothing")

    def remove(self, val):
        """removes node. bad algorithm. val is the node key"""
        if self.val == val:
            # there  are three cases: it has zero, one or two children
            if (self.left or self.right) is None:
                # found 0 children, cut parent
                if self.parent:
                    if self.val > self.parent.val:
                        self.parent.right = None
                    else:
                        self.parent.left = None
            elif ((self.left and self.right) is None) and\
                    ((self.left or self.right) is not None):
                # found 1 child, put it on parent's place
                if self.parent:
                    if self.right:
                        if self.val > self.parent.val:
                            self.parent.right = self.right
                            self.right.parent = self.parent
                        else:
                            self.parent.left = self.right
                            self.right.parent = self.parent
                    if self.left:
                        if self.val < self.parent.val:
                            self.parent.left = self.left
                            self.left.parent = self.parent
                        else:
                            self.parent.right = self.left
                            self.left.parent = self.parent
                else:
                    # one child, no parent
                    if self.right:
                        self.right.parent = None
                    else:
                        self.left.parent = None
            else:
                # if there are two children we find the most
                # left child on the right side
                tmp = self.right
                while tmp.left:
                    tmp = tmp.left
                print(tmp.val)
                self.val = tmp.val
                if tmp.right:
                    tmp.parent.left = tmp.right
                else:
                    tmp.parent.left = None
        # if we dont find, we recursively continue
        elif self.val > val:
            self.left.remove(val)
        elif self.val < val:
            self.right.remove(val)


