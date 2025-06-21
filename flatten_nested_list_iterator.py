# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    """
    TC: Amortized of O(1); each nested element processed exactly once
    AS: O(d), depth of the nested list
    """
    def __init__(self, nestedList):
        # Stack: list of basic iterators
        self.stack = []
        if nestedList:
            self.stack.append(iter(nestedList))

        # To retrieve the nested integer to process
        self.nextElement = None


    def next(self) -> int:
        """
        TC: O(1)
        """
        return self.nextElement.getInteger()

        
    def hasNext(self) -> bool:
        """
        TC: O(d) - worst case , d is depth of the nested list
        """

        while self.stack:
            # 'next' is built-in function of iterator; 
            # gets the next value of the iterator with default to None if iterator is exhausted
            curr = next(self.stack[-1], None)

            if curr is None:
                self.stack.pop()
            else:
                self.nextElement = curr
                if self.nextElement.isInteger():
                    return True
                else:
                    self.stack.append(iter(self.nextElement.getList()))

        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
