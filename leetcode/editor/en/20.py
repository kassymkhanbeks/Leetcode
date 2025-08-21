# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		mapping = {')': '(', ']': '[', '}': '{'}
		for c in s:
			if c in mapping.values():  # opening brackets
				stack.append(c)
			else:  # closing brackets
				if not stack or stack[-1] != mapping[c]:
					return False
				stack.pop()
		return len(stack) == 0
# leetcode submit region end(Prohibit modification and deletion)
