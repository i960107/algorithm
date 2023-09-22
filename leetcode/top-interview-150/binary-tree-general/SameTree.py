class Solution:
    def isSameTree(self, p, q):
        def _isSameTree(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            if not _isSameTree(l.left, r.left):
                return False
            if not _isSameTree(l.right, r.right):
                return False
            return True

        return _isSameTree(p, q)
